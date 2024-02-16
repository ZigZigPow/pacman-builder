import pygame
import sys
import random

# Initialize clock
pygame_clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()  # Starter tick

white = (255, 255, 255)

# Initialize Pygame
pygame.init()



# Colors
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
pink = (255, 105, 180)



# Pac-Man settings
pacman_radius = 15
movement_speed = 0.23

# Wall settings
wall_thickness = 20
gate_width = 50  # Width of the gate
corridor_width = 6 * pacman_radius
tile_side = corridor_width + 1 * wall_thickness

# play background music
pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.play(-1)


maze_walls = []
max_x = 0
with open('maze.txt', 'r', encoding='utf-8') as file: # https://asciiflow.com/legacy/
    y = 0
    for line in file:
        x = 0
        for char in line:
            if  char == '\n':
                break
            if char != ' ':
                # This character represents a wall
                maze_walls.append(pygame.Rect(x, y, wall_thickness, wall_thickness))
            x += wall_thickness
        if x > max_x:
            max_x = x
        y += wall_thickness

# Screen dimensions
screen_width = max_x
screen_height = y

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man in Pygame")

def will_collide_with_walls(next_rect, walls):
    for wall in walls:
        if next_rect.colliderect(wall):
            return True
    return False



# Find a valid starting position for Pac-Man that is not inside a wall
pacman_x, pacman_y = None, None
while pacman_x is None or pacman_y is None:
    temp_x = random.randint(pacman_radius, screen_width - pacman_radius)
    temp_y = random.randint(pacman_radius, screen_height - pacman_radius)
    temp_rect = pygame.Rect(temp_x - pacman_radius, temp_y - pacman_radius, pacman_radius * 2, pacman_radius * 2)
    if not will_collide_with_walls(temp_rect, maze_walls):
        pacman_x, pacman_y = temp_x, temp_y


    # Ghost settings
ghost_color = blue
ghost_radius = pacman_radius
while True:
    ghost_x = random.randint(wall_thickness, screen_width - wall_thickness)
    ghost_y = random.randint(wall_thickness, screen_height - wall_thickness)
    ghost_rect = pygame.Rect(ghost_x - ghost_radius, ghost_y - ghost_radius, ghost_radius * 2, ghost_radius * 2)
    if not will_collide_with_walls(ghost_rect, maze_walls):
        break


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
last_direction = random.choice(directions)
    

def random_walk_ghost(ghost_x, ghost_y, maze_walls, last_direction):
    change_direction_prob = 0.001  # Probability to change direction at random
    if will_collide_with_walls(
            pygame.Rect(
                ghost_x + last_direction[0] * movement_speed - ghost_radius,
                ghost_y + last_direction[1] * movement_speed - ghost_radius,
                ghost_radius * 2,
                ghost_radius * 2),
            maze_walls) or random.random() < change_direction_prob:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        directions.remove((last_direction[0], last_direction[1]))
        last_direction = random.choice(directions)
    
    ghost_x += last_direction[0] * movement_speed
    ghost_y += last_direction[1] * movement_speed
    
    return ghost_x, ghost_y, last_direction

# Game loop flag
running = True



# Dot settings
dot_radius = 5
# Initialize dots in the middle of each cell in the maze
dots = []
for x in range(wall_thickness, screen_width - wall_thickness, pacman_radius * 3):
    for y in range(wall_thickness, screen_height - wall_thickness, pacman_radius * 3):
        dot_rect = pygame.Rect(x - dot_radius, y - dot_radius, dot_radius * 2, dot_radius * 2)
        if not will_collide_with_walls(dot_rect, maze_walls):
            dots.append(dot_rect)

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement handling
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    tongue_out = False
    if keys[pygame.K_LEFT]:
        dx = -movement_speed
    if keys[pygame.K_RIGHT]:
        dx = movement_speed
    if keys[pygame.K_UP]:
        dy = -movement_speed
    if keys[pygame.K_DOWN]:
        dy = movement_speed
    if keys[pygame.K_SPACE]:
        tongue_out = True

    # Create a temporary rect to test the new position
    temp_rect = pygame.Rect(pacman_x + dx - pacman_radius, pacman_y + dy - pacman_radius, pacman_radius * 2, pacman_radius * 2)

    # Check for potential collisions
    if not will_collide_with_walls(temp_rect, maze_walls):
        pacman_x += dx
        pacman_y += dy

    # Prevent Pac-Man from moving outside the screen
    pacman_x = max(pacman_radius, min(screen_width - pacman_radius, pacman_x))
    pacman_y = max(pacman_radius, min(screen_height - pacman_radius, pacman_y))

    # Screen update
    screen.fill(black)
    
    # Draw walls
    for wall in maze_walls:
        pygame.draw.rect(screen, blue, wall)
    
    # Check for Pac-Man eating dots with tongue
    tongue_rect = None
    if tongue_out:
        tongue_length = wall_thickness * 3
        tongue_width = pacman_radius // 5
        if dx < 0:  # Pac-Man facing left
            tongue_rect = pygame.Rect(pacman_x - pacman_radius - tongue_length, pacman_y - tongue_width // 2, tongue_length, tongue_width)
        elif dx > 0:  # Pac-Man facing right
            tongue_rect = pygame.Rect(pacman_x + pacman_radius, pacman_y - tongue_width // 2, tongue_length, tongue_width)
        elif dy < 0:  # Pac-Man facing up
            tongue_rect = pygame.Rect(pacman_x - tongue_width // 2, pacman_y - pacman_radius - tongue_length, tongue_width, tongue_length)
        elif dy > 0:  # Pac-Man facing down
            tongue_rect = pygame.Rect(pacman_x - tongue_width // 2, pacman_y + pacman_radius, tongue_width, tongue_length)

        if tongue_rect:
            pygame.draw.rect(screen, pink, tongue_rect)

    for dot in dots[:]:
        if temp_rect.colliderect(dot) or (tongue_rect and tongue_rect.colliderect(dot)):
            dots.remove(dot)
            pygame.mixer.Sound('pac.mp3').play(maxtime=50)
    
    # Draw dots
    for dot in dots:
        pygame.draw.circle(screen, yellow, dot.center, dot_radius)
    
    # Draw Pac-Man
    pygame.draw.circle(screen, yellow, (pacman_x, pacman_y), pacman_radius)
    # Draw Pac-Man's Eye based on the movement direction
    if dy < 0:  # Pac-Man moving up
        eye_x = pacman_x + pacman_radius * 0.4
        eye_y = pacman_y - pacman_radius * 0.5
    elif dy > 0:  # Pac-Man moving down
        eye_x = pacman_x + pacman_radius * 0.4
        eye_y = pacman_y + pacman_radius * 0.5
    elif dx < 0:  # Pac-Man moving left
        eye_x = pacman_x - pacman_radius * 0.5
        eye_y = pacman_y - pacman_radius * 0.4
    elif dx > 0:  # Pac-Man moving right
        eye_x = pacman_x + pacman_radius * 0.5
        eye_y = pacman_y - pacman_radius * 0.4
    else:  # Pac-Man idle or no specific direction
        eye_x = pacman_x + pacman_radius * 0.5
        eye_y = pacman_y - pacman_radius * 0.4
    eye_radius = int(pacman_radius * 0.15)
    pygame.draw.circle(screen, black, (eye_x, eye_y), eye_radius)


    # Move ghost
    ghost_x, ghost_y, last_direction = random_walk_ghost(ghost_x, ghost_y, maze_walls, last_direction)

    # Draw ghost
    # Shape of the ghost body
    g_ghost_body = [
        (ghost_x - ghost_radius, ghost_y),
        (ghost_x - ghost_radius, ghost_y - ghost_radius * 2),
        (ghost_x + ghost_radius, ghost_y - ghost_radius * 2),
        (ghost_x + ghost_radius, ghost_y),
    ]

    # Shape of the ghost base (wavy)
    base_width = int(ghost_radius * 2 / 5)
    base_height = ghost_radius // 2
    g_ghost_base = []
    for i in range(5):
        offset = base_height if i % 2 == 0 else 0
        g_ghost_base.append((ghost_x - ghost_radius + i * base_width, ghost_y + offset))
    g_ghost_base.append((ghost_x + ghost_radius, ghost_y))

    # Draw ghost body
    pygame.draw.polygon(screen, ghost_color, g_ghost_body)

    # Draw ghost base
    pygame.draw.lines(screen, ghost_color, False, g_ghost_base, base_height)

    # Draw ghost eyes
    eye_x = ghost_x - ghost_radius // 2
    eye_y = ghost_y - ghost_radius
    pygame.draw.circle(screen, white, (eye_x, eye_y), int(ghost_radius * 0.25))
    pygame.draw.circle(screen, white, (eye_x + ghost_radius, eye_y), int(ghost_radius * 0.25))

    # Draw ghost pupils
    pupil_radius = int(ghost_radius * 0.1)
    pupil_x = eye_x + int(pupil_radius * 0.5) + (1 if last_direction[0] > 0 else -1 if last_direction[0] < 0 else 0)
    pupil_y = eye_y + int(pupil_radius * 0.5) + (1 if last_direction[1] > 0 else -1 if last_direction[1] < 0 else 0)
    pygame.draw.circle(screen, black, (pupil_x, pupil_y), pupil_radius)
    pygame.draw.circle(screen, black, (pupil_x + ghost_radius - pupil_radius, pupil_y), pupil_radius)

    # inside the main game loop
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Calculate how many seconds

    # Render the timer
    font = pygame.font.SysFont('Arial', 24)
    timer_text = font.render('Time: {:.1f}'.format(seconds), True, white)
    timer_rect = timer_text.get_rect(topleft=(10, 10))
    screen.blit(timer_text, timer_rect)
    
    # Update the display
    pygame.display.flip()

    if pygame.Rect(ghost_x - ghost_radius, ghost_y - ghost_radius, ghost_radius * 2, ghost_radius * 2).colliderect(pygame.Rect(pacman_x - pacman_radius, pacman_y - pacman_radius, pacman_radius * 2, pacman_radius * 2)):
        death_font = pygame.font.SysFont('Arial', 36)
        death_text = death_font.render('You Died!', True, white)
        death_rect = death_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(death_text, death_rect)
        pygame.mixer.Sound('lose.mp3').play()
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    if not dots:
        winning_font = pygame.font.SysFont('Arial', 36)
        winning_text = winning_font.render('You Win!', True, yellow)
        winning_rect = winning_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(winning_text, winning_rect)
        pygame.mixer.Sound('level-win-6416.mp3').play()
        pygame.display.flip()
        pygame.time.wait(3000)

        running = False

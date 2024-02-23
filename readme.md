
# Customizable Pac-Man Game 🕹️

This project is a Python-based Pac-Man 😀 game using Pygame, featuring customizable levels that users can edit with any text editor. The game is designed for those who wish to explore game development with Python and have a personalized gaming experience by modifying or creating new levels.
Currently we support running it on Windows. If you want to run it on other systems you'll have to figure it out.

## Features

- 🎮 **Simple Controls:** Use arrow keys for movement and the space bar to use Pac-Man's tongue.
- 🌽 **Customizable Maze**: Modify the game's maze by editing a simple text file.
- 👻 **Dynamic Ghost AI**: Ghosts randomly navigate the maze, adding unpredictability to each game.
- 😀 **Dot Collection**: Collect dots while avoiding ghosts.
- 🎵 **Custom Sounds and Graphics**: Includes themed sounds and colorful graphics for an immersive experience.

# Windows Download

To play on windows, get it from here: https://github.com/ZigZigPow/pacman-builder/releases

# For developers:

## Prerequisites:
1. git
2. python 3.9 or 3.10 (Maybe later versions will also work).

## Setup
1. Clone the repo  
`git clone https://github.com/ZigZigPow/pacman-builder.git`
2. Run setup_venv.bat
3. Run build.bat

## Running the Game
After setup the game will be available at:  
`pacman-builder\pacman_game\pacman.exe`  
or use python: navigate to the repo in command prompt and run the game with:

```
activate.bat
python pacman.py
```

## Customizing the Maze

To create your own unique maze for the Pac-Man game, follow these steps:

1. **Edit the Maze**: Open `mazes\maze.txt` or (`pacman-builder\pacman_game\_internal\mazes\maze.txt` for the built package) with a text editor. The maze is represented by characters:
   - ` ` s(space) for paths where the Pac-Man and the Ghost can move.
   - `@` sfor initial pacman location.
   - `U` for initial ghost locations.
   - Any other character for wall blocks.

3. **Design Your Maze**: Modify the arrangement of characters to shape your new maze. Be creative! Ensure there are no enclosed areas where Pac-Man or ghosts can get trapped.

4. **Save Your Changes**: After editing, save the `maze.txt` file.

5. **Test Your Maze**: Run the game to see your new maze in action. Make adjustments as needed to perfect your design.

Enjoy designing your own mazes for Pac-Man to navigate! 🎮👻

```
  ___         _       _ _            __           _     _          __                       _               _   
 |_ _|   __ _(_)_ __ ( ) |_    __ _ / _|_ __ __ _(_) __| |   ___  / _|  _ __   ___     __ _| |__   ___  ___| |_ 
  | |   / _` | | '_ \|/| __|  / _` | |_| '__/ _` | |/ _` |  / _ \| |_  | '_ \ / _ \   / _` | '_ \ / _ \/ __| __|
  | |  | (_| | | | | | | |_  | (_| |  _| | | (_| | | (_| | | (_) |  _| | | | | (_) | | (_| | | | | (_) \__ \ |_ 
 |___|  \__,_|_|_| |_|  \__|  \__,_|_| |_|  \__,_|_|\__,_|  \___/|_|   |_| |_|\___/   \__, |_| |_|\___/|___/\__|
                                                                                      |___/ 
```

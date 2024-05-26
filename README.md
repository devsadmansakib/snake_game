
# Pygame Snake Game

Welcome to the Pygame Snake Game! This is a simple implementation of the classic snake game using Pygame. You can play the game, score points, and restart or quit the game when it's over.

## Features

- **Control the snake** using the **WASD** keys.
- Eat the target to grow the snake and increase your score.
- The game ends if the snake goes out of bounds.
- Display the final score and provide options to restart or quit the game.

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install Pygame using pip:
   ```sh
   pip install pygame
   ```

3. Clone this repository or download the script file `snake_game.py`.

## How to Play

1. Run the game by executing the script:
   ```sh
   python snake_game.py
   ```

2. Control the snake using the following keys:
   - `W` to move up
   - `A` to move left
   - `S` to move down
   - `D` to move right

3. The objective is to eat the target (red square) to grow the snake and increase your score.

4. The game ends if the snake moves out of bounds. Your final score will be displayed.

5. When the game is over, you can:
   - Press `R` to restart the game.
   - Press `Q` to quit the game.

## Code Overview

### Main Loop

The game runs in a while loop, processing events, updating game state, and rendering graphics. The game state can be either `PLAYING` or `GAME_OVER`.

### Key Functions

- `generate_starting_position()`: Generates a random starting position for the snake and the target.
- `is_out_of_bounds()`: Checks if the snake has moved out of bounds.
- `draw_score(score, message="Score: ")`: Draws the current score on the screen.
- `show_game_over()`: Displays the game over message and final score.
- `reset_game()`: Resets the game state, initializing the snake and the target.

### Event Handling

The game handles key events to control the snake's movement and to restart or quit the game when it is over.

### Rendering

The game renders the snake, the target, and the score on the screen. The screen is cleared each frame and updated with the new positions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- This game is built using Pygame, a popular library for creating games in Python.

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

Enjoy the game and happy coding!

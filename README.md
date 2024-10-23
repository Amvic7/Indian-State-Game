# India States Guessing Game

Welcome to the **India States Guessing Game!** This interactive game challenges players to guess all the states of India. When a player correctly identifies a state, it will appear on the India map, making for an engaging and educational experience.

## Table of Contents
- [Features](#features)
- [How to Play](#how-to-play)
- [Code Explanation](#code-explanation)
- [Notes](#notes)

## Features
- **Interactive Gameplay:** Players can guess states using a simple input method.
- **Visual Feedback:** Correct guesses will be displayed on an interactive map of India.
- **Educational Tool:** Learn about Indian geography while having fun!

## How to Play
1. Start the game and view the map of India.
2. Input the name of a state you think is part of India.
3. If your guess is correct, the state will be highlighted on the map.
4. Continue guessing until all states are identified!

## Code Explanation
The game is built using the `turtle` graphics library in Python. Here’s a breakdown of how it works:

1. **Setup the Screen:**
   - The game window is created with a title and an image of the map of India.

   ```python
   screen = turtle.Screen()
   screen.title("India State Game")
   image = "India_map.gif"
   screen.addshape(image)
   turtle.shape(image)

   
## Notes
- Adjust the `main.py` in the setup instructions to match the actual filename of your main script.
- Ensure you have the `LICENSE` file included in your repository for the license section to be meaningful.
- Feel free to modify any sections to better fit your project!


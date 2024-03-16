# Quiz-Game
This Python code implements a simple quiz game where the user is asked questions and has to choose the correct answer from multiple choices. Here's a breakdown of the code:

1. It starts by defining a dictionary called `questions`, which contains questions as keys and their correct answer choices labeled 'A', 'B', 'C', or 'D'.
2. Another list named `options` contains corresponding answer choices for each question. Each inner list holds four options labeled 'A' through 'D'.
3. The `new_game()` function initiates the quiz. It iterates over the questions, presenting them along with their options to the user. The user is prompted to input their choice, and their response is validated until it matches 'A', 'B', 'C', or 'D'.
4. The `check_answer()` function compares the user's answer to the correct answer and provides feedback.
5. After answering all questions, the `show_score()` function displays the user's score.
6. The `play_again()` function asks the user if they want to play again. It validates the input until the user enters 'yes' or 'no', then returns a Boolean value accordingly.
7. The main part of the code starts the quiz with `new_game()`, then loops through `play_again()` to continue playing if the user chooses to do so.
8. Finally, it prints a farewell message when the user decides not to play again.

This code can be added to a GitHub repository with a description explaining its purpose and functionality, along with any necessary instructions for running or modifying the code.
### Note: I am studying from Bro Code so it may seem a little similar like his code, but trust me i did not copied his code but you know, I am learning from him so his and mine methods would be little similar. 

:)

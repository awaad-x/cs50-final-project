
🎯 Guess The Number
video demo: https://youtu.be/IGV-1L75RAc?si=23d0pPbVrN6aOPZz


Python Version Description:

"Guess The Number" is a desktop-based interactive game developed using Python, designed to provide an engaging and user-friendly experience while demonstrating fundamental programming concepts and graphical user interface (GUI) design. The game is built using the customtkinter library, which enhances the traditional Tkinter interface by providing modern UI components, improved styling, and support for both dark and light modes.

The main objective of the game is for the player to guess a randomly generated number within a limited number of attempts and within a specific time limit. Although the concept is simple, the implementation includes several advanced features that improve user interaction and make the gameplay more dynamic and enjoyable.

When the application is launched, the player is first presented with a start screen. This screen serves as the main menu of the game and allows the user to configure key settings before starting. The player can select the desired difficulty level, which directly affects the complexity of the game. The available difficulty levels are Easy, Medium, and Hard. Each level modifies important parameters such as the maximum number of attempts allowed and the range within which the random number is generated. For example, Easy mode provides a smaller range and more attempts, while Hard mode increases the range significantly and reduces the number of attempts, making the game more challenging.

In addition to difficulty selection, the start screen also allows the player to choose the visual theme of the application. The game supports Dark Mode, Light Mode, and System Mode, giving the user flexibility in terms of appearance. This feature is implemented using the built-in appearance settings of the customtkinter library, which dynamically updates the UI elements based on the selected theme.

Once the player presses the "Start Game" button, the application transitions to the main game screen. At this point, a random number is generated using Python’s random module. The player interacts with the game through an input field where they can enter their guesses. The interface is designed to be intuitive and responsive, allowing the user to either click a submit button or press the "Enter" key to submit their guess.

After each guess, the game provides immediate feedback. If the entered number is greater than the target number, the game displays a "Too High" message. If it is lower, a "Too Low" message is shown. Additionally, a hint system is implemented to enhance gameplay; if the player’s guess is very close to the correct number, a "Very Close" message is displayed. This helps guide the player and adds an extra layer of interaction.

A key feature of the game is the attempt tracking system. The player has a limited number of attempts, which decreases with each guess. The remaining attempts are displayed on the screen in real-time. This encourages strategic thinking and prevents random guessing. If the player uses all available attempts without guessing the correct number, the game ends and the correct number is revealed.

Another important component is the countdown timer. The player is given a fixed amount of time to guess the number. The timer continuously updates every second, creating a sense of urgency. If the timer reaches zero before the player successfully guesses the number, the game automatically ends. This time constraint adds excitement and increases the difficulty level.

The game also features a scoring system. The player’s score is calculated based on the number of remaining attempts when the correct number is guessed. The fewer attempts used, the higher the score. Additionally, the game keeps track of the best score achieved during the session. This encourages replayability, as players are motivated to improve their performance and achieve a higher score.

From a user interface perspective, the game includes several visual enhancements. For example, the input field changes color to provide feedback: it briefly turns red when the player makes an incorrect guess and green when the correct number is guessed. A shaking animation is also applied to the window when the player enters a wrong guess, adding a dynamic and interactive feel to the game.

The application is structured using modular functions to separate logic and interface handling. Functions are used for starting the game, updating the timer, checking guesses, calculating scores, and resetting the game. This modular approach improves code readability, maintainability, and scalability.

Overall, "Guess The Number" demonstrates the practical application of Python programming concepts such as conditionals, loops, event-driven programming, and GUI development. It also showcases the use of external libraries like customtkinter to create modern and visually appealing desktop applications.

In conclusion, this project successfully combines simplicity with functionality, resulting in a game that is both entertaining and educational. It highlights the developer’s ability to design interactive software with a clean interface and structured logic, making it a strong example of a beginner-to-intermediate level Python project.

# Quiz Application
This project is a simple command-line quiz application built in Python. The quiz fetches questions from the Open Trivia Database API and allows users to answer true/false questions. It is a fun way to test your knowledge on various topics and improve your trivia skills.

## Description
The Quiz Application:

- Fetches a specified number of easy, true/false questions from the Open Trivia Database API.
- Presents each question to the user in the command line interface.
- Prompts the user to answer each question with 'y' (yes/true) or 'n' (no/false).
- Keeps track of the user's score and displays it at the end of the quiz.

## How It Works
Fetching Questions: The application makes a request to the Open Trivia Database API to retrieve a list of questions.
Processing Questions: Special HTML characters in the questions are converted to their original form using html.unescape.
Quiz Execution: The user is prompted with each question and asked to respond with 'y' or 'n'. The application checks the user's answer against the correct answer and keeps a score.
Scoring: At the end of the quiz, the user's score is displayed.

Installation
1. Clone the Repository:
git clone https://github.com/your-username/quiz-application.git
cd quiz-application
2. Install Dependencies:
Ensure you have Python installed. You can install the required dependencies using pip:
pip install requests

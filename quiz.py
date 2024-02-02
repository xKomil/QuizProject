import requests
import html
# html.unescape zamienia znaki specjalne na ich oryginalne znaczenie, np. &quot; -> " lub &amp; -> &

class Question:
    def __init__(self, category, questionStr, correctAnswerFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag


class Quiz:
    def __init__(self, numQuestions):
        self.apiURL = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questionsList = []
        self.loadQuestions(numQuestions)

    def loadQuestions(self, numQuestions):
        response = requests.get(self.apiURL + str(numQuestions))
        # {'response_code': 0, 'results': [{'type': 'boolean', 'difficulty': 'easy', 'category': 'Mythology',  'question': 'A wyvern is the same as a dragon.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
        if response.ok :
            #print(response.json())
            data = response.json()
            results = data['results']
            for q in results:
                category = html.unescape((q["category"]))
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape(q["question"])
                print(questionStr)
                correctAnswerFlag = q["correct_answer"].lower() in ["true", "1", "yes"]

                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questionsList.append(qObj)

    def startQuiz(self):
        print("\nWelcome in quiz!")
        numCorrectUserAnswers = 0
        n = 0
        numQuestions = len(self.questionsList)

        while( n < numQuestions):
            q = self.questionsList[n]
            print("Question number " + str(n)  + ": " + q.questionStr)
            print("Anserw flag: ", q.correctAnswerFlag)

            answer = input("Give correct answer as y/n: ")
            answerBool = False
            if answer == "y": answerBool = True

            if answerBool == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers += 1
            else:
                print("Wrong!")

            n += 1

        print(f"Your score is: {numCorrectUserAnswers}/{numQuestions}")


quiz = Quiz(10)
quiz.startQuiz()
from Question import Question

questions = [
    "What is the capital of Great Britain?\n (a) Maralik \n (b) London \n (c) Wales \n (d) Pyatigorsk",
    "What is the sum of  5 + 10?\n (a) -15 \n (b) 1.5 \n (c) 15 \n (d) 36.6",
    "How you say a beat in face with an open hand in armenian?\n (a) qaci \n (b) harvats \n (c) hrasment \n (d) chapalax"
]


q = [
    Question(questions[0], "b"),
    Question(questions[1], "c"),
    Question(questions[2], "d")
]


def play_game(q):
    score = 0
    for question in q:
        answer = input(question.prompt + "\n Your answer: ")
        if answer == question.answer:
            score = score + 1
    print("You got " + str(score) + "/" + str(len(q)) + " completed.")


play_game(q)

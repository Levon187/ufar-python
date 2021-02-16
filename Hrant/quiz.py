from lesson7 import Question


def play_quiz():
    question = ""
    score = 0
    with open("quiz_ques_ans.txt", "r") as quiz_file:
        all_lines = quiz_file.readlines()
        i = 0
        for line in all_lines:
            i += 1
            if "answer: " in line:
                ans = line[8]
            else:
                question += line
            if i == 6:
                print("\n")
                print(question)
                user_ans = input("You answer: ")
                if user_ans == ans:
                    score += 1
                i = 0
                question = ""
        print("\n")
        print("Your score is ", score, "/ 3")


play_quiz()

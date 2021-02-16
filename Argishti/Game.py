from Question import Question

# lines starting from 0
def lineCaller(where, fromLine, toLineIncluding):
    to = ""
    file = open(where, 'r')
    if(fromLine > -1):
        for x in range(0, fromLine):
            file.readline()
    for x in range(fromLine, toLineIncluding+1):
        to = to + file.readline()
    return to

a = Question(lineCaller('quests.txt', 0, 4).rstrip(), lineCaller('quests.txt', 5, 5)[-2])

list_of_q_and_a = [Question(lineCaller('quests.txt', 0, 4), lineCaller('quests.txt', 5, 5)[-2]),
                   Question(lineCaller('quests.txt', 6, 10), lineCaller('quests.txt', 11, 11)[-2]),
                   Question(lineCaller('quests.txt', 12, 16), lineCaller('quests.txt', 17, 17)[-2])]


def play_game(q):
    score = 0
    for question in q:
        answer = input(question.question + "Your answer: ")
        if answer == question.answer:
            score = score + 1
    print("You got " + str(score) + "/" + str(len(q)) + " completed.")


play_game(list_of_q_and_a)

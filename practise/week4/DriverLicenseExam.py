def main():
    read_question()


def read_question():
    file = open("questions.txt", "r")
    answer_list = ["A","B", "C", "D"]
    selected_answer = []
    question_list = file.readlines();
    #print(question_list)
    for i in range(len(question_list)):
        if question_list[i] != "###\n":
            print(question_list[i])
        if question_list[i] == "###\n" or i == (len(question_list)-1):
            while True:
                try:
                    answer = input("Answer: ").upper()
                    if answer not in answer_list:
                        print("Choose A/B/C/D only.")
                        continue
                    else:
                        selected_answer.append(answer)
                        break
                except ValueError:
                    print("Choose A/B/C/D ony")
                    continue
    file.close()
    #print(selected_answer)
    print("Your answer: ", selected_answer)
    check_answer(selected_answer)
    # write_answer(selected_answer)


# def write_answer(selected_answer):
#     f = open("answer.txt","a")
#     count = 0
#     for ans in selected_answer:
#         count += 1
#         f.write(count, ": ", ans, "\n")
#     f.close()
#     check_answer(selected_answer)


def check_answer(selected_answer):
    f = open("answer.txt", "r")
    result = []
    count = 0
    ans_list = f.readlines()
    for ans in ans_list:
        ans.strip()
        answer = ans.split(": ")
        answer = answer[1].split("\n")
        result.append(answer[0])
    print("Correct answer: ", result)
    for i in range(len(result)):
        #print(i)
        if result[i] == selected_answer[i]:
           count += 1
    if count >= 5:
        print("Pass with ", count, " correct answers")
    else:
        if count >= 2:
            print("Fail with ", count, " correct answers")
        else:
            print("Fail with ", count, " correct answer")
    # print(answer)
    # print(result)
    # print(list_anwser)


main()

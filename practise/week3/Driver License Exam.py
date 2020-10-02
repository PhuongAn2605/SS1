def main():
    list_answer = []
    str_ans = ""
    answer_list = ["A", "B", "C", "D"]
    for i in range(3):
        while True:
            try:
                print("Question ", ques_dic[i])
                answer = str(input("Answer: "))
                answer = answer.upper()
                if answer not in answer_list:
                    print("Choose A/B/C/D only.")
                    continue
                else :
                    list_answer.append(answer)
                    break
            except ValueError:
                print("Choose A/B/C/D only.")
                continue
    for ans in list_answer:
        str_ans += ans
    return check_answer(str_ans)


ques_dic = [
   "Làn đường là gì?\nA. Là một phần của phần đường xe chạy được" 
       "chia theo chiều dọc của đường, sử dụng cho xe chạy.\B. Là một phần của phần đường xe chạy được chia"
       "theo chiều dọc của đường, có bề rộng đủ cho xe chạy an toàn.\nC. Là đường cho xe ô tô chạy, dừng, đỗ an toàn.\nD.Tat ca",
"Làn đường là gì?\nA. Là một phần của phần đường xe chạy được" 
       "chia theo chiều dọc của đường, sử dụng cho xe chạy.\B. Là một phần của phần đường xe chạy được chia"
       "theo chiều dọc của đường, có bề rộng đủ cho xe chạy an toàn.\nC. Là đường cho xe ô tô chạy, dừng, đỗ an toàn.\nD.Tat ca",
"Làn đường là gì?\nA. Là một phần của phần đường xe chạy được" 
       "chia theo chiều dọc của đường, sử dụng cho xe chạy.\B. Là một phần của phần đường xe chạy được chia"
       "theo chiều dọc của đường, có bề rộng đủ cho xe chạy an toàn.\nC. Là đường cho xe ô tô chạy, dừng, đỗ an toàn.\nD.Tat ca"
]


def check_answer(str_ans):
    correct_answer = ["A", "C", "A"]
    counter = 0
    index = 0
    for ans in str_ans:
        index += 1
        ans = ans.upper()
        if ans == correct_answer[index-1]:
            counter += 1
    if counter >= 2:
        print('Pass exam with ', counter ,' correct answers.')
    else :
        print('Fail exam with ',counter ,' correct answer.')


main()

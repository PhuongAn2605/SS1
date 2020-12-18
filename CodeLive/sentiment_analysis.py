def main():
    # list_data = read_file("training.txt")
    # list_word = get_word(list_data)
    # # print(list_word)
    # create_dict_word(list_word)

    list_choices = ["1", "2", "3", "4", "5"]
    cont = True
    while(cont == True):
        print("What would you like to do? \n"
              "1: Get the score of a word\n"
              "2: Get the average score of words in a file\n"
              "3: Find the highest / lowest scoring words in a file\n"
              "4: Sort the words into positive.txt and negative.txt\n"
              "5: Exit the program\n"
              "Enter a number 1 – 5:")

        try:
            choice = input()
            if choice not in list_choices:
                print("Choose 1 - 5:")
                continue
            else:
                if choice == "1":
                    word = input("Which word?")
                    list_data = read_file("training.txt")
                    list_word = get_word(list_data)
                    # print(list_word)
                    # print(list_word)
                    dict_words = create_dict_word(list_word, word)
                    print(dict_words)

                elif choice == "2":
                    file = input("file name?")
                elif choice == "3":
                    f = input("file name?")
                elif choice == "4":
                    print("output")
                elif choice == "5":
                    cont = False
                    print("Goodbye.")

        except ValueError:
            print("Choose 1-5 only.")
            continue


def read_file(filepath):
    file = open(filepath, "r")
    list_data = file.readlines()
    for i in range(len(list_data)):
        list_data[i] = list_data[i].strip()
    return list_data

def get_word(list_data):
    list_word = []

    for i in range(len(list_data)):
        words = []
        # print(list_data[i])
        words = list_data[i].split(" ")
        # print(words)
        words[0] = int(words[0])
        l = len(words)

        for j in range(1, l):
            for c in words[j]:
                c.lower()
                num = ord(c)
                if num not in range(48, 53) and num not in range(97, 123):
                    # print(num)
                    # print(w)
                    words[j] = words[j].replace(c, "")
        list_word.append(words)
    return list_word

def create_dict_word(list_word, word):
    # print(list_word)
    dict_words= {}
    list_sen = []
    words = []

    score = []
    for list in list_word:
        score.append(list[0])
    # print(score)
    l = len(score)
    appear= []
    print(score)
    for list in list_word:
        score.append(list[0])

        for i in range(len(list)):
            dict_words[list[i]] = appear
    # print(dict_words)
    # temp_appare = appare
    for i in range(len(list_word)):
        for j in range(len(list_word[i])):
            temp_appear =[]
            for key in dict_words:
                if list_word[i][j] == key:
                    # print(dict_words[key])
                    dict_words[key].append(score[i])
                    # print(dict_words)
                    # temp_appear = dict_words[key]
                    # print(temp_appear)
                    # temp_appear.append(score[i])
                    # dict_words[key] = temp_appear
        # print(dict_words)
    # print(dict_words)
    sum = 0
    avg = 0
    count = 0
    for key in dict_words:
        for i in range(len(dict_words[key])):
            if dict_words[key][i] != 0:
                count += 1
                sum += dict_words[key][i]
            avg = sum/count
    print(avg)


    # for i in range(len(list_word)):
    #     appear= []
    #
    #     # print(dict_words)
    #     for j in range(len(list_word[i])):
    #         temp_appear = []
    #         for key in dict_words:
    #             # if key == list_word[i][j]:
    #             temp_appear = dict_words[key]
    #             temp_appear.append(score[i])
    #             dict_words[key] = temp_appear
    print(dict_words)
    return dict_words


main()


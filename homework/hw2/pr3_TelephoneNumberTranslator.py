def main():
    # ask user enter a phone number in format XXX-XXX-XXXX
    phone_number = input("Enter a phone number in format XXX-XXX-XXXX: ")
    # split phone number by '-'
    list_separate = phone_number.split('-')
    # Take the second XXX in input
    second_number = number_translator(list_separate[1])
    # Take the third element XXXX
    third_number = number_translator(list_separate[2])
    # print(list_separate[0], '-', end='')

    # Print in form of number
    print(list_separate[0], end='')
    print('-', end='')
    for j in second_number:
        print(j, end='')
    print('-', end='')
    for n in third_number:
        print(n, end='')


def number_translator(string):
    # Store alphabet with number accordingly
    alpha_dic = {
        ("A", "B", "C"): 2,
        ("D", "E", "F"): 3,
        ("G", "H", "I"): 4,
        ("J", "K", "L"): 5,
        ("M", "N", "O"): 6,
        ("P", "Q", "R", "S"): 7,
        ("T", "U", "V"): 8,
        ("W", "X", "Y"): 9
    }
    # Local list to store number accordingly match letter in string
    number_list = []
    # Find number in alpha_dic equaling to letter in string
    for n in string:
        for i in alpha_dic:
            for j in i:
                if j == n:
                    number_list.append(alpha_dic[i])
    return number_list


main()

def main():
    argument = input("Enter an argument: ")
    num = count(argument)
    print("Number of vowels: ", num[0], ", number of consonants: ", num[1])


def count(string):
    string = string.lower()
    list_vowels = ['u', 'e', 'o', 'a', 'i']
    num = [0, 0]
    for n in string:
        if n.isalpha():
            if n in list_vowels:
                num[0] = num[0] + 1
            else :
                num[1] = num[1] + 1
    return num


main()


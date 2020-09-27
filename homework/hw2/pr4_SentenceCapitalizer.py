def main():
    argument = input("Enter an argument: ")
    print(capitalize(argument))


def capitalize(string):
    # Split string by '. '
    list_argu = string.split('. ')
    # Initialze local variable string_argu to store string after capitalized
    string_argu = ''
    # Capitalize the first letter of each sentence and store in string_argu
    for i in list_argu:
        string_argu = string_argu + i.capitalize() + '. '
    return string_argu


main()


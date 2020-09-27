def main():
    string = input("Enter a string: ")
    print("The most frequence character: ", most_frequence(string))


def most_frequence(string):
    counter = 0
    max_count = 0
    most_fre_char = ''
    # Count the same characters in string
    for ch in string:
        for str in string:
            if ch == str:
                counter += 1
        # Find the most frequence character in string by
        # compare counter to max_count and store the character
        if counter > max_count :
            max_count = counter
            most_fre_char = ch

        # Assign count = 0 to find frequence of next character
        counter = 0
    return most_fre_char


main()


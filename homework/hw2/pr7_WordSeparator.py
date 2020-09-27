def main():
    sentence = input("Enter a sentence in which all of the words are"
                     "run together \nbut the first character of each word is uppercase: ")
    print(convert(sentence))


def convert(string):
    # Store the first character in local variable sen as a unique upper character in the sentence
    sen = string[0]
    # Start from second character and check
    # if it is uppper then convert it to lower and append to the sen with space at start
    # if it is lower then append directly to the sen
    for ch in string[1:]:
        if ch.isupper():
            sen += ' ' + ch.lower()
        else :
            sen += ch
    return sen


main()

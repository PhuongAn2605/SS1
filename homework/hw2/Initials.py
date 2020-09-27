# Programming Exercise_1

def main():
    # Get a string containing a persons first, middle, and last name as input from the user.
    name_string = input('Enter a string containing a persons '
                        'first, middle, and last names: ')
    # Call name_initials method and store the list_initials
    list_initials = name_initials(name_string)
    # print all elements in list_initials include '. '
    for n in list_initials:
        print(n, end='. ')


# The name_initials method receives a string and returns
# The string contains a person first, middle, and last name
def name_initials(string):
    # Split string into 3 parts: first, middle and last name
    list_separate = string.split(' ')
    # Local variable as a list
    list_initials = []
    # Convert the first character of each string in list_separate to uppercase
    # Add the items in list_separate at the end of list_initials
    for i in list_separate:
        list_initials.append(i[0:1].title())

    #return the list_initials
    return list_initials

# Call the main function
main()




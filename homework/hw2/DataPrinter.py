def main():
    # Ask user enter a date in form mm/dd/yyyy
    date = input('Enter a date in the form mm/dd/ yyyy: ')
    # Split date by '/' and store in a list
    list_form = date.split('/')
    # Take the value of date
    month = read_date(list_form[0])
    # print name of month, day year
    print(month, list_form[1], ',', list_form[2])


# Function read_date receives a string and return month in text
def read_date(string):
    # Cast string to integer and store it in m
    m = int(string)
    # Dictionary has key is months in text and
    # value is months in number from 1 to 12
    month_dic = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    # Take the month has value equaling parameter string and return
    for month in month_dic:
        if month_dic[month] == m:
            return month


# Main function
main()

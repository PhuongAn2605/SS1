# Dictonary of number has 3 group: units(from 1 to 9),
# teens(from 11 to 19) and tens(from 10 to 90)
number_dic = {
    1:"mốt",
    2: "hai",
    3: "ba",
    4: "bốn",
    5: "năm",
    6: "sáu",
    7: "bảy",
    8: "tám",
    9: "chín",

    11: "mười một",
    12: "mười hai",
    13: "mười ba",
    14: "mười bốn",
    15: "mười năm",
    16: "mười sáu",
    17: "mười bảy",
    18: "mười tám",
    19: "mười chín",

    10: "mười",
    20: "hai mươi",
    30: "ba mươi",
    40: "bốn mươi",
    50: "năm mươi",
    60: "sáu mươi",
    70: "bảy mươi",
    80: "tám mươi",
    90: "chín mươi"
}
# Store the level of number from thousand to trillion
thousand = 1000
million = thousand * 1000
billion = million * 1000
trillion = billion * 1000


# Main function
def main():
    # Ask user enter number separated by ','
    number = input("Enter a string of number separated by (','): ")
    # Split number by ','
    num_list = number.split(',')
    str = ''
    # Append number to local variable str with no separator
    for n in num_list:
        str += n
    number = int(str)
    # Print number in text
    print(num_text(number), 'đồng chẵn.')


# Function num_text converts number to text and returns
def num_text(num):
    # If num less than 20 then return the value accordingly in num_dic
    if num < 20:
        return number_dic[num]
    # If num less than 100 and if num divided by 10 return value in num_dic
    # else find the units and return
    if num < 100:
        if num % 10 == 0 :
            return number_dic[num]
        else:
            return number_dic[num // 10 * 10] + ' ' + number_dic[num%10]
    # If num less than thousand and num divided by 100 then return value
    # and add 'tram' at the end
    # else find units by recursive
    if num < thousand:
        if num % 100 == 0 :
            return number_dic[num // 100] + ' trăm'
        else:
            return number_dic[num // 100] + ' trăm ' + num_text(num % 100)
    # If num less than million and num divided by 1000 then return value
    # and add 'nagn' at the end
    # else find units by recursive
    if num < million :
        if num % 1000 == 0 :
            return num_text(num // thousand) + ' ngàn'
        else :
            return num_text(num // thousand) + ' ngàn ' + num_text(num % thousand)
    # If num less than billion and num divided by million then return value
    # and add 'trieu' at the end
    # else find units by recursive
    if num < billion :
        if num % thousand == 0:
            return num_text(num // million)+ ' triệu'
        else :
            return num_text(num // million) + ' triệu ' + num_text(num % million)
    # If num less than trillion and num divided by billion then return value
    # and add 'ti' at the end
    # else find units by recursive
    if num < trillion:
        if num % billion == 0:
            return num_text(num // billion) + ' tỉ'
        else :
            return num_text(num // billion) + ' tỉ ' + num_text(num % billion)
    # If num less than trillion and num divided by trillion then return value
    # and add 'nghin ti' at the end
    # else find units by recursive
    if num % trillion == 0:
        return num_text(num // trillion) + ' nghìn tỉ'
    else:
        return num_text(num//trillion) + ' nghìn tỉ' + num_text(num % trillion)


main()

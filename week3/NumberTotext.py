number_dic = {
    "mot": 1,
    "hai": 2,
    "ba": 3,
    "bon": 4,
    "nam": 5,
    "sau": 6,
    "bay": 7,
    "tam": 8,
    "chin": 9
}
number = input("Enter a string number: ")
list1 = []
list2 = []
list3 = []
list = []
list4 = []
list5 = []
b = 0
len_num = len(number)
len_num = len_num // 3
left = len_num % 3

#separate number
for i in range(len_num+1) :
    if 3*i <= len_num * 3 :
        num1 = number[3*i : 3*i+3]
        list.append(num1)
        num1 = 0

#first number
for n in range(left) :
    for m in number_dic :
        if number[n] == m :
            list1.append(number_dic[m])
#3*number
for i in range(len(list)):
    for j in list[i] :
        for m in number_dic :
            if j == m :
                list4.append(number_dic[m])
#read
if left == 1:
    print(list1[0], ' ', list1[1], "ngan", end='')
elif left == 2:
    print(list1[0], ' ', list1[1], "trieu", end='')
elif  left == 3:
    print(list1[0], ' ', list1[1], "ti", end='')
for h in range(len(list4)):
    if 3*h <= len(list4) :
        list5.append(list4[3*h:3*h+3])
    if len_num == 3:
        print(list[0], " tram ", list[1], " muoi ", list[2])
    if len_num == 6:
        print(list[0], " tram ", list[1], " muoi ", list[2], " ngan ", list[3], " tram ", list[4], " muoi ", list[5])

def main():
    RSA(667, 937, 2537)
    RSA(37,53,77);


def RSA(a, b, n):
    b_binary = bin(b)
    binary = b_binary[2:]
    list_binary = []
    list_index = []
    list_mod = []
    print(binary)
    for i in binary:
        list_binary.append(i)
    list_binary.reverse()
    #print(list_binary)
    for j in range(len(list_binary)):
        if int(list_binary[j]) == 1:
            #print(list_binary[j])
            list_index.append(j)
            #print(list_index)
    mod = calculateModular(a, n)
    print(mod)
    for i in range(len(list_binary)):
        mod = calculateModular(mod, n)
        list_mod.append(mod)
        #print(mod)
        mod = pow(mod, 2)
        #print(list_mod)
    result = 1
    for i in range(len(list_mod)):
        if i in list_index:
            result = int(result*list_mod[i])
    print(calculateModular(result, n))


def calculateModular(a,b):
        return a%b

main()

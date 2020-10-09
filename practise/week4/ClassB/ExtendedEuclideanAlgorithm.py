def main():
    calculateModular(15,1,26)
    calculateModular(29, 1, 48)
    calculateModular(28,8,48)


def calculateModular(a,b,n):
    mod = n
    p = []
    x =[]
    p.append(0)
    p.append(1)
    quotient = []
    remainder = []

    print('p0 = ', p[0])
    print('p1 = ', p[1])


    while n%a != 0:
        q = n//a
        #print(q)
        r = n%a
        n= a
        a = r
        quotient.append(q)
        remainder.append(r)
    for i in range(len(quotient)):
        p.append(p[i+2-2] - p[i+2-1]*quotient[i])
        while p[i+2] < 0:
            p[i+2] = p[i+2] + mod
        while p[i+2] > mod:
            p[i+2] = p[i+2] - mod
        print('p', i, ' = ', p[i+2-2], '-', p[i+2-1], '*', quotient[i], ' mod ', mod,  ' = ',p[i+2] )
    print('t = ', p[len(p)-1])
    if b > 1:
        d = remainder[len(remainder)-1]
        x.append((p[len(p)-1]*b)//d)
        while x[0] < 0:
            x[0] = x[0] + mod
        while x[0] > mod:
            x[0] = x[0] - mod
        i = -1
        while (x[0] + i*(mod//d)) < mod and (x[0]+i*(mod//d) > 0):
            x.append(x[0] + i*(mod//d))
            i -= 1
        x.sort()
        print('x = ', x)
    print('---------------------------------------------------------')

main()

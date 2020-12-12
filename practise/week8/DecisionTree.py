import math
def main():
    # entropy (x[a, b])
    overal = [4, 6]
    h_overal = entropy(overal)
    sum = overal[0] + overal[1]

    source = {
        "red": [2, 3],
        "white": [2, 1],
        "pink": [2, 0]
    }

    choice = {
        "meat": [6, 4],
        "source": source,
        "seafood": [2, 8]
    }

    meat = [6, 4]
    h_meat = entropy(meat)

    source = [6, 4]
    red = [2, 3]
    h_red = entropy(red)
    white = [2, 1]
    h_white = entropy(white)
    pink = [2, 0]
    h_pink = entropy(pink)

    h_sum = ((red[0] + red[1])/sum)*h_red + ((white[0] + white[1])/sum)*h_white + ((pink[0] + pink[1])/sum)*h_pink

    h_source = round(entropy(source) - h_sum, 2)

    seafood = [2, 8]
    h_seafood = entropy(seafood)
    h_overal = entropy(overal)
    #print("%.2f"%h_pink)
    print(h_red)
    print(h_white)
    print(h_source)

    #print("%.2f"%h_seafood)

    list_decision = {
        "meat": 0,
        "source": 0,
        "seafood": 0
    }

    #print(list_decision["meat"])
    list_decision["meat"] = h_meat
    list_decision["source"] = h_source
    list_decision["seafood"] = h_seafood

    gain ={}
    gain["meat"] = h_overal - h_meat
    gain["source"] = h_overal - h_source
    gain["seafood"] = h_overal - h_seafood

    sorted_decision = sorted(list_decision.items(), key=lambda x: x[1], reverse=True)
    print(sorted_decision)
    print(gain)




def entropy(x):
    sum =x[0] + x[1]
    #print(sum)
    h = 0
    for i in x:
        #print(i)
        if i == 0:
            h = 0
        else:
            p = i / sum
            #print(p)
            h = (h + (-p * math.log(p, 2)))

    return round(h, 2)


main()



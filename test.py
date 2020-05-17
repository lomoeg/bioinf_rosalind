def isCorrect(num):
    one = 0
    two = 0
    seven = 0
    nine =0
    for i in range(8):
        if num % 10 == 1:
            one += 1
        if num % 10 == 2:
            two += 1
        if num % 10 == 7:
            seven += 1
        if num % 10 == 9:
            nine += 1
        num //= 10
        print(num)
    if one != 4 or two != 1 or seven != 1 or nine != 2:
        return False
    else:
        return True


print(isCorrect(11114799))
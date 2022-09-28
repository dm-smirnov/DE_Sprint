def isPalindrom(str):
    print("'%s' is palindrom?" % str)
    str = str.replace(' ', '')
    for pos in range(0, len(str) // 2):
        pos2 = len(str)-pos-1
        if str[pos] != str[pos2]: return False
    return True

print(isPalindrom('taco cat'))
print(isPalindrom('rotator'))
print(isPalindrom('black cat'))
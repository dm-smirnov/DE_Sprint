romanMap = (('M', 1000), 
            ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
            ('XC', 90),  ('L', 50),  ('XL', 40),  ('X', 10),   
            ('IX', 9),   ('V', 5),   ('IV', 4),   ('I', 1)
           )

def toRoman(decValue):
    initialDecValue = decValue
    result = ""
    if decValue > 0:
        for ch, digit in romanMap:
            while decValue >= digit:
                result += ch
                decValue -= digit
        print('%4d -> %s' % (initialDecValue, result))
    return result

toRoman(3)
toRoman(9)
toRoman(1945)
toRoman(123)
toRoman(456)
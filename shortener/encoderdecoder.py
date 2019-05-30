#For Encoding and Decoding URLS

# Creating ShortURLs
def toBase62(num):
    # Set of characters
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)

    retrun_value = []

    while num>0:
        value = num % base
        retrun_value.append(characters[value])
        num = num // base
    return ''.join(retrun_value[::-1])

# Decoding ShortURLs
def toBase10(str):
    #Set of characters
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    strlen = len(str)
    num = 0
    x = 0

    for char in str:
        power = (strlen - (x + 1))
        num += characters.index(char)*(base**power)
        x +=1
    return num
import string
slovar =  {}
def count_letters(text):
    for i in text:
        slovar[i] = text.count(i)
'''print(slovar)
count_letters('aaaaaaaabbbbbbbbbbbbewrfwaaaaaaaaaaaa')
print(slovar)'''

def dict_string(string):
    dictionary = {}
    seen = ""
    for char in string:
        if char not in seen:
            dictionary[char] = string.count(char)
            seen += char
    return dictionary


def prepoda(text):
    return {ch: text.count(ch) for ch in string.ascii_letters}

a = input()
print(prepoda(a))
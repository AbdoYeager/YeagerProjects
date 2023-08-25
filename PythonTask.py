# Reverse Words in a Sentence:

"""sentence = str(input("Write somthing: "))
print(sentence[::-1])"""

# Title Case Converter:

"""sentence = str(input("Write something: "))
print(sentence.title())"""

#  String Encryption:

"""letter = str(input("Enter a letter: "))
if letter == 'z':
    print('a')
elif letter == 'Z':
    print('A')
else:
    print(chr(ord(letter) + 1))"""

# Vowel Count and Replace:

string = str(input("Write something: "))
string = string.replace('a', '1')
string = string.replace('A', '1')
string = string.replace('e', '2')
string = string.replace('E', '2')
string = string.replace('i', '3')
string = string.replace('I', '3')
string = string.replace('o', '4')
string = string.replace('O', '4')
string = string.replace('u', '5')
string = string.replace('U', '5')
print(string)
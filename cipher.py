alphabet = "abcdefghijklmnopqrstuvwxyz"
word = input("Enter youx text to be encryted: ")
key = 29
encrypted = ''

for c in word:
    if c in alphabet:
                        encrypted += alphabet[(alphabet.index(c)- key) % (len(alphabet))]

print('your encrypted text is: ' + encrypted)

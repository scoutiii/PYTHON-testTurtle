word = "bc2fg57="
word = list(word)
print(chr(ord('b')-1))

for i in range(0, 8):
    print(chr(ord(word[i])-i))

'''Michael Rud, 350787156'''

def ceaser_cypher(word, shift):
    encrypted_word = ''
    for char in word:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)

            encrypted_word += encrypted_char

        else:
            encrypted_word += char

    return encrypted_word

print(ceaser_cypher(word=input("Enter a message: "), shift=int(input("Enter a shift: "))))


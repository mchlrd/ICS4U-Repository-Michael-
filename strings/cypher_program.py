'''Michael Rud, 350787156'''

def ceaser_cypher(word, shift):

    '''
    The function takes word and shift variables as arguments and uses a for loop to check for all characters in word.
    If the character is present in the alphabet - taking the digital data from ascii table of the letter a or A if char is uppercase.
    Then ascii_offset is being subtracted from the digital data of our character and shift being added.
    To ensure that all words are in the alphabet we are keeping it in the range of 26 (letters in the alphabet) and adding
    ascii_offset to it. Then converting it back to a character and adding to an empty string. If the character is not in the alphabet
    then its just being added to the empty string which returns after.
    '''
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


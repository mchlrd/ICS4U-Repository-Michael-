def string_cleaner(text):
    result = ''

    for character in text:
        if character.isalpha():
            result = result + character
        else:
            pass
    return result

value = string_cleaner("Hell0 Worl9")

print(f"The cleaned string is {value}")
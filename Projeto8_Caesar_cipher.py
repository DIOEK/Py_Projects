alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(user_text, desired_shift, user_direction):
    return_text = ""
    if user_direction == "decode":
        desired_shift *= -1
    for letter in user_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + desired_shift
            return_text += alphabet[new_position]
        else:
            return_text += letter
    print(f"The {user_direction}d text is {return_text} ")

caesar(user_text=text,desired_shift=shift,user_direction=direction)
# Ceasar Cipher

while True:

    def Encrypt(letter, shift):
        letter_ord, starting_ord, ending_ord = Get_Ordinal(letter)

        if letter_ord + shift > ending_ord:  # letter + shift > last letter
            return_ordinal = (starting_ord - 1) + (shift - (ending_ord - letter_ord))
        else:
            return_ordinal = letter_ord + shift

        return chr(return_ordinal)

    def Decode(letter, shift):
        letter_ord, starting_ord, ending_ord = Get_Ordinal(letter)

        if letter_ord - shift < starting_ord:
            return_ordinal = (ending_ord + 1) - (shift - (letter_ord - starting_ord))
        else:
            return_ordinal = letter_ord - shift

        return chr(return_ordinal)

    def Get_Ordinal(letter):
        if letter.islower():
            start_ordinal = ord('a')
            end_ordinal = ord('z')
        else:
            start_ordinal = ord('A')
            end_ordinal = ord('Z')
        return ord(letter), start_ordinal, end_ordinal

    enc_dec = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    msg = input("Type your message: ")
    shift_num = int(input("Type your shift number: "))
    new_message = ""

    for letter in msg:
        if letter.isalpha():
            if enc_dec.lower() == 'encode':
                new_message += Encrypt(letter, shift_num)
            elif enc_dec.lower() == 'decode':
                new_message += Decode(letter, shift_num)
        else:
            new_message += letter
    print(new_message)
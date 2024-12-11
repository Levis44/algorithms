def uniCode(string, key):
    caesar_cipher_string = ""
    # Mod na key para valores muito grandes, que o shifted_letter_unicode seria > do que 122, mas o 
    # (96 + shifted_letter_unicode % 122) ainda daria maior do que 122. 
    # Exemplo do key = 54, que a letra z seria 176
    # 176 % 122 = 54. Entao nossa key % 26, sempre respeitaria o alfabeto
    mod_key = key % 26

    for letter in string:
        unicode = ord(letter)
        shifted_letter_unicode = (unicode + mod_key)

        if shifted_letter_unicode > 122:
            caesar_cipher_string += chr(96 + shifted_letter_unicode % 122)
            continue
        
        caesar_cipher_string += chr(shifted_letter_unicode)

    return caesar_cipher_string

def list(string, key):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    mod_key = key % 26
    # usar sempre uma lista e dps o join é mais performatico
    # no python += em uma string é muito custoso, ele copia e cria outra variável
    shifted_string = []

    for letter in string:
        letter_index = alphabet.index(letter)
        shifted_letter_index = letter_index + mod_key
        shifted_string.append(alphabet[shifted_letter_index % 26])

        
    return "".join(shifted_string)


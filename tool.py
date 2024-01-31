def generate_key(text, key):
    key = list(key)
    key_length = len(key)
    key_index = 0
    extended_key = ""
    for char in text:
        if char.isalpha():  # Only extend the key for alphabetic characters
            extended_key += key[key_index % key_length]
            key_index += 1
        else:
            extended_key += char
    return extended_key

def vigenere_cipher(char, key_char, encrypt=True):
    if char.isalpha():
        offset = 65 if char.isupper() else 97
        shift = ord(key_char.lower()) - 97
        if not encrypt:
            shift = -shift
        return chr((ord(char) - offset + shift) % 26 + offset)
    else:
        return char

def encrypt_vigenere(text, key):
    key = generate_key(text, key)
    return ''.join(vigenere_cipher(text[i], key[i]) for i in range(len(text)))

def decrypt_vigenere(cipher_text, key):
    key = generate_key(cipher_text, key)
    return ''.join(vigenere_cipher(cipher_text[i], key[i], False) for i in range(len(cipher_text)))

# Example usage
text = "Hello, World!"
key = "KEY"

encrypted = encrypt_vigenere(text, key)
decrypted = decrypt_vigenere(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

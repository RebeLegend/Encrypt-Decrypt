from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS on all routes

# Vigenère Cipher Functions
def generate_key(text, key):
    key = list(key)
    key_length = len(key)
    key_index = 0
    extended_key = ""
    for char in text:
        if char.isalpha(): 
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

# Routes
@app.route('/')
def index():
    return "Encryption/Decryption API is running!"

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get("text")
    key = data.get("key")
    encrypted_text = encrypt_vigenere(text, key)
    return jsonify({"encrypted": encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data.get("text")
    key = data.get("key")
    decrypted_text = decrypt_vigenere(cipher_text, key)
    return jsonify({"decrypted": decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)

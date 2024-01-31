import requests

# Testing Encryption
encrypt_url = 'http://127.0.0.1:5000/encrypt'
encrypt_data = {'text': 'HelloWorld', 'key': 'Key'}
response = requests.post(encrypt_url, json=encrypt_data)
print('Encrypted:', response.json())

# Testing Decryption
decrypt_url = 'http://127.0.0.1:5000/decrypt'
decrypt_data = {'text': response.json()['encrypted'], 'key': 'Key'}
response = requests.post(decrypt_url, json=decrypt_data)
print('Decrypted:', response.json())

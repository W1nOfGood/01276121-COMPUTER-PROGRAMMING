def decrypt_adfgx(ciphertext, cipher_key):
    valid_chars = 'ADFGX'
    for char in ciphertext:
        if char not in valid_chars:
            return "FAILED TO DECRYPT"
    
    if len(ciphertext) % 2 != 0:
        return "FAILED TO DECRYPT"
    
    digraphs = []
    for i in range(0, len(ciphertext), 2):
        digraphs.append((ciphertext[i], ciphertext[i+1]))
    
    decrypted_message = []
    for digraph in digraphs:
        decrypted_char = cipher_key.get(digraph)
        if not decrypted_char:
            return "FAILED TO DECRYPT"
        decrypted_message.append(decrypted_char)
    
    return ''.join(decrypted_message)

cipher_key = {
    ('A', 'A'): 'b',
    ('A', 'D'): 't',
    ('A', 'F'): 'a',
    ('A', 'G'): 'l',
    ('A', 'X'): 'p',
    
    ('D', 'A'): 'd',
    ('D', 'D'): 'h',
    ('D', 'F'): 'o',
    ('D', 'G'): 'z',
    ('D', 'X'): 'k',
    
    ('F', 'A'): 'q',
    ('F', 'D'): 'f',
    ('F', 'F'): 'v',
    ('F', 'G'): 's',
    ('F', 'X'): 'n',
    
    ('G', 'A'): 'g',
    ('G', 'D'): 'i/j',
    ('G', 'F'): 'c',
    ('G', 'G'): 'u',
    ('G', 'X'): 'x',
    
    ('X', 'A'): 'm',
    ('X', 'D'): 'r',
    ('X', 'F'): 'e',
    ('X', 'G'): 'w',
    ('X', 'X'): 'y',
}

ciphertext = input("Input ADFGX cipher text: ")
decrypted_message = decrypt_adfgx(ciphertext, cipher_key)
print(decrypted_message)

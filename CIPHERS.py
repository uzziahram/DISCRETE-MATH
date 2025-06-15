import os

def Caesar_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = int(input("Input key: "))
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    caesar_cipher_text = ""
    for char in plain_text:
        upper_char = char.upper()
        if upper_char in alphabet:
            index = alphabet.index(upper_char)
            shifted_index = (index + key) % 26
            caesar_cipher_text += alphabet[shifted_index]
        else:
            caesar_cipher_text += char  
            
    os.system("cls")
    print("Original text: ", plain_text)
    print("Cipher Text: ", caesar_cipher_text)

def Rail_fence():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = int(input("Input key: "))
    
    rails = [''] * key  # Initialize rail levels
    row, direction = 0, 1

    for char in plain_text:
        rails[row] += char
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1  # Switch direction

    print("Original text:", plain_text)
    print("Cipher Text:", ''.join(rails))
    

def Vigenere_cipher():
    os.system("cls")

    plain_text = input("Input Plain text: ")
    key = input("Input key (word): ").upper()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = ""
    
    key_index = 0
    for char in plain_text:
        upper_char = char.upper()
        if upper_char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            index = (alphabet.index(upper_char) + shift) % 26
            cipher_text += alphabet[index]
            key_index += 1  # Move to the next letter in the key
        else:
            cipher_text += char

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
def Playfair_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ").upper().replace("J", "I")
    key = input("Input key (word): ").upper().replace("J", "I")

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix_key = ""
    for char in key:
        if char in alphabet and char not in matrix_key:
            matrix_key += char
    for char in alphabet:
        if char not in matrix_key:
            matrix_key += char

    matrix = [list(matrix_key[i*5:(i+1)*5]) for i in range(5)]

    # Prepare plaintext digraphs
    prepared = ""
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        if a not in alphabet:
            i += 1
            continue
        if i + 1 < len(plain_text):
            b = plain_text[i+1]
            if b not in alphabet:
                prepared += a
                i += 1
                continue
            if a == b:
                prepared += a + "X"
                i += 1
            else:
                prepared += a + b
                i += 2
        else:
            prepared += a + "X"
            i += 1

    # Encrypt digraphs
    cipher_text = ""
    for i in range(0, len(prepared), 2):
        a = prepared[i]
        b = prepared[i+1]
        row1 = col1 = row2 = col2 = 0
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == a:
                    row1, col1 = row, col
                if matrix[row][col] == b:
                    row2, col2 = row, col
        if row1 == row2:
            cipher_text += matrix[row1][(col1+1)%5]
            cipher_text += matrix[row2][(col2+1)%5]
        elif col1 == col2:
            cipher_text += matrix[(row1+1)%5][col1]
            cipher_text += matrix[(row2+1)%5][col2]
        else:
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
    
def Vernam_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = input("Input key (same length as plain text): ")

    if len(plain_text) != len(key):
        print("Error: Key must be the same length as the plain text.")
        return

    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_char = chr((ord(plain_text[i]) + ord(key[i])) % 256)
        cipher_text += cipher_char

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
def One_Time_Pad_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = input("Input key (same length as plain text): ")

    if len(plain_text) != len(key):
        print("Error: Key must be the same length as the plain text.")
        return

    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_char = chr((ord(plain_text[i]) + ord(key[i])) % 256)
        cipher_text += cipher_char

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
def Hill_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ").upper().replace(" ", "")
    print("Enter 4 numbers for the 2x2 key matrix (row-wise, separated by spaces):")
    key_input = input("Key: ")
    key_nums = key_input.strip().split()
    if len(key_nums) != 4 or not all(num.isdigit() for num in key_nums):
        print("Invalid key. Enter 4 numbers separated by spaces.")
        return
    key_matrix = [ [int(key_nums[0]), int(key_nums[1])],
                   [int(key_nums[2]), int(key_nums[3])] ]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Pad plaintext if needed
    if len(plain_text) % 2 != 0:
        plain_text += "X"
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        pair = [alphabet.index(plain_text[i]), alphabet.index(plain_text[i+1])]
        c1 = (key_matrix[0][0]*pair[0] + key_matrix[0][1]*pair[1]) % 26
        c2 = (key_matrix[1][0]*pair[0] + key_matrix[1][1]*pair[1]) % 26
        cipher_text += alphabet[c1] + alphabet[c2]
    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
def Columnar_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = input("Input key (word): ").upper()

    # Create a list of columns based on the key
    columns = [''] * len(key)
    for i, char in enumerate(plain_text):
        columns[i % len(key)] += char

    # Sort the key to determine the order of columns
    sorted_key = sorted((char, i) for i, char in enumerate(key))
    
    # Create cipher text by reading columns in sorted order
    cipher_text = ''.join(columns[i] for _, i in sorted_key)

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    

ciphers = [ "Caesar Cipher",
            "Vigenère Cipher",
            "Playfair Cipher",
            "Vernam Cipher",
            "One Time Pad Cipher",
            "Hill Cipher",
            "Rail Fence Cipher",
            "Columnar Cipher"]
running = True
while(running):
    os.system("cls")
    print("Ciphers")
    i = 1
    for cipher in ciphers:
        print(f"{i}.", cipher)
        i = i + 1 
        
    cipher = input("Choose Cipher: " )
    match cipher:
        case "1":
            Caesar_cipher()
            
        case "2":
            Vigenere_cipher()
        case "3":
            Playfair_cipher()
        case "4":
            Vernam_cipher()
        case "5":
            One_Time_Pad_cipher()
        case "6":
            Hill_cipher()
        case "7":
            Rail_fence()
        case "8":
            Columnar_cipher()

    restart = input("\nStart again? [y/n]: ")
    if restart == "n" or restart == "N":
        running = False
import string
from time import time, process_time

alphabet = string.printable + " " + "\n" + "\t" + "\r" + "\f" + "\v"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


# Reverse Cipher
def reverse(text):
    return text[::-1]

# Vigenere Cipher
def vignere_encrypt(message, key):
    encrypted = ""
    split_message = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted

# Decrypt Vigenere Cipher
def vignere_decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted

def main():
    plaintext = input("Enter plaintext: ")
    key = input("\nEnter key: ")
    time_start = time()
    
    # Reverse Cipher
    rev_cipher = reverse(plaintext)
    print("\n==========reverse cipher==========")
    print("\nCiphertext: ", rev_cipher)
    print("\nDecrypted: ", reverse(rev_cipher))
    time1_stop = time()
    print("\nTime taken: ", time1_stop - time_start)

    # Vigenere Cipher
    vig_cipher = vignere_encrypt(plaintext, key)
    print("\n==========vigenere cipher==========")
    print("\nCiphertext: ", vig_cipher)
    print("\nDecrypted: ", vignere_decrypt(vig_cipher, key))
    time2_stop = time()
    print("\nTime taken: ", time2_stop - time1_stop)

    # Reverse + Vigenere Cipher
    ciphertext = reverse(vignere_encrypt(plaintext, key))
    print("\n=================reverse + vignere cipher=================")
    print("\nCiphertext: ", ciphertext)
    print("\nDecrypted: ", vignere_decrypt(reverse(ciphertext), key))
    time3_stop = time()
    print("\nTime taken: ", time3_stop - time_start)

if __name__ == '__main__':
    main()
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char

    return result

def main():
    text = input("Enter the text to be encrypted: ")
    shift = int(input("Enter the shift key: "))
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted:", encrypted_text)
    decrypted_text = caesar_cipher(encrypted_text, 26 - shift)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()


from unidecode import unidecode


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def filter_input(text):
    # Odstranění diakritiky
    text = unidecode(text)

    # Odstranění speciálních znaků (!>.-, apod.)
    special_chars = ['!', '>', '.', '-', ',']
    for char in special_chars:
        text = text.replace(char, '')

    # Nahrazení mezery za "XMEZERAX"
    text = text.replace(' ', 'XMEZERAX')

    return text


def encrypt(text, a, b):
    result = ''
    count = 0
    for char in text:
        if char.isalpha():
            char = char.upper()
            char = chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            result += char
            count += 1
            if count % 5 == 0:
                result += ' '  # Add space every five characters
        elif char.isdigit():
            char = chr(((int(char) + a) % 10) + ord('0'))
            result += char
            count += 1
            if count % 5 == 0:
                result += ' '  # Add space every five characters
        else:
            pass  # Handle special characters if needed

    return result


def decrypt(text, a, b):
    a_inverse = mod_inverse(a, 26)
    if a_inverse is None:
        return "a is not coprime with 26, decryption is not possible."

    result = ''
    word = ''
    for char in text:
        if char.isalpha():
            char = chr(((a_inverse * (ord(char) - ord('A') - b)) % 26) + ord('A'))
            word += char
        elif char.isdigit():
            char = chr(((int(char) - a) % 10) + ord('0'))
            word += char
        else:
            pass  # Handle special characters if needed

        if len(word) == 5:
            result += word
            word = ''

    result += word

    return result

# Příklad použití funkcí
a = int(input("Zadejte hodnotu a (nesoudělné s 26 a GCD(a, 26) == 1): "))
b = int(input("Zadejte hodnotu b: "))
text = input("Zadejte text k zašifrování: ")

filtered_text = filter_input(text)
encrypted_text = encrypt(filtered_text, a, b)
decrypted_text = decrypt(encrypted_text, a, b)

print(f"Zašifrovaný text: {encrypted_text}")
print(f"Dešifrovaný text: {decrypted_text}")
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
        return "a není nesoudělné s 26, nelze provést dešifrování."

    result = ''
    word = ''
    for char in text:
        if char.isalpha():
            char = chr(((a_inverse * (ord(char) - ord('A') - b)) % 26) + ord('A'))
            word += char
        elif char.isdigit():
            # Caesarova dešifra pro čísla (posun o hodnotu 'a')
            char = chr(((int(char) - a) % 10) + ord('0'))
            word += char
        else:
            # Implementujte ošetření speciálních znaků
            pass

        if len(word) == 5:
            result += word
            word = ''

    # Přidejte poslední slovo
    result += word

    # Obnovení původních mezer
    result = result.replace('XMEZERAX', ' ')

    return result

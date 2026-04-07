def caesar_shift(letter, alphabet, k, encrypt=True):
    """Сдвигает одну букву по алфавиту"""
    if letter not in alphabet:
        return letter 
    p = alphabet.index(letter)  
    n = len(alphabet)
    if encrypt:
        p_new = (p + k) % n
    else:
        p_new = (p - k) % n
    return alphabet[p_new]

def caesar(text, language, k, encrypt=True):
    """Шифрует или дешифрует текст методом Цезаря."""
    up, lo = alphabets[language]
    result = []
    for char in text:
        if char in up:
            new_char = caesar_shift(char, up, k, encrypt)
        elif char in lo:
            new_char = caesar_shift(char, lo, k, encrypt)
        else:
            new_char = char
        result.append(new_char)

    return "".join(result)

rus_alph_upp = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
eng_alph_upp  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_alph_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alph_low = 'abcdefghijklmnopqrstuvwxyz'

alphabets = {
    "ru": (rus_alph_upp, rus_alph_low),
    "en": (eng_alph_upp, eng_alph_low), 
}

def main():
    print("1 – шифровать, 2 – дешифровать")
    print("Язык: ru или en")
    print("Шаг сдвига: целое число (>= 0)")

    action = input("Выберите направление (1/2): ").strip()
    language = input("Выберите язык (ru/en): ").strip().lower()
    k = int(input("Шаг сдвига: ").strip())

    if action not in ["1", "2"]:
        print("Ошибочный ввод направления.")
        return
    if language not in ["ru", "en"]:
        print("Ошибочный ввод языка.")
        return
    
    text = input("Напиши свой текст: ")

    encrypt = (action == "1")
    result = caesar(text, language, k, encrypt)

    if encrypt:
        mode = "Шифрование"
    else:
        mode = "Дешифрование"
    print(f"\n{mode} ({language.upper()}, шаг={k}):")
    print(f"Ввод:  {text}")
    print(f"Вывод: {result}")

if __name__ == "__main__":
    main()
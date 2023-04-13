# Функції для перевірки
def get_palindrome(word):
    """ Перевіряє, чи є слово паліндромом """
    return word == word[::-1]

def get_palingrames(word, words_set):
    """ Перевіряє, чи є слово палінграмою """
    return word[::-1] in words_set

# Відкриваємо файл у режимі читання
with open('dictionary.txt', 'r') as file:
    # Зчитуємо вміст файлу
    content = file.read()

    # Розділяємо текст на окремі слова
    words = content.split()

    # Створюємо множину унікальних слів
    words_set = set(words)

    # Знаходимо кількість паліндромів та палінграм в файлі
    palindrome_count = 0
    palingrames_count = 0

    for word in words_set:
        if get_palindrome(word):
            palindrome_count += 1
        if get_palingrames(word, words_set):
            palingrames_count += 1

    # Виводимо результати
    print("Palindromes: ", palindrome_count)
    print("Palingrames: ", palingrames_count)

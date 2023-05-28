
file = open("file_path.txt","r")
text = file.read()
words = text.split()


def get_all_palindromes(content: str):

    # Розділити текст на окремі слова
    words = content.split()

    # Створити список для зберігання усіх паліндромів
    palindromes = []

    # Пройтися по кожному слову
    for word in words:
        # Перевірити, чи є слово паліндромом
        if check_palindrome(word):
            # Якщо слово є паліндромом, додати його до списку паліндромів
            palindromes.append(word)

    # Повернути список паліндромів
    return palindromes


def check_palindrome(word: str):
    # Перевернути слово
    reversed_word = word[::-1]

    # Перевірити, чи співпадає перевернуте слово з оригіналом
    if word == reversed_word:
        return True
    else:
        return False

def get_palingrams(content: str):
    # Розділити текст на окремі слова
    words = content.split()

    # Створити множину для зберігання унікальних паліндромів
    palingrams = set()

    # Пройтися по кожному слову
    for word in words:
        # Визначити унікальні пари літер
        pairs = [word[i:j+1] for i in range(len(word)) for j in range(i, len(word))]

        # Перевірити, чи є паліндромом кожна пара літер
        for pair in pairs:
            if pair == pair[::-1]:
                # Якщо пара літер є паліндромом, додати її до множини паліндромів
                palingrams.add(pair)

    # Повернути множину унікальних паліндромів
    return palingrams

def break_read_file(text) :

    sentences = []
    sentence = ""
    for ch in text :
        sentence += ch 
        if ch in ['?','!','.']:
             sentences.append(sentence.strip())
             sentence = ""
    if sentence:
        sentences.append(sentence.strip())
        return sentences 
    print('sentences:',len(sentences)) 
    print('word:',len(text)) 

print(text)
break_read_file(text)
palindromes = get_all_palindromes(text)
print(palindromes)
palingrams = get_palingrams(text)
print(palingrams)









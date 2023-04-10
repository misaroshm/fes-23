def read_file(file_path: str) -> str:
    """
    param: file_path
    return: The function takes a file path as a param,
        opens and reads the contents of the file,
        then returns it.
    """
    with open(file_path) as f:
        return f.read()


def read_file_converting(file_path: str) -> str:
    """
    param: file_path
    return: The function takes a file path as a param,
        opens, reads the contents, and replaces specified chars in the file,
        then returns converted str.
    """
    with open(file_path) as f:
        return f.read().replace('.', '').replace(',', '').lower()


def words_and_sentences_count(file_path: str) -> (int, int):
    """
    param: file_path
    return: The function returns amount of words and sentences.
    """
    counter_for_words = 0
    counter_for_sentences = 0
    content = read_file(file_path)
    for ch in content:
        if ch == " " or ch == "\n":
            counter_for_words += 1
        elif ch == ".":
            counter_for_sentences += 1
    return counter_for_words, counter_for_sentences


def get_palindromes(file_path: str) -> list:
    """
    param: file_path
    return: The function returns the list of palindromes.
    """
    f = read_file_converting(file_path)
    palindromes = []
    for word in f.split():
        if len(word) == 1:
            continue
        elif word == word[::-1]:
            palindromes.append(word)
        else:
            continue
    return palindromes


def get_palingrames(file_path) -> list:
    """
    param: file_path
    return: The function returns the list of palingrames.
    """
    palingrames = []
    text = read_file(file_path)
    words = text.split()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]
            if word1 in word2[::-1] or word1 in word2:
                palingrames.append(word1 + "-" + word2)
            else:
                continue
    if palingrames == 0:
        print("There is no palingrames")
    return palingrames


file_path1 = "palindromes.txt"
file_path2 = "palingrames.txt"

print(f"The number of words in file '{file_path1}' is {words_and_sentences_count(file_path1)[0]}"
      f" and the number of sentences in file '{file_path1}' is {words_and_sentences_count(file_path1)[1]}")
print(f"The number of words in file '{file_path2}' is {words_and_sentences_count(file_path2)[0] + 1}"
      f" and the number of sentences in file '{file_path2}' is {words_and_sentences_count(file_path2)[1]}")
print("List of palindromes: ", get_palindromes(file_path1))
print("List of palingrames: ", get_palingrames(file_path2))

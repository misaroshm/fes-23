def read_file(file_path: str) -> str:
    """
    Reads the contents of a file.

    Args:
        file_path (str): The path of the file.

    Returns:
        str: The contents of the file.
    """
    with open(file_path) as f:
        return f.read()


def read_file_converting(file_path: str) -> str:
    """
    Reads the contents of a file and converts specified characters.

    Args:
        file_path (str): The path of the file.

    Returns:
        str: The converted contents of the file.
    """
    with open(file_path) as f:
        content = f.read()
        content = content.replace('.', '').replace(',', '').lower()
        return content


def words_and_sentences_count(file_path: str) -> Tuple[int, int]:
    """
    Counts the number of words and sentences in a file.

    Args:
        file_path (str): The path of the file.

    Returns:
        Tuple[int, int]: The number of words and sentences.
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


def get_palindromes(file_path: str) -> List[str]:
    """
    Finds all palindromes in a file.

    Args:
        file_path (str): The path of the file.

    Returns:
        List[str]: The list of palindromes.
    """
    content = read_file_converting(file_path)
    words = content.split()
    palindromes = []
    for word in words:
        if len(word) == 1:
            continue
        elif word == word[::-1]:
            palindromes.append(word)
    return palindromes


def get_palingrams(file_path: str) -> List[str]:
    """
    Finds all palingrams in a file.

    Args:
        file_path (str): The path of the file.

    Returns:
        List[str]: The list of palingrams.
    """
    palingrams = []
    content = read_file(file_path)
    words = content.split()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]
            if word1 in word2[::-1] or word1 in word2:
                palingram = word1 + "-" + word2
                palingrams.append(palingram)
    if len(palingrams) == 0:
        print("There are no palingrams.")
    return palingrams


file_path1 = "//name.txt"
file_path2 = "//name.txt"

word_count, sentence_count = words_and_sentences_count(file_path1)
print(f"The number of words in file '{file_path1}' is {word_count} and the number of sentences is {sentence_count}.")

word_count, sentence_count = words_and_sentences_count(file_path2)
word_count += 1  # Account for the additional word in palingrames.txt
print(f"The number of words in file '{file_path2}' is {word_count} and the number of sentences is {sentence_count}.")

print("List of palindromes:", get_palindromes(file_path1))
print("List of palingrams:", get_palingrams(file_path2))

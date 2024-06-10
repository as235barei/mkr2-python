from collections import Counter


def read_file(file_path):
    # Читає вміст файлу та повертає його як рядок.
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def count_characters(text):
    # Повертає кількість символів у тексті з пробілами та без.
    total_chars_with_spaces = len(text)
    total_chars_without_spaces = len(text.replace(" ", ""))
    return total_chars_with_spaces, total_chars_without_spaces


def find_common_neighbors(words, target_word):
    # Повертає найбільш часті сусідні слова для заданого слова.
    neighbors = []

    for i, word in enumerate(words):
        if word == target_word:
            if i > 0:  # Попереднє слово
                neighbors.append(words[i - 1])
            if i < len(words) - 1:  # Наступне слово
                neighbors.append(words[i + 1])

    common_neighbors = Counter(neighbors).most_common(10)
    return common_neighbors


def main():
    file_path = 'Serdce_Drakona.txt'
    text = read_file(file_path)

    total_chars_with_spaces, total_chars_without_spaces = count_characters(text)
    print(f"Загальна кількість символів з пробілами: {total_chars_with_spaces}")
    print(f"Загальна кількість символів без пробілів: {total_chars_without_spaces}")

    words = text.split()

    while True:
        target_word = input("Введіть слово, для якого потрібно знайти сусідні слова (або 0 для завершення): ")
        if target_word == '0':
            break

        if target_word in words:
            common_neighbors = find_common_neighbors(words, target_word)
            print(f"Найчастіше зустрічаються поряд зі словом '{target_word}': {common_neighbors}")
        else:
            print(f"Слово '{target_word}' не знайдено в тексті.")


main()

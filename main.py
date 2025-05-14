def search_word(word):
    results = []
    try:
        with open("text.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if word.lower() in line.lower():
                    highlighted = line.replace(word, f"*{word}*")
                    results.append(highlighted.strip())
    except Exception as e:
        results.append(f"Ошибка: {e}")
    return results


if __name__ == "__main__":
    word = input("Введите слово для поиска: ")
    matches = search_word(word)
    for line in matches:
        print(line)

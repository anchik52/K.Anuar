import re

def read_text_file(filepath, encoding="utf-8"):
    with open(filepath, "r", encoding=encoding) as f:
        return f.readlines()

def clean_text(lines):
    cleaned = []
    for line in lines:
        line = line.strip().lower()
        line = line.replace(",", "").replace(".", "")
        if line:
            cleaned.append(line)
    return cleaned

def search_text(lines, query):
    if " AND " in query:
        terms = query.split(" AND ")
        return [line for line in lines if all(term in line for term in terms)]
    elif " OR " in query:
        terms = query.split(" OR ")
        return [line for line in lines if any(term in line for term in terms)]
    elif " NOT " in query:
        term1, term2 = query.split(" NOT ")
        return [line for line in lines if term1 in line and term2 not in line]
    else:
        pattern = re.compile(re.escape(query), re.IGNORECASE)
        return [line for line in lines if pattern.search(line)]

def binary_search(sorted_lines, target):
    left, right = 0, len(sorted_lines) - 1
    while left <= right:
        mid = (left + right) // 2
        if target in sorted_lines[mid]:
            return True
        elif target < sorted_lines[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

def print_menu():
    print("\n--- Menu ---")
    print("1. Search by keyword or logical expression")
    print("2. Binary search in sorted text")
    print("0. Exit")

def main():
    file_path = "sample.txt"
    encoding = "utf-8"

    try:
        raw_text = read_text_file(file_path, encoding)
    except Exception as e:
        print(f"File read error: {e}")
        return

    cleaned_lines = clean_text(raw_text)

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            keyword = input("Enter keyword or logical query: ").strip().lower()
            results = search_text(cleaned_lines, keyword)
            print("\nResults:")
            for line in results:
                print(f"- {line}")

        elif choice == "2":
            keyword = input("Enter word for binary search: ").strip().lower()
            sorted_lines = sorted(cleaned_lines)
            found = binary_search(sorted_lines, keyword)
            print("Found!" if found else "Not found.")

        elif choice == "0":
            print("Exiting application.")
            break

        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()

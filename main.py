from stats import number_of_words, char_count, report
import sys

def get_book_text(path):
    with open(f"{path}") as f:
        file_contents = f.read()
        return file_contents
        # print(file_contents)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    number_of_words(book)
    # char_count(book)
    dictionary = char_count(book)
    # print(type(dictionary))
    report(dictionary)
main()
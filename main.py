from typing import AnyStr
from stats import get_num_words,get_char_count,sort_char_stats
import sys

def get_book_text(filepath: AnyStr):
    with open(filepath) as f:
        file_contents = f.read()
        f.close()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path=sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    file_contents=get_book_text(book_path)

    print("----------- Word Count ----------")

    num_words=get_num_words(file_contents)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_stats = get_char_count(file_contents)
    sorted_char_stats = sort_char_stats(char_stats)

    for stat in sorted_char_stats:
        print(f"{list(stat.keys())[0]}: {list(stat.values())[0]}")
    print("============= END ===============")
main()
def number_of_words(book):
    string = book.split()
    num = len(string)
    print(f"{num} words found in the document")

def char_count(book):
    char_dict = {}
    book = book.lower()

    for char in book:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    print(char_dict)
    # print(type(char_dict))
    return char_dict



def report(dictionary):
    # print(type(dictionary))
    sorted_dict = {}

    for k in dictionary:
        sorted_dict.update({k : dictionary[k]})
    # print("test")
    # print(sorted_dict)    
    sorted_dict = dict(sorted(sorted_dict.items()))
    
    # print("test")
    # print(sorted_dict)  

    print("""============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound 75767 total words\n--------- Character Count -------""")


    for k in sorted_dict:
        if k.isalpha():
            print(f"{k}: {sorted_dict[k]}")
    print("============= END ===============")
    
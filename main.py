current_book = "books/frankenstein.txt"

# Open file
with open(current_book) as f:
    # read contents of open file to a string
    file_contents = f.read()


# Return the number of words in the string
def number_of_words(string):
    return len(string.split())


# Convert uppercase letters to lowercase
def to_lowercase(string):
    return string.lower()


# Takes text from book as string, then returns the number of times each character appears
def char_count(string):
    lowercase = to_lowercase(string)
    chars = [x for x in lowercase]
    count = {}
    for char in chars:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


# Takes count dict, sorts it alphabetically, and prints only the alphabet char counts to the console.
def print_report(count):
    keys = list(count.keys())
    keys.sort()
    sorted_count = {i: count[i] for i in keys}

    print(f"--- Begin report of {current_book} ---")
    print(f"{number_of_words(file_contents)} words found in the document")
    print()

    for key in sorted_count:
        if key.isalpha():
            print(f"The '{key}' character was found {count[key]} times")

    print("--- End report ---")


print_report(char_count(file_contents))

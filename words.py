def print_upper_words(words, must_start_with):
    """Convert all words to uppercase and print results.

    - words: array of words to convert to uppercase
    - must_start_with: words tha start with these letters should be converted

    Return results of the conversion that begin with the specified letters.

    For example:

        print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
            => this should print "HELLO", "HEY", "YO", and "YES"
    """
    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                print(word.upper())
                break

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with = ["h", "y"])
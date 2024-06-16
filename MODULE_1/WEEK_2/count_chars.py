'''
    Return a count dictionary of an input word.
'''


def count_chars(word):
    results = {}
    for char in word:
        if char not in results:
            results[char] = 1
        else:
            results[char] += 1
    return results


def main():
    # Example
    string = 'smiles'
    print(count_chars(string))


if __name__ == "__main__":
    main()

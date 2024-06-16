"""
    Read lines from a txt file and return a word frequency dictionary.
"""


def return_word_count(file_path):
    results = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            words = line.split()
            for word in words:
                if word not in results:
                    results[word] = 1
                else:
                    results[word] += 1
    return results


def main():
    file_path = r'MODULE_1\WEEK_2\P1_data.txt'
    print(return_word_count(file_path))


if __name__ == "__main__":
    main()

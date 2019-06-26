# TODO: make different classes for different file types that all have the same interface?
# Then instantiate a class depending on which file path we are given so we can count properly in different file types using the same API
# UNLESS we just want to handle text files in this little project

def get_letter_counts(file):
    counts = {}
    for line in file:
        for char in line:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def get_letter_counts_list(counts_map):
    counts_list = []
    for letter in counts_map:
        counts_list.append((letter, counts_map[letter]))
    return counts_list

if __name__ == '__main__':
    print('\nWelcome to Character Counter!\n')
    print('Pass me a text file, and I will tell you how many of each character are in it.')

    # TODO: can we use a different condition here?
    while True:
        try:
            file_path = input('\nEnter a file path (q to quit): ')
            if file_path.lower() == 'q':
                print('\nGoodbye!')
                break
            file = open(file_path, 'r')
        except IOError:
            print("File not found. Make sure your file path is correct.")
            continue

        counts_map = get_letter_counts(file)

        # list of tuples counting (char, count) to be used for sorting
        unsorted_letter_counts = get_letter_counts_list(counts_map)
        sorted_letter_counts = sorted(unsorted_letter_counts, key=lambda tup: tup[1], reverse=True)

        print('The number of each letter in {} from largest to smallest is:\n'.format(file.name))
        print(sorted_letter_counts)

        file.close()
        break


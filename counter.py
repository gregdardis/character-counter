#TODO: make this object oriented, and just use the main method as the demo section
#Expose an api so this can be imported and called externally, even though who would want to? LOL
#TODO: add docstrings to methods
#TODO: add color to print output
#TODO: format output of letters largest to smallest better

class CharacterCounter():
    '''
    Counts characters in a .txt file and displays them to the console.\n
    Throws IOError if file path doesn't exist.
    '''
    def __init__(self, file_path):
        try:
            self.file = open(file_path, 'r')
        except:
            raise IOError("File not found. Make sure your file path is correct.")

    def display_char_counts(self):
        # list of tuples counting (char, count) to be used for sorting
        unsorted_letter_counts = self._get_letter_counts_list()
        sorted_letter_counts = sorted(unsorted_letter_counts, key=lambda tup: tup[1], reverse=True)

        print('\nThe number of each letter in {} from largest to smallest is:'.format(self.file.name))
        print(sorted_letter_counts)

    def _get_letter_counts(self):
        counts = {}
        for line in self.file:
            for char in line:
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1
        return counts

    def _get_letter_counts_list(self):
        counts_map = self._get_letter_counts()

        counts_list = []
        for letter in counts_map:
            counts_list.append((letter, counts_map[letter]))
        return counts_list

# Demo
if __name__ == '__main__':
    print('\nWelcome to Character Counter!\n')
    print('Pass me a text file, and I will tell you how many of each character are in it.')

    while True:
        file_path = input('\nEnter a file path (q to quit): ')
        if file_path.lower() == 'q':
            print('\nGoodbye!')
            exit()
        try:
            counter = CharacterCounter(file_path)
            break
        except IOError as error:
            print(error.args[0])

    counter.display_char_counts()
    # file.close()#TODO: close file within CharacterCounter? Automatically close it or expose API for user to close it


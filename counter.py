from colorama import Fore
from colorama import Style

class CharacterCounter():
    """Counts characters in a .txt file and displays them to the console\n
    
    Raises:
        IOError: file path doesn't exist
    """
    def __init__(self, file_path):
        try:
            file = open(file_path, 'r')
            self.file = file
        except:
            raise IOError("File not found. Make sure your file path is correct.")
            
    def display_char_counts(self):
        """
        Displays the number of each character in the text file to the console.
        """
        sorted_char_counts = self._get_sorted_char_counts()

        print(f'\n{Style.BRIGHT}{Fore.GREEN}The number of each character in {self.file.name} from largest to smallest is:{Style.RESET_ALL}')

        for char, count in sorted_char_counts:
            if char == '\n':
                print(f'{Style.BRIGHT}{Fore.WHITE}\\n: {count}{Style.RESET_ALL}')
            else:
                print(f'{Style.BRIGHT}{Fore.WHITE}{char}: {count}{Style.RESET_ALL}')
                
    def _count_chars(self):
        counts = {}
        for line in self.file:
            for char in line:
                counts[char] = counts[char] + 1 if char in counts else 1
        return counts

    def _get_sorted_char_counts(self):
        char_counts = self._count_chars()
        unsorted_char_counts = []
        for letter in char_counts:
            unsorted_char_counts.append((letter, char_counts[letter]))

        return sorted(unsorted_char_counts, key=lambda tup: tup[1], reverse=True)

if __name__ == '__main__':
    print(f'\n{Style.BRIGHT}{Fore.GREEN}Welcome to Character Counter!{Style.RESET_ALL}\n')
    print('Pass me a text file, and I will tell you how many of each character are in it.')

    while True:
        file_path = input(f'\nEnter a file path {Style.BRIGHT}{Fore.RED}(q to quit){Style.RESET_ALL}: ')
        if file_path.lower() == 'q':
            print('\nGoodbye!')
            exit()
        try:
            counter = CharacterCounter(file_path)
            break
        except IOError as error:
            print(error.args[0])

    counter.display_char_counts()

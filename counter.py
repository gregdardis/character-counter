# TODO: make different classes for different file types that all have the same interface?
# Then instantiate a class depending on which file path we are given so we can count properly in different file types using the same API
# UNLESS we just want to handle text files in this little project

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

        print(file.read())
        break






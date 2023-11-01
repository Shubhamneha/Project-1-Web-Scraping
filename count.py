def count(file_path):
    try:
        with open(file_path,'r') as file:
            content= file.read()
            word=len(content.split())
            return word
    except FileNotFoundError:
        print('File not found.Please provide a valid file path')
        return -1
    

if __name__ == '__main__':
    try:
        file_path=input('Enter the path of file : ')
        num_words = count(file_path)

        if num_words >= 0:
            print("Number of words in file are : ", num_words)
    except KeyboardInterrupt:
        print('\n Program Interrupted')
    except Exception as e:
        print(f"An error occured : {e}")


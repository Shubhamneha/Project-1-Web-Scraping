import string

def read_file(file_path):
    try:
        with open(file_path,'r') as file:
            return file.read()
    except FileNotFoundError:
        print('File not found.Please provide a valid file path')
        return -1
    
def process_text(text):
    text=text.translate(str.maketrans("","", string.punctuation))
    words=text.lower().split()
    return words

def count_word_frequency(words):
    word_frequency= {}
    for word in words:
        word_frequency[word]= word_frequency.get(word,0)+1
    return word_frequency

def display(word_frequency):
    print("Word Frequency : ")
    for word,count in word_frequency.items():
        print(f"{word} : {count}")

if __name__ == '__main__':
    try:
        file_path=input('Enter the path of file : ')
        text= read_file(file_path)

        if text:
            words= process_text(text)
            word_frequency= count_word_frequency(words)
            display(word_frequency)
            
    except KeyboardInterrupt:
        print('\n Program Interrupted')
    except Exception as e:
        print(f"An error occured : {e}")






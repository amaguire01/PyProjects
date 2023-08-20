from random_word import RandomWords

def main():
    wordle = getWord()
    


def getWord():
#init RandomWords function from random_word library
    r = RandomWords()

#Run while loop to pull random word from library until a 5 letter word is found
    while True:
        word = r.get_random_word()
        if len(word) != 5:
            word = r.get_random_word()
        else:
            return word
        

if __name__ == "__main__":
    main()



from ast import While


def readWords(words):
    with open("./data.txt", "r", encoding= "utf-8")as f:
        for line in f:
            words.append(line)
    return words 

def game():
    pass
    


def main():
    words = []
    words = readWords(words)
    print (words)

    #game_continue = True
    #while game_continue == True:
    #    game_continue = game()


if __name__ == "__main__":
    main()
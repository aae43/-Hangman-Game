def readWords():
    words = []
    with open("./data.txt", "r", encoding= "utf-8")as f:
        for line in f:
            words.append(str(line))
        print(words)
    


def main():
    readWords()

if __name__ == "__main__":
    main()
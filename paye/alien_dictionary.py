import csv
# with open('words_meaning.csv','w',newline="") as fd:
#     csv_write = csv.writer(fd, delimiter=',')
#     csv_write.writerow(['Words in Alien Language','Meaning in English'])

def add_words():
    with open('words_meaning.csv','a',newline="") as fd:
        csv_write = csv.writer(fd, delimiter=',')
        key = input('Enter Alien Language Word: ')
        meaning = input('Enter Meaning in English Language: ')
        csv_write.writerow([key,meaning])

def read_words():
    with open("words_meaning.csv") as fd:
        word_reader = csv.reader(fd)
        words = []
        for each_line in word_reader:
            words += each_line
    return words

while True:
    print("Press 1 to Translate from English to Alien")
    print("Press 2 to Translate from Alien to English")
    print("Press 3 to Add New Word to the Dictionary")
    print("Press 4 to Exit")

    option = int(input("Enter 1 - 4: "))

    if option == 1:
        enterword = input("Enter Word in English Language: ")
        search = []
        search = read_words()
        print(search)
        for i in search:
            if enterword == i:
                word = i
                wordmean = '' #by some way get the previous value in list here
                print("The word "+str(word)+' translates to '+str(wordmean)+' in Alien Language.')

    elif option == 4:
        print("Closing Dictionary....")
        break
    else:
        print("Invalid Option! Exit Dictionary....")
        break
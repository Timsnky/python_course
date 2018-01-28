def playHand(hand,wordList,n):
    Total=0
    hand1=hand.copy()
    for letter in hand1:
        hand2=[]
        for letter in hand.keys():
            for j in range(hand[letter]):
                hand2.append(letter)
    for i in range(len(hand2)):
        if len(hand2)!=0:
            print('Current Hand: '),displayHand(hand1)
            word=str(raw_input('Enter a word, or a "." to indicate that you are finished: ')) 
            dot='.'
            if word==dot:
                print('Goodbye! Total score: '+str(Total)+' points')
                break
            else:
                Bin=isValidWord(word,hand,wordList)
                if Bin==True:
                    Total=Total+(getWordScore(word,n))
                    print('"'+word+'" earned '+str(getWordScore(word,n))+' points. Total: '+str(Total)+' points')
                    hand1=updateHand(hand1,word)
                    hand2=[]
                    for letter in hand1.keys():
                        for j in range(hand1[letter]):
                            hand2.append(letter)
                    print(' ')
            if Bin==False:
                print('Invalid word,please try again.')
                print(' ')
        else:
            print('Run out of letters. Total score: '+str(Total)+' points')
            break

import os
import string
import operator
import nltk
import random

#def getSentences(text):
#    sentenceList = []
#    cont = True
#    while (cont):

        

    
    
#def parseFile(fileName):
#    sentenceList = []
#    with open(fileName, 'r') as f:
#sentenceList.append
# = f.read()
#    sentenceList = getSentences(read_data)



def wordCounter():
    forbiddenTags = ["IN", "DT", "PRP", "PRP$", "CC", "EX", "LS", "MD", "PDT", "POS", "RP", "SYM", "TO", "WDT", "WP", "WP$", "WRB" ]
    stemmer = nltk.PorterStemmer()
    wordCounter = {}
    for i in range (0, 13):
        if (i < 9):
            fileName = "./transcripts/ep0" + str(i + 1) + ".txt"
        else:
            fileName = "./transcripts/ep" + str(i + 1) + ".txt"
        print "fileName: ", fileName
	with open(fileName, 'r') as f:
            print "readeing ", fileName,"..."
            readData = f.read()
            print "...finished"
        words = readData.translate(string.maketrans("",""), string.punctuation).split()
        for w in words:
            try:
                tag =  nltk.pos_tag([w])
                if (len(w) > 3) and (not (tag[0][1] in forbiddenTags)):
                    print w
                    w = stemmer.stem(w)
                    if (w in wordCounter) :
                        wordCounter[w] =  wordCounter[w] + 1
                    else:
                        wordCounter[w] = 1
            except ValueError:
                print "ERROR"
                    
                        

    sortedWords = sorted(wordCounter.items(), key=operator.itemgetter(1), reverse=True)
    
    for i in range (0, 50):
        print sortedWords[i], nltk.pos_tag([sortedWords[i][0]])



def matchLineToQuery(query):
    highScore = 0
    winningLine = ""
    
    wordsInQuery = query.lower().split()
    numWords = len(wordsInQuery)

    print wordsInQuery

    fileName = os.path.dirname(os.path.realpath(__file__)) + "/transcripts/full.txt"

    #first run
    #fileName = "./transcripts/full.txt"
        
    scoreOfLines = []
    print "opening:", fileName
    with open(fileName, 'r') as f:
        print "got it"
        for line in f:
            wordsInLine = line.lower().translate(string.maketrans("",""), string.punctuation).split()
            score = 0
            for word in wordsInQuery:
                if word in wordsInLine:
                    score = score + 1
                                
            scoreOfLines.append(score)
    # add proper scores
    comulateiveScores = []
    for i in range (numWords - 1, len(scoreOfLines)):
        comScore = 0
        for y in range (0, numWords):
            comScore = comScore + scoreOfLines[i - y]
        comulateiveScores.append(comScore)
        if comScore > highScore:
            highScore = comScore
            print "highscroe is now: ", highScore 
    # get all line numbers with high score
    linesWithHighScore = []
    for i in range(0, len(comulateiveScores)):
        if (comulateiveScores[i] == highScore):
            linesWithHighScore.append(i)
    print "lines with highscore: ", linesWithHighScore
    #choose line
    lineNumber = linesWithHighScore[random.randint(0, len(linesWithHighScore) - 1)]
    print "chose line: ", lineNumber
    curLine = 0
   
    with open(fileName, 'r') as f:
        while(True):
            if curLine == lineNumber:
                print "adding lines"
                res = ""
                for l in range (0, numWords):
                    res = res + f.readline()
                return res
            else:
                #print "read: ", curLine, line
                curLine = curLine + 1
                f.readline()


if __name__ == "__main__":
    #wordCounter()
    res = matchLineToQuery("apple pie scratch")
    print "Result: " + res
        

            





import wikipedia


def getASummaryOf(text):

    word = extractWord(text)
    
    summary = wikipedia.summary(word, sentences=5)
    
    return summary



def extractWord(text):

    result = text.split("of", 1)[1].strip()
    result = result.replace(" ", "")

    return result

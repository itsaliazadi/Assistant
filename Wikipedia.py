import wikipedia


def getASummaryOf(text) ->str:
    try:
        word = extractWord(text)
        summary = wikipedia.summary(word, sentences=3)
        
        return summary
    except:
        return "No such page found on wikipedia"

def extractWord(text) ->str:
    result = text.split("of", 1)[1].strip()
    result = result.replace(" ", "")

    return result

def promptForWords():
    global noun, verb, adjective, place
    noun = input ("Enter a noun: ")
    verb = input ("Enter a verb: ")
    adjective = input ("Enter an adjective: ")
    place = input ("Enter a place: ")


def makeAndPrintSentence():
    print("I can't wait to hold my " + noun + " and " + verb + " to our favorite " + adjective + " " + place + ".")


def main():
    promptForWords()
    makeAndPrintSentence()


main()

import re

#PyParagraph Final

def paragraph(inputfile, outputfile):
    with open(str(inputfile), 'r') as file:
        x = file.read()
        totalwords = 0
        totalsent = 0
        wordspersentence = 0
        sent = re.split(r'[.!?]+', x)

        totalsent = len(sent)
        del sent[-1]
        totalsent = len(sent)

        words = x.split()
        num_words = len(words)
        totalcharacters = 0
        for word in words:
            characterlist = list(word)
            s = set(characterlist)

            if '.' in s:
                del characterlist[-1]
            elif ',' in s:
                del characterlist[-1]
            elif '?' in s:
                del characterlist[-1]
            elif '!' in s:
                del characterlist[-1]

        totalcharacters = totalcharacters + len(characterlist)

    averagecharacters = totalcharacters / num_words

    averagewordspersent = num_words / totalsent

    print("Paragraph Analysis for " + str(inputfile))

    print("*********************************************************")

    print("Total Word Count:", num_words)

    print("Total Sentence Count:", totalsent)

    print("The average letter count is: " + str(averagecharacters))

    print("The average sentence length is: " + str(averagewordspersent))

    print("*********************************************************")

    file.close()


#calles to main module
paragraph("paragraph_1.txt", "paragraph1out.csv")
paragraph("paragraph_2.txt", "paragraph2out.csv")
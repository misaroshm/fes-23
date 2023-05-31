# main.py

# this function removes punctuation marks from given string
def deletepunctuation(content: str) -> str:
    listbuff, l = [], len(content)
    for i in range(l):
        if content[i] in ('.', ',', ':', ';'):
            continue
        listbuff.append(content[i])
    return ''.join(listbuff)

def ReadFile(filepath: str) -> tuple[str, int, int]:
    istream = open(filepath, "r", encoding="windows-1252")
    ibuffer = ""
    #ostream = open(AddTailToFilename(filepath, "_info"), "w+", encoding="windows-1252")
    sents, wrds = 0, 0
    for line in istream:
        ibuffer += line
        for word in line.split():
            wrds += 1
            if word[len(word) - 1] == '.':
                sents += 1
    return (ibuffer, wrds, sents)

def CheckPalindrome(word: str) -> bool:
    if len(word) == 1:
        return True
    i, j = 0, len(word) - 1
    for i in range(j):
        if (word[i] != word[j - i]):
            return False
    return True

def GetAllPalindromes(content: str) -> dict:
    palindromes = {}
    text = deletepunctuation(content).split()
    for word in text:
        if (CheckPalindrome(word)):
            if word[0] not in palindromes:
                palindromes[word[0]] = []
            palindromes[word[0]].append(word)
    return palindromes

def getallpalingrams(content: str) -> tuple[dict, int]:
    if len(content) == 0:
        return ({}, 0)
    palingrams, palcount = {}, 0
    text = deletepunctuation(content).split()
    for word in text:
        if len(word) == 1:
            continue
        for coword in text:
            if coword != word:
                if CheckPalingram(word, coword) == (True, False):
                    print(word)
                    if not word[0] in palingrams:
                        palingrams[word[0]] = [1]
                    else: palingrams[word[0]][0] += 1
                    palingrams[word[0]].append([word, coword])
                    palcount += 1
                if CheckPalingram(word, coword) == (True, True):
                    if not word[0] in palingrams:
                        palingrams[word[0]] = [1]
                    else: palingrams[word[0]][0] += 1
                    palingrams[word[0]].append([word, coword, '*'])
                    palcount += 1
    return (palingrams, palcount)

#####  #####

# this function checks whether two given words makes in-pair special palindrome or not
def CheckPalingram(word1: str, word2: str) -> tuple[bool, bool]:
    if CheckPalindrome(word1 + word2):
        return (True, False)
    else:
        len1, len2 = len(word1), len(word2)
        oddatleast, bdict1, bdict2 = 1, {}, {}
        bdictmax = (lambda x, y: (x, y) if len(x) >= len(y) else (y, x))
        for i in range(len1):
            if not word1[i] in bdict1:
                bdict1[word1[i]] = 1
            else:
                bdict1[word1[i]] += 1
        for i in range(len2):
            if not word2[i] in bdict2:
                bdict2[word2[i]] = 1
            else:
                bdict2[word2[i]] += 1
        temp = bdictmax(bdict1, bdict2)
        bdt = temp[0].copy()
        for i in temp[0]:
            if i in temp[1]:
                if (temp[0][i] + temp[1][i]) % 2 == 0:
                    continue
                else:
                    oddatleast -= 1
            else:
                del bdt[i]
                if temp[0][i] % 2:
                    continue
                else:
                    oddatleast -= 1
            if oddatleast == -1:
                return (False, False)
        if bdt == temp[1]:
            return (True, True)
    return (False, False)

#main program
tp = ReadFile("K:\\_python\\2of4brif.txt")
#print(tp[0].split())
#print(tp[0])
#print(getallpalingrams(tp[0]))
print(GetAllPalindromes(tp[0]))
#print(getallpalingrams("nurses run, stir grits, devils lived, bedroom boredom, mowed ameadow"))
#print(GetAllPalingrams(tp[0]))
#print(tp[1])
#rword = word[::-1]
#print(word[3:])
#print(rword[len(word) - 3:])
#print(word[0:])
#print(word[0::-1])
#print(rword[len(word) - 1:])
#print(has_dict_atleast_all_values_even("mowed", "ameadow"))
print(CheckPalingram("mowed", "ameadow"))
#print(CheckPalingram("boredom", "bedroom"))
# end main.py

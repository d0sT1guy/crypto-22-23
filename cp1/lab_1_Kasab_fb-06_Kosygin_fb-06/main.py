from collections import Counter
from math import log
from shutil import rmtree
from re import sub
import os
NewDir = 'Result'
ParentDir = 'D:/ВСЁ МОЁ/KPI/SEM5/Крипта/Labs/crypto-22-23/cp1/Kasab_fb-06_Kosygin_fb-06'
os.chdir(ParentDir)
path = os.path.join(ParentDir, NewDir)
if os.path.exists(NewDir) is True:
    rmtree(NewDir)
    os.mkdir(path)
else:
    os.mkdir(path)

with open('NGNL.txt', 'r', encoding='utf-8') as f:
    file = f.read()
file = sub(r'[^а-яА-Я ]', '', file).lower()
Rfile = file.replace('\n', '')
RfileNoSpaces = Rfile.replace(' ', '')

def Redundancy(H8):
    H0 = log(34, 2)
    return 1 - H8 / H0

def RedundancyNoSpace(H8):
    H0 = log(33, 2)
    return 1 - H8 / H0

def Sort(Dict):
    SortDict = {key: value for key, value in sorted(Dict.items(), key=lambda item: item[1])}
    return SortDict

def ValueCounts(NGNL):
    numd = Counter(NGNL)
    return numd

def ValueFrequency(FreqChar):
    ValueFreq = {}
    CharSum = 0
    for i in FreqChar.values():
        CharSum += i
    for key,value in FreqChar.items():
        ValueFreq[key] = value / float(CharSum)
    return ValueFreq
H1Frequency = Sort(ValueFrequency(ValueCounts(Rfile)))
H1FrequencyNoSpaces = Sort(ValueFrequency(ValueCounts(RfileNoSpaces)))

def Entropy(ValueText, x):
    Entropy = 0
    for i in ValueText:
        Entropy += -ValueText[i] * log(ValueText[i], 2)
    if x == 'bigram':
        Entropy = Entropy * 1 / 2
    return Entropy
Result = '------H1 entropy------'
Result += '\nH1:                                ' + str(Entropy(H1Frequency, 'monogram'))
Result += '\nH1 without spaces:                 ' + str(Entropy(ValueFrequency(ValueCounts(RfileNoSpaces)), 'monogram'))
Result += '\nH1 with redundancy:                ' + str(Redundancy(Entropy(H1Frequency, 'monogram')))
Result += '\nH1 without spaces with redundancy: ' + str(Redundancy(Entropy(ValueFrequency(ValueCounts(RfileNoSpaces)), 'monogram')))

def BigramsCount(NGNL):
    numd = {}
    SlideBigram = [NGNL[i:i + 2] for i in range(0, len(NGNL), 2)]
    for i in SlideBigram:
        numd.setdefault(i, 0)
        numd[i] += 1
    return numd
Bigram = Sort(ValueFrequency(BigramsCount(Rfile)))
BigramNoSpaces = Sort(ValueFrequency(BigramsCount(RfileNoSpaces)))

Result += '\n\n---H2 entropy---'
Result += '\nH2 bigrams:                                ' + str(Entropy(Bigram, 'bigram'))
Result += '\nH2 bigrams without spaces:                 ' + str(Entropy(BigramNoSpaces, 'bigram'))
Result += '\nH2 bigrams with redundancy:                ' + str(Redundancy(Entropy(Bigram, 'bigram')))
Result += '\nH2 bigrams without spaces with redundancy: ' + str(RedundancyNoSpace(Entropy(BigramNoSpaces, 'bigram')))

with open('Result/H1Frequency.csv', 'w') as f: 
    for key, value in H1Frequency.items(): 
        f.write('%s;%s\n' % (key, value))
with open('Result/H1FrequencyNoSpaces.csv', 'w') as f: 
    for key, value in H1FrequencyNoSpaces.items(): 
        f.write('%s;%s\n' % (key, value))
with open('Result/Bigram.csv', 'w') as f: 
    for key, value in Bigram.items(): 
        f.write('%s;%s\n' % (key, value))
with open('Result/BigramNoSpaces.csv', 'w') as f: 
    for key, value in BigramNoSpaces.items(): 
        f.write('%s;%s\n' % (key, value))
with open('Result/Result.txt', 'w', encoding='utf-8') as f: 
        f.write(Result)
"""
Author : Pavan Kulkarni

Rules of first -->
1. First(terminal) - terminal
2. First(ε) - ε
3. First(nT) - First(nT) - terminal ; if ε then replace and find again

Rules of follow -->
1. First(S) - A but A is non terminal or variable -> First(A) -> {a, @} 	
2. First(A) - terminal,epsilon

Rules for LL(1) Table --> 
1. Number the production as 1 2 3 and so on. They are production numbers
2. For table, select the non-terminal and find its first and fill the production number in the resp column. 
3. If one of the production starts with ε then the write the production number in corresponding non-terminal's follow

Using bottom-up approach for finding first 
Using top-down approach for finding follow
"""

import re
from prettytable import PrettyTable 

reg1 = "(?:[*+()@]|[a-z])"
reg2 = "(id)"
reg3 = "(?:[*+()]|[a-z])"

def cal_firsts(rhsList, prodDict, firstDict, i):
    firstSet = set()
    for ele in rhsList:
        if re.match(reg2, ele):
            firstSet.add(ele)
        elif re.match(reg1, ele[i]):
            firstSet.add(ele[i])
        else:
            tempSet = set()
            tempSet.update(firstDict[ele[i]])
            i+=1
            if '@' in tempSet and i < len(ele):
                tempSet.update(cal_firsts(rhsList, prodDict, firstDict, i))
            firstSet.update(tempSet)
    return firstSet

def first(nTKeys, prodDict):
    firstDict = {}
    for nT in reversed(nTKeys): #done for bottom-up approach
        firstDict[nT] = cal_firsts(prodDict[nT], prodDict, firstDict, 0)
    return firstDict

def cal_follow(nT, prodDict, followDict, firstDict):
    followSet = set()
    for key in prodDict:
            for exp in prodDict[key]:
                if nT in exp:
                    if exp.index(nT) == len(exp)-1:
                        if key in list(followDict):
                            return followDict[key]
                        else:
                            cal_follow(key, prodDict, followDict, firstDict)
                    else:
                        if re.match(reg3, exp[exp.index(nT)+1]):
                            return set(exp[exp.index(nT)+1])
                        else:
                            followSet.update(firstDict[exp[exp.index(nT)+1]])
                            if '@' in followSet:
                                followSet.remove('@')
                                if exp[exp.index(nT)+1] in list(followDict):
                                    return followDict[key]
                                else:
                                    followSet.update(cal_follow(exp[exp.index(nT)+1], prodDict, followDict, firstDict))
    return followSet



def follow(nTKeys, prodDict, firstDict):
    followDict = {}
    for nT in nTKeys:
        followDict[nT] = cal_follow(nT, prodDict, followDict, firstDict)
        if nT == 'S':
            followDict[nT].add('$') 
    return followDict




if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        productions = [line.strip() for line in f]
    # print('The given production is - ', productions)
    
    prodDict = {}
    for production in productions:
        nT, rhs = production.split(' --> ')
        prodDict[nT] = rhs.split(' | ')

    rhs = [] # for LL(1)
    for nT in prodDict:
        rhs.append(prodDict[nT])
        print(nT, ':', prodDict[nT])
    
    nTKeys = list(prodDict)
    
    # return values of first to be stored in a dict
    firstDict={}
    firstDict = first(nTKeys, prodDict)
    print('First ---->')
    for keys in nTKeys:
        print(keys, ':', firstDict[keys])
    
    # returns values of follow (dict)
    followDict = follow(nTKeys, prodDict, firstDict)
    print('Follow ---->')
    for key in nTKeys:
        # terminalSet.add(followDict[key])
        print(key, ':', followDict[key])

    # LL(1) Parser
    print('nonterminal keys', nTKeys)
    print('rhslist - ',rhs)

    terminal = []
    for r in rhs:
        for e in r:
            if re.match(reg2, e):
                terminal.append(e)
                continue
            for j in e:
                if re.match(reg1, j):
                    terminal.append(j)
    print('terminals - ',terminal)


    myTable = PrettyTable(['nT/T'] + terminal)



    print(myTable)


    
    


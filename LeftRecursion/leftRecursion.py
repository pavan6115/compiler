"""
Author : Pavan Kulkarni

Elimination of LR - 
A --> Aα | β

A --> βA'
A' --> αA' | ε

Given Production -
S --> Sda | b
A --> Ac | Sd

Output - 
S --> bS'
S' --> daS' | ε

A --> SdA'
A' --> cA' | ε
"""

# 1 logic
# def directLR(nT, rhs, prodDict, nTKeys):  
#     # i to check the first alphabet in lhs and rhs of the production
#     if nTKeys[0] == prodDict['S'][0][0]:
#         print(nTKeys[0], '-->', prodDict['S'][1], nTKeys[0]+"'")
#         print(nTKeys[0]+"'", '-->', prodDict['S'][0][1:3], nTKeys[0]+"'", "| ε")
#     else:
#         pass

#     if nTKeys[1] == prodDict['A'][0][0]:
#         print(nTKeys[1], '-->', prodDict['A'][1], nTKeys[1]+"'")
#         print(nTKeys[1]+"'", '-->', prodDict['A'][0][1], nTKeys[1]+"'", "| ε")
#     else:
#         pass

# 2 logic
def directLR(nTKeys, rhsList):
    for key in nTKeys:
        for element in rhsList:
            if key == element[0][0]:
                print(key + ' --> ', element[1] + key + "'")
                print(key + "'" + ' --> ' + element[0][1] + key + "'" + "| ε")
            



if __name__ == "__main__":
    with open('LR_input.txt', 'r') as f:
        rhs_prod = [line.strip() for line in f]
    # print(rhs_prod)

    prodDict = {}
    nTKeys = []
    rhsList = []
    for prod in rhs_prod:
        nT, rhs = prod.split(' --> ')
        prodDict[nT] = rhs.split(' | ')
        nTKeys.append(nT)
        rhsList.append(prodDict[nT])
    # print('Prod dict - ', prodDict)
    # print('nTKeys --', nTKeys)
    # print('rhsList', rhsList)

    # directLR(nT, rhs, prodDict, nTKeys)
    directLR(nTKeys, rhsList)
    



def alien(words, order):
    ord = {}

    for i, v in enumerate(order):
        ord[v] = i
    
    #compare adj words
    for i in range(len(words)-1):

        for j in range(len(words[i])):
            if j >= len(words[i+1]):
                #if later word, ends before, earlier word
                return False
            
            #if unsame words, then later word needs to be later
            if words[i][j] != words[i+1][j]:
                if ord[words[i][j]] > ord[words[i+1][j]]:
                    return False
    
    return True
def solution(S, K):
    # write your code in Python 3.6
    if len(S) < K or K < 0:
        return 0    
    if len(S) > 2 and K < 2 and K > 0:
        return len(S) - K
    
    idx = 1
    newStr = ''
    repeatNumb = 1
    foundTrimChars = False

    words = []
    while idx < len(S):
        char1 = S[idx - 1]
        char2 = S[idx]   
        if char1 == char2:
            repeatNumb = repeatNumb + 1
        else:
            if repeatNumb > 1:                
                words.append(str(repeatNumb))
            words.append(str(char1))

        idx = idx + 1

    if repeatNumb > 1:
        words.append(str(repeatNumb)) 
    words.append(str(char1))

    print (words)
    return len(words)

    # while idx < len(S):
    #     char1 = S[idx - 1]
    #     char2 = S[idx]   
    #     if char1 == char2:
    #         repeatNumb = repeatNumb + 1
    #     else:  
    #         if len(newStr) > 2 and newStr[-1] == char2 and isInt(newStr[-2]) and repeatNumb > 1 and foundTrimChars == False and K < (int(newStr[-2]) + repeatNumb):
    #                 foundTrimChars = True
    #                 repeatNumb = int(newStr[-2]) - (K - repeatNumb) + 1
    #                 newStr = newStr[:-2]
    #         else:
    #             if repeatNumb > 1:                
    #                 newStr=newStr + str(repeatNumb)
    #             newStr = newStr + char1           
    #             repeatNumb = 1                
    #     idx = idx + 1

    # if repeatNumb > 1:
    #     newStr=newStr + str(repeatNumb)        
    # newStr=newStr + char2
      
    # print (newStr)
    # return len(newStr)

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

S = "ABBBCCDDCCC"
K = 3
print (solution (S, K))

S = "ABCDDDEFG"
K = 3
print (solution (S, K))
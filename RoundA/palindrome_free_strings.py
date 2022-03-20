import re
from itertools import product
def isPalindrome(S):
    s = re.sub(r"[\d]","",S)
    L = []
    R = list(product("01", repeat=len(s)))
    for i in range(len(R)):
        cnt = 0
        L.append(list(S))
        for j in range(len(S)):
            if L[i][j]=='?':
                L[i][j] = R[i][cnt]
                cnt += 1

    L0 = list(map(lambda x: "".join(x).split('0'), L))
    L0 = list(map(lambda x: "111" in x or ("*".join(x)).split("1").count("***") > 0 , L0))
    L1 = list(map(lambda x: "".join(x).split('1'), L))
    L1 = list(map(lambda x: "000" in x or ("*".join(x)).split("0").count("***") > 0, L1))
    if (False in L0) or (False in L1):
        return False
    return True
    
def main():
    for t in range(1, int(input()) + 1):
        N = int(input())
        S = input()
        if isPalindrome(S):
            print(f"Case #{str(t)}: IMPOSSIBLE")
        else:
            print(f"Case #{str(t)}: POSSIBLE")
        
if __name__=="__main__":
    main()
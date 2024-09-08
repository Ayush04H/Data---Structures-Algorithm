map = {}
def isscramble(s1,s2):
    m ={}
    def func(s1, s2):
        if (s1, s2) in m:
            return m[(s1, s2)]
        if not sorted(s1) == sorted(s2):
            return False
        if len(s1) == 1:
            return True
            

        for i in range(1, len(s1)):
            if func(s1[:i], s2[-i:]) and func(s1[i:], s2[:-i]) or func(s1[:i], s2[:i]) and func(s1[i:], s2[i:]):
                m[(s1, s2)] = True
                return True
        m[(s1, s2)] = False
        return False
    return func(s1, s2)
if __name__ == "__main__":
     
    S1 = "coder"
    S2 = "ocder"
     
    if (isscramble(S1, S2)):
        print("Yes")
    else:
        print("No")
        

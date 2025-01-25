def strinf_rot(s1,s2):
    if len(s1) != len(s2):
        print(False)
    
    temp = ''
    temp = s1+s1
    print(temp)
    print(temp.find(s2) != -1)


s1 = 'abab'
s2 = 'abba'
(strinf_rot(s1,s2))
class Solution:
    def decodeString(self, s: str) -> str:
        st = ''
        i = 0
        while i < len(s): 
            if not s[i].isdigit():
                st = st + s[i]
            else:
                findB = s.index('[', i)
                d = int(s[i : findB])
                j = findB + 1
                countB = 1
                temp = ''
                
                #Find the string to multiply by d times
                while True:
                    if s[j] == '[':
                        countB = countB + 1
                    elif s[j] == ']':
                        countB = countB - 1
                    if countB == 0:
                        break
                    else:
                        temp = temp + s[j]
                    j = j + 1
                    
                temp = self.decodeString(temp)
                temp = d* temp
                st = st + temp
                i = j
            i = i + 1
        return st

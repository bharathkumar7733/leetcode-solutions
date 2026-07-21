class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frq ={}

        for chars in s :
            if chars in frq:
                frq[chars] +=1
            else:
               frq[chars] =1
                    
            
            #arr_eq = True

        for chars in t:
            if chars not in frq or frq[chars] == 0:
                return False
                

            frq[chars] -=1
        return True

        
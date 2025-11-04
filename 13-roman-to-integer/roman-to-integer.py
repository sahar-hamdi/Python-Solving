class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        rom = {'I': 1,
        'V' : 5,
        'X' : 10,
        'L' : 50 ,
        'C' : 100,
        'D' : 500,
        'M' : 1000}
        

        for c in range(len(s)-1) :
            if rom[s[c]] < rom[s[c+1]]:
                sum -= rom[s[c]]
            else:
                sum += rom[s[c]]
        
        sum += rom[s[-1]]
        return sum
"""
    Example of code of https://leetcode.com/problems/roman-to-integer
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_string = list(s)
        int_sum = 0
        index_ = len(roman_string)-1
        
        while index_ >= 0: 
            if roman_string[index_] == 'I':
                int_sum+=1
                index_-=1

            elif roman_string[index_] == 'V':
                if index_-1 >= 0:
                    if roman_string[index_-1] == 'I' and roman_string[index_] == 'V':
                        int_sum+=4
                        index_-=2
                    else:    
                        int_sum+=5
                        index_-=1
                else:
                    int_sum+=5
                    index_-=1

            elif roman_string[index_] == 'X':
                if index_-1 >= 0:
                    if roman_string[index_-1] == 'I' and roman_string[index_] == 'X':
                        int_sum+=9
                        index_-=2
                    else:    
                        int_sum+=10
                        index_-=1
                else:    
                    int_sum+=10
                    index_-=1

            elif roman_string[index_] == 'L':
                if index_-1 >= 0:
                    if roman_string[index_-1] == 'X' and roman_string[index_] == 'L':
                        int_sum+=40
                        index_-=2
                    else:    
                        int_sum+=50
                        index_-=1
                else:    
                    int_sum+=50
                    index_-=1

            elif roman_string[index_] == 'C':
                if index_-1 >= 0:
                    if roman_string[index_-1] == 'X' and roman_string[index_] == 'C':
                        int_sum+=90
                        index_-=2
                    else:    
                        int_sum+=100
                        index_-=1
                else:    
                    int_sum+=100
                    index_-=1

            elif roman_string[index_] == 'D':
                if index_-1 >= 0:
                    if roman_string[index_-1] == 'C' and roman_string[index_] == 'D':
                        int_sum+=400
                        index_-=2
                    else:    
                        int_sum+=500
                        index_-=1
                else:    
                    int_sum+=500
                    index_-=1

            elif roman_string[index_] == 'M':
                if index_-1 >= 0:
                    if roman_string[index_-1] == 'C' and roman_string[index_] == 'M':
                        int_sum+=900
                        index_-=2
                    else:    
                        int_sum+=1000
                        index_-=1
                else:    
                    int_sum+=1000
                    index_-=1
        return int_sum
    

if __name__ == '__main__':
    roman_number = 'MCMXCIV'
    int_number = Solution().romanToInt(roman_number)
    print(int_number)

"""
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    
"""




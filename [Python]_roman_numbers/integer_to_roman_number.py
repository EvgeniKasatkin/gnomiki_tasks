"""
    Example of code of https://leetcode.com/problems/integer-to-roman/
"""

class Solution:
    def intToRoman(self, num) -> str:
        num = str(num)
        list_num = list(num)
        list_num.reverse()
        roman_num = []

        for index_, value_ in enumerate(list_num):

            if index_ == 3:
                num = 'M' * int(list_num[index_])

            if index_ == 2:
                if int(list_num[index_]) < 4:
                    num = 'C' * int(list_num[index_])
                elif int(list_num[index_]) == 4:
                    num = 'CD'
                elif int(list_num[index_]) >= 5 and int(list_num[index_]) < 9:
                    num = 'D' + 'C'*(int(list_num[index_]) - 5)
                elif int(list_num[index_]) == 9:
                    num = 'CM' 
            
            if index_ == 1:
                if int(list_num[index_]) < 4:
                    num = 'X' * int(list_num[index_])
                elif int(list_num[index_]) == 4:
                    num = 'XL'
                elif int(list_num[index_]) >= 5 and int(list_num[index_]) < 9:
                    num = 'L' + 'X'*(int(list_num[index_]) - 5)
                elif int(list_num[index_]) == 9:
                    num = 'XC' 
            
            if index_ == 0:
                if int(list_num[index_]) < 4:
                    num = 'I' * int(list_num[index_])
                elif int(list_num[index_]) == 4:
                    num = 'IV'
                elif int(list_num[index_]) >= 5 and int(list_num[index_]) < 9:
                    num = 'V' + 'I'*(int(list_num[index_]) - 5)
                elif int(list_num[index_]) == 9:
                    num = 'IX'

            roman_num.append(num)
        roman_num.reverse()
        roman_num_str = ''.join(roman_num)

        return roman_num_str


if __name__ == '__main__':
    number = 563
    roman_number = Solution().intToRoman(num = number)
    print(roman_number)

"""
    Input: number = 563
    Output: 'DLXIII'
    
"""




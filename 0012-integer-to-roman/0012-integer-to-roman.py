class Solution:
    def intToRoman(self, num: int) -> str:
        #
        hashh = {
                    1000: 'M',
                    500: 'D',
                    100: 'C',
                    50: 'L',
                    10: 'X',
                    5: 'V',
                    1: 'I'
                }
        hashh_check = {
                        100:['D','M'],  
                        10:['L','C'],
                        1:['V','X']     
                    }
        ans = []
        while num:
            place = 10**(math.floor(log10(num)))
            first_num = num//(place)
            number = first_num*place
            if first_num!=4 and first_num!=9:
                while number:
                    for value in hashh:
                        if number>=value:
                            ans.append(hashh[value])
                            number-=value
                            break
            else:
                for value in hashh_check:
                    if number>value:
                        ans.append(hashh[value])
                        if first_num == 4:
                            ans.append(hashh_check[value][0])
                        else:
                            ans.append(hashh_check[value][1])
                        break
            num%=place
        return ''.join(ans)


                    




        
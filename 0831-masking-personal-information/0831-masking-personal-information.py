class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            email = s.split('@')
            name = email[0][0]+'*****'+email[0][-1]
            return name+'@'+email[1]
        else:
            num = []
            for value in s:
                if value.isdigit():
                    num.append(value)
            num = ''.join(num)
            country_num = len(num)-10
            country_code = '+'+'*'*country_num
            return '***-***-'+num[-4:] if country_num == 0 else country_code+'-***-***-'+num[-4:]


        
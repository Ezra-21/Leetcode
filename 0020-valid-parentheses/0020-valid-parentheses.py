
class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        found = True
        for char in s:
            if char in "({[":
                lis.append(char)
            else:
                if (len(lis)==0):
                    return False
                top = lis.pop() 
                if char == ")" and top!="(":
                    return False
                elif char == "}" and top!="{":
                    return False
                elif char == "]" and top!="[":
                    return False
        if found and len(lis)==0:
             return(True)
        return(False)
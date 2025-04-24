class Solution:
    def defangIPaddr(self, address: str) -> str:
        new = address.replace('.','[.]')
        return new
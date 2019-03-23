class Solution:
    def isNumber(self, s: str) -> bool:
        if re.match(r"^\s*[+-]?([0-9]+(\.[0-9]*)?|\.[0-9]+)(e[+-]?[0-9]+)?\s*$", s):
            return True
        else:
            return False
    
        
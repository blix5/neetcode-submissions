class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += (str(len(string)) + '#' + string)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            previ = i
            while s[i] != '#':
                i += 1
            length = int(s[previ:i])
            strs.append(s[i+1:i+1+length])
            i += length+1
                
        return strs

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += (str(len(string)) + '#' + string)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        buffer = ''
        length = -1
        i = 0
        while i < len(s):
            if length == -1:
                buffer += s[i]
                if s[i] == '#':
                    length = int(buffer[:len(buffer)-1])
                    buffer = ''
                i += 1
            if length >= 0:
                strs.append(s[i:i+length])
                i += length
                length = -1
                
        return strs

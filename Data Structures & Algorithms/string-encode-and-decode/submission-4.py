class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for string in strs:
            encoded_string += f"{len(string)}#{string}"

        return encoded_string

    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        result = []
        last_break = 0 
        print("s",s)
        i = 0

        while i <= len(s):
            length = 0
            print("i",i)
            print("s[i]",s[i])
            if s[i] == '#': 
            # and s[i-1] and s[i-1].isdigit() :
                # print("s[i-1]",s[i-1])
                # print("s[i]",s[i])
                print("iin #",i)
                length = int(s[last_break:i])
                last_break = i + length + 1
                string_to_add = s[i+1:i+length+1]
                result.append(string_to_add)
                print(string_to_add)
                i += length + 2
            else:
                i += 1

        return result


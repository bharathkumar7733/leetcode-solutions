class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curnum = 0
        curs = ""

        for char in s:
            if char.isdigit():
                curnum = curnum * 10 + int(char)

            elif char == "[":
                stack.append((curnum, curs))
                curnum = 0
                curs = ""

            elif char == "]":
                number, prev = stack.pop()
                curs = prev + curs * number

            else:
                curs += char

        return curs

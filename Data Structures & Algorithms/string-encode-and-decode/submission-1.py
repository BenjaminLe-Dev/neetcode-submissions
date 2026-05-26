class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for i in strs:
            #For each character in this string from the list
            for c in i:
                sentence += str(ord(c))
                sentence += ' '
            #Use this to mark the end of the string
            sentence += "!"
        return sentence


    def decode(self, s: str) -> List[str]:
        decodeList = []
        numHolder = ""
        fullString = ""
        #For each letter in this string
        for i in s:
            #Right now the structure is "c c c !" where  c = character and ! = end of string
            if i != " " and i != "!":
                numHolder += i
            #' ' represents the end of one char so we need to chr here
            elif i == " ":
                fullString += chr(int((numHolder)))
                numHolder = ""
            #! represents the end of the string itself, this is when we append
            elif i == "!":
                decodeList.append(fullString)
                fullString = ""
                numHolder = ""
        return decodeList





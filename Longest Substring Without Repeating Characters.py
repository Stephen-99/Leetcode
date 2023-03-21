def lengthOfLongestSubstring(s: str) -> int:
        #use that algorithm
            #ahh yep that one.
        #The one where we essentially have a slidign window, i did it in mp last sem. I shoulda remembered 
        #Found out it's Kadane's Algorithm

        

        best = 0
        chars = {}
        startIdx = 0 
        for ii, char in enumerate(s):
            badIdx = chars.get(char)
            if badIdx != None:
                subStrLen = ii - startIdx
                if (subStrLen) > best:
                    best = subStrLen
                
                #Delete chars not part of current sub String
                for idx in range(startIdx, badIdx):
                    chars.pop(s[idx])
                startIdx = badIdx + 1

            chars[char] = ii

        subStrLen = len(s) - startIdx
        if (subStrLen) > best:
            best = subStrLen

        return best

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring(" ") == 1
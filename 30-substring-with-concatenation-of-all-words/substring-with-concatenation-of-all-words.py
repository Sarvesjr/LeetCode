class Solution:
    def findSubstring(self, s, words):
        n = len(s)
        wordLen = len(words[0])
        sentenceDesireLen = wordLen * len(words)

        result = []
        mp = {}

        for word in words:
            if word not in mp:
                mp[word] = [0, 0]
            mp[word][0] += 1

        for i in range(wordLen):
            left = i
            right = i

            while right <= n - wordLen and left <= n - sentenceDesireLen:
                word = s[right:right + wordLen]

                if word in mp:
                    freq = mp[word]

                    while freq[0] == freq[1]:
                        prevWord = s[left:left + wordLen]
                        mp[prevWord][1] -= 1
                        left += wordLen

                    freq[1] += 1

                else:
                    while left != right:
                        prevWord = s[left:left + wordLen]
                        mp[prevWord][1] -= 1
                        left += wordLen

                    left += wordLen

                right += wordLen

                if right - left == sentenceDesireLen:
                    result.append(left)

            while left != right:
                prevWord = s[left:left + wordLen]
                mp[prevWord][1] -= 1
                left += wordLen

        result.sort()
        return result
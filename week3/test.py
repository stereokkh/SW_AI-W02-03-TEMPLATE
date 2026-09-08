class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        word_set = set(wordList)

        dic = {beginWord :set(), endWord:set()}

        for i in wordList:
            dic[i] = set()
            
        for i in dic:
            for word_index in range(len(i)): #index 0~n
                for char in range(ord('a'), ord('z') + 1):
                    possible_next_word = i[:word_index] + chr(char) + i[word_index+1:]
                    if possible_next_word in word_set:
                        dic[i].add(possible_next_word)
                dic[i].discard(i)
        return dic

if __name__ == "__main__":
    a = Solution()
    dic = a.ladderLength("cat", "eat", ["met", "rat", "ctt", "cal", "ret"])

    print(dic)
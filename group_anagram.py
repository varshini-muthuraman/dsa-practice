class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashAnagram = {}
        for char in strs:
            sorted_char = tuple(sorted(char))
            if sorted_char not in hashAnagram:
                hashAnagram[sorted_char] = []
            hashAnagram[sorted_char].append(char)

        return list(hashAnagram.values())
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        t = ord(target)
        for x in letters:
            if ord(x)>t:
                return x
        return letters[0]

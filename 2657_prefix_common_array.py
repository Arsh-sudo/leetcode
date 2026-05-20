class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:

        seenA = set()
        seenB = set()

        common = 0
        result = []

        for a, b in zip(A, B):

            seenA.add(a)
            seenB.add(b)

            if a in seenB:
                common += 1

            if b in seenA:
                common += 1

            # if both are same, we counted twice
            if a == b:
                common -= 1

            result.append(common)

        return result
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr = 0
        step = 1

        for ch in s:
            rows[curr] += ch

            if curr == 0:
                step = 1
            elif curr == numRows - 1:
                step = -1

            curr += step

        return "".join(rows)
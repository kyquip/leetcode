class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currentRow = 0
        direction = True

        for char in s:
            rows[currentRow] += char

            if currentRow == 0:
                direction = True
            elif currentRow == numRows - 1:
                direction = False

            if direction:
                currentRow += 1
            else:
                currentRow -= 1

        return "".join(rows)

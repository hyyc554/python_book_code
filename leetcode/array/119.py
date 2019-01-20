class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        for i in range(rowIndex):
            row = [1]+[row[j]+row[j+1] for j in range(len(row)-1)]+[1]

            return row

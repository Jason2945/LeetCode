class Solution:
    # Done it without bin method
    def addBinary(self, a: str, b: str) -> str:
        binarySum = ""
        holder = 0
        intArr = list(str(int(a) + int(b)))
        for index in range(len(intArr)-1, -1 ,-1):
            if holder == 1:
                if intArr[index] == '2':
                    intArr[index] = '1'
                elif intArr[index] == '1':
                    intArr[index] = '0'
                else :
                    intArr[index] = '1'
                    holder = '0'
                if index == 0:
                        intArr = ['1'] + intArr
                        binarySum = ''.join(intArr)
                        return binarySum
            else :
                if intArr[index] == '2':
                    intArr[index] = '0'
                    holder = 1
                    if index == 0:
                        intArr = ['1'] + intArr
                        binarySum = ''.join(intArr)
                        return binarySum
                if index == 0:
                    binarySum = ''.join(intArr)
                    return binarySum





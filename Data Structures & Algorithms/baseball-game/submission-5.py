class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []
        for i in operations:
            if i == "+":
                ops.append(ops[-1]+ops[-2])
            elif i == "D":
                ops.append(ops[-1]*2)
            elif i == "C":
                del ops[-1]
            else:
                ops.append(int(i))
        
        return sum(ops)
        
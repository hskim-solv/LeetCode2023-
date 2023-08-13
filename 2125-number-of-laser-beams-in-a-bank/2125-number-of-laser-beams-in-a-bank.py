class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        n1 = bank.pop()
        while bank and "1" not in n1:
            n1 = bank.pop()
        while bank:
            node = bank.pop()
            if "1" in node:

                res += n1.count("1") * node.count("1")
                n1 = node
        return res            
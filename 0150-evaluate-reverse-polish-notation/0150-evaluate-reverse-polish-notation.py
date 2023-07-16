class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = tokens[::-1]
        ops = ["+","-","*","/"]
        stack1=[]
        stack2=[]
        def cal(n1,n2,op):
            if op == '*':
                return n2*n1
            elif op =='+':
                return n2+n1
            elif op == '/':
                return trunc(n2/n1)
            else:
                return n2-n1
        while tokens:
            token = tokens.pop()
            if token in ops:
                if len(stack2) > 1:
                    n1 = stack2.pop()
                    n2 = stack2.pop()
                    stack2.append(cal(n1,n2,token))
                else:
                    stack1.append(token)
            else:
                if len(stack1) > 0 and len(stack2) > 0:
                    n2 = stack2.pop()
                    op = stack1.pop()
                    stack2.append(cal(int(token),n2,op))
                else:
                    stack2.append(int(token))
        return stack2[0]
                
        
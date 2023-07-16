class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = tokens[::-1]
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
            if token.lstrip("-").isdecimal():
                #print(token)
                stack2.append(int(token))
            else:
                stack1.append(token)
            if len(stack2) > 1 and len(stack1) > 0:
                n1 = stack2.pop()
                n2 = stack2.pop()
                op = stack1.pop()
                stack2.append(cal(n1,n2,op))
        return stack2[0]
                
        
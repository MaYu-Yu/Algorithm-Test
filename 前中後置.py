from pickletools import StackObject


class Solution:
    isp = list()
    icp = list()
    sym = list()
    def __init__(self):
        self.isp = {'(':0,'^':4,'*':4,'/':4,'+':2,'-':2,')':6,'#':-1}
        self.icp = {'(':6,'^':5,'*':3,'/':3,'+':1,'-':1,')':0,'#':-1}
        self.sym = ['(','^','*','/','+','-',')']
    def calc_post(self, strs):
        stack = list()
        for s in strs:
            if s in self.sym:
                a, b = int(stack.pop()), int(stack.pop())
                if s == '*':
                    c = a*b
                elif s == '/':
                    c = a/b                   
                elif s == '+':
                    c = a+b
                elif s == '-':
                    c = a-b                   
                elif s == '^':
                    c = pow(a,b)
                stack.append(c)
            else:
                stack.append(s)
        return stack.pop()
    def in_to_post(self, strs):
        if len(strs) == 0: 
            print("[ERROR] strs is Empty!")
            return
        print("in_to_post:")        
        result = list()
        stack = list()
        stack.append('#')
        for s in strs:
            if s in self.sym:
                if s == '(':
                    stack.append(s)
                elif s == ')':
                    while stack[-1] != '(': 
                        result.append(stack.pop())
                    stack.pop()
                else:
                    while(self.isp[stack[-1]] > self.icp[s]):
                        result.append(stack.pop()) 
                    stack.append(s)
            else:
                result.append(s)
        while stack[-1] != '#': result.append(stack.pop())
        return "".join(result)
    def post_to_in(self, strs):
        if len(strs) == 0: 
            print("[ERROR] strs is Empty!")
            return
        print("post_to_in:")
    def in_to_pre(self, strs):
        if len(strs) == 0: 
            print("[ERROR] strs is Empty!")
            return
        print("in_to_pre:")
    def pre_to_in(self, strs):
        if len(strs) == 0: 
            print("[ERROR] strs is Empty!")
            return
        print("pre_to_in:")

if __name__ == "__main__":
    x = Solution()
    print(x.in_to_post("((a+b)^(c^d)-e+f)/g"))
    print(x.calc_post("35*4+"))

    # print(x.in_to_pre("A^(B*C)^D"))
    # print(x.post_to_in("ABC*D^^"))
    # print(x.pre_to_in("^A^*BCD"))
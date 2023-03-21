
from Stack import Stack


class Node():
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None
        self.p = None


class Tree():
    def __init__(self):
        self.root = None

class Binary_Search_Tree(Tree):
    def add(self, val):
        def add(val, curr):
            if val < curr.val:
                if curr.l == None:
                    curr.l = Node(val)
                    curr.l.p = curr
                else:
                    add(val, curr.l)
            elif val > curr.val:
                if curr.r == None:
                    curr.r = Node(val)
                    curr.r.p = curr
                else:
                    add(val, curr.r)
        if self.root == None:
            self.root = Node(val)
        else:
            add(val, self.root)


    def delete(self, val):
        curr = self.get_node(val, self.root)
        if curr == None:
            print("val ({}) isn't in the tree.".format(val))
            return 0
    # only have one child
        if curr.l == None:
            self.transplant(curr, curr.r)
        elif curr.r == None:
            self.transplant(curr, curr.l)
        else:
            min = self.tree_minimum(curr.r)
            if min.p != curr:
                self.transplant(curr, curr.r)
                min.r = curr.r
                min.r.p = min
            else:
                self.transplant(curr, min)
                min.l = curr.l
                min.l.p = min

    def transplant(self, curr, next):
        if curr.p == None:
            self.root = next
        elif curr.p.l == curr:
            curr.p.l = next
        else:
            curr.p.r = next

        if curr.p != None:
            next.p = curr.p
    def tree_maximum(self, curr):
        while curr.r != None:
            curr.r
        return curr

    def get_node(self, val, curr):
        while curr != None:
            if curr.val == val:
                return curr
            elif curr.val > val:
                curr = curr.l
            else:
                curr = curr.r
# search
    def show(self):
        if self.root != None:
            print("preOrder:")
            self.preOrder(self.root)
            print("\ninOrder:")
            self.inOrder(self.root)
            print("\npostOrder:")
            self.postOrder(self.root)
    def preOrder(self, t):
        s = Stack()
        s.push(t)
        while not s.isEmpty():
            curr = s.pop()
            if curr != None:
                print(curr.val, end=" ")
                s.push(curr.r)        
                s.push(curr.l)
    def inOrder(self, t):
        s = Stack()
        curr = t
        while curr or not s.isEmpty():
            while curr != None: 
                s.push(curr)
                curr = curr.l
            curr = s.pop()
            print(curr.val, end=" ")
            curr = curr.r
    def postOrder(self, t):         
        s1, s2 = Stack(), Stack()
        curr = t
        s1.push(curr)
        while not s1.isEmpty():
        # 找到後續遍歷的逆序，存到s2中
            curr = s1.pop()
            if curr.l:
                s1.push(curr.l)
            if curr.r:
                s1.push(curr.r)
            s2.push(curr)
        while not s2.isEmpty():
            print(s2.pop().val, end= " ")
    def show_recursive(self):
        if self.root != None:
            print("preOrder:")
            self.pre_order(self.root)
            print("\ninOrder:")
            self.in_order(self.root)
            print("\npostOrder:")
            self.post_order(self.root)

    def pre_order(self, curr):
        if curr != None:
            print(curr.val, end=' ')
            self.pre_order(curr.l)
            self.pre_order(curr.r)
    def in_order(self, curr):
        if curr != None:
            self.in_order(curr.l)
            print(curr.val, end=' ')
            self.in_order(curr.r)
    def post_order(self, curr):
        if curr != None:
            self.post_order(curr.l)
            self.post_order(curr.r)
            print(curr.val, end=' ')
        
    def in_order_stack(self):
        print("\nOrder_stack:")
        t = self.root
        s = []
        s.append((False, t))
        while(len(s) != 0):
            flag, t = s.pop()
            if t != None:
                if flag:
                    print(t.val, end=' ')
                else:
                    s.append((False, t.r))
                    s.append((True, t))
                    s.append((False, t.l))
        print()
# 樹的高度
    def height(self):
        def height(t):
            if t == None:
                return 0
            else:
                return max(height(t.l), height(t.r)) + 1
        return height(self.root)
# 節點總數
    def count_node(self):
        def count_node(t):
            if t == None:
                return 0
            else:
                return count_node(t.l) + count_node(t.r) + 1
        return count_node(self.root)
# 葉節點數
    def leaves(self):
        def leaves(t):
            if t == None:
                return 0
            elif t.l == None and t.r == None:
                return 1
            else:
                return leaves(t.l) + leaves(t.r)
        return leaves(self.root)
# Mirror
    def mirror(self):
        def mirror(t):
            if t != None:
                t.l, t.r = t.r, t.l
                mirror(t.l)
                mirror(t.r)
if __name__ == "__main__":
    arr = [6, 4,8,5,2,1,3]
    t = Binary_Search_Tree()
    for i in arr:
        t.add(i)
    # t.in_order_stack()
    # print("There are ", t.count_node(), " nodes.")
    # print("There are ", t.leaves(), " leaf nodes.")
    # print("Tree's height is ", t.height(), " .")
    #t.mirror()
    t.show()
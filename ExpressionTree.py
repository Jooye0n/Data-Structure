from BinaryTree import BinaryTree
class Stack:
    """General stack implementation using a Python list at the end."""
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return str(self._items)

    def is_empty(self):
        return self._items == []

    def push(self, item):
        """Push item at the end of the list _items"""
        self._items.append(item)

    def pop(self):
        """Pop items at the end of the list _items"""
        if not self.is_empty():
            return self._items.pop()
        else:  # No item can be popped
            return None

    def top(self):
        if not self.is_empty():
            return self._items[-1]
        else:
            return None

class ExpressionTree(BinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree."""
        super().__init__(None)

        root = super().add_root(token)
        self.set_root(root)
        root.set_left(left)
        root.set_right(right)



    def _do_op(self, op, stack):
        """Apply operator from opStack to two operands from valStack"""
        x = stack.pop()
        y = stack.pop()

        if op == '*':
            stack.push(y * x)
        elif op == '+':
            stack.push(y + x)
        elif op == '-':
            stack.push(y - x)
        elif op == '/':
            stack.push(y / x)
        else:
            raise ValueError(f"Unknown operators: {op}")

        # print("\tOp: " + op)
        # print("\t--valStk: {0}".format(val_stack))
        # print("\t--opStk:  {0}".format(op_stack))


    def evaluate(self):
        """Return the numeric result of the expression."""
        if super().is_empty():
            return None

        post_str = self.postfix_string()
        token_list = post_str.split()

        stack = Stack()
        for token in token_list:
            if not token in "+-/*":  # 연산자라면
                stack.push(float(token))
            else:
                self._do_op(token,stack)
                #self._repeat_ops(token, val_stack, op_stack)
                #op_stack.push(token)

        return stack.pop()




    def infix_string(self):
        """Return the infix expression string of an expression tree"""
        post_str = self.postfix_string()
        post_list = post_str.split()

        if self.is_empty():
            return None

        stack = Stack()

        for token in post_list:
            if not token in "+-/*": #부호!!!!!!!
                stack.push(token)
            else:
                y = stack.pop()
                x = stack.pop()
                oper = "( "+x+" "+token+" "+y+" )"
                stack.push(oper)

        #마지막에 val_stack에서 하나를 빼서 리턴하면 그 내용이 전체 수식에 대한 ExpressionTree가 된다.
        return stack.pop()


    def prefix_string(self):
        """Return the prefix expression string of an expression tree"""
        pre_list = []
        if self.is_empty():
            return None

        for token in self.preorder():
            pre_list.append(token.element())

        return ' '.join(pre_list)




    def postfix_string(self):
        """Return the postfix expression string of an expression tree"""
        post_list = []
        if self.is_empty():
            return None

        for token in self.postorder():
            post_list.append(token.element())

        return ' '.join(post_list)






def tokenize(raw):
    """Produces list of tokens indicated by a raw expression string."""
    symbols = '+-*/() '
    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in symbols:
            if mark != j:
                tokens.append(raw[mark:j])
            if raw[j] != ' ':
                tokens.append(raw[j])
            mark = j + 1
    if mark != n:
        tokens.append(raw[mark:n])
    return tokens


def _prec(op):
    if op == "*" or op == "/":
        return 2
    elif op == "+" or op == "-":
        return 1
    else:  # operator is $
        return 0

def convert_infix2postfix(i_exp):
    p_exp = []
    stack = Stack()

    for token in i_exp:
        if token == '(':
            stack.push(token)
        elif token == ')':
            while stack.top() != '(':
                p_exp.append(stack.pop())
            stack.pop()
        elif token in "+-*/":
            while not stack.is_empty() and _prec(stack.top()) >= _prec(token):
                p_exp.append(stack.pop())
            stack.push(token)
        else:
            p_exp.append(token)

    while not stack.is_empty():
        temp = stack.pop()
        p_exp.append(temp)

    return p_exp


def build_expression_tree(tokens):
    """Returns an ExpressionTree based upon by a tokenized expression."""
    post_exp = convert_infix2postfix(tokens)
    stack = Stack()

    for i in post_exp:
        if not i in "+-/*":
            temp = ExpressionTree(i, None, None)
            stack.push(temp)
        else:
            tree = ExpressionTree(i, None, None)
            y = stack.pop() #right sub tree
            x = stack.pop() #left sub tree
            tree._attach(tree.root(), x, y) #attach
            stack.push(tree)

    return stack.pop()




if __name__ == '__main__':
    exp = '( ( ( ( 3 + 1 ) * 3 ) / ( ( 9 - 5 ) + 2 ) ) - ( ( 3 * ( 7 - 4 ) ) + 6.3 ) )'
    tokens = tokenize(exp)
    print(tokens)
    big = build_expression_tree(tokens)
    print(big)
    print(big.postfix_string())
    print(big.infix_string(), '=', big.evaluate())

    exp = '5 - 6 / 2 + 4 * 3'
    tokens = tokenize(exp)
    print(tokens)
    big = build_expression_tree(tokens)
    print(big)
    print(big.prefix_string())
    print(big.infix_string(), '=', big.evaluate())



# ['(', '(', '(', '(', '3', '+', '1', ')', '*', '3', ')', '/', '(', '(', '9', '-', '5', ')', '+', '2', ')', ')', '-', '(', '(', '3', '*', '(', '7', '-', '4', ')', ')', '+', '6.3', ')', ')']
# [- [/ [* [+ [3] [1]] [3]] [+ [- [9] [5]] [2]]] [+ [* [3] [- [7] [4]]] [6.3]]]
# 3 1 + 3 * 9 5 - 2 + / 3 7 4 - * 6.3 + -
# ( ( ( ( 3 + 1 ) * 3 ) / ( ( 9 - 5 ) + 2 ) ) - ( ( 3 * ( 7 - 4 ) ) + 6.3 ) ) = -13.3
# ['5', '-', '6', '/', '2', '+', '4', '*', '3']
# [+ [- [5] [/ [6] [2]]] [* [4] [3]]]
# + - 5 / 6 2 * 4 3
# ( ( 5 - ( 6 / 2 ) ) + ( 4 * 3 ) ) = 14.0

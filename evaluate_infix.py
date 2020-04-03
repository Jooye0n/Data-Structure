"""
Evaluating infix arithmetic/logical expression.
Expressions are well spaced strings without any parenthesis
Operators: + - * /
Operands: int
"""

from Stack import Stack

val_stack = Stack()
op_stack = Stack()

def _prec(op):
    if op == "*" or op == "/":
        return 2
    elif op == "+" or op == "-":
        return 1
    else:  # operator is $
        return 0


def _do_op():
    """Apply operator from opStack to two operands from valStack"""
    x = val_stack.pop()
    y = val_stack.pop()
    op = op_stack.pop()

    if op == '*':
        val_stack.push(y * x)
    elif op == '+':
        val_stack.push(y + x)
    elif op == '-':
        val_stack.push(y - x)
    elif op == '/':
        val_stack.push(y / x)
    else:
        raise ValueError(f"Unknown operators: {op}")

    #print("\tOp: " + op)
    #print("\t--valStk: {0}".format(val_stack))
    #print("\t--opStk:  {0}".format(op_stack))


def _repeat_ops(ref_op):
    """Apply the operator on top of opStack while its precedence is
    higher or equal to the reference operator"""
    while len(val_stack) > 1 and (_prec(ref_op) <= _prec(op_stack.top())):
        _do_op()


def evaluate_expression(i_exp="1 + 1"):
    """ Evaluating infix expression expr,
    assuming that each token is separated by white space properly."""
    token_list = i_exp.split()
    #print(f"Token list of input expression: {token_list}")

    for token in token_list:
        #print(f"\nToken:  {token}")
        if token not in "+-*/":
            val_stack.push(int(token))
        else:
            _repeat_ops(token)
            op_stack.push(token)

        #print(f"--valStk: {val_stack}")
        #print(f"--opStk:  {op_stack}")

    _repeat_ops("$")
    #print(f"\nToken: $")
    #print(f"--valStk: {val_stack}")
    #print(f"--opStk:  {op_stack}")

    return val_stack.top()


def convert_infix2postfix(i_exp):

    opStack = Stack()
    postfixList = []
    tokenList = i_exp.split()

    for token in tokenList:
        if token.isdigit():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and _prec(opStack.top()) >= _prec(token):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


if __name__ == "__main__":
    #EXP = "14 - 3 * 2 + 7"
    #print(f"Evaluation of \'{EXP}\' is {evaluate_expression(EXP)}")

    postfixList1 = "1 * 2 + 3 * 4"
    print(f"Evaluation of \'{postfixList1}\' is {evaluate_expression(postfixList1)}")
    print(f"Postfix of \'{postfixList1}\' is {convert_infix2postfix(postfixList1)}")

    postfixList2 = "24 * 3 * 2"
    print (convert_infix2postfix(postfixList2))

    postfixList3 = "( 14 + 2 ) * ( 3 - 2 )"
    print (convert_infix2postfix(postfixList3))


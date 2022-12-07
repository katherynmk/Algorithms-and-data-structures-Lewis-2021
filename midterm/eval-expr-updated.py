from stack_list import Stack, Empty

ops = '+-*/'
test_exp = '3 + 2 * 4 / 4 * 2 + 1 - 2'
tokens = test_exp.split()

val_stack = Stack()
op_stack = Stack()

def higher_priority(op1: str, op2: str):
    if op1 in '*/' and op2 in '+-':
        return True

    if op1 in '+-' and op2 in '+-':
        return True

    if op1 in '*/' and op2 in '*/':
        return True

    return False


for token in tokens:
    if token.isalnum():
        val_stack.push(token)
    elif token in ops:
        # keep_evaluating will stay true if an operation exists in the stack
        # that is higher priority than the current token
        keep_evaluating = True
        while keep_evaluating:
            # compare priorities with top ops
            try:
                top_ops = op_stack.top()
            except Empty:
                # the ops stack is empty, push our current op it to ops_stack and continue for
                # next token
                keep_evaluating = False
                continue

            if higher_priority(top_ops, token):
                # need to evalute
                result = eval('{val1} {op} {val2}'.format(val2=val_stack.pop(),
                                                          val1 = val_stack.pop(),
                                                          op = op_stack.pop()))
                val_stack.push(result)
            else:
                keep_evaluating = False

        op_stack.push(token)

while not op_stack.is_empty():
    result = eval('{val1} {op} {val2}'.format(val2=val_stack.pop(),
                                              val1 = val_stack.pop(),
                                              op = op_stack.pop()))
    val_stack.push(result)

print('result = {}'.format(val_stack.pop()))
print('done')


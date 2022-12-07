ops = '+-'
test_exp = ''
tokens = test_exp.split()

val_stack = []
op_stack = []


for token in tokens:
    if token.isalnum():
        val_stack.append(token)
    elif token in ops:

        keep_evaluating = True
        while keep_evaluating:
            try:
                top_ops = op_stack.top()
            except:

                keep_evaluating = False

                continue

while not op_stack == []:
    result = eval('{val1} {op} {val2}'.format(val2=val_stack.pop(),
                                              val1 = val_stack.pop(),
                                              op = op_stack.pop()))
    val_stack.append(result)

print('result = {}'.format(val_stack.pop()))
print('done')
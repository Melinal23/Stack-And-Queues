def postfix_to_infix(string):
    vals = string.split()
    stack = []


    for val in vals:

        if val.isdigit():
            stack.append(val)
        elif val in "/*+-^":
            op1 = stack.pop()
            op2 = stack.pop()
            new_str = "(" + str(op2) +" " + val + " " + str(op1) + ")"
            stack.append(new_str)

    return stack.pop()


print(postfix_to_infix("3 4 2 * 1 5 - 2 3 ^ ^ / +"))
# 3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3
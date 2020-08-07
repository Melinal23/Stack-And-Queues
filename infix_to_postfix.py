def infix_to_postfix(infix_str):

    vals = infix_str.split()

    output = []
    stack  = []

    dict = {}

    dict["^"] = 4
    dict["/"] = 3
    dict["*"] = 3
    dict["+"] = 2
    dict["-"] = 2
    dict["("] = 1

    for val in vals:
        if val == "(":
            stack.append(val)

        elif val == ")":
            curr = stack.pop()

            while (curr != "("):
                output.append(curr)
                curr = stack.pop()

        elif val.isdigit() or "." in val:  # Count ints (pos), floats
            output.append(val)

        elif val in "^/*+-":
            while len(stack) > 0 and ((val != "^" and dict[val] <= dict[stack[-1]]) or
                                      (val == "^" and dict[val] < dict[stack[-1]])):
                output.append(stack.pop())

            stack.append(val)

    while len(stack) > 0:
        output.append(stack.pop())

    return ''.join(output)


print(infix_to_postfix("1 ^ 7 ^ 6 * 8 - 2"))
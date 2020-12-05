def valid_parenthesis(sequence):

    pairs = {'}' : '{', ']' : '[', ')' : '('}
    stack = []

    for item in sequence:
        if item in "{([":
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            elif stack and stack.pop() != pairs[item]:
                return False

    if len(stack) != 0:
        return False

    return True

print(valid_parenthesis("{{}}()[()]")) #True
print(valid_parenthesis("{][}")) #False
print(valid_parenthesis("()(")) #False
print(valid_parenthesis("()")) #True
print(valid_parenthesis("()[]{}")) #True
print(valid_parenthesis("(]")) #False
print(valid_parenthesis("([)]")) #False
print(valid_parenthesis("{[]}")) #True
def validate(pushed, popped):

    stack = []
    i = 0

    for num in pushed:
        stack.append(num)
        if popped[i] == stack[-1]:
            stack.pop()
            popped.pop(0)

    if stack[::-1] == popped:
        return True
    else:
        return False



print(validate([1, 2, 3, 4, 5],[4, 3, 5, 1, 2]))

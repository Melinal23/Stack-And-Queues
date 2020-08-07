def reverseFirstKElements(q,k):
    stack = []

    rest_of_queue = q.qsize() - k

    if q.empty():
        return q

    while k > 0:
        val = q.get_nowait()
        stack.append(val)
        k -= 1

    while len(stack) > 0:
        q.put_nowait(stack.pop())

    while rest_of_queue > 0:
        q.put_nowait(q.get_nowait())
        rest_of_queue -= 1
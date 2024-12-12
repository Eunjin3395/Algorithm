def solution(s):
    stack = []
    for elem in s:
        if elem == "(":
            stack.append(0)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False

    return True
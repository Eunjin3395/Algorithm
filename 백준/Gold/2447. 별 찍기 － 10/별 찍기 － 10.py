
def recursion(n):
    # base case
    if(n == 1):
        return ["*"]

    stars = recursion(n//3)
    result = []

    for star in stars:
        result.append(star*3)

    for star in stars:
        result.append(star+' '*(n//3)+star)

    for star in stars:
        result.append(star*3)

    return result


n = int(input())

print('\n'.join(recursion(n)))

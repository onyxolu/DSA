def countStudents(height):
    target = sorted(height)
    count, n = 0, len(target)
    for i in range(n):
        if height[i] != target[i]:
            count += 1
    return count
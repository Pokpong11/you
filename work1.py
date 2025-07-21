a = {10, 20, 30, 40, 50, 60}
b = {30, 40, 50, 60, 70, 80}

# 1. Union
print(a.union(b))  # {10, 20, 30, 40, 50, 60, 70, 80}

# 2. Intersection
print(a.intersection(b))  # {30, 40, 50, 60}

# 3. Difference (a - b)
print(a.difference(b))  # {10, 20}

# 4. Symmetric Difference
print(a.symmetric_difference(b))  # {10, 20, 70, 80}
print(sorted(a.union(b)))

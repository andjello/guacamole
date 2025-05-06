# Define fuzzy sets
A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.8}
B = {'x1': 0.6, 'x2': 0.4, 'x3': 0.3}

# Union: max(A(x), B(x))
def union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

# Intersection: min(A(x), B(x))
def intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) & set(B)}

# Complement: 1 - A(x)
def complement(A):
    return {x: 1 - val for x, val in A.items()}

# Difference: min(A(x), 1 - B(x))
def difference(A, B):
    return {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in A}

# Cartesian Product (fuzzy relation)
def cartesian_product(A, B):
    return {(a, b): min(A[a], B[b]) for a in A for b in B}

# Max-Min Composition of two fuzzy relations
def max_min_composition(R1, R2):
    result = {}
    X = {a for (a, _) in R1}
    Z = {c for (_, c) in R2}
    for a in X:
        for c in Z:
            min_vals = []
            for b in {b for (_, b) in R1} & {b for (b, _) in R2}:
                min_vals.append(min(R1.get((a, b), 0), R2.get((b, c), 0)))
            if min_vals:
                result[(a, c)] = max(min_vals)
    return result

# Display results
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("Union:", union(A, B))
print("Intersection:", intersection(A, B))
print("Complement of A:", complement(A))
print("Difference A - B:", difference(A, B))

# Fuzzy Relations from Cartesian Product
R1 = cartesian_product(A, B)
R2 = cartesian_product(B, A)
print("Fuzzy Relation R1 (A x B):", R1)
print("Fuzzy Relation R2 (B x A):", R2)

# Max-Min Composition
composition = max_min_composition(R1, R2)
print("Max-Min Composition (R1 o R2):", composition)

# Strassen recursion trace for demonstration
# This code prints the full recursive trace from 1x1 scalar multiplications up to the full matrix.
# It assumes square matrices with size a power of two.

from copy import deepcopy
import pprint

pp = pprint.PrettyPrinter(width=80, compact=False)


def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def split(A):
    n = len(A) // 2
    A11 = [[A[i][j] for j in range(n)] for i in range(n)]
    A12 = [[A[i][j + n] for j in range(n)] for i in range(n)]
    A21 = [[A[i + n][j] for j in range(n)] for i in range(n)]
    A22 = [[A[i + n][j + n] for j in range(n)] for i in range(n)]
    return A11, A12, A21, A22


def join(C11, C12, C21, C22):
    n = len(C11)
    N = 2 * n
    C = [[0] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            C[i][j] = C11[i][j]
            C[i][j + n] = C12[i][j]
            C[i + n][j] = C21[i][j]
            C[i + n][j + n] = C22[i][j]
    return C


def is_scalar_mat(A):
    return len(A) == 1


def pretty_mat(A):
    return "[" + "; ".join(" ".join(f"{v:>4}" for v in row) for row in A) + "]"


def strassen_trace(A, B, name="C", depth=0):
    indent = "  " * depth
    n = len(A)
    print(f"{indent}Strassen call {name}: size {n}x{n}")
    if is_scalar_mat(A):
        a = A[0][0];
        b = B[0][0]
        print(f"{indent}  Base multiply: {a} * {b} = {a * b}")
        return [[a * b]]

    # show input matrices at this node
    print(f"{indent}  A = {pretty_mat(A)}")
    print(f"{indent}  B = {pretty_mat(B)}")

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    # compute operands for M1..M7 and show them
    S1 = add(A11, A22);
    S2 = add(B11, B22)
    print(f"{indent}  M1 operands: (A11 + A22) and (B11 + B22)")
    print(f"{indent}    (A11+A22) = {pretty_mat(S1)}")
    print(f"{indent}    (B11+B22) = {pretty_mat(S2)}")
    M1 = strassen_trace(S1, S2, name=f"{name}.M1", depth=depth + 1)
    print(f"{indent}  M1 = {pretty_mat(M1)}\n")

    S3 = add(A21, A22)
    print(f"{indent}  M2 operands: (A21 + A22) and B11")
    print(f"{indent}    (A21+A22) = {pretty_mat(S3)}")
    M2 = strassen_trace(S3, B11, name=f"{name}.M2", depth=depth + 1)
    print(f"{indent}  M2 = {pretty_mat(M2)}\n")

    S4 = sub(B12, B22)
    print(f"{indent}  M3 operands: A11 and (B12 - B22)")
    print(f"{indent}    (B12-B22) = {pretty_mat(S4)}")
    M3 = strassen_trace(A11, S4, name=f"{name}.M3", depth=depth + 1)
    print(f"{indent}  M3 = {pretty_mat(M3)}\n")

    S5 = sub(B21, B11)
    print(f"{indent}  M4 operands: A22 and (B21 - B11)")
    print(f"{indent}    (B21-B11) = {pretty_mat(S5)}")
    M4 = strassen_trace(A22, S5, name=f"{name}.M4", depth=depth + 1)
    print(f"{indent}  M4 = {pretty_mat(M4)}\n")

    S6 = add(A11, A12)
    print(f"{indent}  M5 operands: (A11 + A12) and B22")
    print(f"{indent}    (A11+A12) = {pretty_mat(S6)}")
    M5 = strassen_trace(S6, B22, name=f"{name}.M5", depth=depth + 1)
    print(f"{indent}  M5 = {pretty_mat(M5)}\n")

    S7 = sub(A21, A11)
    S8 = add(B11, B12)
    print(f"{indent}  M6 operands: (A21 - A11) and (B11 + B12)")
    print(f"{indent}    (A21-A11) = {pretty_mat(S7)}")
    print(f"{indent}    (B11+B12) = {pretty_mat(S8)}")
    M6 = strassen_trace(S7, S8, name=f"{name}.M6", depth=depth + 1)
    print(f"{indent}  M6 = {pretty_mat(M6)}\n")

    S9 = sub(A12, A22)
    S10 = add(B21, B22)
    print(f"{indent}  M7 operands: (A12 - A22) and (B21 + B22)")
    print(f"{indent}    (A12-A22) = {pretty_mat(S9)}")
    print(f"{indent}    (B21+B22) = {pretty_mat(S10)}")
    M7 = strassen_trace(S9, S10, name=f"{name}.M7", depth=depth + 1)
    print(f"{indent}  M7 = {pretty_mat(M7)}\n")

    # recombine
    print(f"{indent}  Recombining to form {name}:")
    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    print(f"{indent}    C11 = {pretty_mat(C11)}")
    print(f"{indent}    C12 = {pretty_mat(C12)}")
    print(f"{indent}    C21 = {pretty_mat(C21)}")
    print(f"{indent}    C22 = {pretty_mat(C22)}")

    C = join(C11, C12, C21, C22)
    print(f"{indent}  {name} = {pretty_mat(C)}\n")
    return C


# Given matrices from the conversation
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7]
]
B = [
    [8, 9, 1, 2],
    [3, 4, 5, 6],
    [7, 8, 9, 1],
    [2, 3, 4, 5]
]

print("==== Strassen recursion trace for the provided 4x4 matrices ====\n")
C = strassen_trace(A, B, name="C")
print("==== Final result C ====")
pp.pprint(C)


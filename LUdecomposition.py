def LU_decomposition(matrix):
    rhs = []
    U = []
    for row in matrix:
        U.append(row.copy())
    L = []
    for i in range(len(matrix)):  # initialize L
        L.append([])
        for j in range(len(matrix[0]) - 1):
            if i == j:
                L[i].append(1)
            else:
                L[i].append(0)
    to_be_swapped = []
    column_indices=[]
    for i in range(len(U) - 1):
        swapped = False
        pivot = U[i][i]
        pivot_index = i
        for r in range(i + 1, len(U)):
            if abs(U[r][i]) > pivot:
                pivot = U[r][i]
                pivot_index = r
                swapped = True
        if swapped:
            for c in range(len(U[0])):
                U[i][c], U[pivot_index][c] = U[pivot_index][c], U[i][c]  # pivot swapping
            if i != 0:
                column_indices.append(i - 1)
                to_be_swapped.append([i, pivot_index])
        for k in range(i + 1, len(U)):
            multiplier = U[k][i] / U[i][i]
            L[k][i] = multiplier
            for j in range(len(U[0]) - 1):
                U[k][j] = U[k][j] - multiplier * U[i][j]
    for i in range(len(to_be_swapped)):
        row_index = to_be_swapped[i][0]
        p_index = to_be_swapped[i][1]
        print(row_index, row_index)  # fixing L
        print(p_index, row_index)
        L[row_index][column_indices[i]], L[p_index][column_indices[i]] = L[p_index][column_indices[i]], L[row_index][column_indices[i]]
    for i in range(len(U)):  # initialize rhs of equation
        rhs.append(U[i].pop())
    d = [0] * len(rhs)
    for i in range(len(L)):  # forward substitution
        d[i] = rhs[i]
        for j in range(len(L[0])):
            if i != j:
                d[i] -= d[j] * L[i][j]
    results = [0] * len(d)
    for i in range(len(U) - 1, -1, -1):  # backward substitution
        results[i] = d[i]
        for j in range(0, len(U[0])):
            if i != j:
                results[i] -= results[j] * U[i][j]
        results[i] = results[i] / U[i][i]
    print('U:')
    for row in U:
        print(row)
    print('\n')
    print('L:')
    for row in L:
        print(row)
    print('\n')
    for i in range(len(d)):
        print(f'd{i + 1}={d[i]}')
    print('\n')
    for i in range(len(results)):
        print(f'x{i + 1}={results[i]}')


matrix = [[2, -6, -1, -38], [-3, -1, 7, -34], [-8, 1, -2, -20]]
LU_decomposition(matrix)

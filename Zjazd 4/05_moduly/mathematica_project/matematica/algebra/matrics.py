
def add_matrices(x, y):
    out = []
    for i, row in enumerate(a):
        n_row = []
        for j, col in enumerate(row):
            n_row.append(col + b[i][j])
        out.append(n_row)

    return out
def sub_matrices():
    out = []
    for i, row in enumerate(a):
        n_row = []
        for j, col in enumerate(row):
            n_row.append(col - b[i][j])
        out.append(n_row)

    return out
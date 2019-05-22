A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = 3  # Numero de filas
m = 3  # Numero de columnas

# Recorrido de una matriz
# De izquierda a derecha
# De arriba hacia abajo
for i in range(n):
    for j in range(n):
        print (A[i][j],
    print
print

# Recorrido de una matriz
# De derecha a izquierda
# De arriba hacia abajo
for i in xrange(n):
    for j in xrange(m):
        print
        A[i][m - j - 1],
    print
print

# Recorrido de una matriz
# De izquierda a derecha
# De abajo hacia arriba
for i in xrange(n):
    for j in xrange(m):
        print
        A[n - i - 1][j],
    print
print

# Recorrido de una matriz
# De derecha a izquierda
# De abajo hacia arriba
for i in xrange(n):
    for j in xrange(m):
        print
        A[n - i - 1][m - j - 1],
    print
print
class Matrix:
    """
    Clase con métodos para operaciones sobre matrices.
    """

    def suma_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las dimensiones de las matrices deben ser iguales.")
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def resta_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las dimensiones de las matrices deben ser iguales.")
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def multiplicar_matrices(self, A, B):
        m, n, p = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise ValueError("Columnas de A deben coincidir con filas de B.")
        
        resultado = [[0 for _ in range(p)] for _ in range(m)]
        for i in range(m):
            for j in range(p):
                resultado[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
        return resultado

    def multiplicar_escalar(self, matriz, escalar):
        return [[elemento * escalar for elemento in fila] for fila in matriz]

    def transpuesta(self, matriz):
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

    def es_cuadrada(self, matriz):
        return len(matriz) == len(matriz[0]) if matriz else False

    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        return matriz == self.transpuesta(matriz)

    def traza(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada.")
        return sum(matriz[i][i] for i in range(len(matriz)))

    def determinante_2x2(self, matriz):

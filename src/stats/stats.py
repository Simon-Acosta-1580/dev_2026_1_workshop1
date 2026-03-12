import math

class Stats:
    def promedio(self, numeros):
        if not numeros: return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        if not numeros: return 0
        datos = sorted(numeros)
        n = len(datos)
        mitad = n // 2
        
        if n % 2 == 0:
            return (datos[mitad - 1] + datos[mitad]) / 2
        else:
            return float(datos[mitad])
    
    def moda(self, numeros):
        if not numeros: return None
        frecuencias = {}
        for n in numeros:
            frecuencias[n] = frecuencias.get(n, 0) + 1
        
        max_frecuencia = max(frecuencias.values())
        
        for n in numeros:
            if frecuencias[n] == max_frecuencia:
                return n
    
    def varianza(self, numeros):
        if not numeros: return 0
        mu = self.promedio(numeros)
        suma_cuadrados = sum((x - mu) ** 2 for x in numeros)
        return suma_cuadrados / len(numeros)
    
    def desviacion_estandar(self, numeros):
        if not numeros: return 0
        return math.sqrt(self.varianza(numeros))
    
    def rango(self, numeros):
        if not numeros: return 0
        return max(numeros) - min(numeros)

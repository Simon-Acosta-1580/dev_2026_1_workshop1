import re
class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        procesado = "".join(texto.lower().split())
        return procesado == self.invertir_cadena(procesado)
    
    def invertir_cadena(self, texto):
        invertida = ""
        for caracter in texto:
            invertida = caracter + invertida
        return invertida
    
    def contar_vocales(self, texto):
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        contador = 0
        for caracter in texto:
            if caracter in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        consonantes = "bcdfghjklmnpqrstvwxyz"
        return sum(1 for letra in texto.lower() if letra in consonantes)
    
    def es_anagrama(self, texto1, texto2):
        t1 = sorted("".join(texto1.lower().split()))
        t2 = sorted("".join(texto2.lower().split()))
        return t1 == t2
    
    def contar_palabras(self, texto):
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        return re.sub(r'\w+', lambda m: m.group(0).capitalize(), texto)
    
    def eliminar_espacios_duplicados(self, texto):
        return " ".join(texto.split())
    
    def es_numero_entero(self, texto):
        if not texto:
            return False
        
        inicio = 0
        if texto[0] in ('-', '+'):
            if len(texto) == 1: return False
            inicio = 1
            
        numeros = "0123456789"
        for i in range(inicio, len(texto)):
            if texto[i] not in numeros:
                return False
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                # Determinamos si es mayúscula o minúscula para mantener el caso
                base = ord('A') if char.isupper() else ord('a')
                # Fórmula César: (x + n) % 26
                nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
                resultado += nuevo_char
            else:
                resultado += char
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        n, m = len(texto), len(subcadena)
        if m == 0: return posiciones

        for i in range(n - m + 1):
            coincide = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    coincide = False
                    break
            if coincide:
                posiciones.append(i)
        return posiciones

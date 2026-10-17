class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None


def aplicar_operador(operador, a, b):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
    elif operador == '^':
        return a ** b
    else:
        raise ValueError(f"Operador no válido: {operador}")


def evaluar_posfija(expresion):
    """Evalúa una expresión en notación posfija de izquierda a derecha."""
    pila = Pila()
    tokens = expresion.split()

    for token in tokens:
        if token.lstrip('-').isdigit():  # Si es un número (positivo o negativo)
            pila.apilar(float(token))
        else:  # Si es un operador
            b = pila.desapilar()
            a = pila.desapilar()
            resultado = aplicar_operador(token, a, b)
            pila.apilar(resultado)

    return pila.desapilar()


def evaluar_prefija(expresion):
    """Evalúa una expresión en notación prefija de derecha a izquierda."""
    pila = Pila()
    tokens = expresion.split()[::-1]  # Invertimos para leer de derecha a izquierda

    for token in tokens:
        if token.lstrip('-').isdigit():
            pila.apilar(float(token))
        else:
            a = pila.desapilar()
            b = pila.desapilar()
            resultado = aplicar_operador(token, a, b)
            pila.apilar(resultado)

    return pila.desapilar()


if __name__ == "__main__":
    print("=== EVALUADOR DE EXPRESIONES CON PILA ===")
    
    # Ejemplo: (5 + 3) * 2 - 4 = 12
    exp_posfija = "5 3 + 2 * 4 -"
    print(f"\nExpresión Posfija: {exp_posfija}")
    print(f"Resultado Posfija: {evaluar_posfija(exp_posfija)}")

    # El mismo ejemplo en Prefija: - * + 5 3 2 4 = 12
    exp_prefija = "- * + 5 3 2 4"
    print(f"\nExpresión Prefija: {exp_prefija}")
    print(f"Resultado Prefija: {evaluar_prefija(exp_prefija)}")

    # Prueba interactiva opcional
    print("\n--- Prueba personalizada ---")
    entrada = input("Ingresa una expresión posfija (separada por espacios, ej. '10 5 + 2 *'): ")
    if entrada.strip():
        print(f"Resultado: {evaluar_posfija(entrada)}")
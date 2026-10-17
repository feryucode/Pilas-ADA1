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

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def obtener_elementos(self):
        return self.items


class NavegadorWeb:
    def __init__(self):
        self.historial = Pila()

    def visitar_sitio(self, url):
        self.historial.apilar(url)
        print(f"[Navegando] Has ingresado a: {url}")

    def regresar(self):
        if self.historial.esta_vacia():
            print("[Aviso] El historial está vacío.")
            return

        sitio_saliente = self.historial.desapilar()
        sitio_actual = self.historial.ver_tope()

        if sitio_actual:
            print(f"[Atrás] Saliste de '{sitio_saliente}'. Ahora estás en: {sitio_actual}")
        else:
            print(f"[Atrás] Saliste de '{sitio_saliente}'. Ya no hay más páginas anteriores.")

    def mostrar_historial(self):
        if self.historial.esta_vacia():
            print("\nEl historial de navegación está vacío.")
        else:
            print("\n--- Historial de sitios (del más reciente al más antiguo) ---")
            for i, sitio in enumerate(reversed(self.historial.obtener_elementos()), 1):
                marcador = " <-- (Sitio actual)" if i == 1 else ""
                print(f"{i}. {sitio}{marcador}")


if __name__ == "__main__":
    navegador = NavegadorWeb()

    while True:
        print("\n=== NAVEGADOR WEB (CON PILA) ===")
        print("1. Visitar nueva página")
        print("2. Regresar a la página anterior (Atrás)")
        print("3. Ver historial completo")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            url = input("Ingresa la URL del sitio (ej. google.com): ")
            navegador.visitar_sitio(url)
        elif opcion == "2":
            navegador.regresar()
        elif opcion == "3":
            navegador.mostrar_historial()
        elif opcion == "4":
            print("Cerrando el navegador...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
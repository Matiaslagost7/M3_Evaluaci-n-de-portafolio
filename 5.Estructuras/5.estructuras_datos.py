def catalogo_productos_simple():
    print("--- Catálogo de Productos ---")
    productos = []  # Lista para almacenar diccionarios de productos

    while True:
        print("\n1. Añadir producto")
        print("2. Ver catálogo")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            precio_str = input("Ingrese el precio del producto: ")
            precio = float(precio_str)  # Conversión directa (sin try/except)
            producto = {'nombre': nombre, 'precio': precio}  # Crear diccionario
            productos.append(producto)  # Añadir a la lista
            print(f"Producto '{nombre}' añadido.")
        elif opcion == '2':
            if not productos:
                print("El catálogo está vacío.")
            else:
                print("Catálogo actual:")
                for prod in productos:  # Iterar sobre la lista de diccionarios
                    print(f"- {prod['nombre']}: ${prod['precio']:.2f}")  # Acceder a valores por clave
        elif opcion == '3':
            print("Saliendo del catálogo. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    catalogo_productos_simple()

def registro_usuario_simple():
    print("--- Registro de Usuario ---")

    nombre = input("Ingrese su nombre: ") # Cadena
    apellido = input("Ingrese su apellido: ") # Cadena

    edad_str = input("Ingrese su edad: ")
    edad = int(edad_str) # Entero (asume entrada válida)

    altura_str = input("Ingrese su altura en metros (ej. 1.75): ")
    altura = float(altura_str) # Flotante (asume entrada válida)

    correo = input("Ingrese su correo electrónico: ") # Cadena

    acepta_terminos_str = input("¿Acepta los términos y condiciones? (si/no): ").lower()
    acepta_terminos = (acepta_terminos_str == "si") # Booleano

    print("\n--- Resumen de Registro ---")
    print(f"Nombre Completo: {nombre} {apellido}")
    print(f"Edad: {edad} años")
    print(f"Altura: {altura} metros")
    print(f"Correo Electrónico: {correo}")
    print(f"Términos Aceptados: {acepta_terminos}")

if __name__ == "__main__":
    registro_usuario_simple()

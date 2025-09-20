def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def metros_a_pies(metros):
    return metros * 3.28084

def pies_a_metros(pies):
    return pies / 3.28084

def conversor_unidades_con_funciones():
    print("--- Conversor de Unidades ---")

    while True:
        print("\n1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Metros a Pies")
        print("4. Pies a Metros")
        print("5. Salir")

        opcion = input("Seleccione una conversión: ")

        if opcion == '5':
            print("Saliendo del conversor. ¡Adiós!")
            break

        if opcion in ('1', '2', '3', '4'):
            valor_str = input("Ingrese el valor a convertir: ")
            valor = float(valor_str)  # Conversión directa (sin try/except)

            if opcion == '1':
                resultado = celsius_a_fahrenheit(valor)
                print(f"{valor:.1f} Celsius son {resultado:.1f} Fahrenheit.")
            elif opcion == '2':
                resultado = fahrenheit_a_celsius(valor)
                print(f"{valor:.1f} Fahrenheit son {resultado:.1f} Celsius.")
            elif opcion == '3':
                resultado = metros_a_pies(valor)
                print(f"{valor:.2f} Metros son {resultado:.2f} Pies.")
            elif opcion == '4':
                resultado = pies_a_metros(valor)
                print(f"{valor:.2f} Pies son {resultado:.2f} Metros.")
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    conversor_unidades_con_funciones()

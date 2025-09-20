def adivina_el_numero_simple():
    print("--- Adivina el Número ---")
    numero_secreto = 7 # El número fijo que el programa "piensa"
    adivinado = False

    print("Estoy pensando en un número entre 1 y 10. ¡Intenta adivinarlo!")

    while not adivinado:
        suposicion_str = input("Tu suposición: ")
        suposicion = int(suposicion_str) # Asume que el usuario ingresa un entero válido

        if suposicion < numero_secreto:
            print("Demasiado bajo.")
        elif suposicion > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Correcto! Adivinaste el número {numero_secreto}.")
            adivinado = True # Cambia la condición para salir del bucle

if __name__ == "__main__":
    adivina_el_numero_simple()

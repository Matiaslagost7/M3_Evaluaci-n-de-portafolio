def calificador_notas():
    print("--- Calificador de Notas ---")

    nota_str = input("Ingrese la calificación (0-100): ")
    nota = float(nota_str)

    if nota >= 90:
        print(f"Su calificación es {nota}. ¡Excelente!")
    elif nota >= 70:
        print(f"Su calificación es {nota}. Muy Bien.")
    elif nota >= 50:
        print(f"Su calificación es {nota}. Aprobado.")
    else:
        print(f"Su calificación es {nota}. Reprobado.")

if __name__ == "__main__":
    calificador_notas()

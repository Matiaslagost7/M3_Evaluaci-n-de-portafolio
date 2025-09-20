# conversor de monedas basico

def conversor_monedas_basico():
    print("--- Conversor de Monedas Básico ---")
    print("Monedas disponibles: USD (Dólar Americano), EUR (Euro), GBP (Libra Esterlina)")

    # Definición de tasas de cambio (variables)
    # Tasas de cambio respecto a 1 USD
    tasa_usd_eur = 0.92  # 1 USD = 0.92 EUR
    tasa_usd_gbp = 0.79  # 1 USD = 0.79 GBP

    # Tasas de cambio respecto a 1 EUR
    tasa_eur_usd = 1.08  # 1 EUR = 1.08 USD (aproximado)
    tasa_eur_gbp = 0.86  # 1 EUR = 0.86 GBP

    # Tasas de cambio respecto a 1 GBP
    tasa_gbp_usd = 1.26  # 1 GBP = 1.26 USD
    tasa_gbp_eur = 1.16  # 1 GBP = 1.16 EUR

    # Solicitar entrada del usuario (sentencias básicas, tipos de datos)
    # Se asume que el usuario ingresará un número válido.
    cantidad_str = input("\nIngrese la cantidad a convertir: ")
    cantidad = float(cantidad_str) # Convertir la cadena a número flotante

    moneda_origen = input("Ingrese la moneda de origen (USD, EUR, GBP): ").upper() # Convertir a mayúsculas
    moneda_destino = input("Ingrese la moneda de destino (USD, EUR, GBP): ").upper() # Convertir a mayúsculas

    resultado = 0.0 # Inicializar variable para el resultado
    mensaje_error = "" # Variable para almacenar mensajes de error

    # Lógica de conversión (sentencias condicionales if/elif/else)
    if moneda_origen == "USD":
        if moneda_destino == "EUR":
            resultado = cantidad * tasa_usd_eur
        elif moneda_destino == "GBP":
            resultado = cantidad * tasa_usd_gbp
        elif moneda_destino == "USD":
            resultado = cantidad # No hay conversión si origen y destino son iguales
        else:
            mensaje_error = "Moneda de destino no reconocida para USD."
    elif moneda_origen == "EUR":
        if moneda_destino == "USD":
            resultado = cantidad * tasa_eur_usd
        elif moneda_destino == "GBP":
            resultado = cantidad * tasa_eur_gbp
        elif moneda_destino == "EUR":
            resultado = cantidad
        else:
            mensaje_error = "Moneda de destino no reconocida para EUR."
    elif moneda_origen == "GBP":
        if moneda_destino == "USD":
            resultado = cantidad * tasa_gbp_usd
        elif moneda_destino == "EUR":
            resultado = cantidad * tasa_gbp_eur
        elif moneda_destino == "GBP":
            resultado = cantidad
        else:
            mensaje_error = "Moneda de destino no reconocida para GBP."
    else:
        mensaje_error = "Moneda de origen no reconocida. Por favor, use USD, EUR o GBP."

    # Mostrar resultado o mensaje de error
    if mensaje_error: # Si hay un mensaje de error, significa que la conversión no fue exitosa
        print(f"\nError: {mensaje_error}")
    else:
        print(f"\n{cantidad:.2f} {moneda_origen} equivale a {resultado:.2f} {moneda_destino}")

# Ejecutar el conversor
if __name__ == "__main__":
    conversor_monedas_basico()

# Conversor de Temperatura Celsius a Fahrenheit
#  Este programa solicita el nombre del usuario y una temperatura en grados Celsius,
# la convierte a grados Fahrenheit usando la fórmula (C * 9/5) + 32, y verifica si la entrada es válida.
# Utiliza tipos de datos: string (nombre), float (temperaturas), boolean (validación).
# Convención: snake_case para identificadores.

def convertir_celsius_a_fahrenheit(celsius):
    """
    Función que convierte una temperatura de Celsius a Fahrenheit.
    
    Parámetros:
    celsius (float): La temperatura en grados Celsius.
    
    Retorna:
    float: La temperatura convertida en grados Fahrenheit.
    """
    # Fórmula de conversión: (C * 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    # Solicitar el nombre del usuario (tipo string)
    nombre_usuario = input("Ingresa tu nombre: ")
    
    # Solicitar la temperatura en Celsius (tipo float)
    try:
        temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    except ValueError:
        print("Error: La temperatura debe ser un número válido.")
        return  # Salir si hay error
    
    # Verificar si la temperatura es razonable (tipo boolean, por ejemplo, no menor a -273.15)
    es_temperatura_valida = temperatura_celsius >= -273.15
    
    if es_temperatura_valida:
        # Convertir la temperatura usando la función
        temperatura_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_celsius)
        
        # Mostrar el resultado (tipo float formateado)
        print(f"Hola, {nombre_usuario}. {temperatura_celsius}°C equivalen a {temperatura_fahrenheit:.2f}°F.")
    else:
        print("Error: La temperatura no puede ser menor al cero absoluto (-273.15°C).")

# Ejecutar la función principal si el script se corre directamente
if __name__ == "__main__":
    main()
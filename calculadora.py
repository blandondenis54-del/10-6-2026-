def calculadora():
    print("=== CALCULADORA SIMPLE ===")
    print("Operaciones: + (suma), - (resta), * (multiplicación), / (división), ** (potencia)")
    print("Escribe 'salir' para terminar\n")
    
    while True:
        try:
            # Obtener entrada del usuario
            entrada = input("Ingresa una operación (ej: 5 + 3): ").strip()
            
            if entrada.lower() == 'salir':
                print("¡Hasta luego!")
                break
            
            # Evaluar la expresión
            resultado = eval(entrada)
            print(f"Resultado: {resultado}\n")
            
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero\n")
        except Exception as e:
            print(f"Error: Ingresa una operación válida. {e}\n")

if __name__ == "__main__":
    calculadora()
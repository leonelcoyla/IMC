import tkinter as tk

def clasificarIMC(imc): #Clasificación de Indice de Masa Corporal
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def calcularIMC():
    try:
        peso = float(entryPeso.get())
        altura = float(entryAltura.get())
        if altura <= 0:
            raise ValueError("La altura debe ser mayor que cero.")
        imc = peso / (altura ** 2)
        clasificacion = clasificarIMC(imc)
        rpta_label.config(text=f"Tu IMC es: {imc:.2f}\nClasificación: {clasificacion}")
        error_label.config(text="", fg="navy")  # Limpiar mensaje de error
    except ValueError as e:
        error_label.config(text=f"Error: Ingrese datos validos ", fg="navy")
        rpta_label.config(text="")  # Limpiar resultado en caso de error

# Crea ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("400x400")  # Tamaño de la ventana

# Título
titulo_label = tk.Label(ventana, text="ÍNDICE DE MASA CORPORAL", font=("Arial", 16), fg="navy")
titulo_label.pack(pady=10)

# Etiquetas y entradas
tk.Label(ventana, text="Peso (kg):").pack(pady=5)
entryPeso = tk.Entry(ventana)
entryPeso.pack(pady=5)

tk.Label(ventana, text="Altura (m):").pack(pady=5)
entryAltura = tk.Entry(ventana)
entryAltura.pack(pady=5)

# Botón para calcular IMC
btnCalcular = tk.Button(ventana, text="Calcular IMC", command=calcularIMC)
btnCalcular.pack(pady=10)

# Label para mostrar el resultado
rpta_label = tk.Label(ventana, text="", justify="center")
rpta_label.pack(pady=10)

# Label para mostrar mensajes de error
error_label = tk.Label(ventana, text="", justify="center")
error_label.pack(pady=10)

# Label para mostrar el autor con color gris claro
autor_label = tk.Label(ventana, text="Autor: Leonel Coyla Idme", font=("Arial", 10), fg="#D3D3D3")  # Gris claro
autor_label.pack(side=tk.BOTTOM, pady=5)


# Iniciar el bucle principal de la interfaz
ventana.mainloop()

from tkinter import *

# Tasas de conversión para cada moneda
tasas_conversion = {
  "Yenes": 0.0067,
    "Dólares": 1.0,
    "Pesos Mexicanos": 0.059,
    "Euros": 1.08,
    "Pesetas": 0.0065,
    "Libras": 1.26,
    "Dólar Canadiense": 0.74,
    "Rublo": 0.011,
    "Rupia": 0.012
}

root = Tk()
root.title("Conversor de Monedas")

opciones = ["Yenes", "Dólares", "Pesos Mexicanos", "Euros", "Pesetas", "Libras", "Dólar Canadiense", "Rublo", "Rupia"]

desde_moneda = StringVar()
desde_moneda.set(opciones[0])
hacia_moneda = StringVar()
hacia_moneda.set(opciones[1])

frame_cantidad = Frame(root)
frame_cantidad.pack()

label_cantidad = Label(frame_cantidad, text="Cantidad:", font=("Arial", 14))
label_cantidad.grid(row=0, column=0)

entrada_cantidad = Entry(frame_cantidad)
entrada_cantidad.grid(row=1, column=0, padx=10)

frame_moneda = Frame(root)
frame_moneda.pack()

label_desde = Label(frame_moneda, text="De:")
label_desde.grid(row=0, column=0)

label_hacia = Label(frame_moneda, text="A:")
label_hacia.grid(row=0, column=1)

for i, opcion in enumerate(opciones):
    Radiobutton(frame_moneda, text=opcion, variable=desde_moneda, value=opcion).grid(row=i+1, column=0)
    Radiobutton(frame_moneda, text=opcion, variable=hacia_moneda, value=opcion).grid(row=i+1, column=1)

label_resultado = Label(root, text="")
label_resultado.pack()

def convertir_moneda():
    desde_curr = desde_moneda.get()
    hacia_curr = hacia_moneda.get()
    cantidad = float(entrada_cantidad.get())
    resultado = cantidad * tasas_conversion[desde_curr] / tasas_conversion[hacia_curr]
    label_resultado.config(text=f"Resultado: {resultado} {hacia_curr}")

boton_convertir = Button(root, text="Convertir", command=convertir_moneda)
boton_convertir.pack()

root.mainloop()

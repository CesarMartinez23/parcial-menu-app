# Importamos los modulos necesarios.
from tabulate import tabulate
from tkinter import StringVar, Tk, Label, Button, Radiobutton
from PIL import ImageTk, Image

# Creamos la ventana.
root = Tk()

# Configuramos la ventana.
root.title("Menu App")
root.geometry("750x825")
root.resizable(0, 0)
root.configure(bg="#8B5656")

# Creamos listas para almacenar los datos de las ordenes de comida.
order = []
prices = []

# Creamos las variables para los radio buttons.
selectedCarnes = StringVar()
selectedCarnes.set(None)

selectedEnsaladas = StringVar()
selectedEnsaladas.set(None)

selectedBebidas = StringVar()
selectedBebidas.set(None)

# Creamos una funcion para limpiar las listas.
def clearList():
    order.clear()
    prices.clear()

# Creamos una funcion para llamar las imagenes.
def showImage(nameImage: str):
    image = ImageTk.PhotoImage(Image.open(f'./img/{nameImage}.jpg').resize((100, 100)))
    return image

# Creamos una funcion para obtener los datos seleccionados en el area de las carnes.
def getCarnes():
    if selectedCarnes.get() == "Carne":
        # print("Carne")
        order.append(["Carne Asada", "$2.50"])
        prices.append(2.50)
    elif selectedCarnes.get() == "Pollo":
        # print("Pollo Guisado")
        order.append(["Pollo Guisado", "$2.25"])
        prices.append(2.25)
    elif selectedCarnes.get() == "Lasaña":
        # print("Lasaña")
        order.append(["Lasaña", "$3.00"])
        prices.append(3.00)
    else:
        print("No se ha seleccionado ninguna carne")

# Creamos una funcion para obtener los datos seleccionados en el area de las ensaladas.
def getEnsaladas():
    if selectedEnsaladas.get() == "Fresca":
        # print("Ensalada Fresca")
        order.append(["Ensalada Fresca", "$0.25"])
        prices.append(0.25)
    elif selectedEnsaladas.get() == "Coditos":
        # print("Ensalada de Coditos")
        order.append(["Ensalada de Coditos", "$0.25"])
        prices.append(0.25)
    elif selectedEnsaladas.get() == "Rusa":
        # print("Ensalada Rusa")
        order.append(["Ensalada Rusa", "$0.25"])
        prices.append(0.25)
    else:
        print("No se ha seleccionado ninguna ensalada")

# Creamos una funcion para obtener los datos seleccionados en el area de las bebidas.
def getBebidas():
    if selectedBebidas.get() == "Gaseosa":
        # print("Gaseosa")
        order.append(["Gaseosa", "$0.75"])
        prices.append(0.75)
    elif selectedBebidas.get() == "Fresco":
        # print("Fresco")
        order.append(["Fresco", "$0.50"])
        prices.append(0.50)
    elif selectedBebidas.get() == "Cafe":
        # print("Café")
        order.append(["Café", "$0.65"])
        prices.append(0.65)
    else:
        print("No se ha seleccionado ninguna bebida")

# Creamos la funcion para imprimir la orden.
def printFactura():
    clearList()
    getCarnes()
    getEnsaladas()
    getBebidas()
    # Hacemos la suma de los precios de los productos seleccionados en la orden.
    order.append(["Total", f"${sum(prices)}"])
    # Impresion de la factura.
    print(tabulate(order, headers=["Producto", "Precio"], tablefmt="presto"))

# Creamos los labels
labelTitle = Label(root, text="Cafeteria", font=("Arial", 20), bg="#7677B8")

labelCarnes = Label(root, text="Carnes", font=("Arial", 15), bg="#6FA2AE")
labelEnsaladas = Label(root, text="Ensaladas",
                       font=("Arial", 15), bg="#6FA2AE")
labelBebidas = Label(root, text="Bebidas", font=("Arial", 15), bg="#6FA2AE")



# Creamos los radio buttons

# Seccion de las carnes.
selectCarne = Radiobutton(root, text="Carne Asada", font=(
    "Arial", 15), value='Carne', variable=selectedCarnes, bg="#B2B3C8")

selectPollo = Radiobutton(root, text="Pollo Guisado", font=(
    "Arial", 15), value='Pollo', variable=selectedCarnes, bg="#B2B3C8")

selectLasana = Radiobutton(root, text="Lasaña", font=(
    "Arial", 15), value='Lasaña', variable=selectedCarnes, bg="#B2B3C8")

# Seccion de las ensaladas.
selectFresca = Radiobutton(root, text="Fresca", font=("Arial", 15), value='Fresca',variable=selectedEnsaladas,  bg="#B2B3C8")

selectCoditos = Radiobutton(root, text="Coditos", font=(
    "Arial", 15), value='Coditos', variable=selectedEnsaladas,  bg="#B2B3C8")

selectRusa = Radiobutton(root, text="Rusa", font=(
    "Arial", 15), value='Rusa', variable=selectedEnsaladas,  bg="#B2B3C8")

# Seccion de las bebidas.
selectGaseosa = Radiobutton(root, text="Gaseosa", font=(
    "Arial", 15), value='Gaseosa', variable=selectedBebidas, bg="#B2B3C8")

selectFresco = Radiobutton(root, text="Fresco", font=(
    "Arial", 15), value='Fresco', variable=selectedBebidas, bg="#B2B3C8")

selectCafe = Radiobutton(root, text="Café", font=(
    "Arial", 15), value='Cafe', variable=selectedBebidas, bg="#B2B3C8")

# Creamos el boton para imprimir la factura.
buttonFactura = Button(root, text="Imprimir Factura",
                       font=("Arial", 15), command=printFactura, bg='#7677B8')


# Carnes
carne = showImage('carne')
imagenCarne = Label(root, image=carne)
labelPrecioCarne = Label(root, text="Precio: $2.50", font=("Arial", 15), bg="#B2B3C8")

pollo = showImage('pollo')
imagenPollo = Label(root, image=pollo)
labelPrecioPollo = Label(root, text="Precio: $2.25", font=("Arial", 15), bg="#B2B3C8")

lasana = showImage('lasana')
imagenLasana = Label(root, image=lasana)
labelPrecioLasana = Label(root, text="Precio: $3.00", font=("Arial", 15), bg="#B2B3C8")

# Ensaladas
ensaladaFresca = showImage('ensaladaFresca')
imagenEnsaladaFresca = Label(root, image=ensaladaFresca)
labelPrecioEnsaladaFresca = Label(root, text="Precio: $0.25", font=("Arial", 15), bg="#B2B3C8")

coditos = showImage('coditos')
imagenCoditos = Label(root, image=coditos)
labelPrecioEnsaladaCoditos = Label(root, text="Precio: $0.25", font=("Arial", 15), bg="#B2B3C8")

ensaladaRusa = showImage('ensaladaRusa')
imagenEnsaladaRusa = Label(root, image=ensaladaRusa)
labelPrecioEnsaladaRusa = Label(root, text="Precio: $0.25", font=("Arial", 15), bg="#B2B3C8")

# Bebidas
gaseosa = showImage('gaseosa')
imagenGaseosa = Label(root, image=gaseosa)
labelPrecioGaseosa = Label(root, text="Precio: $0.75", font=("Arial", 15), bg="#B2B3C8")

fresco = showImage('fresco')
imagenFresco = Label(root, image=fresco)
labelPrecioFresco = Label(root, text="Precio: $0.50", font=("Arial", 15), bg="#B2B3C8")

cafe = showImage('cafe')
imagenCafe = Label(root, image=cafe)
labelPrecioCafe = Label(root, text="Precio: $0.65", font=("Arial", 15), bg="#B2B3C8")


# Posicionamos los elementos en la ventana.
labelTitle.place(x=325, y=10)

# Carnes
labelCarnes.place(x=50, y=50)

imagenCarne.place(x=150, y=75)
labelPrecioCarne.place(x=150, y=190)
selectCarne.place(x=150, y=225)

imagenPollo.place(x=350, y=75)
labelPrecioPollo.place(x=350, y=190)
selectPollo.place(x=350, y=225)

imagenLasana.place(x=550, y=75)
labelPrecioLasana.place(x=550, y=190)
selectLasana.place(x=550, y=225)

# Ensaladas
labelEnsaladas.place(x=50, y=300)

imagenEnsaladaFresca.place(x=150, y=320)
labelPrecioEnsaladaFresca.place(x=150, y=435)
selectFresca.place(x=150, y=470)

imagenCoditos.place(x=350, y=320)
labelPrecioEnsaladaCoditos.place(x=350, y=435)
selectCoditos.place(x=350, y=470)

imagenEnsaladaRusa.place(x=550, y=320)
labelPrecioEnsaladaRusa.place(x=550, y=435)
selectRusa.place(x=550, y=470)

# Bebidas
labelBebidas.place(x=50, y=540)

imagenGaseosa.place(x=150, y=570)
labelPrecioGaseosa.place(x=150, y=685)
selectGaseosa.place(x=150, y=720)

imagenFresco.place(x=350, y=570)
labelPrecioFresco.place(x=350, y=685)
selectFresco.place(x=350, y=720)

imagenCafe.place(x=550, y=570)
labelPrecioCafe.place(x=550, y=685)
selectCafe.place(x=550, y=720)

# Button Print
buttonFactura.place(x=575, y=775)

# Mostramos la ventana.
root.mainloop()
## MENÚ PRODUCTOS

def agregarProducto(productos):
    pass

def mostrarProducto(productos):
    pass

def buscarProducto():
    pass

def productoCaro():
    pass

ops = {
    1:agregarProducto,
    2:mostrarProducto,
    3:buscarProducto,
    4:productoCaro
}

productos = {
    "Mouse":[1, ],
    "Teclado":[3, 25000],
    "Monitor":[3,180000]
}

while True:
    print("--- MENU ---")
    print("1. Agregar Producto\n2. Mostrar productos\n3. Buscar producto\n4. Producto mas caro\n5. Salir")
    op = int(input("Seleccione una opción: "))
    if op==5:
        break
    else:
        try:
            ops[op]()
        except KeyError:
            print("Ingrese una opción válida!")
        except Exception as e:
            print(f"Error: {e}, probablemente un error dentro de la función?")
        else:
            pass
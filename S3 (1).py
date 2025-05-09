Inventario = {}
#Funciones.
def añadir_producto():
    #Entrada de datos:
    while True:
        nombre_product = input("Ingresa el nombre del producto: ").lower()
        if not nombre_product:
            print("No puedes ingresar valores vacios.")
            continue
        if not nombre_product.isalpha():
            print(f"El nombre del producto debe contener solo letras y sin espacios.")
            continue
        if nombre_product in Inventario:
            print(f"El producto {nombre_product} ya se encuentra en el Inventario.")
            continue
        while True:
            try:
                precio = float(input("Ingresa el precio del producto: "))
                if precio <= 0:
                    print("No puedes ingresar valores como cero o negativos.")
                    continue
                break
            except ValueError:
                    print("Valor ingresado de manera incorrecta, ingresalo de nuevo")
        while True:
            try:
                cantidad = int(input("Ingresa la cantidad del preducto: "))
                if cantidad < 0:
                    print("No pueden ingresar valores negativos.")
                    continue
                break
            except ValueError:
                print("Ingresaste una cantidad erronea, hazlo de nuevo: ")
        Inventario[nombre_product] = [precio, cantidad]
        print(f"Producto {nombre_product} agregado al Inventario.")
        break

def buscar_producto():
    producto = input("Ingresa el producto que deseas buscar: ").strip().lower()
    if producto in Inventario:
        precio = Inventario[producto][0]
        cantidad = Inventario[producto][1]
        print(f"Producto {producto} encontrado")
        print(f"Su producto {producto} fue encontrado, su precio es de {precio} pesos.\nCantidad disponible es de {cantidad}")
    else:
         print(f"{producto} no se encuentra en el inventario.")

def new_price():
    name_product = input("Ingresa el nombre del producto al cual deseas actualizar su precio: ").lower().strip()
    if name_product in Inventario:
        precio = Inventario[name_product][0]
        print(f"El producto {name_product} fue encontrado en el inventario y tiene un precio actual de {precio}")
        while True:
            try:
                new_price = float(input("Ingresa el nuevo precio del producto: "))
                if new_price <= 0:
                    print("El precio debe ser mayor a cero.")
                    continue
                Inventario[name_product][0] = new_price
                print(f"Precio de {name_product} actualizado a {new_price} pesos.")
                break
            except ValueError:
                print("Valor ingresado no valido, ingresa un número.")
    else:
        print(f"El producto {name_product} no se encontro en el inventario.")

def delete_product():
    print(f"Cual de los siguientes productos deseas eliminar:\n{Inventario}")
    product = input("Ingresa el nombre del producto: ").strip().lower()
    if product in Inventario:
        operacion = input(f"Seguro que deseas eliminar el producto {product}?: ")
        if operacion.lower() == "si":
            del Inventario[product]
            print(f"Se ha eliminado el producto {product} correctamente.")
        else:
            print(f"Cancelado. Producto {product} no fue eliminado, volviendo al menú.")
    else: 
        print(f"Producto {product} no se encuentra en el inventario.")

def calcular_valores():
    valores = map(lambda producto: Inventario[producto][0]*Inventario[producto][1], Inventario)
    cantidad_total = sum(valores)
    print(f"El valor total de los productos del inventario es de {cantidad_total} pesos.")

while True:
    print("\n      MENÚ PRINCIPAL     ")
    print("_________________________")
    print("Que opcion deseas ejecutar.\n")
    print("1. Añadir un producto.")
    print("2. Buscar producto.")
    print("3. Actualiza precio.")
    print("4. Eliminar producto.")
    print("5. Calcular valor total.")
    print("6. Salir.")

    opcion = input("Digita la opción: ")
    if opcion == "1":
        añadir_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        new_price()
    elif opcion == "4":
        delete_product()
    elif opcion == "5":
            calcular_valores()
    elif opcion == "6":
        print("Saliendo del programa. Adios!")
        break
    else:
        print("Opcion invalida. Digita de nuevo")

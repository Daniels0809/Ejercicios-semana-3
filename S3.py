Inventario = {}
cantidad = []
#Funciones.
def añadir_producto():
    #Entrada de datos:
    while True:
        nombre_product = input("Ingresa el nombre del producto: ")
        while True:
            try:
                precio = float(input("Ingresa el precio del preducto: "))
                break
            except ValueError:
                    print("Valor ingresado de manera incorrecta, ingresalo de nuevo")
        while True:
            try:
                cantidad = int(input("Ingresa la cantidad del preducto: "))
                break
            except ValueError:
                print("Ingresaste una cantidad erronea, hazlo de nuevo: ")
        break
    Inventario[nombre_product] = [precio, cantidad]


def buscar_producto():
    lista = Inventario
    #print(lista)
    producto = input("Ingresa el producto que deseas buscar: ")
    if lista:
        print(f"Producto {producto} encontrado")
        return print(f"Su producto {producto} fue encontrado, su precio es de {lista[producto][0]} pesos.\nCantidad disponible es de {lista[producto][1]}")
    else:
         print(f"{producto} no se encuentra en el inventario.")

def new_price():
    lista = Inventario
    name_product = input("Ingresa nombre del producto al que quieres actualizar su precio: ")
    print(lista)
    for producto in lista:
        if producto == name_product:
            print(f"Excelente, {name_product} tiene un precio actual de: {lista[name_product][0]}")
            new_price = int(input(f"Ingresa el nuevo valor de {name_product}: "))
            lista[producto][0] = new_price
            nuevo = lista[producto][0]
            return print(f"Precio actualizado, {lista}, {nuevo}")
        else:
            print("No se encontro el producto.")

def delete_product():
    productos = Inventario
    print(f"Cual de los siguientes productos deseas eliminar:\n{productos}")
    product = input("Ingresa el nombre del producto: ")
    for p in productos:
        if p == product:
            operacion = input(f"Seguro que deseas eliminar el producto {product}?")
            if operacion.lower() == "si":
                del productos[product]
                print(f"Se ha eliminado el producto {product} correctamente.")
                return productos
            else:
                break
        else:
            print(f"Producto {product} no se encuentra en el inventario.")
def calcular_valores():
    calculo = sum(lambda x, y: x+y, Inventario)
    print(calculo)



print(añadir_producto())
print(new_price())
print(delete_product())
print(buscar_producto())



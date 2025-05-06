#Entrada de datos:

lista_productos = []
cantidad = []

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
#Funciones.

def añadir_producto(lista_productos,nombre_product, precio, cantidad):
     productos = {"nombre": nombre_product, "precio": precio, "cantidad": cantidad}
     lista_productos.append(productos)

def buscar_producto(lista_producto):
    lista = lista_producto
    print(lista)
    valor = input("Ingresa el producto que deseas buscar: ")
    if lista:
        print(f"Producto {valor} encontrado")
        return print(f"Su producto {valor} fue encontrado, tiene un precio de {precio} y su cantidad es de {cantidad}")
        
    else:
         print("Producto no encontrado.")

print(añadir_producto(lista_productos, nombre_product, precio, cantidad))
print(buscar_producto(lista_productos))




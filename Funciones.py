def new_price():
    name_product = input("Ingresa nombre del producto al que quieres actualizar su precio: ")
    for producto in lista:
        if producto == name_product:
            print(f"Excelente, {name_product} tiene un precio actual de: {lista[name_product][0]}")
            new_price = int(input(f"Ingresa el nuevo valor de {name_product}: "))
            lista[producto][0] = new_price
            nuevo = lista[producto][0]
            return print(f"Precio actualizado, {lista}, {nuevo}")
        else:
            print("No se encontro el producto.")
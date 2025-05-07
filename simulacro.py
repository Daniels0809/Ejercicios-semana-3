libros = {'Cien años de soledad': ['Cien años de soledad', 'Gabriel García Márquez', 5, 'Realismo mágico'], 'El señor de los anillos': ['La comunidad del anillo', 'J.R.R. Tolkien', 3, 'Fantasía épica'], 'Orgullo y prejuicio': ['Orgullo y prejuicio', 'Jane Austen', 7, 'Novela romántica']}
print("----Vamos a ingresar los libros----")
def añadir_libro():
    while True:
        libro = input("Ingresa el libro de tu preferencia o fin para finalizar: ")
        if libro.lower() == "fin":
            break
        atributos_str = input("Excelente. Ahora ingresa título, autor, cantidad de copias disponibles y género literario, seguido de comas: ")
        lista_atributos = atributos_str.lower().split(",")
        libros[libro] = [lista_atributos]
        

def titulo_libro(libro):
    titulo = input("Ingresa el titulo que deseas buscar: ")
    if not titulo:
        print("El titulo no fue encontrado")
    if titulo in libro:
        return print(f"Titulo {titulo} encontrado.")

print(añadir_libro())
print(f"Los libros disponibles son: {libros}")
print(titulo_libro(libros))

-----------------------------------------------------------------------------------------------------------------------------------------------------------


libros = {'Cien años de soledad': ['Cien años de soledad', 'Gabriel García Márquez', 5, 'Realismo mágico'], 'El señor de los anillos': ['La comunidad del anillo', 'J.R.R. Tolkien', 3, 'Fantasía épica'], 'Orgullo y prejuicio': ['Orgullo y prejuicio', 'Jane Austen', 7, 'Novela romántica']}
cantidad = 0
list_generos = ["Fiction", "Non-Fiction", "Science", "Biography", "Children"]

print("----It's time to add a book----")
def añadir_libro():
    while True:
        libro = input("Enter the book of your choice or 'finish' to finish: ")
        if libro.lower() == "finish":
            break
        while True:
            titulo = input(f"Enter the title of the book {libro}: ")
            if not titulo:
                print("Wrong, there can't be a book without a title.")
            else:
                print("Excelent.")
                break
        while True:
            autor = input(f"Enter the name of the author of the book {libro}")
            if not autor:
                print("X You must enter the name of the author of the book.")
            else:
                print("Excelent.")
                break
        while True:
                copias = int(input(f"Enter the number of copies of the book{libro}"))
                if copias < 0:
                    print("Impossible, there can be no negative copies")
                else:
                    print("Excelent.")
                    break
        while True:
            print(f"Estos son los tipos de genero dispinibles: {list_generos}")
            genero = print("Escribe el tipo de genero")
            if not genero:
                print("Tipo de genero incorrecto")
            else:
                print("Excelent.")
                break
    libros[libro] = [titulo, autor, copias, genero]
    return libros           


"""atributos_str = input("Excelente. Ahora ingresa título, autor, cantidad de copias disponibles y género literario, seguido de comas: ")
    lista_atributos = atributos_str.lower().split(",")
    libros[libro] = lista_atributos"""


def titulo_libro(libro):
    titulo = input("Enter the title you want to search for: ")
    if not titulo:
        print("The title was not found")
    if titulo in libro:
        return print(f"Title {titulo} found.")
    
def prestar_book():
    prestamo = input(f"Which book do you want to borrow?: {libros}")
    
    
    




print(cantidad = libros[])
print(len(libros)-1)
print(añadir_libro())
print(f"Los libros disponibles son: {libros}")
print(titulo_libro(libros))

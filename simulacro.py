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
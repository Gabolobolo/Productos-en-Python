import os

class Product:
    def __init__(self, nombre, categoria, marca, precio, indice):
        self.nombre = nombre
        self.categoria = categoria
        self.marca = marca
        self.precio = precio
        self.indice = indice

productos = [
    Product("Jordan", "Zapatos", "Nike", 120, 1),
    Product("Classic", "Camisas", "Nike", 40, 2),
    Product("Terrex", "Zapatos", "Adidas", 122, 3),
    Product("Classic", "Zapatos", "Puma", 89, 4),
    Product("Venture", "Camisas", "Nike", 150, 5),
    Product("Superst", "Zapatos", "Adidas", 110, 6),
    Product("Terrex", "Chompas", "Adidas", 150, 7),
    Product("Classic", "Chompas", "Puma", 120, 8),
    Product("Venture", "Chompas", "Adidas", 40, 9),
    Product("Hoddie", "Chompas", "Puma", 45, 10)
]

def listar_productos(productos):
    print("Numero\tNombre\t\tCategoria\tMarca\t\tPrecio")
    for prod in productos:
        print(f"{prod.indice}\t\t{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}")

def buscar_por_marca(productos, marca):
    print("Nombre\t\tCategoria\tMarca\t\tPrecio")
    found = False
    for prod in productos:
        if prod.marca == marca:
            print(f"{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}")
            found = True
    if not found:
        print("No existe ningun producto con esa marca")

def buscar_por_categoria(productos, categoria):
    print("Nombre\t\tCategoria\tMarca\t\tPrecio")
    found = False
    for prod in productos:
        if prod.categoria == categoria:
            print(f"{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}")
            found = True
    if not found:
        print("No existe ningun producto con esa categoria")

def buscar_por_precio_menor(productos, precio_maximo):
    print("Nombre\t\tCategoria\tMarca\t\tPrecio")
    found = False
    for prod in productos:
        if prod.precio <= precio_maximo:
            print(f"{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}")
            found = True
    if not found:
        print("No existe ningun producto con ese precio menor")

def editar_producto(productos, indice, nuevo_nombre, nueva_categoria, nueva_marca, nuevo_precio):
    for prod in productos:
        if prod.indice == indice:
            prod.nombre = nuevo_nombre
            prod.categoria = nueva_categoria
            prod.marca = nueva_marca
            prod.precio = nuevo_precio
            print("Producto editado exitosamente!")
            guardar_productos_en_archivo(productos, "productos.txt")
            return
    print("No se encontró un producto con ese ID")

def anadir_producto(productos, nombre, categoria, marca, precio):
    max_indice = max([prod.indice for prod in productos], default=0) + 1
    productos.append(Product(nombre, categoria, marca, precio, max_indice))
    print("Producto agregado exitosamente!")
    guardar_productos_en_archivo(productos, "productos.txt")

def eliminar_producto(productos, indice):
    for i, prod in enumerate(productos):
        if prod.indice == indice:
            productos.pop(i)
            for j in range(i, len(productos)):
                productos[j].indice -= 1
            print("Producto eliminado exitosamente!")
            guardar_productos_en_archivo(productos, "productos.txt")
            return
    print("No se encontró un producto con ese ID")

def guardar_productos_en_archivo(productos, filename):
    with open(filename, 'w') as file:
        file.write("Numero\tNombre\t\tCategoria\tMarca\t\tPrecio\n")
        for prod in productos:
            file.write(f"{prod.indice}\t\t{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}\n")
    print(f"Productos guardados en {filename} exitosamente!")

def ejecutar_archivo(filename):
    if os.name == 'nt':  #Windows
        os.system(f"start {filename}")
    elif os.name == 'posix':  #Mac
        os.system(f"open {filename}")

def main():
    while True:
        print("Elija una opción:")
        print("1. Listar Productos")
        print("2. Buscar Productos")
        print("3. Editar Productos")
        print("4. Agregar Productos")
        print("5. Eliminar Productos")
        print("6. Salir")
        opcion1 = int(input(">> "))

        if opcion1 == 1:
            listar_productos(productos)
        elif opcion1 == 2:
            print("Buscar por:")
            print("1. Marca")
            print("2. Categoría")
            print("3. Precio Menor de")
            opcion2 = int(input(">> "))
            if opcion2 == 1:
                marca = input("Ingrese la marca: ")
                buscar_por_marca(productos, marca)
            elif opcion2 == 2:
                categoria = input("Ingrese la categoría: ")
                buscar_por_categoria(productos, categoria)
            elif opcion2 == 3:
                precio_maximo = float(input("Ingrese el precio máximo: "))
                buscar_por_precio_menor(productos, precio_maximo)
        elif opcion1 == 3:
            indice = int(input("Ingrese el ID del producto que desea editar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nueva_categoria = input("Ingrese la nueva categoría: ")
            nueva_marca = input("Ingrese la nueva marca: ")
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            editar_producto(productos, indice, nuevo_nombre, nueva_categoria, nueva_marca, nuevo_precio)
        elif opcion1 == 4:
            nombre = input("Ingrese el nombre: ")
            categoria = input("Ingrese la categoría: ")
            marca = input("Ingrese la marca: ")
            precio = float(input("Ingrese el precio: "))
            anadir_producto(productos, nombre, categoria, marca, precio)
        elif opcion1 == 5:
            indice = int(input("Ingrese el ID del producto que desea eliminar: "))
            eliminar_producto(productos, indice)
        elif opcion1 == 6:
            guardar_productos_en_archivo(productos, "productos.txt")
            ejecutar_archivo("productos.txt")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        continuar = input("¿Desea elegir otra opción? (s/n): ")
        if continuar.lower() != 's':
            guardar_productos_en_archivo(productos, "productos.txt")
            ejecutar_archivo("productos.txt")
            break

if __name__ == "__main__":
    main()

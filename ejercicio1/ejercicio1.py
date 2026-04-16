agenda = {}

# Agregar contactos 
for i in range(3):
    nombre = input("Nombre: ").upper()
    telefono = input("telefono: ")
    agenda[nombre] = telefono

# consultar 
buscar = input("Buscar nombre. ").upper()
print(agenda.get(buscar, "No exixte"))

# Eliminar 
eliminar = input("Eliminar nombre. ").upper()
agenda.pop(eliminar, None)

# Mostrar agenda inal
print(agenda)
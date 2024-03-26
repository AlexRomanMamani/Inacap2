# Crear un diccionario para administrar usuarios
usuarios = {
    '111-1': {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'email': 'juan@example.com'
    },
    '222-2': {
        'nombre': 'María',
        'apellido': 'Gómez',
        'email': 'maria@example.com'
    },
    '333-3': {
        'nombre': 'Pedro',
        'apellido': 'López',
        'email': 'pedro@example.com'
    }
}

# Imprimir información de todos los usuarios
for usuario, info in usuarios.items():
    print(f"Usuario: {usuario}")
    print(f"Nombre: {info['nombre']}")
    print(f"Apellido: {info['apellido']}")
    print(f"Email: {info['email']}")
    print()

# Acceder a la información de un usuario específico
usuario = '222-2'
info_usuario = usuarios.get(usuario)
if info_usuario:
    print(f"Información del usuario '{usuario}':")
    print(f"Nombre: {info_usuario['nombre']}")
    print(f"Apellido: {info_usuario['apellido']}")
    print(f"Email: {info_usuario['email']}")
else:
    print(f"No se encontró el usuario '{usuario}'")

# Agregar un nuevo usuario
nuevo_usuario = {
    'nombre': 'Ana',
    'apellido': 'González',
    'email': 'ana@example.com'
}
usuarios['444-4'] = nuevo_usuario

# Modificar información de un usuario existente
usuarios['333-3']['email'] = 'pedro_nuevo@example.com'

# Eliminar un usuario
del usuarios['111-1']

# Imprimir el diccionario completo actualizado
print(usuarios)
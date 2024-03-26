import archivoProfe as f

f.crear_archivo("usuarios.txt")

print(f.contar_registros("usuarios.txt"))

contador = f.contar_registros("usuarios.txt")

if f.menu() == 1:
    f.crear_registro("usuarios.txt", f.agregar_usuario(contador))

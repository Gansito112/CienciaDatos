import os

# Configurar usuario (solo la primera vez)
os.system('git config --global user.name "Gansito112"')
os.system('git config --global user.email "christianantoniocescalera@gmail.com"')

# Verificar si el repositorio ya está inicializado
if not os.path.exists(".git"):
    print("🔹 Inicializando repositorio...")
    os.system("git init")
else:
    print("✅ El repositorio ya está inicializado.")

# Verificar si el repositorio remoto ya está configurado
remote_check = os.popen("git remote -v").read()
if "origin" not in remote_check:
    print("🔹 Agregando repositorio remoto...")
    os.system("git remote add origin https://github.com/Gansito112/CienciaDatos.git")
else:
    print("✅ El repositorio remoto ya está configurado.")

# Agregar archivos al commit
print("🔹 Agregando archivos al commit...")
os.system("git add .")

# Hacer commit
commit_message = "Commit desde script Python"
print(f'🔹 Realizando commit: "{commit_message}"...')
os.system(f'git commit -m "{commit_message}"')

# Asegurar que la rama es "main"
print("🔹 Cambiando a la rama main...")
os.system("git branch -M main")

# Subir cambios a GitHub
print("🔹 Subiendo cambios a GitHub...")
os.system("git push -u origin main")

print("✅ ¡Repositorio actualizado exitosamente!")

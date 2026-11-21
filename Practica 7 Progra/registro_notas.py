# Práctica 7: Trabajando con diccionarios
# Registro de estudiantes y sus notas (máximo 5 notas por estudiante)

MAX_NOTAS = 5

# Clave: nombre del estudiante -> Valor: lista de notas
registro = {}


def agregar_estudiante():
    nombre = input("Nombre del estudiante: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
    elif nombre in registro:
        print(f"El estudiante {nombre} ya existe en el registro.")
    else:
        registro[nombre] = []
        print(f"Estudiante {nombre} agregado correctamente.")


def agregar_nota():
    nombre = input("Nombre del estudiante: ").strip()
    if nombre not in registro:
        print(f"El estudiante {nombre} no existe.")
        return
    if len(registro[nombre]) >= MAX_NOTAS:
        print(f"{nombre} ya tiene el máximo de {MAX_NOTAS} notas.")
        return
    try:
        nota = float(input("Ingrese la nota: "))
    except ValueError:
        print("Nota inválida. Debe ser un número.")
        return
    if nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
        return
    registro[nombre].append(nota)
    print(f"Nota {nota} agregada a {nombre}.")


def mostrar_registro():
    if not registro:
        print("El registro está vacío.")
        return
    for nombre, notas in registro.items():
        print(f"{nombre}: {notas}")


def mostrar_promedio():
    nombre = input("Nombre del estudiante: ").strip()
    if nombre not in registro:
        print(f"El estudiante {nombre} no existe.")
    elif len(registro[nombre]) == 0:
        print(f"{nombre} aún no tiene notas.")
    else:
        notas = registro[nombre]
        promedio = sum(notas) / len(notas)
        print(f"Promedio de {nombre}: {promedio:.1f}")


def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar estudiante")
        print("2. Agregar nota a estudiante")
        print("3. Mostrar registro completo")
        print("4. Mostrar promedio de un estudiante")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_nota()
        elif opcion == "3":
            mostrar_registro()
        elif opcion == "4":
            mostrar_promedio()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
import time
import os

# --- Estilos de texto ---
class Color:
    TITULO = "\033[96m"
    RESET = "\033[0m"
    OK = "\033[92m"
    WARN = "\033[93m"
    ERR = "\033[91m"
    INFO = "\033[94m"

# --- Función para limpiar pantalla ---
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# --- Pausa ---
def pausa():
    input(Color.INFO + "\nPresiona ENTER para continuar..." + Color.RESET)

# --- Mostrar secciones ---
def explicar(titulo, texto):
    print(Color.TITULO + f"\n=== {titulo.upper()} ===" + Color.RESET)
    print(texto)
    pausa()
    limpiar()

# --- Menú principal ---
def menu():
    print(Color.TITULO + "=== CURSO INTERACTIVO BÁSICO DE GIT ===\n" + Color.RESET)
    print("1) Iniciar curso")
    print("2) ¿Qué aprenderás?")
    print("3) Salir\n")

    while True:
        opcion = input("Elige una opción (1-3): ")
        if opcion in ["1", "2", "3"]:
            return opcion
        print(Color.ERR + "Opción inválida. Intenta nuevamente." + Color.RESET)

# --- Curso principal ---
def curso_git():
    limpiar()

    while True:
        opcion = menu()

        if opcion == "2":
            limpiar()
            print(Color.INFO + "📘 En este curso aprenderás:\n" + Color.RESET)
            print("- Qué es Git")
            print("- Crear un repositorio (git init)")
            print("- Agregar cambios (git add)")
            print("- Guardar versiones (git commit)")
            print("- Conectar con GitHub (git remote)")
            print("- Subir código (git push)")
            pausa()
            limpiar()

        elif opcion == "3":
            print(Color.OK + "\n¡Hasta pronto!" + Color.RESET)
            break

        elif opcion == "1":
            limpiar()
            print(Color.OK + "Bienvenido al curso interactivo básico de Git.\n" + Color.RESET)

            explicar("¿Qué es git?",
            "Git es un sistema de control de versiones que te permite guardar cambios, regresar a versiones "
            "anteriores y trabajar en equipo sin perder código.")

            explicar("git init",
            "Inicializa un repositorio:\n\n    git init\n\nEsto crea la carpeta .git que guarda el historial.")

            explicar("git add",
            "Agrega archivos al área de preparación (staging):\n\n    git add archivo.py\n    git add .")

            explicar("git commit",
            "Guarda los cambios con un mensaje:\n\n    git commit -m \"Mensaje describiendo cambios\"")

            explicar("git remote add origin",
            "Conecta tu proyecto local con GitHub:\n\n    git remote add origin https://github.com/usuario/repositorio.git")

            explicar("git push",
            "Sube el código al repositorio remoto:\n\n    git push -u origin main")

            print(Color.OK + "\n🎉 ¡Curso básico completado!\n" + Color.RESET)

            # Retroalimentación
            print("Antes de terminar, responde unas preguntas:\n")

            nombre = input("¿Cuál es tu nombre?: ").strip().title()

            respuesta = input("\n¿Entendiste el flujo básico para subir código? (sí/no): ").lower().strip()

            while respuesta not in ["si", "sí", "no", "nop", "n"]:
                respuesta = input(Color.WARN + "Respuesta inválida, escribe sí/no: " + Color.RESET).lower()

            entendio = respuesta in ["si", "sí"]

            if entendio:
                print(Color.OK + f"\nExcelente, {nombre}! 🎉 Ya tienes las bases para comenzar con Git." + Color.RESET)
            else:
                print(Color.WARN + f"\nNo te preocupes, {nombre}. 😊 Puedes repetir el curso cuando quieras." + Color.RESET)

            # Opción para repetir
            repetir = input("\n¿Quieres repetir el curso? (sí/no): ").lower().strip()
            if repetir not in ["si", "sí"]:
                print(Color.OK + "\nGracias por usar este curso interactivo. ¡Hasta la próxima!\n" + Color.RESET)
                break

            limpiar()

curso_git()

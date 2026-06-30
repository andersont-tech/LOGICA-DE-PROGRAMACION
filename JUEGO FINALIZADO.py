import random

# Palabras por nivel
Fácil = ["mar", "gato", "silla", "perro", "mesa"]
Medio = ["ciclo", "cobija", "computadora", "programacion"]
Difícil = ["algoritmo", "hardware", "inteligencia", "software"]

# Dibujo del ahorcado
ahorcado = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]

print("=== JUEGO DEL AHORCADO ===")
print("1. Fácil")
print("2. Medio")
print("3. Difícil")

nivel = input("Seleccione un nivel: ")

if nivel == "1":
    palabra = random.choice(Fácil)
    intentos = 6
elif nivel == "2":
    palabra = random.choice(Medio)
    intentos = 5
elif nivel == "3":
    palabra = random.choice(Difícil)
    intentos = 4
else:
    print("Nivel no válido")
    exit()

letras_adivinadas = []
letras_usadas = []

while intentos > 0:

    print(ahorcado[6 - intentos])

    oculta = ""

    for letra in palabra:
        if letra in letras_adivinadas:
            oculta += letra + " "
        else:
            oculta += "_ "

    print("\nPalabra:", oculta)
    print("Letras usadas:", " ".join(letras_usadas))
    print("Intentos restantes:", intentos)

    if "_" not in oculta:
        print("\n ¡Felicidades! Has ganado.")
        break

    letra = input("Ingrese una letra: ").lower()

    # Validar entrada
    if len(letra) != 1 or not letra.isalpha():
        print("Ingrese solo una letra.")
        continue

    if letra in letras_usadas:
        print("Ya intentaste esa letra.")
        continue

    letras_usadas.append(letra)

    if letra in palabra:
        print(" Correcto.")
        letras_adivinadas.append(letra)
    else:
        intentos -= 1
        print(" Incorrecto.")

if intentos == 0:
    print(ahorcado[6])
    print("\n Has perdido.")
    print("La palabra era:", palabra)
from pelicula import Pelicula
from funcion import Funcion
from sala import Sala
def main():
    pelicula_uno = Pelicula("joker", "suspenso", 120)

    print(pelicula_uno.mostrar_datos())

    funcion_uno = Funcion("03-09-2019","22:00",5000)

    sala_uno = Sala(3,200)
    sala_uno.mostrar_datos()
    print(sala_uno.hay_disponibilidad(220))

if __name__ == "__main__":
    main()
import random # Esta libreria sirve para escoger posiciones aleatorias.

# Esta variable guarda el tamano del tablero.
tamanio = 5

# Esta variable guarda la cantidad de minas.
num_minas = 5

def meme_inicio():
    # Esta funcion muestra un meme al iniciar el juego.
    print(" /\\_/\\\\") # Esta linea dibuja las orejas del gato.
    print("( o.o )  miau, cuidado con las minas") # Esta linea dibuja la cara del gato.
    print(" > ^ <") # Esta linea dibuja las patas del gato.
    print() # Esta linea deja un espacio.

def meme_seguro():
    # Esta funcion muestra un meme cuando el jugador escoge una casilla segura.
    print("(=^.^=) buena, sigues vivo") # Esta linea muestra un gato feliz.
    print() # Esta linea deja un espacio.

def meme_repetido():
    # Esta funcion muestra un meme cuando el jugador escoge una casilla repetida.
    print("(= -_- =) esa ya la habias elegido") # Esta linea muestra un gato serio.
    print() # Esta linea deja un espacio.

def meme_perdiste():
    # Esta funcion muestra un meme cuando el jugador pisa una mina.
    print(" /\\_/\\\\") # Esta linea dibuja las orejas del gato.
    print("( x.x )  BOOM") # Esta linea dibuja el gato derrotado.
    print(" > ^ <") # Esta linea dibuja las patas del gato.
    print() # Esta linea deja un espacio.

def meme_ganaste():
    # Esta funcion muestra un meme cuando el jugador gana.
    print(" /\\_/\\\\") # Esta linea dibuja las orejas del gato.
    print("( ^.^ )  ganaste, crack") # Esta linea dibuja el gato feliz.
    print(" > ^ <") # Esta linea dibuja las patas del gato.
    print() # Esta linea deja un espacio.

def linea():
    # Esta funcion imprime una linea para separar textos.
    print("--------------------------------") # Esta linea hace que la pantalla se vea mas ordenada.

def crear_tablero(valor_inicial):
    # Esta funcion crea una matriz.
    tablero = [] # Esta lista guardara todo el tablero.

    for i in range(tamanio): # Este ciclo recorre las filas.
        fila = [] # Esta lista guarda una fila del tablero.

        for j in range(tamanio): # Este ciclo recorre las columnas.
            fila.append(valor_inicial) # Esta linea agrega una casilla a la fila.

        tablero.append(fila) # Esta linea agrega la fila completa al tablero.

    return tablero # Esta linea devuelve el tablero creado.

def colocar_minas(tablero):
    # Esta funcion pone minas aleatorias en el tablero oculto.
    minas_colocadas = 0 # Esta variable cuenta cuantas minas se han puesto.

    while minas_colocadas < num_minas: # Este ciclo se repite hasta poner todas las minas.
        fila = random.randint(0, tamanio - 1) # Esta linea escoge una fila aleatoria.
        col = random.randint(0, tamanio - 1) # Esta linea escoge una columna aleatoria.

        if tablero[fila][col] != '*': # Esta condicion revisa que no haya una mina ahi.
            tablero[fila][col] = '*' # Esta linea pone una mina.
            minas_colocadas += 1 # Esta linea aumenta el contador de minas.

def contar_minas_alrededor(tablero, fila, col):
    # Esta funcion cuenta cuantas minas hay alrededor de una casilla.
    minas_adyacentes = 0 # Esta variable guarda la cantidad de minas cercanas.

    for i in range(-1, 2): # Este ciclo revisa una fila arriba, la misma fila y una fila abajo.
        for j in range(-1, 2): # Este ciclo revisa una columna izquierda, la misma y una derecha.
            f_vecina = fila + i # Esta linea calcula la fila vecina.
            c_vecina = col + j # Esta linea calcula la columna vecina.

            # Esta condicion revisa que la posicion vecina exista dentro del tablero.
            if f_vecina >= 0 and f_vecina < tamanio and c_vecina >= 0 and c_vecina < tamanio:

                if tablero[f_vecina][c_vecina] == '*': # Esta condicion revisa si hay una mina.
                    minas_adyacentes += 1 # Esta linea suma una mina encontrada.

    return minas_adyacentes # Esta linea devuelve cuantas minas hay alrededor.

def llenar_numeros(tablero):
    # Esta funcion llena el tablero oculto con los numeros.
    for i in range(tamanio): # Este ciclo recorre las filas.
        for j in range(tamanio): # Este ciclo recorre las columnas.

            # Esta condicion evita cambiar las minas por numeros.
            if tablero[i][j] != '*':
                tablero[i][j] = contar_minas_alrededor(tablero, i, j) # Esta linea guarda el numero.

def mostrar_tablero(tablero):
    # Esta funcion muestra el tablero en pantalla.
    print() # Esta linea deja un espacio.
    print("       BUSCAMINAS") # Esta linea muestra el titulo del tablero.
    print("     0   1   2   3   4") # Esta linea muestra los numeros de las columnas.
    print("   ---------------------") # Esta linea muestra una separacion.

    for i in range(tamanio): # Este ciclo recorre las filas del tablero.
        print(i, "|", end="") # Esta linea muestra el numero de la fila.

        for j in range(tamanio): # Este ciclo recorre las columnas del tablero.
            casilla = tablero[i][j] # Esta linea guarda el valor de la casilla actual.

            if casilla == '*': # Esta condicion revisa si la casilla tiene mina.
                print(" * |", end="") # Esta linea muestra una mina.

            elif casilla == ' ': # Esta condicion revisa si la casilla esta tapada.
                print("   |", end="") # Esta linea muestra una casilla vacia.

            else: # Esta parte se usa cuando la casilla tiene un numero.
                print(" " + str(casilla) + " |", end="") # Esta linea muestra el numero.

        print() # Esta linea baja a la siguiente linea.
        print("   ---------------------") # Esta linea separa una fila de otra.

    print() # Esta linea deja un espacio.

def pedir_entrada(mensaje):
    # Esta funcion pide una fila o columna al jugador.
    entrada_valida = False # Esta variable controla si el dato sirve o no.

    while entrada_valida == False: # Este ciclo se repite hasta que el usuario escriba bien.
        texto_ingresado = input(mensaje) # Esta linea pide un dato al usuario.

        if texto_ingresado.isdigit() == True: # Esta condicion revisa si el dato es un numero.
            valor = int(texto_ingresado) # Esta linea convierte el texto a numero entero.

            if valor >= 0 and valor <= 4: # Esta condicion revisa que el numero este entre 0 y 4.
                return valor # Esta linea devuelve el numero correcto.

            else: # Esta parte se ejecuta si el numero no esta entre 0 y 4.
                print("Ingresa un numero entre 0 y 4.") # Esta linea muestra un aviso.

        else: # Esta parte se ejecuta si el usuario no escribio un numero.
            print("Debes ingresar un numero.") # Esta linea muestra un aviso.

def main():
    # Esta funcion controla el juego completo.
    linea() # Esta linea imprime una separacion.
    print("Bienvenido a Buscaminas") # Esta linea muestra el saludo.
    print("Encuentra las casillas seguras sin tocar minas.") # Esta linea explica el objetivo.
    linea() # Esta linea imprime otra separacion.
    meme_inicio() # Esta linea muestra el primer meme.

    tablero_visible = crear_tablero(' ') # Esta matriz es la que ve el jugador.
    tablero_oculto = crear_tablero(0) # Esta matriz guarda las minas y los numeros.

    colocar_minas(tablero_oculto) # Esta linea coloca las minas.
    llenar_numeros(tablero_oculto) # Esta linea coloca los numeros alrededor de las minas.

    casillas_seguras_totales = (tamanio * tamanio) - num_minas # Esta linea calcula las casillas sin mina.
    casillas_descubiertas = 0 # Esta variable cuenta las casillas seguras descubiertas.
    juego_terminado = False # Esta variable dice si el juego sigue o termina.

    while juego_terminado == False: # Este ciclo mantiene el juego funcionando.
        mostrar_tablero(tablero_visible) # Esta linea muestra el tablero actual.

        print("Ingresa las coordenadas de la casilla:") # Esta linea pide las coordenadas.
        fila = pedir_entrada("Fila (0-4): ") # Esta linea pide la fila.
        col = pedir_entrada("Columna (0-4): ") # Esta linea pide la columna.
        print() # Esta linea deja un espacio.

        if tablero_visible[fila][col] != ' ': # Esta condicion revisa si la casilla ya esta descubierta.
            print("Esa casilla ya fue descubierta.") # Esta linea muestra un aviso.
            meme_repetido() # Esta linea muestra un meme.

        else: # Esta parte se ejecuta si la casilla no estaba descubierta.

            if tablero_oculto[fila][col] == '*': # Esta condicion revisa si el jugador piso una mina.
                print("Pisaste una mina.") # Esta linea avisa que el jugador perdio.
                meme_perdiste() # Esta linea muestra un meme.
                juego_terminado = True # Esta linea termina el juego.

                for i in range(tamanio): # Este ciclo recorre las filas.
                    for j in range(tamanio): # Este ciclo recorre las columnas.

                        if tablero_oculto[i][j] == '*': # Esta condicion busca las minas.
                            tablero_visible[i][j] = '*' # Esta linea muestra las minas.

                mostrar_tablero(tablero_visible) # Esta linea muestra el tablero final.

            else: # Esta parte se ejecuta si la casilla es segura.
                tablero_visible[fila][col] = tablero_oculto[fila][col] # Esta linea descubre la casilla.
                casillas_descubiertas += 1 # Esta linea suma una casilla descubierta.
                meme_seguro() # Esta linea muestra un meme.

                if casillas_descubiertas == casillas_seguras_totales: # Esta condicion revisa si gano.
                    print("Felicidades, ganaste.") # Esta linea muestra el mensaje de victoria.
                    meme_ganaste() # Esta linea muestra un meme.
                    mostrar_tablero(tablero_visible) # Esta linea muestra el tablero final.
                    juego_terminado = True # Esta linea termina el juego.

juego_activo = True # Esta variable controla si se sigue jugando o no.

while juego_activo == True: # Este ciclo permite jugar multiples veces.
    main() # Esta linea llama la funcion principal para iniciar el juego.
    
    respuesta_valida = False # Esta variable controla si la respuesta es valida.
    
    while respuesta_valida == False: # Este ciclo se repite hasta obtener una respuesta valida.
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ") # Esta linea pide si quiere jugar de nuevo.
        
        if respuesta.lower() == 's': # Esta condicion revisa si el usuario quiere seguir jugando.
            respuesta_valida = True # Esta linea valida la respuesta.
        
        elif respuesta.lower() == 'n': # Esta condicion revisa si el usuario quiere salir.
            juego_activo = False # Esta linea termina el ciclo principal.
            respuesta_valida = True # Esta linea valida la respuesta.
        
        else: # Esta parte se ejecuta si la respuesta no es valida.
            print("Debes ingresar 's' o 'n'.") # Esta linea muestra un aviso.

#cd "C:\Users\anfel\Desktop\Buscaminas"--> COMANDO PARA EJECUTAR EL JUEGO
#python "Juego buscaminas con memes.py"--> COMANDO PARA EJECUTAR EL JUEGO

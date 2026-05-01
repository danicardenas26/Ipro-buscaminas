import random # Única librería permitida

# Constantes del juego[cite: 2]
TAMANIO = 5
NUM_MINAS = 5

def crear_tablero(valor_inicial):
    """Crea una matriz de 5x5 usando ciclos básicos para mayor claridad."""
    tablero = []
    for i in range(TAMANIO):
        fila = [] 
        for j in range(TAMANIO):
            fila.append(valor_inicial) 
        tablero.append(fila) 
    return tablero

def colocar_minas(tablero, num_minas):
    """Coloca las minas de forma aleatoria sin repetir posiciones."""
    minas_colocadas = 0
    while minas_colocadas < num_minas: #[cite: 1]
        fila = random.randint(0, TAMANIO - 1) #[cite: 1]
        col = random.randint(0, TAMANIO - 1) #[cite: 1]
        
        # Si no hay una mina en esa posición, la colocamos
        if tablero[fila][col] != '*': #[cite: 1]
            tablero[fila][col] = '*' #[cite: 1]
            minas_colocadas += 1 #[cite: 1]

def contar_minas_alrededor(tablero, fila, col):
    """Cuenta cuántas minas hay en las 8 casillas vecinas."""
    if tablero[fila][col] == '*':
        return -1 
    
    minas_adyacentes = 0
    
    for i in range(-1, 2):
        for j in range(-1, 2):
            f_vecina = fila + i
            c_vecina = col + j
            
            if f_vecina >= 0 and f_vecina < TAMANIO and c_vecina >= 0 and c_vecina < TAMANIO:
                if tablero[f_vecina][c_vecina] == '*':
                    minas_adyacentes += 1
                    
    return minas_adyacentes

def mostrar_tablero(tablero):
    """Dibuja el tablero en pantalla usando print() continuos."""
    print("\n    0   1   2   3   4") 
    print("  ---------------------")
    
    for i in range(TAMANIO):
        print(f"{i} |", end="") 
        
        for j in range(TAMANIO):
            casilla = tablero[i][j]
            
            if casilla == '*':
                print(" * |", end="") 
            elif casilla == ' ':
                print("   |", end="") #[cite: 2]
            elif type(casilla) == int:
                print(f" {casilla} |", end="") 
                    
        print("\n  ---------------------")
    print()

def pedir_entrada(mensaje):
    """Pide una coordenada al usuario y valida usando condicionales e isdigit()."""
    entrada_valida = False
    while entrada_valida == False:
        texto_ingresado = input(mensaje)
        
        if texto_ingresado.isdigit() == True:
            valor = int(texto_ingresado) 
            
            if valor >= 0 and valor <= 4: #[cite: 2]
                return valor
            else:
                print("Advertencia: Ingresa un número entre 0 y 4.") #[cite: 2]
        else:
            print("Error: Entrada no válida. Debes ingresar un número.") #[cite: 2]

def main():
    """Controla el flujo principal del juego."""
    print("--- ¡Bienvenido a Buscaminas! ---")
    print("Encuentra las casillas seguras sin tocar las minas.\n")
    
    tablero_visible = crear_tablero(' ') #[cite: 2]
    tablero_oculto = crear_tablero(0)
    
    colocar_minas(tablero_oculto, NUM_MINAS) #[cite: 2]
    
    for i in range(TAMANIO):
        for j in range(TAMANIO):
            tablero_oculto[i][j] = contar_minas_alrededor(tablero_oculto, i, j)
            
    casillas_seguras_totales = (TAMANIO * TAMANIO) - NUM_MINAS
    casillas_descubiertas = 0
    juego_terminado = False
    
    while juego_terminado == False:
        mostrar_tablero(tablero_visible)
        
        print("Ingresa las coordenadas de la casilla a descubrir:")
        fila = pedir_entrada("Fila (0-4): ")
        col = pedir_entrada("Columna (0-4): ")
        
        if tablero_visible[fila][col] != ' ': #[cite: 2]
            print("Advertencia: Esta casilla ya fue descubierta. Intenta de nuevo.") #[cite: 2]
            continue
            
        if tablero_oculto[fila][col] == '*':
            print("¡Boom! Pisaste una mina.") #[cite: 2]
            juego_terminado = True
            
            for i in range(TAMANIO):
                for j in range(TAMANIO):
                    if tablero_oculto[i][j] == '*':
                        tablero_visible[i][j] = '*' #[cite: 2]
            mostrar_tablero(tablero_visible)
            
        else:
            tablero_visible[fila][col] = tablero_oculto[fila][col]
            casillas_descubiertas += 1
            
            if casillas_descubiertas == casillas_seguras_totales: #[cite: 2]
                print("¡Felicidades! Ganaste.") #[cite: 2]
                mostrar_tablero(tablero_visible)
                juego_terminado = True


main()
# Programa para verificar el cuadrante de una coordenada.

# Aqui digitamos una variable fundamental a ser estudiada por la funcion evaluar_variable_uno()

variable_numeros = '-123456789.'

# Esta funcion ayudará a verificar que el usuario no digite mal un dato de tipo numerico o float al momento de digitar coordenadas para
# estudiar sus cuadrantes en el que se encuentren
def evaluar_variable_uno(param,variable):
    cont = 0
    if(param.count('.') > 1 or param.count('-') > 1 or param == '0'):
        cont += 1
    for i in param:
        # el objetivo de esta condicional esque si se cumple almenos una vez la condición, se le aumentará un uno, y para esta 
        # variable (cont_tres) solo basta con un uno para indicar que hay un error en el dato del usuario
        if(i not in variable):
            cont += 1
    return int(cont)

def evaluar_variable_dos(cadena):
    while(evaluar_variable_uno(cadena,variable_numeros)>0):
        cadena = input('Favor de intentarlo de nuevo: ')
    return float(cadena)

# Estas variables se usaran a lo largo de este programa para que al preguntarle al usuario de si le gusto o no el programa, estas 
# cuenten de uno en uno las cantidad de valoraciones ya sean positivas o negativas dependiendo de si el usuario responde con un "Y" o un
# "N" (en ingles yes o no)
cont = 0; cont_seg = 0

# Esta funcion ayudará a verificar para cuando al usuario le toqué responder de si quiere trabajar en el plano 3D o 2D, ya que si llega-
# rá a responder algo diferente de los incisos a) ó b), le lanzará al usuario que debe digitar su respuesta de nuevo.
def leervar_curt(param,letra_uno,letra_dos,letra_tres,letra_cuatro):
    while(param != letra_uno and param != letra_dos and param != letra_tres and param != letra_cuatro):
        param = input(f'Favor de ingresar de nuevo el dato por favor ({letra_uno}/{letra_tres}): ')
    return param
    
# Esta es la función dedicada a leer coordenadas de tipo 2D en caso de que el usuario digite la "a" para el inciso a) 
def CalC_Cuad():
    x = input('Favor de digitar la coordenada en "X": ')
    # Usamos la funcion evld_var() para validar el dato de manera correcta
    x = evaluar_variable_dos(x) 
    y = input('Favor de digitar la coordenada en "Y": ')
    y = evaluar_variable_dos(y)
    
    # Y de a cuerdo a las condiciones en las que se encuentre la coordenada, verificará a que cuadrante peertenece
    if(x > 0 and y > 0):
        print('Su punto se encuentra en el cuadrante I')
    elif(x < 0 and y > 0):
        print('Su punto se encuentra en el cuadrante II')
    elif(x < 0 and y < 0):
        print('Su punto se encuentra en el cuadrante III')
    elif(x > 0 and y < 0):
        print('Su punto se encuentra en el cuadrante IV')

# Esta es la función dedicada a leer coordenadas de tipo 3D en caso de que el usuario digite la "b" para el inciso b)
def CalC_Cuad_seg():
    x = input('Favor de digitar la coordenada en "X": ')
    # Aplicamos las mismas logicas que con la CalC_Cuad()
    x = evaluar_variable_dos(x)
    
    y = input('Favor de digitar la coordenada en "Y": ')
    y = evaluar_variable_dos(y)
    
    z = input('Favor de digitar la coordenada en "Z": ')
    # Solo que esta vez agregandole la coordenada 3ra en z
    z = evaluar_variable_dos(z)
    
    # Y en esta ocasión evaluará pero para un octante
    if(x > 0 and y > 0 and z > 0):
        print('Su punto se encuentra en el octante I')
    elif(x > 0 and y < 0 and z > 0):
        print('Su punto se encuentra en el octante IV')
    elif(x < 0 and y > 0 and z > 0):
        print('Su punto se encuentra en el octante II')
    elif(x < 0 and y < 0 and z > 0):
        print('Su punto se encuentra en el octante III')
    elif(x > 0 and y > 0 and z < 0):
        print('Su punto se encuentra en el octante V')
    elif(x > 0 and y < 0 and z < 0):
        print('Su punto se encuentra en el octante VIII')
    elif(x < 0 and y > 0 and z < 0):
        print('Su punto se encuentra en el octante VI')
    elif(x < 0 and y < 0 and z < 0):
        print('Su punto se encuentra en el octante VII')

    
answer = 's'
while(answer == 's' or answer == 'S'):
    print("""En que plano desea trabajar? 
a) Plano 2D,\tb) Plano 3D""")
    # preguntamos por el plano (a o b) en el que desea trabajar
    answer = input('Digite su respuesta (a/b): ')
    # nos aseguramos de que sea correcta entre "a" ó "b"
    answer = leervar_curt(answer,'A','a','B','b')
    # Y nos enfocamos en llamar a la función correcta de a cuerdo al inciso que haya digitado
    if(answer == 'a' or answer == 'A'):
        CalC_Cuad()
    elif(answer == 'b' or answer == 'B'):
        CalC_Cuad_seg()
    # Valoramos la experiencia que haya tenido nuestro usuario
    answer = input('Le gusto nuestro servicio (S/N)? ')
    answer = leervar_curt(answer,'S','s','N','n')
    
    # Luego de asegurarnos de que haya respondido bien entre "y" o "n" con leervar_quint(), dependiendo de la respuesta,
    # le sumamos de uno en uno a alguna de nuestras variables anteriormente explicadas
    if(answer == 's' or answer == 'S'):
        cont += 1
    elif(answer == 'n' or answer == 'N'):
        cont_seg += 1
    answer = input('Desea volver a intentarlo (S/N)? ')
    answer = leervar_curt(answer,'S','s','N','n')
if(cont > cont_seg):
    conclusión = 'A la gente le gusto mas el programa de lo que no le gusto'
elif(cont_seg > cont):
    conclusión = 'A la gente le desagrado mas el programa de lo que le gusto'
else:
    conclusión = 'A la gente le gusto el programa tanto como no le gusto'
print(f'''\n Has llegado al final del programa
Valoraciones buenas: {cont}
Valoraciones malas: {cont_seg}
Conclusión Final: {conclusión}
''')

#################################################################################################################################

# Programa para medir la longitud de una palabra

answer = 's'
while(answer == 'S' or answer == 's'):
    palabra = input('Digite su correspondiente palabra: ')
    cantidad = len(palabra)
    
    if(cantidad >= 4 and cantidad <= 8):
        print(f'Su palabra "{palabra}" es ¡CORRECTO!')
    elif(cantidad < 4):
        print(f'Hacen falta letras. Solo tiene "{cantidad}" letras.')
    elif(cantidad > 8):
        print(f'Sobran letras. Tiene "{cantidad}" letras.')
    
    answer = input('Le gustaria volver a intentarlo (S/N)? ')
    answer = leervar_curt(answer,'S','s','N','n')

print('Usted ya ha llegado al final del programa, gracias por su visita.')
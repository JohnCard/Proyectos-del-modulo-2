# Programa para verificar el cuadrante de una coordenada.

# Aqui digitamos una variable fundamental a ser estudiada por la funcion evaluar_variable_uno()

variable_numeros = '-123456789.'

# Esta funcion ayudará a verificar que el usuario no digite mal un dato de tipo numerico o float al momento de digitar coordenadas para
# estudiar sus cuadrantes en el que se encuentren
def evaluar_variable_uno(param):
    cont = 0
    for i in param:
        # el objetivo de esta condicional esque si se cumple almenos una vez la condición, se le aumentará un uno, y para esta 
        # variable (cont_tres) solo basta con un uno para indicar que hay un error en el dato del usuario
        if(i not in variable_numeros or param.count('.') > 1 or param.count('-') > 1 or param == '0'):
            cont += 1
    return cont

# Estas variables se usaran a lo largo de este programa para que al preguntarle al usuario de si le gusto o no el programa, estas 
# cuenten de uno en uno las cantidad de valoraciones ya sean positivas o negativas dependiendo de si el usuario responde con un "Y" o un
# "N" (en ingles yes o no)
cont = 0; cont_seg = 0

# Esta funcion ayudará a verificar para cuando al usuario le toqué responder de si quiere trabajar en el plano 3D o 2D, ya que si llega-
# rá a responder algo diferente de los incisos a) ó b), le lanzará al usuario que debe digitar su respuesta de nuevo.
def leervar_curt(param,letra_uno,letra_dos,letra_tres,letra_cuatro):
    while(param != letra_uno and param != letra_dos and param != letra_tres and param != letra_cuatro):
        param = input('Favor de ingresar de nuevo el dato por favor (A/B): ')
    return param
    
# Esta es la función dedicada a leer coordenadas de tipo 2D en caso de que el usuario digite la "a" para el inciso a) 
def CalC_Cuad():
    x = input('Favor de digitar la coordenada en "X": ')
    # Usamos la funcion evld_var() para validar el dato de manera correcta
    x = evld_var(x) 
    
    y = input('Favor de digitar la coordenada en "Y": ')
    y = evld_var(y)
    
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
    x = evld_var(x)
    
    y = input('Favor de digitar la coordenada en "Y": ')
    y = evld_var(y)
    
    z = input('Favor de digitar la coordenada en "Z": ')
    # Solo que esta vez agregandole la coordenada 3ra en z
    z = evld_var(z)
    
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

    
answer = 'y'
while(answer_prim == 'y' or answer_prim == 'Y'):
    print("""En que plano desea trabajar? 
a) Plano 2D
b) Plano 3D""")
    # preguntamos por el plano (a o b) en el que desea trabajar
    answer_seg = input('Digite su respuesta (a/b): ')
    # nos aseguramos de que sea correcta entre "a" ó "b"
    answer_seg = leervar_curt(answer_seg)
    # Y nos enfocamos en llamar a la función correcta de a cuerdo al inciso que haya digitado
    if(answer_seg == 'a' or answer_seg == 'A'):
        CalC_Cuad()
    elif(answer_seg == 'b' or answer_seg == 'B'):
        CalC_Cuad_seg()
    # Valoramos la experiencia que haya tenido nuestro usuario
    answer_tir = input('Le gusto nuestro servicio (Y/N)? ')
    answer_tir = leervar_quint(answer_tir)
    
    # Luego de asegurarnos de que haya respondido bien entre "y" o "n" con leervar_quint(), dependiendo de la respuesta,
    # le sumamos de uno en uno a alguna de nuestras variables anteriormente explicadas
    if(answer_tir == 'y' or answer_tir == 'Y'):
        cont += 1
    elif(answer_tir == 'n' or answer_tir == 'N'):
        cont_seg += 1
    answer_prim = input('Desea volver a intentarlo (Y/N)? ')
    answer_prim = leervar_quint(answer_prim)
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
    while(answer != 'S' and answer != 's' and answer != 'n' and answer != 'N'):
        answer = input(f'El dato {answer} es incorrecto, favor de digitarlo de nuevo: ')

print('Usted ya ha llegado al final del programa, gracias por su visita.')
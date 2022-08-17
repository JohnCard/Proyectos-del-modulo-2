# Programa para verificar el cuadrante de una coordenada.

# Aqui digitamos unas cuantas variables con distintos valores a leer por otras funciones para despues validar distintos datos y 
# asegurarnos de que el usuario digite bien sus respuestas, con los distintos caracteres que claramente esperariamos que por error
# podria poner al llenar el formulario
var_prim = 'ZXCVBMASDFGHJKLÑQWERTUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvbmasdfghjklñqwertuiop 1234567890.'

var_seg = 'ZXCVBNMASDFGHJKLÑQWERTYUIOP¨¨+*~[]^``/|¬°!"#$%&()=_;:,zxcvbnmasdfghjklñqwertyuiop '

var_ter = 'ZXCVNMSDFGHJKLÑQWERTYUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvnmsdfghjklñqwertyuiop 1234567890.'

# Estas variables se usaran a lo largo de este programa para que al preguntarle al usuario de si le gusto o no el programa, estas 
# cuenten de uno en uno las cantidad de valoraciones ya sean positivas o negativas dependiendo de si el usuario responde con un "Y" o un
# "N" (en ingles yes o no)
cont = 0; cont_seg = 0

# Esta es la funcion que recibe como parametro una palabra o caracter (xy) y una cadena de otros caracteres a evaluar (x) para despues
# ir contando de uno en uno si esque efectivamente llega a encontrarse con uno de estos caracteres, al final si el return devuelve 
# algo mayor a 0, significaria que el usuario efectivamente esta llenando mal el formulario
def leerparams(xy,x):
    cont = 0
    for i in xy:
        if i in x:
            cont +=1
    return cont

# Esta funcion verificará la variable var_seg
def leervar_prim(param):
    return leerparams(param,var_seg)

# Esta funcion verificará la variable var_prim
def leervar_seg(param):
    return leerparams(param,var_prim)

# Esta funcion verificará la variable var_ter
def leervar_tir(param):
    return leerparams(param,var_ter)

# Esta funcion ayudará a verificar para cuando al usuario le toqué responder de si quiere trabajar en el plano 3D o 2D, ya que si llega-
# rá a responder algo diferente de los incisos a) ó b), le lanzará al usuario que debe digitar su respuesta de nuevo.
def leervar_curt(param):
    while(param != 'a' and param != 'A' and param != 'B' and param != 'b'):
        param = input('Favor de ingresar de nuevo el dato por favor (A/B): ')
    return param

# Esta funcion validará un dato (param) de cuando al usuario le toque responder algo tan simple como si o no 
# (yes o no en ingles con Y y N).
def leervar_quint(param):
    while(param != 'y' and param != 'Y' and param != 'N' and param != 'n'):
        param = input('Favor de ingresar de nuevo el dato por favor (Y/N): ')
    return param

# Aqui la funcion recorr_un(), validará si el usuario al tener que digitar algun dato numerico, lo digita 
# con mas de un punto decimal, ya que si se cumple que en el recorrido del string (param) o cadena digitada por el usuario durante
# el input(___), efectivamente hace el conteo y el return devuelve un valor 
# mayor a uno, significa que efectivamente hay mas de un punto decimal (lect) en su cadena o string.
def recorr_un(param, lect):
    cont = 0
    for i in param:
        if i == lect:
            cont += 1
    return cont

# Esta funcion ayudará a verificar que cuando al usuario le toqué digitar las correspondientes coordenadas, no haya valor igual a 0
# o que simplemente se asegure que sean numericas (de tipo float incluidas).
def evld_var(xy):
    while(leervar_prim(xy) > 0 or len(xy) == 0 or recorr_un(xy,'.') > 1 or float(xy) == 0):
        xy = input('Favor de digitar su variable de nuevo: ')
    return float(xy)
    
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

# Una vez definidas las funciones, ya podemos romper el hielo preguntandole al usuario si quiere empezar a buscar cuadrantes u
# distintos octantes de distintas coordenadas, ya que si digita la n, el programa directamente se terminará
answer_prim = input('\n Le gustaría saber del cuadrante de una coordenada dada (Y/N)? ')

# Usamos leervar_quint() para asegurarnos de que solo digite y o n
answer_prim = leervar_quint(answer_prim)

# Si es que la respuesta efectivamente fue si o digito algun error, iniciará un bucle en el cual, mientras quiera, puede seguir buscando
# otros octanes o cuadrantes de distintas coordenadas o intentar digitar su respuesta de nuevo hasta hacerlo bien, esto gracias a la 
# lógica escrita en los parentesis de abajo, que dependiendo de las repsuestas, realizarán ciertas instrucciones
if(answer_prim == 'y' or answer_prim == 'Y' or len(answer_prim) == 0 or leervar_seg(answer_prim) > 0 or 'yy' in answer_prim or 'YY' in answer_prim or 'NN' in answer_prim or 'nn' in answer_prim):
    
    # Es aqui donde efectivamente inicia el ciclo, yaque antes fue simplemente una validación
    while(answer_prim == 'y' or answer_prim == 'Y' or len(answer_prim) == 0 or leervar_seg(answer_prim) > 0 or 'yy' in answer_prim or 'YY' in answer_prim or 'NN' in answer_prim or 'nn' in answer_prim):
        
        # Si es que digita correctamente un si o y para este caso, iniciará ahora si ha preguntarle todo lo necesario para buscar el
        # estado en el que se encuentra una coordenada 
            if(answer_prim == 'y' or answer_prim == 'Y'):
                print('''\n En que plano desea trabajar? 
a) Plano 2D
b) Plano 3D
                        ''')
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
            elif(answer_prim != 'y' and answer_prim != 'Y' and answer_prim != 'n' and answer_prim != 'N'):
                answer_prim = input('Su respuesta es incorrecta, intentelo de nuevo (Y/N): ')
    else:
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
                
elif(answer_prim == 'n' or answer_prim == 'N'):
    print('''\n En ese caso, Usted ya ha llegado al final del programa. 
\n''')

#################################################################################################################################

# Programa para medir la longitud de una palabra

answer = input('\n Desea digitar algun mensaje (S/N): ')
while(answer != 'S' and answer != 's' and answer != 'n' and answer != 'N'):
    answer = input(f'El dato {answer} es incorrecto, favor de digitarlo de nuevo (S/N): ')
    
while(answer == 'S' or answer == 's'):
    palabra = input('Digite su correspondiente mensaje o frase: ')
    fixture = []
    fixture.extend(palabra.split())
    if(len(fixture) >= 4 and len(fixture) <= 8):
        print(f'Su mensaje "{palabra}" es ¡CORRECTO!')
    elif(len(fixture) < 4):
        print(f'Hacen falta letras. Solo tiene "{len(fixture)}" letras.')
    elif(len(fixture) > 8):
        print(f'Sobran letras. Tiene "{len(fixture)}" letras.')
    
    answer = input('Le gustaria volver a intentarlo (S/N)? ')
    while(answer != 'S' and answer != 's' and answer != 'n' and answer != 'N'):
        answer = input(f'El dato {answer} es incorrecto, favor de digitarlo de nuevo: ')
    
    if(answer == 'n' or answer == 'N'):
        print('Entonces usted ya ha llegado al final del programa, gracias por su visita.')
        exit()

if(answer == 'n' or answer == 'N'):
    print('En ese caso usted ya ha llegado al final del programa, gracias.')
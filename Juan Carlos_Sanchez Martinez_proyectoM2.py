# Programa para verificar el cuadrante de una coordenada.

# Aqui digitamos una variable fundamental a ser estudiada por la funcion evaluar_variable_uno()

cuarta_variable = '-123456789.'

# Esta funcion ayudará a verificar que el usuario no digite mal un dato de tipo numerico o float al momento de digitar coordenadas para
# estudiar sus cuadrantes en el que se encuentren
def evaluar_variable_uno(param):
    # inicializaremos estas variables con 0, las cuales se les aumentara un uno en uno si esque su condición se cumple para asi verificar
    # el error y prevenir que lo pase por alto el usuario
    cont_tres = 0
    cont_cuatro = 0
    cont_cinco = 0
    for i in param:
        # el objetivo de esta condicional esque si el cont_cuatro llegase a superar el uno durante el recorrido del for en el param o la
        # cadena digitada por el usuario, es porque hay mas de un '.' en el dato y eso claro que no esta permitido en un dato numerico
        # sea normal o decimal
        if i == '.':
            cont_cuatro += 1
        # el objetivo de esta condicional esque si el cont_cinco llegase a superar el uno durante el recorrido del for en el param o la
        # cadena digitada por el usuario, es porque hay mas de un '-' en el dato y eso claro que no esta permitido en un dato numerico
        # sea normal o decimal
        if i == '-':
            cont_cinco += 1
        # el objetivo de esta condicional esque si se cumple almenos una de estas condiciones, se le aumentará un uno, y para esta 
        # variable (cont_tres) solo basta con un uno para indicar que hay un error en el dato del usuario
        if((i not in cuarta_variable) or (cont_cuatro > 1) or (cont_cinco > 1) or (float(param) < 0)):
            cont_tres += 1
    return cont_tres

# Estas variables se usaran a lo largo de este programa para que al preguntarle al usuario de si le gusto o no el programa, estas 
# cuenten de uno en uno las cantidad de valoraciones ya sean positivas o negativas dependiendo de si el usuario responde con un "Y" o un
# "N" (en ingles yes o no)
cont = 0; cont_seg = 0

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

# Esta funcion ayudará a verificar que cuando al usuario le toqué digitar las correspondientes coordenadas, no haya valor igual a 0
# o que simplemente se asegure que sean numericas (de tipo float incluidas).
def evld_var(param):
    while(evaluar_variable_uno(param) > 0):
        param = input('Favor de digitar su variable de nuevo: ')
    return float(param)
    
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
if(answer_prim == 'y' or answer_prim == 'Y'):
    
    # Es aqui donde efectivamente inicia el ciclo, yaque antes fue simplemente una validación
    while(answer_prim == 'y' or answer_prim == 'Y'):
        
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
            # aqui se hace referencia a la lógica integrada en el bucle que le da inicio a este formulario
            elif(answer_prim != 'y' and answer_prim != 'Y' and answer_prim != 'n' and answer_prim != 'N'):
                answer_prim = input('Su respuesta es incorrecta, intentelo de nuevo (Y/N): ')
    # aqui de a cuerdo a cual de los contadores fuera mas grande que el otro, o si en caso de que llegasen a ser iguales,
    # se le informará al usuario(s) que hayan usado el programa sobre la satisfacción en general que se llevaron la gran mayoria
    # para ser guardado en una variable que contendrá ese mensaje de conclusión
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

# En caso de que el usuario digite directamente que no esta interesado con un n, el programa acabará inmediatamente con un mensaje de
# despedida 🙋‍♂️.
elif(answer_prim == 'n' or answer_prim == 'N'):
    print('''\n En ese caso, Usted ya ha llegado al final del programa. 
\n''')

#################################################################################################################################

# Programa para medir la longitud de una palabra


answer = input('\n Desea digitar alguna palabra (S/N): ')

# Validamos la respuesta anterior del usuario, para asegurarnos de que la digite de acuerdo a lo que se le solicita escribir
while(answer != 'S' and answer != 's' and answer != 'n' and answer != 'N'):
    answer = input(f'El dato {answer} es incorrecto, favor de digitarlo de nuevo (S/N): ')

# Una vez validada su respuesta, si es que dijo que si con "S", mientras la variable answer sea igual a 's', significará que el bucle
# continuará o que el usuario quiere seguir intentando con mas mensajes de prueba
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
    
    if(answer == 'n' or answer == 'N'):
        print('Entonces usted ya ha llegado al final del programa, gracias por su visita.')
        exit()

if(answer == 'n' or answer == 'N'):
    print('En ese caso usted ya ha llegado al final del programa, gracias.')

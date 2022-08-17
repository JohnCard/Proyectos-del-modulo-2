var_prim = 'ZXCVBMASDFGHJKLÑQWERTUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvbmasdfghjklñqwertuiop 1234567890.'

var_seg = 'ZXCVBNMASDFGHJKLÑQWERTYUIOP¨¨+*~[]^``/|¬°!"#$%&()=_;:,zxcvbnmasdfghjklñqwertyuiop '

var_ter = 'ZXCVNMSDFGHJKLÑQWERTYUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvnmsdfghjklñqwertyuiop 1234567890.'

cont = 0; cont_seg = 0

def leerparams(xy,x):
    cont = 0
    for i in xy:
        if i in x:
            cont +=1
    return cont

def leervar_prim(param):
    return leerparams(param,var_seg)

def leervar_seg(param):
    return leerparams(param,var_prim)

def leervar_tir(param):
    return leerparams(param,var_ter)

def leervar_curt(param):
    while(param != 'a' and param != 'A' and param != 'B' and param != 'b'):
        param = input('Favor de ingresar de nuevo el dato por favor: ')
    return param

def leervar_quint(param):
    while(param != 'y' and param != 'Y' and param != 'N' and param != 'n'):
        param = input('Favor de ingresar de nuevo el dato por favor: ')
    return param

def recorr(param, lect):
    cont = 0
    for i in param:
        if i == lect:
            cont += 1
    return cont

def recorr_un(param):
    return recorr(param, '.' )

def evld_var(xy):
    while(leervar_prim(xy) > 0 or len(xy) == 0 or recorr_un(xy) > 1 or float(xy) == 0):
        xy = input('Favor de digitar su variable de nuevo: ')
    return float(xy)
    
def CalC_Cuad():
    x = input('Favor de digitar la coordenada en "X": ')
    x = evld_var(x) 
    
    y = input('Favor de digitar la coordenada en "Y": ')
    y = evld_var(y)
    
    if(x > 0 and y > 0):
        print('Su punto se encuentra en el cuadrante I')
    elif(x < 0 and y > 0):
        print('Su punto se encuentra en el cuadrante II')
    elif(x < 0 and y < 0):
        print('Su punto se encuentra en el cuadrante III')
    elif(x > 0 and y < 0):
        print('Su punto se encuentra en el cuadrante IV')

def CalC_Cuad_seg():
    x = input('Favor de digitar la coordenada en "X": ')
    x = evld_var(x)
    
    y = input('Favor de digitar la coordenada en "Y": ')
    y = evld_var(y)
    
    z = input('Favor de digitar la coordenada en "Z": ')
    z = evld_var(z)
    
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

answer_prim = input('\n Le gustaría saber del cuadrante de una coordenada dada (Y/N): ')
answer_prim = leervar_quint(answer_prim)

if(answer_prim == 'y' or answer_prim == 'Y' or len(answer_prim) == 0 or leervar_seg(answer_prim) > 0 or 'yy' in answer_prim or 'YY' in answer_prim or 'NN' in answer_prim or 'nn' in answer_prim):
    while(answer_prim == 'y' or answer_prim == 'Y' or len(answer_prim) == 0 or leervar_seg(answer_prim) > 0 or 'yy' in answer_prim or 'YY' in answer_prim or 'NN' in answer_prim or 'nn' in answer_prim):
            if(answer_prim == 'y' or answer_prim == 'Y'):
                print('''\n En que plano desea trabajar: 
a) Plano 2D
b) Plano 3D
                        ''')
                answer_seg = input('Digite su respuesta: ')
                answer_seg = leervar_curt(answer_seg)
                if(answer_seg == 'a' or answer_seg == 'A'):
                    CalC_Cuad()
                    answer_tir = input('Le gusto nuestro servicio: ')
                    answer_tir = leervar_quint(answer_tir)
                    if(answer_tir == 'y' or answer_tir == 'Y'):
                        cont += 1
                    elif(answer_tir == 'n' or answer_tir == 'N'):
                        cont_seg += 1
                    answer_prim = input('Desea volver a intentarlo (Y/N): ')
                    answer_prim = leervar_quint(answer_prim)
                elif(answer_seg == 'b' or answer_seg == 'B'):
                    CalC_Cuad_seg()
                    answer_tir = input('Le gusto nuestro servicio: ')
                    answer_tir = leervar_quint(answer_tir)
                    if(answer_tir == 'y' or answer_tir == 'Y'):
                        cont += 1
                    elif(answer_tir == 'n' or answer_tir == 'N'):
                        cont_seg += 1
                    answer_prim = input('Desea volver a intentarlo (Y/N): ')
                    answer_prim = leervar_quint(answer_prim)
            elif(len(answer_prim) == 0 or leervar_seg(answer_prim) > 0 or 'yy' in answer_prim or 'YY' in answer_prim or 'NN' in answer_prim or 'nn' in answer_prim):
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
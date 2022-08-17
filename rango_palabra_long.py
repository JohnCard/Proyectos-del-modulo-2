answer = input('Desea digitar algun mensaje (S/N): ')
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
    if(answer == 'n' or answer == 'N'):
        print('Entonces usted ya ha llegado al final del programa, gracias por su visita.')
        exit()

if(answer == 'n' or answer == 'N'):
    print('En ese caso usted ya ha llegado al final del programa, gracias.')
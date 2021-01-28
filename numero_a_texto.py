# -*- coding: utf-8 -*-

VALOR_MAXIMO = 999999999

unidades = {
    0: 'Cero',
    1: 'Uno',
    2: 'Dos',
    3: 'Tres',
    4: 'Cuatro',
    5: 'Cinco',
    6: 'Seis',
    7: 'Siete',
    8: 'Ocho',
    9: 'Nueve',
}

decenas = {
    10: 'Diez',
    11: 'Once',
    12: 'Doce',
    13: 'Trece',
    14: 'Catorce',
    15: 'Quince',
    16: 'Dieciséis',
    17: 'Diecisiete',
    18: 'Dieciocho',
    19: 'Diecinueve',
    20: 'Veinte',
    30: 'Treinta',
    40: 'Cuarenta',
    50: 'Cincuenta',
    60: 'Sesenta',
    70: 'Setenta',
    80: 'Ochenta',
    90: 'Noventa',
}

centenas = {
    100: 'Cien',
    200: 'Doscientos',
    300: 'Trescientos',
    400: 'Cuatrocientos',
    500: 'Quinientos',
    600: 'Seiscientos',
    700: 'Setecientos',
    800: 'Ochocientos',
    900: 'Novecientos',
}



def numero_a_texto(numero:int) -> str: 
    """ Retorna la representacion en letras de un numero entero positivo o negativo.  
        
        Parametros
        ----------
        numero: int

        Numero entero positivo o negativo entre -999999999 hasta 999999999

        Devuelve
        --------
        str: Representacion en letras del valor numerico.

    """
    entero = int(numero)
    
    assert entero <= VALOR_MAXIMO, f'El numero a convertir debe ser menor o igual a {MAX_VALUE}'
    
    if entero < 0:
        return f'Menos {numero_a_texto(abs(entero))}'

    if entero >= 0 and entero <= 9:
        return unidades_a_texto(entero)
    elif entero >= 10  and entero <= 99:
       return decenas_a_texto(entero)
    elif entero >= 100 and entero <= 999:
        return centenas_a_texto(entero)
    elif entero >= 1000 and entero <= 999999:
    	return miles_a_texto(entero)
    else:
    	return millones_a_texto(entero)

def unidades_a_texto(numero:int) -> str:
    """ Retorna la representacion en letras de un valor positivo entre 0 y 9 """
    return unidades[numero]

def decenas_a_texto(numero:int) -> str:
    """ Retorna la representacion en letras de un valor positivo entre 10 y 99 """
    if numero in decenas.keys():
        return decenas[numero]

    decena = numero // 10 * 10
    restante = numero - decena

    if decena == 20:
        return f'Veinti{numero_a_texto(restante).lower()}'
    else:
        return f'{decenas[decena]} y {numero_a_texto(restante).lower()}'

def centenas_a_texto(numero:int) -> str:
    """ Retorna la representacion en letras de un valor positivo entre 100 y 999 """
    if numero in centenas.keys():
        return centenas[numero]

    centena = numero // 100 * 100
    restante = numero - centena

    if centena == 100:
        return f'Ciento {numero_a_texto(restante).lower()}'
    else:
        return f'{centenas[centena]} {numero_a_texto(restante).lower()}'

def miles_a_texto(numero:int) -> str:
    """ Retorna la representacion en letras de un valor positivo entre 1000 y 999999 """
    millar = numero // 10 ** 3
    restante = numero - (millar * 10 ** 3)

    millar_texto = numero_a_texto(millar)
    
    if millar_texto.endswith(('Uno', 'uno')):
        millar_texto = 'Mil' if millar == 1 else millar_texto.replace('uno', 'un mil')
    else:
        millar_texto = millar_texto + ' mil'  

    if restante:
        return f'{millar_texto} {numero_a_texto(restante).lower()}'
    else:
        return millar_texto

def millones_a_texto(numero:int) -> str:
    """ Retorna la representacion en letras de un valor positivo entre 1000000 y 999999999 """
    millones = numero // 10 ** 6
    restante = numero - (millones * 10 ** 6)
    pos = 'millon' if millones == 1 else 'millones'

    millones_texto = numero_a_texto(millones)

    if millones_texto.endswith(('Uno', 'uno')):
        millones_texto = 'Un' if millones == 1 else millones_texto.replace('uno', 'un')

    millones_texto = f'{millones_texto} {pos}'

    if restante:
        return f'{millones_texto} {numero_a_texto(restante)}'
    else:
        return millones_texto


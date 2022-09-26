"""
Métodos de previsão da receita
"""

def media_indice(indice0, indice1, indice2, val_1, val_2, val_3, val_4, arred):
    media = (val_1 + val_2 + val_3 + val_4)/4
    val0 = media * (1 + indice0)
    val1 = val0 * (1 + indice1)
    val2 = val1 * (1 + indice2)
    return round(val0, arred), round(val1, arred), round(val2, arred)

def indice(indice0, indice1, indice2, val_1, arred):
    val0 = val_1 * (1+indice0)
    val1 = val0 * (1 + indice1)
    val2 = val1 * (1 + indice2)
    return round(val0, arred), round(val1, arred), round(val2, arred)

def crescimento(val_1, val_2, val_3, val_4, arred):
    var_1_2 = val_1 / val_2
    var_2_3 = val_2 / val_3
    var_3_4 = val_3 / val_4
    media = (var_2_3 + var_1_2 + var_3_4) / 3
    val0 = val_1 * media
    val1 = val0 * media
    val2 = val1 * media
    return round(val0, arred), round(val1, arred), round(val2, arred)

def media(val_1, val_2, val_3, val_4, arred):
    media = round((val_1 + val_2 + val_3 + val_4) / 4, arred)
    return media, media, media

def manual(val_0, val_1, val_2):
    return val_0, val_1, val_2
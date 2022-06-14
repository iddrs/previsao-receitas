"""
Métodos de previsão da receita
"""

def media_indice(indice0, indice1, indice2, val_1, val_2, val_3, val_4):
    media = (val_1 + val_2 + val_3 + val_4)/4
    val0 = media * (1 + indice0)
    val1 = val0 * (1 + indice1)
    val2 = val1 * (1 + indice2)
    return round(val0, 2), round(val1, 2), round(val2, 2)

def indice(indice0, indice1, indice2, val_1):
    val0 = val_1 * (1+indice0)
    val1 = val0 * (1 + indice1)
    val2 = val1 * (1 + indice2)
    return round(val0, 2), round(val1, 2), round(val2, 2)

def crescimento(val_1, val_2, val_3, val_4):
    var_1_2 = val_1 / val_2
    var_2_3 = val_2 / val_3
    var_3_4 = val_3 / val_4
    media = (var_2_3 + var_1_2 + var_3_4) / 3
    val0 = val_1 * media
    val1 = val0 * media
    val2 = val1 * media
    return round(val0, 2), round(val1, 2), round(val2, 2)

def media(val_1, val_2, val_3, val_4):
    media = round((val_1 + val_2 + val_3 + val_4) / 4, 2)
    return media, media, media
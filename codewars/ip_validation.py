def is_valid_IP(strng):

    lista, check = strng.split("."), 0

    if ' ' in lista or not lista: return False 
    elif len(lista) == 4:
        for k in lista:
            if k.startswith('0') and len(k) > 1: return False
            elif k.isdecimal() and int(k) <= 255 and int(k) >= 0: continue
            else: return False
        return True
    else: return False


print(is_valid_IP("134.123.234.025"))

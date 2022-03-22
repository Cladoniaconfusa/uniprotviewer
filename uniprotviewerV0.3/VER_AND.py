def verificar_and(memory:list,queries:list)->bool:
    cnt = len(queries)
    for termino in queries:
        value_to_match,campo = termino.split(".in.")
        for line in memory:
            campo_bd = line[:2]
            value_bd = line[2:].strip()
            if campo == campo_bd and value_to_match in value_bd :
                cnt -=1
                break
    return(cnt == 0)
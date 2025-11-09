def fun_teste(nome, idade, bonito = True, emprego = "Progamador"):
    print(f"Meu nome é {nome}, tenho {idade}, sou bem bonito? {"Sim" if bonito else "Não"}. Trabalho como {emprego}.")

fun_teste("Carlos", 27)
fun_teste("Mario", 46, False, "Bixeiro")
fun_teste("Felipe", 46, emprego="Desempregado", bonito=False)
mes = ["0","jan.","fev.","mar.","abr.","mai.","jun.","jul.","ago.","set.","out.","nov.","dez."]
ano = 2022
tipo = int(input("=========================\n\n[1] Jornal com Autor\n[2] Jornal sem Autor\n[3] Site com Autor\n[4] Site sem Autor.\n[5] Livro com 1 autor.\n[6] Livro com 2 autores.\n[7] Livro com 3 autores.\n[8] Livro com mais de 3 autores.\n[9] Livro com autor anonimo.\n\nDigite uma opção: "))

while tipo >=0 and tipo <=9:
	if tipo == 1:
		cautor_last = input("SOBRENOME: ").upper()
		cautor_name = input("Nome: ")
		cautor_title = input("Nome do Jornal: ")
		cautor_city = input ("Cidade de publicação: ")
		cautor_date = input("Dia de publicação: ")
		cautor_datem = int(input("Mês de publicação: "))
		cautor_datey = input("Ano de publicação: ")
		cautor_section = input("Seção (se houver): ")
		cautor_site = input("Disponível em: ")
		cautor_access = input("Acesso em (dia): ")
		cautor_accessm = int(input("Acesso em (mês): "))
		print("==================================\n\n" + cautor_last + ", " + cautor_name + ". " + cautor_title + ", " + cautor_city + ", " + cautor_date + " de  " + mes[cautor_datem] + " de " + cautor_datey + ". " + cautor_section + ". Disponível em:  " + cautor_site + ". Acesso em: " + cautor_access + " de " + mes[cautor_accessm] + "de " + str(ano) + ".\n\n")
	elif tipo == 2:
		sautor_title = input("Titulo da matéria: ").upper()
		sautor_name = input ("Nome do Jornal: ")
		sautor_city = input ("Cidade de publicação: ")
		sautor_date = input("Dia de publicação: ")
		sautor_datem = int(input("Mês de publicação: "))
		sautor_datey = input("Ano de publicação: ")
		sautor_section = input("Seção (se houver): ")
		sautor_site = input("Disponível em: ")
		sautor_access = input("Acesso em (dia): ")
		sautor_accessm = int(input("Acesso em (mês): "))
		print("==================================\n\n" + sautor_title + ". " + sautor_name + ", " + sautor_city + ", " + sautor_date + " de " + mes[sautor_datem] + " de " + sautor_datey + ". " +  sautor_section + ". Disponível em: " + sautor_site + ". Acesso em: " + sautor_access + " de " + mes[sautor_accessm] + " de " + str(ano) + ".\n\n")
	elif tipo == 3:
		cautor_last = input("SOBRENOME: ").upper()
		cautor_name = input("Nome: ")
		cautor_title = input("Titulo da matéria: ")
		cautor_sname = input ("Nome do site: ")
		cautor_year = input("Ano de publicação: ")
		cautor_site = input("Disponível em: ")
		cautor_access = input("Acesso em (dia): ")
		cautor_accessm = int(input("Acesso em (mês): "))
		print("==================================\n\n" + cautor_last + ", " + cautor_name + ". " + cautor_title + ". " + cautor_sname + ", " + cautor_year + ". Disponível em: " + cautor_site + ". Acesso em: " + cautor_access + " de " + mes[cautor_accessm] + " de " + str(ano) + ".\n\n")
	elif tipo == 4:
		sautor_title = input("Titulo da matéria: ").upper()
		sautor_sname = input ("Nome do site: ")
		sautor_year = input("Ano de publicação: ")
		sautor_site = input("Disponível em: ")
		sautor_access = input("Acesso em (dia): ")
		sautor_accessm = int(input("Acesso em (mês): "))
		print("==================================\n\n" + sautor_title + ". " + sautor_sname + ", " + sautor_year + ". Disponível em: " + sautor_site + ". Acesso em: " + sautor_access + " de " + mes[sautor_accessm] + " de " + str(ano) + ".\n\n")
	elif tipo == 5:
		cautor_last = input("SOBRENOME: ").upper()
		cautor_name = input("Nome em sigla (A. B): ")
		cautor_title = input("Titulo (negrito): subtitulo (se houver): ")
		cautor_edition = input("Edição (2+): ")
		cautor_city = input("Local de publicação: editora: ")
		cautor_ano = input("Ano de publicação: ")
		print("==================================\n\n" + cautor_last + ", " + cautor_name + ". " + cautor_title + ". " + cautor_edition + ". ed. " + cautor_city + ", " + cautor_ano + ".\n\n")
	elif tipo == 6:
		cautor_last1 = input("SOBRENOME: ").upper()
		cautor_name1 = input("Nome em sigla (A. B.): ")
		cautor_last2 = input("SOBRENOME: ").upper()
		cautor_name2 = input("Nome em sigla (A. B): ")
		cautor_title = input("Titulo (negrito): subtitulo (se houver): ")
		cautor_edition = input("Edição (2+.): ")
		cautor_city = input("Local de publicação: editora: ")
		cautor_ano = input("Ano de publicação: ")
		print("==================================\n\n" + cautor_last1 + ", " + cautor_name1 + "; " + cautor_last2 + ", " + cautor_name2 + ". " + cautor_title + ". " + cautor_edition + ". ed. " + cautor_city + ", " + cautor_ano + ".\n\n")
	elif tipo == 7:
		cautor_last1 = input("SOBRENOME: ").upper()
		cautor_name1 = input("Nome em sigla (A. B.): ")
		cautor_last2 = input("SOBRENOME: ").upper()
		cautor_name2 = input("Nome em sigla (A. B.): ")
		cautor_last3 = input("SOBRENOME: ").upper()
		cautor_name3 = input("Nome em sigla (A. B): ")
		cautor_title = input("Titulo (negrito): subtitulo (se houver): ")
		cautor_edition = input("Edição (2+.): ")
		cautor_city = input("Local de publicação: editora: ")
		cautor_ano = input("Ano de publicação: ")
		print("==================================\n\n" + cautor_last1 + ", " + cautor_name1 + "; " + cautor_last2 + ", " + cautor_name2 + "; " + cautor_last3 + ", " + cautor_name3 + ". " + cautor_title + ". " + cautor_edition + ". ed. " + cautor_city + ", " + cautor_ano + ".\n\n")
	elif tipo == 8:
		cautor_last = input("SOBRENOME: ").upper()
		cautor_name = input("Nome em sigla (A. B.): ")
		cautor_title = input("Titulo (negrito): subtitulo (se houver): ")
		cautor_edition = input("Edição (2+): ")
		cautor_city = input("Local de publicação: editora: ")
		cautor_ano = input("Ano de publicação: ")
		print("==================================\n\n" + cautor_last + ", " + cautor_name + " et al. " + cautor_title + ". " + cautor_edition + ". ed. " + cautor_city + ", " + cautor_ano + ".\n\n")
	elif tipo == 9:
		sautor_title = input("Titulo: ").upper()
		sautor_city = input("Local de publição: editora: ")
		sautor_ano = input("Ano de publicação: ")
		print("==================================\n\n" + sautor_title + ". " + sautor_city + ", " + sautor_ano + ".\n\n")
	tipo = int(input("=========================\n\n[1] Jornal com Autor\n[2] Jornal sem Autor\n[3] Site com Autor\n[4] Site sem Autor.\n[5] Livro com 1 autor.\n[6] Livro com 2 autores.\n[7] Livro com 3 autores.\n[8] Livro com mais de 3 autores.\n[9] Livro com autor anonimo.\n\nDigite uma opção: "))

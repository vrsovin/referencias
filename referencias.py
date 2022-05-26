tipo = input("=========================\n\nJornal: J\nSite: S\nDigite uma opção: ").upper()
mes = ["0","Jan.","Fev.","Mar.","Abr.","Mai.","Jun.","Jul.","Ago.","Set.","Out.","Nov.","Dez."]
ano = 2022

if tipo == "J":  
   autor = input("Com ou sem autor?\n Resposta [Y/N]: ").upper()
   if autor == "Y":
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
   elif autor == "N":
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
   else:
      print("saas")
elif tipo == "S":
   autor = input("Com ou sem autor?\n Resposta [Y/N]: ").upper()
   if autor == "Y":
      cautor_last = input("SOBRENOME: ").upper()
      cautor_name = input("Nome: ")
      cautor_title = input("Titulo da matéria: ")
      cautor_sname = input ("Nome do site: ")
      cautor_year = input("Ano de publicação: ")
      cautor_site = input("Disponível em: ")
      cautor_access = input("Acesso em (dia): ")
      cautor_accessm = int(input("Acesso em (mês): "))
      print("==================================\n\n" + cautor_last + ", " + cautor_name + ". " + cautor_title + ". " + cautor_sname + ", " + cautor_year + ". Disponível em: " + cautor_site + ". Acesso em: " + cautor_access + " de " + mes[cautor_accessm] + " de " + str(ano) + ".\n\n")
   elif autor == "N":
      sautor_title = input("Titulo da matéria: ").upper()
      sautor_sname = input ("Nome do site: ")
      sautor_year = input("Ano de publicação: ")
      sautor_site = input("Disponível em: ")
      sautor_access = input("Acesso em (dia): ")
      sautor_accessm = int(input("Acesso em (mês): "))
      print("==================================\n\n" + sautor_title + ". " + sautor_sname + ", " + sautor_year + ". Disponível em: " + sautor_site + ". Acesso em: " + sautor_access + " de " + mes[sautor_accessm] + " de " + str(ano) + ".\n\n")
   else:
      print("saas")

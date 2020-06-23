from pet import Pet
from costumer import Costumer
import json
import os
users = {}
opx = 99
p=Pet(namepet="",owner="",race="")
c=Costumer(nameclient="",address="",phone="",registered_by="")

while opx != 0:
    try:
        print("SISTEMA DE CONTROLE - PETIKÃO\n[1] - FAZER LOGIN\n[2] - CADASTRAR USUÁRIO\n[0] - FINALIZAR O PROGRAMA")
        opx = int(input("Escolha uma opção: "))
        if opx ==1:
            opy = 9
            try:
                login = input("Digite o nome do usuário:  ")
                password = input("Digite a senha:  ")
                if os.path.isfile("users.json"): 
                    l =open("users.json", "r")
                    data =json.load(l)
                    if login in data :
                        if data[login] == password:
                             while opy !=0:    
                                try:
                               
                                    print("SISTEMA DE CONTROLE - PETIKÃO\n[1] - CADASTRAR CLIENTE\n[2] - CADASTRAR PET\n[3] - INFORMAÇÃO DE CLIENTE\n[4] - INFORMAÇÃO DE PET\n[0] - RETORNAR AO MENU INICIAL")
                                    opy = int(input("Escolha uma opção: "))
                                    if opy ==1:
                                    
                                        if os.path.isfile("costumers.json"): # caso já exista o arquivo
                                            j = open("costumers.json", "r")
                                            datacos = json.load(j)
                                            j.close()  
                                            nameclient = input("Digite o nome do cliente:  ")
                                            address = input("Digite o endereço:  ")
                                            phone = input("Digite o telefone:  ")
                                            registered_by = login
                                            c=Costumer(nameclient,address,phone,registered_by)
                                            c.save_in_file(c.nameclient,c.address,c.phone,c.registered_by)
                                        else:
                                            nameclient = input("Digite o nome do cliente:  ")
                                            address = input("Digite o endereço:  ")
                                            phone = input("Digite o telefone:  ")
                                            registered_by = login
                                            c=Costumer(nameclient,address,phone,registered_by)
                                            c.save_in_file(nameclient,address,phone,registered_by)

                                    if opy ==2:
                                        if os.path.isfile("pets.json"): # caso já exista o arquivo
                                            l = open("pets.json", "r")
                                            datapet = json.load(l)
                                            l.close()
                                            namepet = input("Digite o nome do seu animal:  ")
                                            owner=  input("Digite o nome do dono:  ")
                                            race = input("Digite a raça:  ")
                                            consultclient =open("costumers.json", "r")
                                            dataclient =json.load(consultclient)
                                            
                                            if owner in dataclient :
                                                p=Pet(namepet,owner,race)
                                                p.save_in_file(p.namepet,p.owner,p.race)
                                            else:
                                                print("cliente nao encontrado")
                                        else:
                                            namepet = input("Digite o nome do seu animal:  ")
                                            owner=  input("Digite o nome do dono:  ")
                                            race = input("Digite a raça:  ")
                                            consultclient =open("costumers.json", "r")
                                            dataclient =json.load(consultclient)
                                            p=Pet(namepet,owner,race)
                                            if os.path.isfile("pets.json") :
                                                if owner in dataclient:
                                                    p.save_in_file(p.namepet,p.owner,p.race)
                                                else:
                                                    print("Dono não encontrado")
                                            else:
                                                if owner in dataclient:
                                                    p.save_in_file(p.namepet,p.owner,p.race)
                                                else:
                                                    print("Dono não encontrado")
                                            
                                            
                                    if opy ==3:
                                        nameclient = input("Digite o nome do cliente:  ")
                                        c.Show_info(c.nameclient)
                                    if opy ==4:
                                        namepet = input("Digite o nome do pet:  ")
                                    
                                        p.Show_info(namepet)
                                except ValueError:
                                    print("opção invalida")
                        else :
                            print('login incorreto')
                    else:
                        print('login nao encontrado!')
                else:
                    print("Login invalido")
            except ValueError:
                print("opção invalida")

        elif opx == 2:
            if os.path.isfile("users.json"): # caso já exista o arquivo
                f = open("users.json", "r")
                data = json.load(f)
                f.close()
                #print (data)
                h = open("max_users.json", "r")
                number_users = json.load(h)
                h.close()
                if number_users["number_users"] == "2":
                    print("Não é possível cadastrar mais do que 2 users")
                else:
                    login = input("Digite o nome do usuário:  ")
                    password = input("Digite a senha:  ")
                    users[login] = password
                    if login in data: # caso já exista um usuário com esse nome
                        print("usuário já cadastrado")
                    else:
                        data[login] = password
                        f = open("users.json", "w")
                        json.dump(data, f)
                        f.close()
                        h = open("max_users.json","w")
                        number_users = {"number_users": "2"}
                        json.dump(number_users,h)
                        h.close
            else: # Criar arquivo, caso não exista
                login = input("Digite o nome do usuário:  ")
                password = input("Digite a senha:  ")
                
                users[login] = password
                f = open("users.json","w") # w = write = escrita
                json.dump(users, f)
                f.close()
                h = open("max_users.json","w")
                number_users = {"number_users": "1"}
                json.dump(number_users,h)
                h.close
    except ValueError:
        print("opção invalida")
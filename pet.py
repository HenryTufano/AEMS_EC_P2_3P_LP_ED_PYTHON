import os
import json
pets = {}
class Pet(object):
    def __init__(self,owner,namepet,race):
      self.namepet=namepet
      self.owner=owner
      self.race=race
      
    
    def Show_info(self,namepet):
        if os.path.isfile("pets.json"):
            l = open("pets.json", "r")
            datapet = json.load(l)
            l.close()  
            if namepet in datapet:                
                print(datapet[namepet])
            else:
                print("Dados não encontrado")
                
        else:
            print("Dados não encontrado")

    def show_owner_info(self,owner):
        if os.path.isfile("costumers.json") and os.path.isfile("pets.json"):
            cl = open("costumers.json", "r")
            datacliente = json.load(cl)
            cl.close()  
            if owner in datacliente:
                retorno = True
            else:
                retorno = False
        else:
                retorno = False
        return retorno
    
    def save_in_file(self,namepet,owner,race):
        if os.path.isfile("pets.json"): # caso já exista o arquivo
            l = open("pets.json", "r")
            datapet = json.load(l)
            l.close()  
        
            if namepet in datapet: # caso já exista um usuário com esse nome
                print("pet já cadastrado")
            else:
                pets[namepet] = {'namepet':namepet,'race': race, 'owner':owner}
                l = open("pets.json", "w")
                json.dump(pets, l)
                l.close()

            
        else: # Criar arquivo, caso não exista
            pets[namepet] = {'namepet':namepet,'race': race, 'owner':owner}
            l = open("pets.json","w") # w = write = escrita
            json.dump(pets, l)
            l.close()
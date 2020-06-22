import json
import os
costumers = {}
class Costumer(object):
    def __init__(self,nameclient,address,phone,registered_by):
        self.nameclient=nameclient
        self.address=address
        self.phone=phone
        self.registered_by=registered_by  
    def Show_info(self,nameclient):
        consultacliente =open("costumers.json", "r")
        datacliente =json.load(consultacliente)
        if nameclient in datacliente :
            print (datacliente[nameclient])
    
    def save_in_file(self,nameclient,address,phone,registered_by):
        if os.path.isfile("costumers.json"): # caso já exista o arquivo
            j = open("costumers.json", "r")
            datacos = json.load(j)
            j.close()  
            
            
            if nameclient in datacos: # caso já exista um usuário com esse nome
                print("Cliente já cadastrado")
            else:
                costumers[nameclient] = {'nameclient':nameclient,'address': address,'phone' : phone,'registered_by' : registered_by}
                j = open("costumers.json", "w")
                json.dump(costumers, j)
                j.close()
        else: # Criar arquivo, caso não exista
            
           
            costumers[nameclient] = {'nameclient':nameclient,'address': address,'phone' : phone,'registered_by' : registered_by}
            j = open("costumers.json","w") # w = write = escrita
            json.dump(costumers, j)
            j.close()
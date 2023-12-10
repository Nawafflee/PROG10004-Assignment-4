

"""
https://github.com/Nawafflee/PROG10004-Assignment-4
"""

#Resource module
class Resource:
    #Constructor to initialize an object blueprint for a Watercraft Inventory CRUD system for a Dealership
    #Based on name, manufacturer(company name manufacturing the Watercraft), country of manufacture,price MSRP
    def __init__(self,id,name,manufacturer,country,price):
        self.id = id
        self.name = name
        self.manufacturer = manufacturer
        self.country = country
        self.price = price

    #Method converts Watercraft item to Dictionary
    def getDictionary(self):
        return {"id" : self.id, 
                "name" : self.name, 
                "manufacturer" : self.manufacturer, 
                "country" : self.country,
                "price" : self.price}
"""
#Test Cases 
#create object instance 
resource1 = Resource(101,"Seadoo RXT X 400","Seadoo","Canada",49_580)
print(resource1.getDictionary())
"""


#Data Persistence
class DataPersistence:
    pass


#Resource Managment 
class ResourceManager:
    def __init__(self):
        self.resources = []




#UI Interface
class UserInteraction:
    pass
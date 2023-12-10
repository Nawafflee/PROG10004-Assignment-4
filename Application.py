
import csv 
import os
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
    #Loads the data from a CSV file into a list of dictionaries
    @staticmethod
    def load_data():
        data = []
        if os.path.exists("Watercraft_Data.csv"):
            with open("Watercraft_Data.csv","r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    craft_data = {key : row[key] for key in row}
                    data.append(craft_data)
        return data
    
    #Saves the data to a CSV file
    @staticmethod
    def save_data(data):
        with open("Watercraft_Data.csv","w", newline="") as file:
            fields = ["id","name","manufacturer","country","price"]
            writer = csv.DictWriter(file, fieldnames = fields)
            writer.writeheader()
            for item in data:
                writer.writerow(item.getDictionary()) #Converts Watercraft to dictionary


#Resource Management 
class ResourceManager:

    def __init__(self):
        self.resources = []

    # Creates a new Watercraft item and add it to the resources list
    def create_resource(self,key_attributes):
        resource_creation = Resource(key_attributes["id"],
                                     key_attributes["name"],
                                     key_attributes["manufacturer"],
                                     key_attributes["country"],
                                     key_attributes["price"])

        self.resources.append(resource_creation)

    def search_resource(self, key_attribute, non_key_attribute):
        # Convert the non_key_attribute to lowercase and remove any leading/trailing whitespaces
        non_key_attribute = str(non_key_attribute).strip().lower()

        # Initialize an empty list to store the matching resources
        result = []

        # Iterates through each resource in the list
        for resource in self.resources:
            # Gets the value of the specified key_attribute for the current resource
            resource_value = getattr(resource, key_attribute, None)

            # Checks if the resource_value matches the non_key_attribute (case-insensitive)
            if resource_value is not None and str(resource_value).strip().lower() == non_key_attribute:
                # If there's a match, add the resource details to the result list
                result.append({
                    "id" : resource.id,
                    "name" : resource.name,
                    "manufacturer" : resource.manufacturer,
                    "country" : resource.country,
                    "price" : resource.price
                })

        # Returns the list of matching resources
        return result

    # Edit Watercraft details
    def edit_resource(self,unique_characteristic,new_attributes):
        for resource in self.resources:
            if str(getattr(resource, "id")) == unique_characteristic:
                for key, value in new_attributes.items():
                    setattr(resource,key,value)

    #Delete Watercraft details
    def delete_resource(self,unique_characteristic):
        original_count = len(self.resources)

        #create a new list
        updated_resources = []
        deleted_item_found = False

        for resource in self.resources:
            if str(getattr(resource, "id")) == unique_characteristic:
                deleted_item_found = True
            else:
                updated_resources.append(resource)
        
        #update the resources list 

        self.resources = updated_resources

        new_count = len(self.resources)

        if deleted_item_found:
            print("Watercraft with ID {} has been successfully deleted".format(unique_characteristic))
        else:
            print("No Watercraft Resource has been found with ID {}".format(unique_characteristic))    


#UI Interface
class UserInteraction:
    pass
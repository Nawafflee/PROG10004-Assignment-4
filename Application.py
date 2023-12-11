
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
        
        #updates the resources list 
        self.resources = updated_resources

        new_count = len(self.resources)

        if deleted_item_found:
            print("Watercraft with ID {} has been successfully deleted".format(unique_characteristic))
        else:
            print("No Watercraft Resource has been found with ID {}".format(unique_characteristic))    


#UI Interface
class UserInteraction:
    #Display the Menu Options
    @staticmethod
    def show_menu():

        print("\tWelcome to the Watercraft Inventory CRUD System: ")
        print("What would you like to do?")
        print("1. Add Watercraft to Inventory")
        print("2. Search for a Watercraft in Inventory")
        print("3. Edit Watercraft in Inventory")
        print("4. Delete Watercraft from inventory")
        print("5. Exit CRUD System")

    #Obtain User Input
    @staticmethod
    def user_choice():
        try:
            choice = int(input("Please Enter your choice from the Main Menu: "))
            return choice
        except ValueError:
            print("Invalid Input. Please Enter an integer number")

    #Get an attribute for a new watercraft 
    @staticmethod
    def get_resource_attributes():

        id = input("Enter ID: ")
        name = input("Enter Watercraft Name: ")
        manufacturer = input("Enter Watercraft Manufacturer: ")
        country = input("Enter Country of Manufacture: ")
        price = input("Enter Price in $CAD MSRP: ")

        return {"id" : id,
                "name" : name,
                "manufacturer" : manufacturer,
                "country" : country,
                "price": price}

    #Displays the list containing the watercraft details
    @staticmethod
    def display_resources(resources):
        if not resources:
            print("No matching Watercraft can be found!")
        for resource in resources:
            print("id : {} | name : {} | manufacturer : {} | country : {} | price : {}".format(resource["id"],
                                                                                            resource["name"],
                                                                                            resource["manufacturer"],
                                                                                            resource["country"],
                                                                                            resource["price"]))

#Object Instances Intialization
ui = UserInteraction()
watercraft_resource_manager = ResourceManager()
data_persistance = DataPersistence()

#Load existing Data
existing_data = data_persistance.load_data()
watercraft_resource_manager.resources = [Resource(**item) for item in existing_data]

#User interaction loop
while True:
    ui.show_menu()
    choice = ui.user_choice()

    if choice == 1:
        attributes = ui.get_resource_attributes()
        watercraft_resource_manager.create_resource(attributes)
        print("Successfully added a New Watercraft to Inventory!")

    elif choice == 2:
        key_attribute = input("Enter Key Attribute (e.g, id): ")
        non_key_attribute = input("Enter {} value to search: ".format(key_attribute))
        result = watercraft_resource_manager.search_resource(key_attribute,non_key_attribute)
        ui.display_resources(result)
    
    elif choice == 3:
        unique_characteristic = input("Enter Unique Value (e.g, ID Value) to update: ")
        new_attributes = ui.get_resource_attributes()
        watercraft_resource_manager.edit_resource(unique_characteristic,new_attributes)
    
    elif choice == 4:
        unique_characteristic = input("Enter Unique Value (e.g., ID Value) to delete: ")
        watercraft_resource_manager.delete_resource(unique_characteristic)

    elif choice == 5:
        break #exits the UI 

#Data Saving Before Exiting 
data_persistance.save_data(watercraft_resource_manager.resources)
print("Terminated Gracefully. Now Exiting Program...")



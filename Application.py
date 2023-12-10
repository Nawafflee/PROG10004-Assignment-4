

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


#UI Interface
class UserInteraction:
    pass
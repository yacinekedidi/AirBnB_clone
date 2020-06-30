![](https://github.com/yacinekedidi/AirBnB_clone/blob/master/pictures/hbnb.png?raw=true)
# AirBnB_clone
##Description:
AirBnB_clone is a project emulating the airbnb website it's still at the early stages of developement as it only implements the back end console and the models/classes to be stored later on on a database and represented on a front end interface, 
at its last stage it's expected to be a complete web application that clones the airbnb website

##Models/Classes:
|  classes | description  | attributes   |
| ------------ | ------------ | ------------ |
|  BaseModel  | this is the parent of all the other classes    | id, created_at, updated_at  |
|  FIleStorage | serializes instances to a JSON file and deserializes JSON file to instances  | \__objects,  __file_path   |
| HBNBCommand   | contains the entry point of the command interpreter   | prompt, classes  |
| User  | contains user information | email, password, first_name, last_name  |
|  State |  contains state information  |  name |
|  City |  contains city information  | state_id, name  |
|  Amenity | contains amenity information  |  name |
| Review | contains review information |  place_id, user_id, text |
| Place | contains place information | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |

#storage:
an object of the FileStorage class that reloads the FileStorage attribute __objects by seriliazing the JSON file into objects 

#How to start and use:
|  command | description   |
| ------------ | ------------ |
|      ./console.py |  enter the console by typing that on the command line |
|  (hbnb ) quit | enter to leave the console  |
|  (hbnb ) help  | to display help for a, list of suggested commands  |
| (hbnb ) EOF   | another way of exiting the console program  |
|  (hbnb ) create class_name  |  creates an instance of the entered class |
|  (hbnb ) show class_name instance_id | prints the instance with the enetered id   |
| (hbnb ) all [class_name]  | without option shows all the existing instances otherwise show the instance of the entered class  |
| (hbnb ) destroy class_name instance_id | deletes the instance with that id |
| (hbnb ) update class_name instance_id attribute_name attribute_value | changes the value of the mentioned attribute corresponding to the inputed class and instance id |
| (hbnb ) class_name.all() | another way to check the instances for a given class |
| (hbnb ) class_name.count() | prints the number of instances for a particular class |
| (hbnb ) class_name.show(instance_id) | shows the instance with given id and class |
| (hbnb ) class_name.destroy(instance_id) | deletes the instance with the given id and class |

#examples:
![](https://github.com/yacinekedidi/AirBnB_clone/blob/master/pictures/example.png?raw=true)
![](https://github.com/yacinekedidi/AirBnB_clone/blob/master/pictures/example_advanced.png?raw=true)
![](https://github.com/yacinekedidi/AirBnB_clone/blob/master/pictures/example_advanced_2.png?raw=true)
![](https://github.com/yacinekedidi/AirBnB_clone/blob/master/pictures/example_advanced_3.png?raw=true)

#Release Date
30 June 2020 
-- Still working on other features

#Authors 
Yacine Kedidi [GITHUB](https://github.com/yacinekedidi "GITHUB")
Taïb Kefi [GITHUB](https://github.com/kefitaib "GITHUB")
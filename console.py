#!/usr/bin/python3
"""Module



"""
import cmd
import models
import re
import shlex
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    cl
    """
    prompt = '(hbnb) '
    classes = ["BaseModel",
               "User", "City", "Amenity", "Place", "Review", "State"]

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """executes nothing
        """
        pass

    def default(self, inp):
        """func
        """
        x = inp.split(".")
        if x[1] == "all()" and x[0] in HBNBCommand.classes:
            return self.do_all(x[0])
        if x[1] == "count()" and x[0] in HBNBCommand.classes:
            a = 0
            for k, v in models.storage.all().items():
                if v.__class__.__name__ == x[0]:
                    a += 1
            print(a)
            return
        g = re.match(r"show(?P<id>.*)", x[1])
        if g and x[0] in HBNBCommand.classes:
            a = g.group("id")[1:-1]
            if len(a) != 0:
                if a[0] == '"' and \
                   a[-1] == '"' or (a[0] == "'" and a[-1] == "'"):
                    a = a[1:-1]
                return self.do_show(x[0] + " " + a)

        g = re.match(r"destroy(?P<id>.*)", x[1])
        if g and x[0] in HBNBCommand.classes:
            a = g.group("id")[1:-1]
            if len(a) != 0:
                if a[0] == '"' and a[-1] == '"' or \
                   (a[0] == "'" and a[-1] == "'"):
                    a = a[1:-1]
                return self.do_destroy(x[0] + " " + a)

        if re.match(r".*{.*}.*", x[1]):
            g = re.match(r"update((?P<id>.*) (?P<dic>.*))", x[1])
            if g and x[0] in HBNBCommand.classes:
                a = g.group("id")[2:] + " " + g.group(3)[:-1]
                a = a.split("{")
                b = a[1].split(",")
                dict_arg = {}
                kk = ""
                b[len(b)-1] = b[len(b)-1][:-1]
                for i in b:
                    i = i.split(":")
                    dict_arg[i[0].strip()[1:-1]] = i[1].strip()[1:-1]

                for k, v in dict_arg.items():
                    self.do_update(x[0] + " " + a[0][:-3] + " " + k + " " + v)

        else:
            g = re.match(r"update((.*), (.*), (.*))", x[1])
            if g and x[0] in HBNBCommand.classes:
                a = g.group(2)[2:-1] + " " + \
                    g.group(3)[1:-1] + " " + g.group(4)[:-1]
                return self.do_update(x[0] + " " + a)

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                a = models.base_model.BaseModel()
            elif line == "User":
                a = User()
            elif line == "City":
                a = City()
            elif line == "Amenity":
                a = Amenity()
            elif line == "Place":
                a = Place()
            elif line == "Review":
                a = Review()
            elif line == "State":
                a = State()
            a.save()
            print(a.id)

    def do_show(self, line):
        """ show """

        if line == "":
            print("** class name missing **")

        else:
            l = shlex.split(line)
            if l[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")

            elif len(l) == 1:
                print("** instance id missing **")

            else:
                models.storage.reload()
                d = models.storage.all()
                if l[0] + '.' + l[1] in list(d.keys()):
                        print(d[l[0] + '.' + l[1]])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """ show """

        if line == "":
            print("** class name missing **")

        else:
            l = shlex.split(line)
            if l[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")

            elif len(l) == 1:
                print("** instance id missing **")

            else:
                models.storage.reload()
                d = models.storage.all()
                if l[0] + '.' + l[1] in list(d.keys()):
                    del d[l[0] + '.' + l[1]]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """ show """

        res = []
        models.storage.reload()
        d = models.storage.all()
        l = shlex.split(line)
        if len(l) == 0 or (len(l) == 1 and l[0] in HBNBCommand.classes):
            for k in list(d.keys()):
                if line == "":
                    res.append(str(d[k]))
                else:
                    if l[0] in k:
                        res.append(str(d[k]))
            print(res)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ show """

        if line == "":
            print("** class name missing **")

        else:
            l = shlex.split(line)
            if l[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")

            elif len(l) == 1:
                print("** instance id missing **")

            else:
                models.storage.reload()
                d = models.storage.all()
                if l[0] + '.' + l[1] not in list(d.keys()):
                    print("** no instance found **")

                elif len(l) == 2:
                    print("** attribute name missing **")

                elif len(l) == 3:
                    print("** value missing **")

                else:
                    s = l[3]
                    x = d[l[0] + '.' + l[1]]
                    if (l[3][0] == '"' and l[3][len(l[3]) - 1] == '"') or \
                       (l[3][0] == "'" and l[3][len(l[3]) - 1] == "'"):
                        s = l[3][1:len(l[3]) - 1]
                    setattr(x, l[2], s)
                    d[l[0] + '.' + l[1]] = x
                    models.storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

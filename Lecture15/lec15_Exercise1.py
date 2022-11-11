def query():
    name = input("What is the name?\n\t")
    age = input("What is the age\n\t")
    color = input("What is your favorite color\n\t")
    python = input("Do you like python?\n\t")
    flatworld = input("The world is flat? True or False\n\t")
    return name, age, color, python, flatworld

name, age, color, python, flatworld = query()


def comment(name_in, age_in, color_in, python_in, flatworld_in):
    archive = {"name" : name_in, "age" : age_in, "color" : color_in, "python" : python_in, "flatworld" : flatworld_in}
    return archive

arc = comment(name, age, color, python, flatworld)
print(arc)
# Normal argument -
'''You have to pass 10 nubers of argument if you want to pass 10 number of parameter'''

def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)

function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

##############################################################################################

# *args -
'''You have to pass only *arg (arg is just an example name, can be passed any but * is mandatory) then you can pass any number of parameter.
Here you can pass only list, tuble but not disctonary'''

def function_name_print_args(*args):
    for item in args:
        print(item)

function_name_print_args("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

list = ["gvv", "jhh", "hjbbh"]
function_name_print_args(*list)

##############################################################################################

# **kwargs -
'''You have to pass only **kwarg (kwarg is just an example name, can be passed any but ** is mandatory) then you can pass any number of parameter.
Here you can pass only disctonary, not list of tuple'''

def function_name_print_kwargs(**kwargsbala):
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


dis = {"Harry" :"Rohan", "Skillf" : "Hammad"}
function_name_print_kwargs(**dis)

################################################################################################

# All together -
def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]

normal = "I am a normal Argument and the students are:"

kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}

funargs(normal, *har, **kw)

# limitation - At first have to pass normal, then single star, then double star
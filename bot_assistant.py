import re


CONTACTS={}
CALENDAR={}




def input_error(func): #decorator
    
    def wrapper(*args, **kwargs):
        try:
            result=func(*args, **kwargs)
        
        except (KeyError, ValueError, IndexError) as e:
            print(f"Input data caused the error: {e}.")
            result="----Not result.----"
        return result
    return wrapper

    


    
#@input_error
#--------------------------------------------------------
@input_error
def hello_handler():
    print("How can i help you?")
#--------------------------------------------------------
#@input_error
def exit_handler():
    print("Good bye!")
    exit()
#--------------------------------------------------------
#@input_error
def show_contacts_handler():
    counter=0
    for name, phone in CONTACTS.items():
        counter+=1
        print(f"{counter}. Contact:{name}, phone number: {phone}")
#--------------------------------------------------------
#@input_error
def add_contact_handler(name, phone):
    CONTACTS[" ".join(name)]="".join(phone)
    print("Contact added")
#--------------------------------------------------------
#@input_error
def change_handler(name, phone):
    if " ".join(name) in CONTACTS:
        CONTACTS[" ".join(name)]="".join(phone)
        print("Changed")
    else:
        print("This person not defined in your contacts.")
#--------------------------------------------------------
#@input_error
def phone_handler(name):
    if " ".join(name) in CONTACTS:
        print(CONTACTS[" ".join(name)])
    else:
        print("This person not defined in your contacts.")  
#-------------------------------------------------------- нужно указать после всех используемых функций

COMMANDS={

    "hello":hello_handler, 
    "add":add_contact_handler,
    "change":change_handler,
    "phone":phone_handler,
    "show all":show_contacts_handler,
    "good bye":exit_handler,
    "close":exit_handler,
    "exit":exit_handler,
    ".":exit_handler

    }

#--------------------------------------------------------
def command_parser(input_data):

    input_data=str(input_data.lower()) #register non-sensative

    name=[]
    phone=[]
        
    for key, value in COMMANDS.items():
        
        if input_data.startswith(key):

            if key in ["add", "change", "phone"]:

                particles_input_data= (input_data.removeprefix(key)).strip()
                particles_input_data=particles_input_data.split(" ")
                
                for i in  particles_input_data:

                    if re.search('[a-z]+', i):
                        name.append(i)
                        
                    elif re.search('[\+0-9]+', i):
                        phone.append(i)
     
                command=COMMANDS[key]  
                out_func=command(name, phone)
                
            elif key not in ["add", "change", "phone"]:
                   
                command=COMMANDS[key]
                out_func=command()

            return out_func

    if "out_func" not in locals(): #Проверяем находится ли доступная команда в инпут через конечный результат функции
        print("Command not definded ")


#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
def main():
    

    while True:

        input_variable= input("Please, input your command:")

        command_parser(input_variable)
        

if __name__ == '__main__':  
    exit(main())
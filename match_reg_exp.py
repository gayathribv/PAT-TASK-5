import re

#Validate
def validate_email_addr(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

# Validate Bangladesh mobile number
def validate_cell_no_Bangladesh(mobile_num):
    return (re.match(r'^88[ -]01[ -][0-9]{8}$', mobile_num)) is not None

#Validate mobile numbers of USA
def validate_cell_no_USA(mobile_num_US):
    pattern=re.compile("^001[ -](\d){3}[ -](\d){7}$")
    "return (re.match(r'^001[ -][1-9][0-9][0-9][ -][1-9][0-9][0-9][0-9][0-9][0-9][0-9]$', mobile_num_US)) is not None"
    return (re.match(pattern, mobile_num_US)) is not None

#Password validation
#16 Characters, lowercase, uppercase, numbers, special characters
def validate_password(passwd):
    if len(passwd) != 16:
        print("Password length should be 16 Characters")
        return False
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{16}$"
     
    # compiling regex
    pat = re.compile(reg)
     
    # searching regex
    mat = re.search(pat, passwd)
     
    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")

if __name__ == "__main__":
    
# Display Menu to Choose an option to Validate
    print("    MENU OF ITEMS FOR VALIDATION  ")
    print("----------------------------------")
    print("\#1. EMail ID")
    print("\#2. Mobile No. Bangaldesh")
    print("\#3. Mobile No. US")
    print("\#4. 16 Character Password")
    option=0
    while option != "Q":
        option=input("Enter Menu Option to Validate or Q to quit ")
        if option == "1":
            email=input("Enter email id:  ")
            if validate_email_addr(email):
                print(email, "is valid")
            else:
                print(email, "is not valid")

        elif option == "2":
            mobile_num=input("Enter a Bangladesh Mobile Number to validate:    ")
            if validate_cell_no_Bangladesh(mobile_num):
               print(mobile_num, "is a valid Bangladesh Mobile Number")
            else:
                print(mobile_num, "is not a valid Bangladesh Mobile Number")
                
        elif option == "3":
            mobile_num_US=input("Enter a USA's Mobile Number to validate:    ")
            if validate_cell_no_USA(mobile_num_US):
               print(mobile_num_US, "is a valid USA Mobile Number")
            else:
               print(mobile_num_US, "is not a valid USA Mobile Number")

        elif option == "4":
            passwd=input("Enter 16 character passwd to validate: ")
            validate_password(passwd)
        elif option == "Q":
            break
        else:
            continue

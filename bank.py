
#create class 
class BankApp:
    '''BankApp class to manage bank operations''' 

    global global_var  # global variable
    global_var= "Baking Application" 

    ifsc = 0 # class variable, similar to static variable in C#

    #Constructor
    def __init__(self,name,branch):
        BankApp.ifsc += 1
        '''Constructor to initialize the bank app'''
        self.name = name # instance variable
        self.branch = branch
        self.ifsc = f"TEST { BankApp.ifsc.__str__()}"  

    # Method to display the bank name
    def getDetails(self):
        '''Method to display information about the bank app'''
        details = f"Bank  Name: {self.name} Branch: {self.branch} IFSC: {self.ifsc}"
        return details


# print global variable 
print(global_var)

#print class variable # 1#
print("Bank IFC code", BankApp.ifsc) 

# create an instance of the class
bankApp = BankApp("TestBank","ABC") 
# print bank info, ex. accessing instance variable
print(bankApp.getDetails())

#create another instance of the class
bankApp2 = BankApp("TestBank2","XYZ")
# print bank info, ex. accessing instance variable
print(bankApp2.getDetails())

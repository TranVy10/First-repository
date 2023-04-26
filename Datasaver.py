import json
from tkinter import *

root = Tk()
root.configure(bg='white')
root.title('DataSaver')
# root.iconbitmap(r"C://Users//ADMIN//Desktop//VsCode//Data Saver//spa.ico")

def write_json(data, filename="storage.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

Email = Entry(root, width=50, bg='pink')
Email.insert(0,"")
Email_label = Label(root,text = "Email:" ,width = 20, bg='pink',borderwidth=-1)
Name = Entry(root, width=50, bg='pink')
Name.insert(0,"")
Name_label = Label(root,text="Name:",width = 20, bg='pink',borderwidth=-1)
PhoneNumber = Entry(root, width=50, bg='pink')
PhoneNumber.insert(0,"")
PhoneNumber_label = Label(root, text="Phone number:", width=20, bg='pink',borderwidth=-1)
Date_of_birth = Entry(root, width=50, bg='pink')
Date_of_birth.insert(0,"")
Date_of_birth_label = Label(root,text="Date of birth:",width=20, bg='pink', borderwidth=-1)
LabelPhoneNumandName = Label(root, text = 'Information', bg='white')

def ExistName(Exist_Name):
    with open("storage.json") as json_file:
        data = json.load(json_file)
    for person in data["Person"]:
        if person["Name"] == Exist_Name:
            return True
    return False

def ExistEmail(Exist_Email):
    with open("storage.json") as json_file:
        data = json.load(json_file)
    for person in data["Person"]:
        if person["Email"] == Exist_Email:
            return True
    return False

def ExistPhoneNumber(Exist_Phone_Number):
    with open("storage.json") as json_file:
        data = json.load(json_file)
    for person in data["Person"]:
        if person["Phone Number"] == Exist_Phone_Number:
            return True
    return False

def refresh():
    Email.delete(0, 'end')
    Name.delete(0, 'end')
    PhoneNumber.delete(0, 'end')
    Date_of_birth.delete(0,'end')

def DeleteSearch():
    LabelPhoneNumandName.grid_forget()

def StoreData():
    global LabelPhoneNumandName
    Email_get = Email.get()#input("Please input your email: ")
    Name_get = Name.get()#input("Please enter your name: ")
    PhoneNumber_get = PhoneNumber.get()#input("Please input your phone number: ")
    Date_of_birth_get = Date_of_birth.get()#input("Please input your date of birth(dd/mm/yy): ")
    if ExistName(Name_get) == True or ExistPhoneNumber(PhoneNumber_get) == True or ExistEmail(Email_get) == True:
        DeleteSearch()
        LabelPhoneNumandName = Label(text= "ERROR"+"\nDATA EXIST",bg='white')
        LabelPhoneNumandName.grid(column=1, row=4, rowspan=4)
    else:
        Email_get = Email.get()#input("Please input your email: ")
        Name_get = Name.get()#input("Please enter your name: ")
        PhoneNumber_get = PhoneNumber.get()#input("Please input your phone number: ")
        Date_of_birth_get = Date_of_birth.get()#input("Please input your date of birth(dd/mm/yy): ")
        with open("storage.json") as json_file:
            data = json.load(json_file)
            temp = data["Person"]
            y = {"Email": Email_get, "Name": Name_get, "Phone Number": PhoneNumber_get, "Date of Birth": Date_of_birth_get, "ID": len(temp)+1}
            temp.append(y)
        write_json(data)
    refresh()

def FindPhoneNumber():
    global LabelPhoneNumandName
    DeleteSearch()
    PhoneNumber_get = PhoneNumber.get()
    with open('storage.json') as read:
        data_is_read = json.load(read)
    for person in data_is_read['Person']:
        if person['Phone Number'] == PhoneNumber_get:
            LabelPhoneNumandName = Label(text="Email: " + person["Email"] + "\nName: " + person["Name"] + "\nPhone number: " + person["Phone Number"] +
            "\nDate Of Birth: " + person["Date of Birth"] + "\nID: " + str(person["ID"]),bg='white')
            LabelPhoneNumandName.grid(column=1, row=4, rowspan=4)
    refresh()

def FindName():
    global LabelPhoneNumandName
    DeleteSearch()
    Name_get = Name.get()
    with open('storage.json') as read:
        data_is_read = json.load(read)
    for person in data_is_read['Person']:
        if person['Name'] == Name_get:
            LabelPhoneNumandName = Label(text="Email: " + person["Email"] + "\nName: " + person["Name"] + "\nPhone number: " + person["Phone Number"] +
            "\nDate Of Birth: " + person["Date of Birth"] + "\nID: " + str(person["ID"]),bg='white')
            LabelPhoneNumandName.grid(column=1, row=4, rowspan=4)
    refresh()

Find_Phone_Number_Button = Button(root, text = "Find Phone Number", command = FindPhoneNumber, width=20, bg='pink', borderwidth=1)
Store_button = Button(root, text="Store data", command = StoreData, width=20, bg='pink',borderwidth=1)
Find_Name_button = Button(root, text= "Find name", command = FindName,width=20, bg='pink',borderwidth=1)
Clear_Label_button = Button(root, text="Clear search", command=DeleteSearch,width=20,bg='pink',borderwidth=1)
Name_label.grid(column=0, row=0)
Name.grid(column=1,row=0)
Email_label.grid(column=0, row=1)
Email.grid(column=1,row=1)
PhoneNumber_label.grid(column=0, row=2)
PhoneNumber.grid(column=1, row=2)
Date_of_birth_label.grid(column=0, row=3)
Date_of_birth.grid(column=1, row=3)
Store_button.grid(column=0, row=4)
Find_Phone_Number_Button.grid(column=0,row=5)
Find_Name_button.grid(column=0, row=6)
Clear_Label_button.grid(column=0, row=7)

root.mainloop()
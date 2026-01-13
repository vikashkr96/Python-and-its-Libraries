import os

def create_file(filename):
    try:                                                                      
        with open(filename , 'x') as f:                                            
            print(f"File Name {filename} : Created Succesfully!")              

    except FileExistsError:
        print("File Name {filename} already exists!")

    except Exception as e:                                                   
        print("An error occured!" )

def view_all_files():
    files= os.listdir()     
    if not files:
        print("File not found !")
    else:
         print("Files in directory! ")
         for file in files:
             print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted succesfully ! ")
    except FileNotFoundError:
        print("File not found !")
    except Exception as e:
        print("An error occured!")

def read_file(filename):
    try:
        with open('vikash.txt','r') as f:
            content = f.read()
            print(f"Content of '{filename}' :\n{content}")

    except FileNotFoundError:
        print(f"{filename} does not exist!")

    except Exception as e:
        print("An error occured!")

def edit_file(filename):
    try:
        with open('vikash.txt','a') as f:                                                     
            content = input("Enter data to add:")
            f.write(content + "\n")
            print(f"content added to {filename} successfully!")

    except FileNotFoundError:
        print(f"{filename} does not exist!")
        
    except Exception as e:
        print("An error occured!")

def main():
    while True:
        print("FILE MANAGEMENT APP BY VIKASH")
        print("1:Create a file")
        print("2:View all files")
        print("3:Delete a file")
        print("4:Read a file")
        print("5:Edit a file")
        print("6:Exit the app")

        choice = input('Enter your choice (1-6) = ' )

        if choice =='1':
            filename = input("Enter the name of file you want to create = ")
            create_file(filename)
        elif choice =='2':
            view_all_files()
        elif choice=='3':
            filename = input("Enter the name of the file you want to delete : ")
            delete_file(filename)
        elif choice=='4':
            filename = input("Enter the name of file you want to read : ")
            read_file(filename)
        elif choice=='5':
            filename = ("Enter the file name you want to edit = ")
            edit_file(filename)
        elif choice=='6':
            print("Closing the app........")
            break
        else:
            print("In-valid input")

if __name__== "__main__":
    main()












##### Data Student College
Menu = ['1. Report Data Student',
        '2. Add Data Student',
        '3. Change Data Student',
        '4. Delete Data Student',
        '5. Exit']

student = [{'NIM' : '22A', 'Name' : 'Miller', 'Gender' : 'Men', 'City' : 'Berlin'},
{'NIM' : '23B', 'Name' : 'Sasy', 'Gender' : 'Woman', 'City' : 'Texas'}]


###### Read Data Function
def Read_Data():
    read = True
    while read != '3':
        print("\n+++++++Report Data Student+++++++\n")    
        print("1. Report All Data")
        print("2. Report Certain Data")
        print("3. Back Ke Menu Utama")                                                                     
        read = input("Please Select Sub Menu Read Data [1-3] : ")
        if read == '1':
            if len(student) != 0 :                                                                      
                print('List Student :')                                                    
                for j, i in enumerate(student):                                                                       
                    print(f"{j+1}. NIM : {i['NIM']}, Name : {i['Name']}, Gender : {i['Gender']}, City : {i['City']}")                                                           
            else:                                                                                   
                print('\n****Data Student Empty****')   
            continue                                            
        elif read == '2':
            if len(student) != 0 :                                                                      
                std = input("Enter NIM : ").upper() 
                print(f"Student Data with NIM : {std}")                                                 
                for j, i in enumerate(student):                                                                       
                    if i['NIM'] == std:
                        print(f"{j+1}. NIM : {i['NIM']}, Name : {i['Name']}, Gender : {i['Gender']}, City : {i['CIty']}")  
                        break
                else:
                    print("\n****Data Student Empty*****")                                                       
            else:                                                                                   
                print('\n****Data Student Empty****')  
            continue
        elif read == '3':
            Main_Menu() 


#### Create Data Function
def Create_Data():
    create = True 
    while create != '2':
        print("++++++++Add Data Student++++++++++++")
        print('1. Add Data Student')
        print('2. Back to Main Menu')
        create = input('Please select Sub Menu Create Data [1-2] : ')
        if create == '1':
            nim = input('Enter NIM : ').upper()
            for i in student:
                if i['NIM'] == nim:
                    print("Data Exist")
                    break
            else:
                nama = input("Enter Name : ").capitalize()
                gender = input("Enter Gender : ").capitalize()
                kota = input("Enter City : ").capitalize()
                save = True
                while save:
                    simpan = input("Will Data be saved?? (Y/N) : ").upper()
                    if simpan == 'Y':
                        data = {'NIM' : nim, 'Name' : nama, 'Gender' : gender, 'City' : kota}
                        student.append(data)
                        print('Data saved')
                        save = False
                        break
                    elif simpan == 'N':
                        print("Data is not Saved")
                        save = False
                        break

        elif create == '2':
            Main_Menu()



###### Update Data Function
def Update_Data():
    Update = True 
    while Update != '2':
        print("==================Changed Data College==============")
        print('1. Change Data Student')
        print('2. Back to Main Menu')
        Update = input('Please select Sub Menu Update Data [1-2] : ')
        if Update == '1':
            nim = input('Enter NIM : ').upper()
            for i in student:
                if i['NIM'] == nim:
                    print(f"NIM : {i['NIM']}, Name : {i['Name']}, Gender : {i['Gender']}, City : {i['City']}")
                    askU = True
                    while askU:
                        ask = input("Press Y if you next Update data or N if want cancel Update (Y/N) : ").lower()
                        if ask == 'y':
                            kolom = input("insert column/Description you want to edit : ").capitalize()
                            new_data = input(f"Enter {kolom} Baru : ")
                            askU = False
                            save = True
                            while save:
                                simpan = input("Will Data be Updated? (Y/N) : ").upper()
                                if simpan == 'Y':
                                    i[kolom] = new_data
                                    print('Data Updated')
                                    save = False
                                    break
                                elif save == 'N':
                                    print("Data No Update")
                                    save = False
                                    break
                            break
                        elif ask == 'n':
                            print("Data is not Update")
                            askU = False
                        else:
                            continue
                    break
                else:
                    continue
            else:
                print("Data Empty")

        elif Update == '2':
            Main_Menu()


######## Delete Data Function
def Delete_Data():
    Delete = True 
    while Delete != '2':
        print("==================Delete Data Student College==================")
        print('1. Delete Data College')
        print('2. Back to Main Menu')
        Update = input('Please select Sub Menu Delete Data [1-2] : ')
        if Update == '1':
            nim = input('Enter NIM : ').upper()
            for i in student:
                if i['NIM'] == nim:
                    Hapus = True
                    while Hapus:
                        Hapus = input("Will Data be Deleted? (Y/N) : ").upper()
                        if Hapus == 'Y':
                            ind = student.index(i)
                            student.pop(ind)
                            print('Data Deleted')
                            Hapus = False
                            break
                        elif Hapus == 'N':
                            print("Data is Not Deleted")
                            Hapus = False
                            break
                    break
                else:
                    continue
            else:
                print("Data Empty")
            continue
        elif Update == '2':
            Main_Menu()

#### Main Menu Function
def Main_Menu():
    Opsi = 5


    while (Opsi != '5'):
        print("\n==========Data Student College=============\n")
        for i in Menu:
            print(i)
        Opsi = input("Please Select Main_Menu [1-5] : ")
        if Opsi == '1':
            Read_Data()
        elif Opsi == '2':
            Create_Data()
        elif Opsi == '3':
            Update_Data()
        elif Opsi == '4':
            Delete_Data()
        elif Opsi == '5':
            print('Thank you byebyeee!!!')
            quit()
        else:
            print("*****Sorry Stil Newbie************** \n")


###### Run the Application
Main_Menu()
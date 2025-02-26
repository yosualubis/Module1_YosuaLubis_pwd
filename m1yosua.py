# Start
##### Data Student Supplier
Menu = ['1. Report Data Supplier',
        '2. Add Data Supplier',
        '3. Change Data Supplier',
        '4. Delete Data Supplier',
        '5. Exit']
supplier = {'Ref001': {'Code' : '4123', 'Name' : 'PT.Halcom', 'Type' : 'IT', 'City' : 'Batam', 'Status' : 'Fixterm'},
'Ref002': {'Code' : '4124', 'Name' : 'PT.Wischo', 'Type' : 'Accessories', 'City' : 'Batam', 'Status' : 'Contract' },
'Ref003': {'Code' : '4125', 'Name' : 'PT.Dutacom', 'Type' : 'Accessories', 'City' : 'Batam', 'Status' : 'Fixterm'},
'Ref004': {'Code' : '4126', 'Name' : 'PT.Infocom', 'Type' : 'IT', 'City' : 'Jakarta', 'Status' : 'Contract' },
'ref005': {'Code' : '4127', 'Name' : 'PT.Generate', 'Type' : 'IT', 'City' : 'Bandung', 'Status' : 'Fixterm'},
'ref006': {'Code' : '4128', 'Name' : 'PT.Sunlicom', 'Type' : 'IT', 'City' : 'Medan', 'Status' : 'Fixterm'},
'ref007': {'Code' : '4129', 'Name' : 'PT.Servicejaya', 'Type' : 'Accessories', 'City' : 'Bogor', 'Status' : 'Contract'},
'ref008': {'Code' : '4130', 'Name' : 'PT.Petron', 'Type' : 'IT', 'City' : 'Surabaya', 'Status' : 'Contract'},
'ref009': {'Code' : '4131', 'Name' : 'PT.Pilar', 'Type' : 'Accessories', 'City' : 'Bekasi', 'Status' : 'Fixterm'},
'ref010': {'Code' : '4132', 'Name' : 'PT.Bisnet', 'Type' : 'IT', 'City' : 'Jakarta', 'Status' : 'Fixterm'}}


# Read function
def view_suppliers(supplier):
    print(f"{'RefID':<10} {'Code':<6} {'Name':<20} {'Type':<12} {'City':<10} {'Status':<10}")
    print("=" * 65)
    for ref, details in supplier.items():
        print(f"{ref:<10} {details['Code']:<6} {details['Name']:<20} {details['Type']:<12} {details['City']:<10} {details['Status']:<10}")
# Create function
def add_data():
    newref=input("ref")
    newCode=input("Code")
    newName=input("Name")
    newType=input("Type")
    newCity=input("City")
    newStatus=input("Status")
    supplier[newref]={'Code':newCode,'Name': newName,'Type':newType,'City':newCity,'Status':newStatus}
def change_data():
    ref = input("Enter reference ID: ").strip().lower()
    supplier_lower = {key.lower(): value for key, value in supplier.items()}

    if ref in supplier_lower:
        print("\nEnter values you want to change or leave blank:")
        newName = input("Name: ") or supplier_lower[ref]['Name']
        newCity = input("City: ") or supplier_lower[ref]['City']
        newStatus = input("Status: ") or supplier_lower[ref]['Status']

        supplier[ref] = {
            'Code': supplier_lower[ref]['Code'],  
            'Name': newName,
            'Type': supplier_lower[ref]['Type'],  
            'City': newCity,
            'Status': newStatus
        }

        print("\nData updated successfully.")
    else:
        print("Reference ID not found.")

def delete_data():
    ref = input("Enter the reference ID to delete: ").strip()
    lower_keys = {key.lower(): key for key in supplier}
    
    if ref.lower() in lower_keys:
        actual_key = lower_keys[ref.lower()]
        del supplier[actual_key]
        print(f"Supplier with reference '{actual_key}' has been deleted.")
    else:
        print("Reference not found.")

def app():

# Start 
    email = input("Enter your email: ")
    print("You entered:", email)
    while True:
        print("\n".join(Menu))
        try:
            opt = int(input("Please enter the menu number you'd like to access: ").strip())
            if opt == 1:  # Read
                view_suppliers(supplier)
            elif opt == 2:  # Create
                add_data()
                view_suppliers(supplier)
            elif opt == 3:  # Update
                change_data()
                view_suppliers(supplier)
            elif opt == 4:  # Delete
                delete_data()
                view_suppliers(supplier)
            elif opt == 5:  # Exit
                print("\tExiting the program. Goodbye!")
                break  # Exit the loop
            else:
                print("\tInvalid input! Please enter a number.")
                continue
        except ValueError:
            print("\tInvalid input! Please enter a number.")
            continue
if __name__ == "__main__":
    app()
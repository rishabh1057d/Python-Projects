import csv
import pandas as pd

CSV_FILE = 'contacts.csv'

def initialize_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Address'])
    except FileExistsError:
        pass

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email, address])

    print("Contact added successfully.")

def view_contacts():
    df = pd.read_csv(CSV_FILE)
    print(df)

def search_contact():
    query = input("Enter name or phone number to search: ")
    df = pd.read_csv(CSV_FILE)

    df['Name'] = df['Name'].astype(str)
    df['Phone'] = df['Phone'].astype(str)
    
    results = df[(df['Name'].str.contains(query, case=False)) | (df['Phone'].str.contains(query))]
    if not results.empty:
        print(results)
    else:
        print("No contacts found.")

def update_contact():
    query = input("Enter name or phone number of the contact to update: ")
    df = pd.read_csv(CSV_FILE)

    df['Name'] = df['Name'].astype(str)
    df['Phone'] = df['Phone'].astype(str)

    results = df[(df['Name'].str.contains(query, case=False)) | (df['Phone'].str.contains(query))]
    
    if not results.empty:
        print(results)
        index = int(input("Enter the index of the contact to update: "))
        if index in results.index:
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")

            df.at[index, 'Name'] = name
            df.at[index, 'Phone'] = phone
            df.at[index, 'Email'] = email
            df.at[index, 'Address'] = address

            df.to_csv(CSV_FILE, index=False)
            print("Contact updated successfully.")
        else:
            print("Invalid index.")
    else:
        print("No contacts found.")

def delete_contact():
    query = input("Enter name or phone number of the contact to delete: ")
    df = pd.read_csv(CSV_FILE)

    df['Name'] = df['Name'].astype(str)
    df['Phone'] = df['Phone'].astype(str)

    results = df[(df['Name'].str.contains(query, case=False)) | (df['Phone'].str.contains(query))]
    
    if not results.empty:
        print(results)
        index = int(input("Enter the index of the contact to delete: "))
        if index in results.index:
            df = df.drop(index)
            df.to_csv(CSV_FILE, index=False)
            print("Contact deleted successfully.")
        else:
            print("Invalid index.")
    else:
        print("No contacts found.")

def main():
    initialize_csv()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print('Thank You..')
            break
        else:
            print("Invalid choice. Please try again.")
 
if __name__ == "__main__":
    main()

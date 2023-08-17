import pandas as pd
import os
from tabulate import tabulate
class MediaDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.columns = ["Title", "Author", "Type", "Year", "Genre", "Rating"]

        if not os.path.exists(filename):
            self.create_empty_database()

        self.load_database()

    def create_empty_database(self):
        data = pd.DataFrame(columns=self.columns)
        data.to_csv(self.filename, index=False)

    def load_database(self):
        self.data = pd.read_csv(self.filename)

    def save_database(self):
        self.data.to_csv(self.filename, index=False)

    def list_media(self):
        print("\nMedia List:")
        if not self.data.empty:
            print(tabulate(self.data, headers='keys', tablefmt='grid'))
        else:
            print("The database is empty.")

    def insert_media(self, title, author, media_type, year, genre, rating):
        new_entry = pd.DataFrame([[title, author, media_type, year, genre, rating]], columns=self.columns)
        self.data = pd.concat([self.data, new_entry], ignore_index=True)
        self.save_database()
        print(f"Added {title} to the database.")

    def remove_media(self, title):
        self.data = self.data[self.data['Title'] != title]
        self.save_database()
        print(f"Removed {title} from the database.")

    def search_media(self, title):
        result = self.data[self.data['Title'] == title]
        if not result.empty:
            print(tabulate(result, headers='keys', tablefmt='grid'))
        else:
            print(f"{title} not found in the database.")

    def count_media(self):
        print(f"Total media items in the database: {len(self.data)}")

    def edit_media(self, title):
        result = self.data[self.data['Title'] == title]
        if not result.empty:
            field = input("Enter field to edit (Title, Author, Type, Year, Genre, Rating): ").title()
            if field in self.columns:
                new_value = input(f"Enter new value for {field}: ")
                self.data.loc[self.data['Title'] == title, field] = new_value
                self.save_database()
                print(f"{field} updated for {title}.")
            else:
                print("Invalid field name.")
        else:
            print(f"{title} not found in the database.")

    def sort_media(self, column):
        if column in self.columns:
            sorted_data = self.data.sort_values(by=column)
            print(tabulate(sorted_data, headers='keys', tablefmt='grid'))
        else:
            print("Invalid column name.")

    def filter_media(self, column, value):
        if column in self.columns:
            filtered_data = self.data[self.data[column] == value]
            print(tabulate(filtered_data, headers='keys', tablefmt='grid'))
        else:
            print("Invalid column name.")

if __name__ == "__main__":
    db = MediaDatabase("media_database.csv")

    while True:
        print("\nMedia Database Menu:")
        print("1. List all media")
        print("2. Insert new media")
        print("3. Remove media")
        print("4. Search media")
        print("5. Count media items")
        print("6. Edit media")
        print("7. Sort media")
        print("8. Filter media")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            db.list_media()
        elif choice == "2":
            title = input("Enter title: ")
            author = input("Enter author: ")
            media_type = input("Enter media type: ")
            year = input("Enter year: ")
            genre = input("Enter genre: ")
            rating = input("Enter rating: ")
            db.insert_media(title, author, media_type, year, genre, rating)
        elif choice == "3":
            title = input("Enter title to remove: ")
            db.remove_media(title)
        elif choice == "4":
            title = input("Enter title to search: ")
            db.search_media(title)
        elif choice == "5":
            db.count_media()
        elif choice == "6":
            title = input("Enter title to edit: ")
            db.edit_media(title)
        elif choice == "7":
            column = input("Enter column to sort by: ")
            db.sort_media(column)
        elif choice == "8":
            column = input("Enter column to filter by: ")
            value = input(f"Enter value to filter {column} by: ")
            db.filter_media(column, value)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

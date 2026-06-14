from src.services.password_generator import generate_password
from src.services.vault_service import VaultService


def show_entries(entries):
    if not entries:
        print("No entries found.")
        return

    for entry in entries:
        print("\n----------------")
        print("ID:", entry.entry_id)
        print("Title:", entry.title)
        print("Username:", entry.username)
        print("Password:", entry.password)


def create_entry(vault):
    title = input("Title: ")
    username = input("Username: ")

    generate_choice = input("Generate a password? (y/n): ").strip().lower()

    if generate_choice == "y":
        length_text = input(
            "Password length or press Enter for default: "
        ).strip()

        if length_text:
            password = generate_password(int(length_text))
        else:
            password = generate_password()

        print("Generated password:", password)
    else:
        password = input("Password: ")

    entry = vault.create_entry(title, username, password)

    print("Entry created.")
    print("Entry ID:", entry.entry_id)


def edit_entry(vault):
    vault.edit_entry(
        input("Entry ID: "),
        input("New title: "),
        input("New username: "),
        input("New password: ")
    )

    print("Entry updated.")


def delete_entry(vault):
    entry_id = input("Entry ID: ")
    vault.delete_entry(entry_id)

    print("Entry deleted.")


def search_entries(vault):
    search_text = input("Search by title or username: ")
    results = vault.search_entries(search_text)

    show_entries(results)


def generate_new_password():
    length_text = input(
        "Password length or press Enter for default: "
    ).strip()

    if length_text:
        password = generate_password(int(length_text))
    else:
        password = generate_password()

    print("Generated password:", password)


def main():
    vault = VaultService()

    while True:
        print("\nSecuraVault")
        print("1. Create entry")
        print("2. View entries")
        print("3. Edit entry")
        print("4. Delete entry")
        print("5. Search entries")
        print("6. Generate password")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                create_entry(vault)

            elif choice == "2":
                show_entries(vault.view_entries())

            elif choice == "3":
                edit_entry(vault)

            elif choice == "4":
                delete_entry(vault)

            elif choice == "5":
                search_entries(vault)

            elif choice == "6":
                generate_new_password()

            elif choice == "7":
                print("Goodbye.")
                break

            else:
                print("Invalid option.")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
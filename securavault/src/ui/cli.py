from src.services.vault_service import VaultService


def show_entries(vault):
    entries = vault.view_entries()

    if not entries:
        print("No entries found.")
        return

    for entry in entries:
        print("\n----------------")
        print("ID:", entry.entry_id)
        print("Title:", entry.title)
        print("Username:", entry.username)
        print("Password:", entry.password)


def main():
    vault = VaultService()

    while True:
        print("\nSecuraVault")
        print("1. Create entry")
        print("2. View entries")
        print("3. Edit entry")
        print("4. Delete entry")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                entry = vault.create_entry(
                    input("Title: "),
                    input("Username: "),
                    input("Password: ")
                )

                print("Entry created.")
                print("Entry ID:", entry.entry_id)

            elif choice == "2":
                show_entries(vault)

            elif choice == "3":
                vault.edit_entry(
                    input("Entry ID: "),
                    input("New title: "),
                    input("New username: "),
                    input("New password: ")
                )

                print("Entry updated.")

            elif choice == "4":
                vault.delete_entry(
                    input("Entry ID: ")
                )

                print("Entry deleted.")

            elif choice == "5":
                print("Goodbye.")
                break

            else:
                print("Invalid option.")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
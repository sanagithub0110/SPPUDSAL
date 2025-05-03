size = 10

# Three separate hash tables
client_list_linear = [None] * size
client_list_quadratic = [None] * size
client_list_chain = [[] for _ in range(size)]


# --- LINEAR PROBING METHODS ---
def add_client_linear():
    client_id = int(input("Client ID: "))
    name = input("Client Name: ")
    telephone = input("Telephone Number: ")
    client = [client_id, name, telephone]
    index = client_id % size

    for i in range(size):
        new_index = (index + i) % size
        if client_list_linear[new_index] is None or client_list_linear[new_index] == "DELETED":
            client_list_linear[new_index] = client
            print("Client added at index:", new_index)
            return
    print("Hash table (Linear) is full!")


def search_client_linear():
    client_id = int(input("Client ID to search: "))
    index = client_id % size
    comparisons = 0

    for i in range(size):
        new_index = (index + i) % size
        comparisons += 1
        entry = client_list_linear[new_index]
        if entry is None:
            break
        if entry != "DELETED" and entry[0] == client_id:
            print("Client found at index:", new_index, entry)
            print("Comparisons:", comparisons)
            return
    print("Client not found.")
    print("Comparisons:", comparisons)


def delete_client_linear():
    client_id = int(input("Client ID to delete: "))
    index = client_id % size

    for i in range(size):
        new_index = (index + i) % size
        if client_list_linear[new_index] is None:
            break
        if client_list_linear[new_index] != "DELETED" and client_list_linear[new_index][0] == client_id:
            client_list_linear[new_index] = "DELETED"
            print("Client deleted from index:", new_index)
            return
    print("Client not found.")


# --- QUADRATIC PROBING METHODS ---
def add_client_quadratic():
    client_id = int(input("Client ID: "))
    name = input("Client Name: ")
    telephone = input("Telephone Number: ")
    client = [client_id, name, telephone]
    index = client_id % size

    for i in range(size):
        new_index = (index + i * i) % size
        if client_list_quadratic[new_index] is None or client_list_quadratic[new_index] == "DELETED":
            client_list_quadratic[new_index] = client
            print("Client added at index:", new_index)
            return
    print("Hash table (Quadratic) is full!")


def search_client_quadratic():
    client_id = int(input("Client ID to search: "))
    index = client_id % size
    comparisons = 0

    for i in range(size):
        new_index = (index + i * i) % size
        comparisons += 1
        entry = client_list_quadratic[new_index]
        if entry is None:
            break
        if entry != "DELETED" and entry[0] == client_id:
            print("Client found at index:", new_index, entry)
            print("Comparisons:", comparisons)
            return
    print("Client not found.")
    print("Comparisons:", comparisons)


def delete_client_quadratic():
    client_id = int(input("Client ID to delete: "))
    index = client_id % size

    for i in range(size):
        new_index = (index + i * i) % size
        if client_list_quadratic[new_index] is None:
            break
        if client_list_quadratic[new_index] != "DELETED" and client_list_quadratic[new_index][0] == client_id:
            client_list_quadratic[new_index] = "DELETED"
            print("Client deleted from index:", new_index)
            return
    print("Client not found.")


# --- CHAINING METHODS ---
def add_client_chain():
    client_id = int(input("Client ID: "))
    name = input("Client Name: ")
    telephone = input("Telephone Number: ")
    client = [client_id, name, telephone]
    index = client_id % size
    client_list_chain[index].append(client)
    print("Client added at index (chain):", index)


def search_client_chain():
    client_id = int(input("Client ID to search: "))
    index = client_id % size
    comparisons = 0

    for client in client_list_chain[index]:
        comparisons += 1
        if client[0] == client_id:
            print("Client found at index (chain):", index, client)
            print("Comparisons:", comparisons)
            return
    print("Client not found.")
    print("Comparisons:", comparisons)


def delete_client_chain():
    client_id = int(input("Client ID to delete: "))
    index = client_id % size
    for i in range(len(client_list_chain[index])):  
        client = client_list_chain[index][i]
        if client[0] == client_id:
            del client_list_chain[index][i]
            print("Client deleted from index (chain):", index)
            return
    print("Client not found.")

# --- MAIN MENU ---
def Main():
    while True:
        print("\n----- Telephone Book (Hashing Techniques) -----")
        print("1. Add Client (Linear Probing)")
        print("2. Search Client (Linear Probing)")
        print("3. Delete Client (Linear Probing)")
        print("4. Add Client (Quadratic Probing)")
        print("5. Search Client (Quadratic Probing)")
        print("6. Delete Client (Quadratic Probing)")
        print("7. Add Client (Chaining)")
        print("8. Search Client (Chaining)")
        print("9. Delete Client (Chaining)")
        print("10. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_client_linear()
        elif choice == 2:
            search_client_linear()
        elif choice == 3:
            delete_client_linear()
        elif choice == 4:
            add_client_quadratic()
        elif choice == 5:
            search_client_quadratic()
        elif choice == 6:
            delete_client_quadratic()
        elif choice == 7:
            add_client_chain()
        elif choice == 8:
            search_client_chain()
        elif choice == 9:
            delete_client_chain()
        elif choice == 10:
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Try again.")


Main()

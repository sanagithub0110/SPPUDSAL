def accept_set(A):
    n = int(input("Enter no. of elements in set : "))
    for i in range(n):
        x = input("Add element to the set : ")
        if x not in A:
            A.append(x)
    print("Set accepted successfully")

def display_set(A):
    n = len(A)
    if n == 0:
        print("Set is empty")
    else:
        print("Elements of set are : ")
        for i in range(n):
            print(A[i], end=' ')
        print()

def delete_element(A, X):
    if X in A:
        A.remove(X)
        print("Deleted element :", X)
    else:
        print("Element not found in the set.")

def set_contain(A):
    return 1 if len(A) != 0 else 0

def size_of_set(A):
    print("Size of set A is : ", len(A))
    print("Size of set B is : ", len(B))

def search_set(A, X):
    for i in range(len(A)):
        if A[i] == X:
            return 1
    return 0

def intersection(A, B, C):
    for i in range(len(A)):
        flag = search_set(B, A[i])
        if flag == 1:
            C.append(A[i])

def union(A, B, C):
    for i in range(len(A)):
        C.append(A[i])
    for i in range(len(B)):
        flag = search_set(A, B[i])
        if flag == 0:
            C.append(B[i])

def difference(A, B, C):
    for i in range(len(A)):
        flag = search_set(B, A[i])
        if flag == 0:
            C.append(A[i])

def is_subset(A, B):
    for item in A:
        if item not in B:
            return False
    return True

def main():
    set_A = []
    set_B = []
    while True:
        print("\n1. Accept Set")
        print("2. Display Set")
        print("3. Delete Element")
        print("4. Size of set")
        print("5. Intersection of two sets")
        print("6. Union of two sets")
        print("7. Difference of two sets")
        print("8. Subset")
        print("9. Exit")

        ch = int(input("Enter your choice : "))
        set_R = []

        if ch == 9:
            print("End of the program!")
            break
        elif ch == 1:
            print("\nEnter first Set :")
            set_A.clear()
            accept_set(set_A)
            print("\nEnter second Set :")
            set_B.clear()
            accept_set(set_B)
        elif ch == 2:
            print("\nFirst set :")
            display_set(set_A)
            print("Second set :")
            display_set(set_B)
        elif(ch == 3):
            print("From which set do you want to delete? (A/B): ", end="")
            set_choice = input().strip().upper()
            X = input("Enter the element you want to delete: ")
            if set_choice == 'A':
               delete_element(set_A, X)
            elif set_choice == 'B':
               delete_element(set_B, X)
            else:
               print("Invalid set choice. Please enter A or B.")
        elif ch == 4:
            size_of_set(set_A, set_B)
        elif ch == 5:
            print("\nIntersection set : ")
            intersection(set_A, set_B, set_R)
            display_set(set_R)
        elif ch == 6:
            print("\nUnion set : ")
            union(set_A, set_B, set_R)
            display_set(set_R)
        elif ch == 7:
            print("\nDifference set : ")
            difference(set_A, set_B, set_R)
            display_set(set_R)
        elif ch == 8:
            if is_subset(set_A, set_B):
                print("First set is a subset of the second set.")
            else:
                print("First set is NOT a subset of the second set.")
        else:
            print("Enter valid choice!")

main()
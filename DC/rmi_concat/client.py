import Pyro5.api

def main():
    uri = input("Enter the URI of the remote object (e.g., PYRO:obj_xxxxx@localhost:xxxx): ")
    string_service = Pyro5.api.Proxy(uri)

    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    result = string_service.concatenate(s1, s2)
    print("Concatenated result:", result)

if __name__ == "__main__":
    main()

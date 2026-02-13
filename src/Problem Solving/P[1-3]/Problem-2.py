def name_checker(name):
    """Checks if the name is valid.

    Args: name (string)
    returns: True if the name is valid, False otherwise
    """
    if name.startswith("R") or name.startswith("r"):
        return f"{name} plays banjo"
    else: 
        return f"{name} does not play banjo"
    

if __name__ == "__main__":
    print("Enter a name to check if it plays banjo:")
    name = input()
    print(name_checker(name))

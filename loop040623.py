# Open the file for reading
with open('list.txt', 'r') as f:
    # Loop through each line in the file and use it as input
    for line in f:
        response = input(line.strip())
        if response  == "hello":
            print("Great")
        else:
            continue

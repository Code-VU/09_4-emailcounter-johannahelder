def countEmail():
    # This first line is provided for you
    file_name = input("Enter file:")
    sender_day = []
    sender_dict= dict()

    with open(file_name, 'r') as user_file:
        local_file = user_file.readlines()

    for line in local_file:
        if line.startswith('From '):
            sender_day.append(line.split(' ')[1])
    for key in sender_day:
        sender_dict[key] = sender_dict.get(key,0) +1
    max_val = max(list(sender_dict.values()))

    # Traversing in the key-value pairs of the dictionary using the items() function
    for key,val in sender_dict.items():
   # checking whether the key value of the iterator is equal to the above-entered key
        if(val==max_val):
            print(key, val)


## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()

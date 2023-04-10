def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    sender_day = []
    sender_dict= dict()

    for line in handle:
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

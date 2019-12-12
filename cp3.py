import sys

list = []


while True:
    x = input("Choose an action: Edit[1]/Analysis[2]/Quit[3] \n")
    if x == "1":
        y = input("Choose an action: Add Item[a]/Remove Item[b]/Return Menu[c] \n")
        if y == 'a':
                class Edit:
                    def __init__(self, item,category,spend):
                        self.item = item
                        self.category = category
                        self.spend = spend
                    for i in range(0, 1):
                        item = input('Please enter item name: ')
                        category = input('Which category does it belong: ')
                        spend = input('Please enter the amount you have spend: ')
                        list.append(item+","+category+","+spend)
                        print("you have added a new item in your list! \n")
            
    elif x == "2":
        list_len = len(list)
        print("Here is your list", list_len, " of total item")
        print(list)
        
    elif x == "3":
        print("Goodbye!")
        sys.exit()
    

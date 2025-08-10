
database = ["Croaks","Eat Flies","Shrimps","Sings"]
knowbase = ["Frog", "Canary"]
color = ["Green", "Yellow"]

def display_objects():
    print("\n X is: \n1. Frog \n2. Canary", end='')
    print("\nSelect one:", end='')
def main():
    print("*-----Backward--Chaining-----*", end='')
    display_objects()
    
    try: 
        x = int(input())
    except ValueError:
        print("\n---Invalid input! Please select a valid option between 1 and 2.")
        return
    
    if x == 1:
        print("Chance of eating flies", end='')
    elif x ==2:
        print("Chance of shrimping", end='')
    else:
        print("\n----Invalid Option! Please select a valid option between 1 and 2.")
        return
    if 1 <= x <= 2:
        print("\nObject is:", knowbase[x-1])
        print("\nColor option: 1. Green 2. Yellow", end='')
        print("\nSelect color option:", end='')
        
        try:
            k = int(input())
        except ValueError:
            print("\n---Invalid input! Please select either option 1 or 2 for color.")
            return
        if k == 1 and x ==1:
            print("Yes, it is in", color[0],"color and will",database[0])
        elif k == 2 and x == 2:
            print("Yes, it is in", color[1], "color and will",database[1])
        else:
            print("\n---Invalid Knowledge Database! Please select a valid option.")
if __name__ == "__main__":
    main()            
            
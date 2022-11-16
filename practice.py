# function named hello to greet user
def hello():
    print("greetings user!")


# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

def pack(a, b, c):
    return [a, b, c]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __"
# (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!".
# The function should not return anything.


def eat_lunch(list):
    if len(list) == 0:
        print("lunchbox is empty! :(")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"first I eat {list[0]}")
            else:
                print(f"Next I eat my {list[i]}")


hello()
print(pack("a", "b", "c"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["sammy"])
eat_lunch(["Soup", "Chips", "Yogurt"])

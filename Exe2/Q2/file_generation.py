
try:
    n=int(input("Type Number of files:"))
    image_list = [] # your logic for the image data here
    n = int(n)
    for i in range(n):
        filename = "demo/demofile" + str(i) +".txt"
    with open(filename, 'w'):
        pass
except ValueError:
    print("This is not a whole number.")

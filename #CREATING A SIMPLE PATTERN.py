# #CREATING A SIMPLE PATTERN
# #HOLLOW SQUARE
size = 5
for i in range(size):
    for j in range(size):
        if i==0 or i==size - 1 or j==0 or j==size-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("\n")
# #A SIMPLE NUMBER PATTERN
rows = int(input('Enter the desired number of rows'))
for i in range(rows):
    for j in range(i):
        print(i, end='')
    print()
print('\n')
# # ****
# # ****
# # ****

height = 5

for i in range(0, height):
    for j in range(0, height):
        print('*', end='')
    print()

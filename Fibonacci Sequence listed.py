# Fibonacci Sequence
num_range = int(input("Enter the range: "))
num0 = 0
num1 = 1
num2 = 0
fib_Seq = []   # add this to creat a list of the range
for x in range(0,num_range,1):
    fib_Seq.append(num2) # add this to creat list
    print(num2)  # can delete this part to just get a list of numbers
    num0 = num1
    num1 = num2
    num2 = num0 + num1
print("--------Fibonacci Sequence List--------")
print(f"Fibonacci Sequence range of {num_range}: ", fib_Seq) # add this to crreat the list

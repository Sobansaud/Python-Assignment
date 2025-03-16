# CONTROL FLOWS AND LOOPS

# EXAMPLE 1

trafficlight = str(input("Enter The Traffic Light Color: "))
if trafficlight == "red":
    print("Stop")
elif trafficlight == "green":
    print("Go")
elif trafficlight == "yellow":
    print("Get Ready")
else:
    print("Light Is Broken! ")


# EXAMPLE 2 

stdmarks = int(input("Enter your marks : "))
if stdmarks > 80 and stdmarks <= 100:
    print("Student Got A+ Grade")
elif stdmarks > 70 and stdmarks <= 80:
    print("Student Got A Grade")
elif stdmarks > 60 and stdmarks <= 70:
    print("Student Got B Grade")
elif stdmarks > 50 and stdmarks <= 60:
    print("Student Got C Grade")
elif stdmarks > 40 and stdmarks <= 50:
    print("Student Got D Grade")
else:
    print("Student Got F Grade")


# LOOPS CONDITION


i = 2
for i in range(10):
    print(i)




number = 1
while number <= 10:
    print(number)
    number += 1



for i in range(1, 10):
    if i == 6:
        break  # Jab i 6 ho, loop ko break kar do
    print(i)

for n in range(1,50):
    if n == 25:
         continue   #  Jab n 25 ho, loop ko skip kar do
    print(n)


for outer in range(3): # outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(11): # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()
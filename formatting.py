# print('Hello'.rjust(10,'-'))
num = int(input("enter num"))
width = len(bin(num))-2
# print(f"binary of {num} is: {bin(num)}")
# print(f"octal of {num} is: {oct(num)}")
# print(f"hex of {num} is: {hex(num)}")
for i in range(1,num+1):
    # print(width)
    dec = str(i).rjust(width)
    binary = bin(i)[2:].rjust(width)
    ot = oct(i)[2:].rjust(width)
    hx = hex(i)[2:].upper().rjust(width)
    print(f"{dec} {ot} {hx} {binary}")


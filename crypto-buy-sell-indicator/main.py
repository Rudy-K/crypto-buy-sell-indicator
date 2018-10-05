import RSI
coin = input("Input coin>>")
RSI.getRSI()
print("The RSI of",coin,"is",RSI)
if RSI>80:
    print("You should sell")
elif RSI<20:
    print("You should buy")
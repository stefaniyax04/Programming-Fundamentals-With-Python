# You will be given strings until you receive the command "End". For each string given,
# you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!

while True:
    s = input()
    if s == "End":
        break
    if s == "SoftUni":
        continue
    doubled = ''.join([ch * 2 for ch in s])
    print(doubled)

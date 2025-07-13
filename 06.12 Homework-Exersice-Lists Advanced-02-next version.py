# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
# Your task is to print the next version. For example, if the current version is "1.3.4", the next version
# will be "1.3.5".
# The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0
# and increase the previous number. For more clarification, see the examples below.


version = input().split(".")
version = list(map(int, version))

version[2] += 1
if version[2] > 9:
    version[2] = 0
    version[1] += 1
    if version[1] > 9:
        version[1] = 0
        version[0] += 1

print(f"{version[0]}.{version[1]}.{version[2]}")

# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder
# (0, 10, 20, 30...). Your task is to create a function that returns a loading bar depending on the number you
# have received in the input. Print the result on the console. For more clarification, see the examples below.


def loading_bar(progress):
    bar = "%" * (progress // 10) + "." * (10 - progress // 10)

    if progress == 100:
        print("100% Complete!")
        print(f"[{bar}]")
    else:
        print(f"{progress}% [{bar}]")
        print("Still loading...")


num = int(input())
loading_bar(num)

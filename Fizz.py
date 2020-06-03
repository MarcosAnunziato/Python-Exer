def fizz_buzz(n):
    n = []
    nums = print(input('Digite um número: '))
    for nums in n:
        if nums % 5 == 0 and nums % 3 == 0:
            print("fizz buzz")
        elif nums % 3 == 0:
            print("fizz")
        elif nums % 5 == 0:
            print("buzz")
        elif nums % 3 != 0 and nums % 5 != 0:
            print(nums)
        else:
            print("invalid arguement")

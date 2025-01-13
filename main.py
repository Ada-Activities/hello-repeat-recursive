def hello_repeat_recursive(num):
    print(f'Hello {num}!')
    # base case
    if num == 1:
        return
    # recursive case
    else:
        hello_repeat_recursive(num - 1)

hello_repeat_recursive(5)
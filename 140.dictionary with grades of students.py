grades = {"anusha":"100","mohith":"95","surya":"90"}
print(grades)
x = grades["mohith"]
print(x)
for i in grades:
    if "anusha" in grades:
        print("hello world")
        break
    else:
        print("Hi world")
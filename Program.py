def fizzBuzz():
  for i in range (1,100):
    if i % 5 == 0 and i % 3 == 0:
      print("fizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)
fizzBuzz()
n = 0
for zmienna in range(101):
  if zmienna >0 and zmienna <101:
    if zmienna%15 == 0:
      print("FizzBuzz")
      n = n+1
    elif zmienna%3 == 0:
      print("Fizz")
      n = n+1
    elif zmienna%5 == 0:
      print("Buzz")
    else:
      print(zmienna)
print(f"Liczby podzielne przez 3 (Fizz/FizzBuzz) wystąpiły {n} razy")

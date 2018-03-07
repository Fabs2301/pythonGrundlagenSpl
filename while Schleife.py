summe = 0
n = 1
while n <= 100000:
  summe = summe + n
  print(n, end=",")
  n=n+1
  if n >= 11:
    break
  
print(summe)
  
#fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

fibonacci = [1, 1]
while max(fibonacci) < 55:
  fibonacci.append(fibonacci[-1]+fibonacci[-2])

print(fibonacci)

import sys

a, b, c = sys.argv[1:4]
s = int(a) + int(b) + int(c)

print("Average of the 3 games: " + str(s/3))
print("Series of the 3 games: " + str(s))
print("Handicap: " + str(max(0, int(0.9 * (220-s/3)))))

from bigO import BigO

from app.csv_processor import csv_processer

# A big-O calculator to estimate time complexity of sorting functions.
# You can test time complexity, calculate runtime, etc
lib = BigO()

# We can test all "random", "sorted", "reversed", "partial", "Ksorted",
# "almost_equal" at once, and it shows, best, average and worst time complexity
result = lib.test_all(csv_processer)

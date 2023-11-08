"""
Modules in Python are like toolkits that contain a bunch of related tools. Each module is a file containing Python code that can include functions, variables, and even other objects. You can use these tools in your own code by "importing" the module with the import statement. For example, if you need math-related functions, you can import math and then use its functions like math.sqrt(16) to calculate the square root of 16. Modules help keep Python code organized and reusable by grouping related functionality together, and they allow you to extend your programs with capabilities from these "toolkits".
"""

# get function that's defined in another file
from utils import square

for i in range(10):
    print(square(i))
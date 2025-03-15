import random
from time import sleep
class MathQuiz:
 def __init__(self):
  self.operations = {
   "+": lambda x, y: x + y,
   "-": lambda x, y: x - y,
   "*": lambda x, y: x * y,
   "/": lambda x, y: x / y,
   "mod": lambda x, y: x % y
  }

 def generate_question(self):
  number1 = random.randint(0, 10)
  number2 = random.randint(0, 10)
  operation = random.choice(list(self.operations.keys()))

  return f"What is {number1} {operation} {number2}?"
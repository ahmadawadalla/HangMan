import time
import random

operaters = ["+","-","*","/"]
min_val = 1
max_val = 9

def problem_generator():

    while True:
        left_operand = random.randint(min_val,max_val)
        right_operand = random.randint(min_val,max_val)
        operator = random.choice(operaters)
        expr = str(left_operand) + " " + operator + " " + str(right_operand)
        answer = eval(expr)
        if (answer * 10) % 10 == 0 and (answer * 100) % 10 == 0:
            answer = int(answer)
            break

    return expr,answer

right = 0

while True:
    num_problems = input("How many math problems do you want to do? ")
    if num_problems.isdigit():
        num_problems = int(num_problems)
        break

input("Click enter to start: ")
print("----------------------")

start = time.time()

for i in range(num_problems):
    expr, answer = problem_generator()
    problem = input(expr + " = ")
    if problem == str(answer):
        right += 1

end = time.time()
total_time = round(end - start, 2)
score = round(((right / num_problems) * 100),2)

if (score * 10) % 10 == 0 and (score * 100) % 10 == 0:
    score = int(score)

print("----------------------")
print("Good Job! ")
print("You got a score of " + str(score) + "% in " + str(total_time) + " seconds")
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "green", "blue", "pink", "purple"]
all_turtles = []

for index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.up()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-210, y=-100 + index * 50)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            winner = colors[all_turtles.index(turtle)]
            is_race_on = False
        random_steps = random.randint(0, 10)
        turtle.forward(random_steps)


if winner == user_bet:
    print("You win!")
else:
    print(f"You lose. Winner was {winner}.")

screen.exitonclick()

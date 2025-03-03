import turtle

from turtle import *
import pandas as pd

screen = Screen()
screen.setup(width=650,height=850)
screen.title("India States Game")
image = "ezgif-68be87702a94a6.gif"

screen.addshape(image)
turtle.shape(image)

#Used to find co-ordinates of state
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

Data = pd.read_csv("info.csv")
all_states = Data.State.to_list()
guessed_states = []

while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States correct",
                                    prompt="What's is another state's name").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        df = pd.DataFrame(missing_state)
        df.to_csv("missed_state")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        correct_data = Data[Data.State == answer_state]
        t.goto(x=correct_data.x.item(),y=correct_data.y.item())
        t.write(answer_state)

screen.exitonclick()


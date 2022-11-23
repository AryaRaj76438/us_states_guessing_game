import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guessed_state = []
while len(guessed_state)<50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",prompt="State Name").title()
    if answer_state == "Exit":
        missing_state = [state for state in all_state if answer_state not in guessed_state]
        # missing_state = []
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        # print(missing_state)
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        w_turt = turtle.Turtle()
        w_turt.hideturtle()
        w_turt.penup()
        state_data = data[data.state == answer_state]
        w_turt.goto(int(state_data.x), int(state_data.y))
        w_turt.write(answer_state)


turtle.mainloop()
import turtle
import pandas

screen = turtle.Screen()
screen.title("India State Game")
image = "India_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("28_states_name.csv")
all_states = data.state.to_list()
guessed_states = []

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 State Correct",
                                    prompt="What's another state's name?").title()
    # want the prompt in this coordinate (114.0,264.0)
    print(answer_state)

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        #     missing_state = []
        #     for state in all_states:
        #         if state not in guessed_states:
        #             missing_state.append(state)

        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

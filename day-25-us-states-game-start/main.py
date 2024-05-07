import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



state_data = pd.read_csv('./50_states.csv')

all_state = state_data.state.to_list()
guessed_states = list()

print(all_state)

while len(guessed_states) < 50:
    usr_input = screen.textinput(title=f"{len(guessed_states)}/50 correct", prompt="Enter State")

    if usr_input == "Exit":
        break
    #if user input in data.csv then print state name at x,y values
    if usr_input.title() in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = state_data.state == usr_input.title()
        state_row = state_data[state].to_dict(orient='tight', index = False)
        state_info = list(*state_row["data"])
        state_x_coor = state_info[1]
        state_y_coor = state_info[2]
        t.goto(state_x_coor, state_y_coor)
        t.write(state_info[0])
        guessed_states.append(state_info[0])
    
for state in all_state:
    if state in guessed_states:
        all_state.remove(state)
        
print(all_state)
        
states_to_learn = pd.Series(all_state)
states_to_learn.to_csv("states_to_learn.csv")
screen.exitonclick()
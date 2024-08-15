import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    states_answer = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What is the states?").title() # when use the title() first letter of the word will be capital

    if states_answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                # missing_states.append(state)
                missing_data = state_data[state_data.state == state]
                m = turtle.Turtle()
                m.hideturtle()
                m.penup()
                m.goto(missing_data.x.item(), missing_data.y.item())
                m.color("red")
                m.write(missing_data.state.item(), font=("Arial", 8, "normal"))

        break

    if states_answer in all_states:
        guessed_states.append(states_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = state_data[state_data.state == states_answer]
        t.goto(data.x.item(), data.y.item())  #Identify the only item without index
        t.write(data.state.item())








screen.exitonclick()
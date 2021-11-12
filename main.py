import turtle
import pandas as pd
screen = turtle.Screen()
screen.setup(528,400)
image = "image.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("names.csv")
all_list = data.names.to_list()
guessed_districts = []
# x_cor = []
# y_cor = []
# def get_cor(x,y):
#     x_cor.append(x)
#     y_cor.append(y)
#     print(x_cor)
#     print(y_cor)
# screen.onscreenclick(get_cor)

while len(guessed_districts) < 30:
    guess = screen.textinput(title=f"{len(guessed_districts)} / 30 Districts Correct", prompt='What is next District?').title()

    if guess == "Exit":
        district_not_guessed = [i for i in all_list if i not in guessed_districts]
        missing_districts = pd.DataFrame(district_not_guessed)
        missing_districts.to_csv("missed_districts")
        break
    if guess in all_list:

        guessed_districts.append(guess)
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        cordinates = data[data["names"] == guess]
        tim.goto(int(cordinates.x), int(cordinates.y))
        tim.write(guess)
if len(guessed_districts) == 30:
    print("Congratulations you guessed all the districts. Pro genius")
screen.mainloop()
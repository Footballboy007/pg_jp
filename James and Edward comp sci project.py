import pyautogui as pg
import webbrowser
import time

sport = pg.prompt(
    """
Which sport do you like better?
a)Golf
b)Tennis
c)Squash

""")

if sport == "a":
    category = pg.prompt(
        """
What would you like to do?
a)Watch golf fails
b)Buy golf gear
c)Play golf on a course near you

        """)
    
    if category == "a":
        webbrowser.open("https://www.youtube.com/watch?v=OAK17RvcMto")

    if category == "b":
        webbrowser.open("https://www.tgw.com/golf-clubs")

    if category == "c":
        webbrowser.open("https://www.teeoff.com/search?gclid=EAIaIQobChMIsqbUso3Y2gIVUVcMCh2SgAFaEAAYASAAEgKCzPD_BwE#location=Greenwich%2C%20CT&view=course&date=4-26-2018")

elif sport == "b":
    category = pg.prompt(
        """
What would you like to do?
a)Watch tennis  highlights
b)Buy tennis gear


""")

    if category == "a":
        webbrowser.open("https://www.youtube.com/watch?v=rAtCkf3NBA4")

    if category == "b":
        webbrowser.open("http://www.tennis-warehouse.com/")



elif sport == "c":
    category = pg.prompt(
        """

What would you like to do?
a) Watch squash highlights
b) By squash gear
c) Learn how to play squash

""")
    if category == "a":
        webbrowser.open("https://www.youtube.com/watch?v=-KxgMl0Wp04")

    if category == "b":
        webbrowser.open("http://www.harrowsports.com/squash")

    if category == "c":
        webbrowser.open("http://www.squashgame.info/squashlibrary/2")










        

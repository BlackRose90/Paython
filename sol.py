import solara
from my_lib.area import find_area


clicks = solara.reactive(0)


@solara.component
def Page():
    # Radio Button (Area, permiter)
    # radio button (Square, Rectangle , circle)
    #Circle: Radius
    radius = 5
    find_area(5)
    # Square side:
    #Rectangle: Width, Height

    # Permiter is ""
    # Area is ""
    color = "green"
    if clicks.value >= 5:
        color = "red"

    def increment():
        clicks.value += 1
        print("clicks", clicks)  # noqa

    solara.Button(label=f"Clicked: {clicks}", on_click=increment, color=color)

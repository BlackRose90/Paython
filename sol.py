import solara
from solara.alias import rv

Calculator_initial = """
# Large
## Smaller

## List items

    * item 1
    * item 2
## Code highlight support
```python
code = "formatted" and "supports highlighting"
```

    """.strip()


@solara.component
def Calculator():
  area = side * side
side = 5

def find_area(r):
    PI = 3.124
    PI * (r*r)

def areaRectangle(a,b):
    return (a*b)
def perimeterRectangle(a,b):
    return (2*(a+b))
a=6
b=5
print("area = ", areaRectangle(a,b))
print("perimeter = ", perimeterRectangle(a,b))


# create an alias of the Calculate component so Solara can find it
Page = Calculator 

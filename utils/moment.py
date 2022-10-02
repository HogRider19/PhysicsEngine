

def rect_moment(a: float, b: float, mas: float) -> float:
    moment = a*b/12 * mas
    return moment
    

def circle_moment(r: float, mas: float) -> float:
    moment = 3.14*r**4/64*mas
    return moment


def rect_moment(a: float, b: float) -> float:
    moment = a*b/12
    return moment
    

def circle_moment(r: float) -> float:
    moment = 3.14*r**4/64
    return moment
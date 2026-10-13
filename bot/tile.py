"""Map tile (x, y) -> screen pixel for the current view.
screen = (OX + S*(y-x), OY + S/2*(x+y)), S = 8 at zoom 3, 16 at zoom 4.
Re-calibrate (cal) whenever the view scrolls or zooms."""
import json, sys
CAL = "/tmp/sc/cal.json"
def load():
    return json.load(open(CAL))
def to_screen(x, y):
    c = load(); s = c["s"]
    return round(c["ox"] + s*(y-x)), round(c["oy"] + s/2*(x+y))
def to_tile(sx, sy):
    c = load(); s = c["s"]
    a = (sx - c["ox"]) / s; b = (sy - c["oy"]) / (s/2)   # a = y-x, b = x+y
    return round((b - a) / 2), round((a + b) / 2)
if __name__ == "__main__":
    if sys.argv[1] == "cal":   # cal X Y SX SY S : tile X,Y is at screen SX,SY, tile step S
        x, y, sx, sy, s = map(float, sys.argv[2:7])
        json.dump({"s": s, "ox": sx - s*(y-x), "oy": sy - s/2*(x+y)}, open(CAL, "w")); print(load())
    elif sys.argv[1] == "inv":
        print(*to_tile(float(sys.argv[2]), float(sys.argv[3])))
    else:
        print(*to_screen(float(sys.argv[1]), float(sys.argv[2])))

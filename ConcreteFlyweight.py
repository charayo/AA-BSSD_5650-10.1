from Flyweight import Flyweight


class ConcreteFlyweight(Flyweight):
    """
    Implement the Flyweight interface and add storage for intrinsic
    state, if any. A ConcreteFlyweight object must be sharable. Any
    state it stores must be intrinsic; that is, it must be independent
    of the ConcreteFlyweight object's context.
    """

    def __init__(self):
        super().__init__()
        self.color = None
        self.shape = ""

    def set_color(self, color):
        if color == "white":
            self.color = (255, 255, 255)
        elif color == "black":
            self.color = (0, 0, 0)
        elif color == "red":
            self.color = (247, 21, 45)

    def set_shape(self, shape):
        self.shape = shape

    def operation(self, extrinsic_state):
        print("You asked me to do this extrinsic thing:", extrinsic_state)
        # pass

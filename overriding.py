class ParentPoint:
    is_parent = True

    def print_me(self):
        print("I am a parent point")


class ChildPoint(ParentPoint):
    is_parent = False

    def print_me(self):
        print("I am a child point")


parent = ParentPoint()
parent.print_me()
print(parent.is_parent)


child = ChildPoint()
child.print_me()
print(child.is_parent)

def equilateral(sides):
    is_greater_than_zero= sides[0] > 0 and sides[1] > 0 and sides[2] > 0
    sum_of_two_sides_equal= is_greater_than_zero and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]
    return sum_of_two_sides_equal and sides[0] == sides[1] and sides[1] == sides[2] and sides[0] == sides[2]

def isosceles(sides):
    is_valid= sides[0] > 0 and sides[1] > 0 and sides[2] > 0 and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]
    return is_valid and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])

def scalene(sides):
    is_valid= sides[0] > 0 and sides[1] > 0 and sides[2] > 0 and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]
    return is_valid and not(sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])
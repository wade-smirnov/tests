import random

class Generator:
    @staticmethod
    def location(x=0,y=0,z=0):
        return f"({x},{y},{z})"

    @staticmethod
    def random_location():
        axis = []
        for i in range(3):
            axis.append(round(random.uniform(-100, 100),5))
        return f"({axis[0]},{axis[1]},{axis[2]})"

    @staticmethod
    def rotation(x=0,y=0,z=0):
        return f"({x},{y},{z})"

    @staticmethod
    def scale(x=1,y=1,z=1, size = 'default'):
        match size:
            case 'small':
                scale = []
                for i in range(3):
                    scale.append(round(random.uniform(0.1, 0.5),5))
                return f"({scale[0]},{scale[1]},{scale[2]})"
            case 'normal':
                scale = []
                for i in range(3):
                    scale.append(round(random.uniform(0.9, 1.5),5))
                return f"({scale[0]},{scale[1]},{scale[2]})"
            case 'huge':
                scale = []
                for i in range(3):
                    scale.append(round(random.uniform(5, 50),5))
                return f"({scale[0]},{scale[1]},{scale[2]})"
            case _:
                return f"({x},{y},{z})"

    @staticmethod
    def random_scale():
        scale = []
        for i in range(3):
            scale.append(round(random.uniform(0.1, 100),5))
        return f"({scale[0]},{scale[1]},{scale[2]})"
    
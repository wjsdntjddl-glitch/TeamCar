class Car:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def json_default(obj):
        if isinstance(obj, Car):
            return {
                "name": obj.name,
            }

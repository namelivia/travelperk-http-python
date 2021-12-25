class DataclassWrapper:
    @staticmethod
    def wrap(_class, data):
        return _class(**data)

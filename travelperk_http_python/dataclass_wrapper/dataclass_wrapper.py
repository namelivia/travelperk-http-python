import inspect


class DataclassWrapper:
    @staticmethod
    def wrap(_class, data):
        arguments = inspect.getfullargspec(_class.__init__).args
        arguments.pop(0)  # Remove self
        filtered_data = {}
        extra_values = []
        for attr, value in data.items():
            if attr in arguments:
                filtered_data[attr] = value
            else:
                extra_values.append(attr)  # TODO: These should be reported
        return _class(**filtered_data)

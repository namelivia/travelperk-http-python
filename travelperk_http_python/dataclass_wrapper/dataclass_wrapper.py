import inspect


class DataclassWrapper:
    @staticmethod
    def _filter_dict(_class, data):
        class_description = inspect.getfullargspec(_class.__init__)
        arguments = class_description.args
        arguments.pop(0)  # Remove self
        filtered_data = {}
        extra_values = []
        for attr, value in data.items():
            if attr in arguments:
                filtered_data[attr] = DataclassWrapper._get_filtered_item(
                    value, attr, class_description
                )
            else:
                extra_values.append(attr)  # TODO: These should be reported
        return filtered_data

    @staticmethod
    def _get_filtered_item(value, attr, class_description):
        if type(value) is dict:
            return DataclassWrapper._filter_dict(
                DataclassWrapper._get_target_class(attr, class_description), value
            )
        if type(value) is list:
            return DataclassWrapper._filter_list(value, attr, class_description)
        return value

    @staticmethod
    def _filter_list(_list, attr, class_description):
        return [
            DataclassWrapper._get_filtered_item(item, attr, class_description)
            for item in _list
        ]

    @staticmethod
    def _is_list_annotation(_class):
        return _class.__module__ == "typing" and _class.__name__ == "List"

    @staticmethod
    def _get_target_class(attr, class_description):
        result = class_description.annotations[attr]
        if DataclassWrapper._is_list_annotation(result):
            return result.__args__[0]
        return result

    @staticmethod
    def wrap(_class, data):
        return _class(**DataclassWrapper._filter_dict(_class, data))

class Helpers:

    def check_list_of_type(lst, expected_type):
        # Проверяет, является ли переданный объект списком и содержит ли он элементы указанного типа.
        return isinstance(lst, list) and all(isinstance(item, expected_type) for item in lst)
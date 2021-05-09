import datetime


def logger_path(path: str):
    def logger(old):
        """Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась
        и возвращаемое значение."""

        def logger_new(*args, **kwargs):
            func_to_log = old(*args, **kwargs)
            date = datetime.datetime.now()
            name = old.__name__
            with open(f"{path}/start.log", 'a', encoding='utf-8') as f:
                f.writelines(
                    ['Дата : ', str(date), '\n', 'Имя функции :', name, '\n', 'Аргументы :', str(args), str(kwargs),
                     '\n', 'Значение : ', str(func_to_log)])

            return func_to_log

        return logger_new

    return logger

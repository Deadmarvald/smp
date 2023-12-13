from colorama import Fore
from shared import color_processor


def flatten_json(json_data: dict, parent_key: str = '', delimiter='_'):
    if (not isinstance(json_data, dict) and not isinstance(parent_key, str)
            and not isinstance(delimiter, str)):
        raise ValueError("Wrong data types!")
    flat_data = {}

    for key, value in json_data.items():
        new_key = parent_key + delimiter + key if parent_key else key

        if isinstance(value, dict):
            flat_data.update(flatten_json(value, new_key, delimiter))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                flat_data.update(flatten_json({str(i): item}, new_key, delimiter))
        else:
            flat_data[new_key] = value

    return flat_data


def display_flattened_json(jsons, color_position: int = 4):
    if ((not isinstance(jsons, dict) or not isinstance(jsons, list))
            and not isinstance(color_position, int)):
        raise ValueError("Wrong data types!")
    if color_position < 0 or color_position > len(color_processor.colors):
        raise ValueError("Wrong color position!")
    if isinstance(jsons, list):
        for _, json_data in enumerate(jsons):
            flat_json = flatten_json(json_data)
            for key, value in flat_json.items():
                print(getattr(Fore, color_processor.colors[color_position]) + f'{key}:'
                      + Fore.RESET + f' {value}')

    elif isinstance(jsons, dict):
        flat_json = flatten_json(jsons)
        for key, value in flat_json.items():
            print(getattr(Fore, color_processor.colors[color_position])
                  + f'{key}:' + Fore.RESET + f' {value}')


class JSONProcessor:

    @staticmethod
    def flatten_json(json_data: dict, parent_key: str = '', delimiter='_'):
        if (not isinstance(json_data, dict) and not isinstance(parent_key, str)
                and not isinstance(delimiter, str)):
            raise ValueError("Wrong data types!")
        flat_data = {}

        for key, value in json_data.items():
            new_key = parent_key + delimiter + key if parent_key else key

            if isinstance(value, dict):
                flat_data.update(JSONProcessor.flatten_json(value, new_key, delimiter))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    flat_data.update(JSONProcessor.flatten_json({str(i): item}, new_key, delimiter))
            else:
                flat_data[new_key] = value

        return flat_data

    @staticmethod
    def display_flattened_json(jsons, color_position: int = 4):
        if ((not isinstance(jsons, dict) or not isinstance(jsons, list))
                and not isinstance(color_position, int)):
            raise ValueError("Wrong data types!")
        if color_position < 0 or color_position > len(color_processor.colors):
            raise ValueError("Wrong color position!")
        if isinstance(jsons, list):
            for _, json_data in enumerate(jsons):
                flat_json = JSONProcessor.flatten_json(json_data)
                for key, value in flat_json.items():
                    print(getattr(Fore, color_processor.colors[color_position]) + f'{key}:'
                          + Fore.RESET + f' {value}')

        elif isinstance(jsons, dict):
            flat_json = JSONProcessor.flatten_json(jsons)
            for key, value in flat_json.items():
                print(getattr(Fore, color_processor.colors[color_position])
                      + f'{key}:' + Fore.RESET + f' {value}')

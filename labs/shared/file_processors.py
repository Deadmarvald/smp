import json
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


class FileProcessor:

    @staticmethod
    def write_into_file(file_path: str, text: str) -> None:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def read_from_json(file_path: str) -> dict:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def write_into_json(file_path: str, jsons: list) -> None:
        jsons_text_representation = json.dumps(jsons, indent=4)
        json.loads(jsons_text_representation)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(jsons_text_representation)

    def write_into_csv(file_path: str, json_data: list) -> None:
        df = pd.json_normalize(json_data)
        df.to_csv(file_path, index=False)

    @staticmethod
    def write_into_txt(file_path: str, json_data: list) -> None:
        with open(file_path, "w", encoding="utf-8") as file:
            for item in json_data:
                file.write(json.dumps(item, indent=4))
                file.write("\n\n")


class CsvProcessor:

    @staticmethod
    def read(file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)

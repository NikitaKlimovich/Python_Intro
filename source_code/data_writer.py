import json

from dict2xml import dict2xml


class DataWriter:
    def __init__(self, write_folder):
        self.path_to_write = write_folder

    def write_info(self, file_name, output_format, info):
        if output_format == "json":
            result = json.dumps(info, indent=4)
        if output_format == "xml":
            result = dict2xml(info, indent="   ")
        with open(self.path_to_write + file_name, "w") as res_file:
            res_file.write(result)

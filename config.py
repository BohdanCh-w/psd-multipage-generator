"""Configuration for application"""
from pathlib import Path

import yaml


class Config:
    """App configuration"""

    __srs = "source"
    __dst = "destination"
    __tpl = "template"
    __prc = "precise"

    def __init__(self, path: str = None):
        if path is None:
            self.source = None
            self.destination = None
            self.template = None
            self.precise = False
        else:
            self.read_from_file(path)

    def read_from_file(self, path: str) -> None:
        """Read configuration from file specified by path"""

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)["config"]

                for key in (self.__srs, self.__dst, self.__tpl, self.__prc):
                    if key not in data:
                        raise KeyError(f"{key} pararmeter is missing")
                    if "value" not in data[key]:
                        raise KeyError(f"value missing in {key}")

                self.source = Path(data[self.__srs]["value"])
                self.template = Path(data[self.__tpl]["value"])
                self.precise = data[self.__prc]["value"]

                if data[self.__dst]["value"] != "":
                    self.destination = Path(data[self.__dst]["value"])
                else:
                    self.destination = self.source.parents[0] / "output.psd"

        except FileNotFoundError:
            print("Configuration file not found")
            exit(1)
        except KeyError as err:
            print("Bad configuration file - key is missing : " + str(err))
            exit(1)

        if self.destination is None:
            self.destination = self.source.parents[0]

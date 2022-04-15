'''Configuration for application'''
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
            with open(path, 'r', encoding='utf-8') as f:
                data: dict = yaml.safe_load(f)
                if 'config' in data.keys():
                    self._parse_config_v1(data)
                else:
                    self._parse_config_v2(data)

        except FileNotFoundError as err:
            raise FileNotFoundError("Configuration file not found") from err
        except KeyError as err:
            raise KeyError("Bad configuration file") from err

    def _parse_config_v1(self, data: dict) -> None:
        data = data['config']
        for key in (self.__srs, self.__tpl, self.__prc):
            if key not in data:
                raise KeyError(f'{key} pararmeter is missing')
            if 'value' not in data[key]:
                raise KeyError(f'value missing in {key}')

        self.source = Path(data[self.__srs]['value'])
        self.template = Path(data[self.__tpl]['value'])
        self.precise = data[self.__prc]['value']

        if not data.get(self.__dst):
            self.destination = self.source.parents[0] / 'output.psd'
        else:
            self.destination = Path(data[self.__dst])

    def _parse_config_v2(self, data: dict) -> None:
        for key in (self.__srs, self.__tpl, self.__prc):
            if key not in data:
                raise KeyError(f'{key} pararmeter is missing')

        self.source = Path(data[self.__srs])
        self.template = Path(data[self.__tpl])
        self.precise = data[self.__prc]

        if not data.get(self.__dst):
            self.destination = self.source.parents[0] / 'output.psd'
        else:
            self.destination = Path(data[self.__dst])

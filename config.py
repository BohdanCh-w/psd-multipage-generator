'''Configuration for application'''
from pathlib import Path

import yaml


class Config:
    '''App configuration'''

    def __init__(self, path: str = None):
        if path is None:
            self.sourse = None
            self.destination = None
            self.template = None
        else:
            self.read_from_file(path)

    def read_from_file(self, path: str) -> None:
        '''Read configuration from file specified by path'''

        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)['config']

                for key in ('sourse', 'destination', 'template'):
                    if key not in data:
                        raise KeyError(f'{key} pararmeter is missing')
                    if 'value' not in data[key]:
                        raise KeyError(f'value missing in {key}')

                self.sourse = Path(data['sourse']['value'])
                self.template = Path(data['template']['value'])

                if data['destination']['value'] != '':
                    self.destination = Path(data['destination']['value'])
                else:
                    self.destination = self.sourse.parents[0] / 'output.psd'

        except FileNotFoundError:
            print("Configuration file not found")
            exit(1)
        except KeyError as err:
            print("Bad configuration file - key is missing : " + str(err))
            exit(1)

        if self.destination is None:
            self.destination = self.sourse.parents[0]

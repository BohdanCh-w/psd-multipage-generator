"""Startup point"""

import sys
from os import listdir
from config import Config
import new_service
from helpers import validate

def validate_config(config: Config) -> None:
    """Validate configuration check for existance"""
    requirements = [
        (config.source.exists(), "specified sourse directory does not exist"),
        (config.source.is_dir(), "specified sourse is not a directory"),
        (lambda: len(listdir(config.source)) > 0, "sourse directory is empty"),
        #
        (config.destination.parents[0].exists(), "specified destination folder does not exist"),
        (config.destination.parents[0].is_dir(), "specified destination is not a directory"),
        (config.destination.name.endswith(".psd"), "destination is not a .psd file"),
        #
        (config.template.exists(), "specified template file does not exist"),
        (config.template.name.endswith(".psd"), "specified template is not a .psd file"),
    ]

    for req in requirements:
        validate(req[0], req[1])


def generate_file(config: Config) -> None:
    """Use Psd Service to generate output file"""
    srv = new_service.PsdService(new_service.new_photoshop_app())
    srv.generate_file(config.source, config.destination, config.template, config.precise)


def main():
    """Main function"""
    config_file = sys.argv[1] if len(sys.argv) > 1 else "config.yaml"
    config = Config(config_file)
    validate_config(config)

    generate_file(config)


if __name__ == "__main__":
    main()

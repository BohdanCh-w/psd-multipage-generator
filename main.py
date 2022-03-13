"""Startup point"""

import sys
import shutil
from config import Config
from psd_service import PsdService


def validate(condition: bool, error: str) -> bool:
    """Validate condition"""

    if not condition:
        print("Error: ", error)
        return False
    return True


def validate_config(config: Config) -> None:
    """Validate configuration check for existance"""

    requirements = [
        (config.sourse.is_dir(), "specified sourse directory does not exist"),
        (config.template.is_file(), "specified template file does not exist"),
        (config.destination.parents[0].is_dir(), "specified destination folder does not exist"),
        (config.destination.name.endswith(".psd"), "destination is not a .psd file"),
        (config.template.name.endswith(".psd"), "template is not a .psd file"),
    ]

    for req in requirements:
        if not validate(req[0], req[1]):
            exit(1)


def generate_file(config: Config) -> None:
    """Use Psd Service to generate output file"""

    file = str(config.destination.resolve())
    srv = PsdService()

    shutil.copyfile(config.template, config.destination)
    srv.populate(file, config.sourse, False)


def main():
    """Main function"""

    config_file = sys.argv[1] if len(sys.argv) > 1 else "config.yaml"
    config = Config(config_file)
    validate_config(config)

    generate_file(config)


if __name__ == "__main__":
    main()

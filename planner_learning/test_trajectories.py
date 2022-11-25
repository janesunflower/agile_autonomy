import argparse

from config.settings import create_settings
from dagger_training import Trainer
import os


def main():
    parser = argparse.ArgumentParser(description='Evaluate Trajectory tracker.')
    # parser.add_argument('--settings_file', help='Path to settings yaml', required=True)
    parser.add_argument('--settings_file', help='Path to settings yaml', default="config/test_settings.yaml")

    args = parser.parse_args()
    root = os.path.abspath(os.path.dirname(__file__)) +"/"
    settings_filepath = root + args.settings_file
    # settings_filepath = args.settings_file
    print("settings_filepath: ", settings_filepath)
    settings = create_settings(settings_filepath, mode='test')
    trainer = Trainer(settings)
    trainer.perform_testing()


if __name__ == "__main__":
    main()

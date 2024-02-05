import yaml
from argparse import ArgumentParser

def arguments(location: list[str] | None):
    """
    Function to get user inputs
    """
    parser = ArgumentParser()

    parser.add_argument("location", help="Location to YAML file")
    args = parser.parse_args(location)
    yaml_reader(args.location)

def yaml_reader(loc: str):
    """
    Function to read YAML config file
    """
    with open(loc, "r") as yamlfile:
     data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print(data)


## Here arguments() is the main function
if __name__ == "__main__":
    arguments()

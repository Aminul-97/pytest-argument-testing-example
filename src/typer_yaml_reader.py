import yaml
import typer
import os
app = typer.Typer()

@app.command()
def main(configpath: str) -> None:
    """
    Main function to read YAML file

    Args:
    configpath: path to the YAML file

    Returns:
    None
    """

    if configpath and os.path.isfile(configpath):
        yaml_reader(configpath)
    else:
        print(
            f"`configpath` must be a valid file path. Provided path: `{configpath}` does not exist."
        )

def yaml_reader(path: str) -> None:
    """
    Function to read YAML config file
    """
    try:
        with open(path, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            print(data)
    except Exception as e:
        print(f"Error reading YAML file: {e}")

if __name__ == "__main__":
    app()

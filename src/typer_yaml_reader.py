import yaml
import typer

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
    yaml_reader(configpath)

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

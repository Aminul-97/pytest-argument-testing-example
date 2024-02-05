import yaml
import typer

app = typer.Typer()

@app.command()
def user_input(location:str):
    """
    Function to get user inputs
    """
    yaml_reader(location)

def yaml_reader(loc: str):
    """
    Function to read YAML config file
    """
    with open(loc, "r") as yamlfile:
     data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print(data)

## Here app() is the main function
if __name__ == '__main__':
    app()
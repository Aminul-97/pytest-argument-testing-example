from typer.testing import CliRunner
from src.typer_yaml_reader import app
import pytest
import shlex

runner = CliRunner()

# Test cases with location and expected result
test_cases = [
    (
        "src/yaml_configs/config.yml",  # Valid path without optional args
        "{'url': 'https://example.com/', 'port': 3001}",
    ),
    (
        "src/yaml_configs/config.yml --env 'dev'",  # Valid path witho optional args
        "{'url': 'https://dev.com/', 'port': 3010}",
    ),
    (
        "--env 'prod' 'src/yaml_configs/config.yml'",  # Different order
        "{'url': 'https://prod.com/', 'port': 2007}",
    ),
    (
        "src/config.yml --env 'prod'",  # Path not exist 
        "`configpath` must be a valid file path. Provided path: `src/config.yml` does not exist.",
    ),
    (
        " ",  # Null or None value passed 
        "Missing argument",
    ),
    (
        "",  # No argument passed
        "Missing argument",
    ),
    (
        "'src/yaml_configs/config.yml' -env 'dev'",  # Invalid flag
        "No such option",
    ),
    (
        "src/yaml_configs==config.yml --env 'dev'",  # Invalid ascii character passsed
        "`configpath` must be a valid file path. Provided path: `src/yaml_configs==config.yml` does not exist.",
    ),
    (
        "path/to/nonexistent/file.yml --env 'dev'",  # Nonexistent file
        "`configpath` must be a valid file path. Provided path: `path/to/nonexistent/file.yml` does not exist.",
    ),
]

# Testing typer_yaml_reader()
@pytest.mark.parametrize("command, expected_output", test_cases)
def test_typer_yaml_reader(command, expected_output):
    result = runner.invoke(app, shlex.split(command))
    assert expected_output in result.stdout


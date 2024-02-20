from typer.testing import CliRunner
from src.typer_yaml_reader import app
import pytest
import shlex

runner = CliRunner()

# Test cases with location and expected result
test_cases = [
    (
        "src/yaml_configs/config.yml",  # Valid path 
        "{'rest': {'url': 'https://example.com/', 'port': 3001}, 'details': 'A Demo Website'}",
    ),
     (
        "src/config.yml",  # Path not exist 
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
        "src/yaml_configs==config.yml",  # Invalid ascii character passsed
        "`configpath` must be a valid file path. Provided path: `src/yaml_configs==config.yml` does not exist.",
    ),
    (
        "path/to/nonexistent/file.yml",  # Nonexistent file
        "`configpath` must be a valid file path. Provided path: `path/to/nonexistent/file.yml` does not exist.",
    ),
]

# Testing typer_yaml_reader()
@pytest.mark.parametrize("command, expected_output", test_cases)
def test_typer_yaml_reader(command, expected_output):
    result = runner.invoke(app, shlex.split(command))
    assert expected_output in result.stdout


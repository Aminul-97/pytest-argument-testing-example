from typer.testing import CliRunner
from src.typer_yaml_reader import app
import pytest
import shlex

runner = CliRunner()

# Test cases with location and expected result
test_cases = [
    ("src/yaml_configs/config.yml", "{'rest': {'url': 'https://example.com/', 'port': 3001}, 'details': 'A Demo Website'}"),
    ("src/yaml_configs/server_config.yml", "{'server': {'ip': '172.0.0.1', 'port': 81}}")
]

# Testing typer_yaml_reader()
@pytest.mark.parametrize('command, expected_output', test_cases)
def test_typer_yaml_reader(command, expected_output):
    result = runner.invoke(app, shlex.split(command))
    assert result.exit_code == 0
    assert expected_output in result.stdout


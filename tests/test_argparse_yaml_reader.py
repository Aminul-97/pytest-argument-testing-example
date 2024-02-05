from src.argparse_yaml_reader import arguments
import pytest
import shlex

# Test cases with location and expected result
test_cases = [
    ("src/yaml_configs/config.yml", "{'rest': {'url': 'https://example.com/', 'port': 3001}, 'details': 'A Demo Website'}"),
    ("src/yaml_configs/server_config.yml", "{'server': {'ip': '172.0.0.1', 'port': 81}}")
]


# Testing argparse_yaml_reader()
@pytest.mark.parametrize('command, expected_output', test_cases)
def test_argparse_yaml_reader(capsys, command, expected_output):
    arguments(shlex.split(command))
    output = capsys.readouterr().out.rstrip()
    assert output == expected_output
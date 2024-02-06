from src.argparse_yaml_reader import main
import pytest
import shlex

# Test cases with location and expected result
test_cases = [
    ("--configpath 'src/yaml_configs/config.yml'", "{'rest': {'url': 'https://example.com/', 'port': 3001}, 'details': 'A Demo Website'}"),
    ("--configpath 'src/yaml_configs/server_config.yml'", "No such file or directory"),
    ("", "Error reading YAML file: expected str, bytes or os.PathLike object")
]


# Testing argparse_yaml_reader()
@pytest.mark.parametrize('command, expected_output', test_cases)
def test_argparse_yaml_reader(capsys, command, expected_output):
    main(shlex.split(command))
    output = capsys.readouterr().out.rstrip()
    assert expected_output in output
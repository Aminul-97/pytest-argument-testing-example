import pytest
import shlex
from src.argparse_yaml_reader import main, yaml_reader
from typer.testing import CliRunner
from src.typer_yaml_reader import app


# Fixture to get user inputs and find expected outputs
@pytest.fixture
def get_user_input(request):
    yaml_location = str(request.config.getoption("--yaml_location"))
    env = str(request.config.getoption("--env"))
    expected_output = str(yaml_reader(yaml_location, env))
    return yaml_location, env, expected_output

# Testing argparse_yaml_reader()
def test_argparse_yaml_reader(capsys, get_user_input):
    yaml_location, env, expected_output = get_user_input
    main(shlex.split("--configpath "+yaml_location+ " --env "+env))
    output = capsys.readouterr().out.rstrip()
    assert expected_output in output

runner = CliRunner()

# Testing typer_yaml_reader()
def test_typer_yaml_reader(get_user_input):
    yaml_location, env, expected_output = get_user_input
    result = runner.invoke(app, shlex.split(yaml_location + " --env " + env))
    assert expected_output in result.stdout



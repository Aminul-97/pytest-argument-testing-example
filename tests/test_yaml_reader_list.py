from src.argparse_yaml_reader import main
from typer.testing import CliRunner
from src.typer_yaml_reader import app


def test_argparse_yaml_with_list(capsys):
    test_args = ['--configpath', 'src/yaml_configs/config.yml', '--env', 'rest'] 
    print(test_args)
    expected_output = "{'url': 'https://example.com/', 'port': 3001}"
    main(test_args)
    output = capsys.readouterr().out.rstrip()
    assert expected_output in output


def test_typer_yaml_with_list():
    runner = CliRunner()
    test_args = ['src/yaml_configs/config.yml', '--env', 'rest'] 
    result = runner.invoke(app, test_args)
    assert result.exit_code == 0
    # Use result.stdout to access the command's output
    output = result.stdout.rstrip()
    expected_output = "{'url': 'https://example.com/', 'port': 3001}"
    assert expected_output in output

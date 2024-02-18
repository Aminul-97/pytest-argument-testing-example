from src.argparse_yaml_reader import main

def test_argparse_yaml_with_list(capsys):
    test_args = ["--configpath", "src/yaml_configs/config.yml"]
    expected_output = "{'rest': {'url': 'https://example.com/', 'port': 3001}, 'details': 'A Demo Website'}"
    main(test_args)
    output = capsys.readouterr().out.rstrip()
    assert expected_output in output
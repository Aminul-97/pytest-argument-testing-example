def pytest_addoption(parser):
    parser.addoption(
        "--yaml_location", action="store", help="Location to YAML file"
    )
    parser.addoption(
        "--env", action="store", help="Location to YAML file"
    )

# pytest -v tests/test_yaml_reader_custom_cli.py --yaml_location="src/yaml_configs/config.yml" --env="dev"
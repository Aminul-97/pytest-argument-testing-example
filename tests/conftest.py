def pytest_addoption(parser):
    parser.addoption("--configpath", action="store", help="Location to YAML file")
    parser.addoption("--env", action="store", help="Environment to read from YAML file")


# pytest -v tests/test_yaml_reader_custom_cli.py --yaml_location="src/yaml_configs/config.yml" --env="dev"

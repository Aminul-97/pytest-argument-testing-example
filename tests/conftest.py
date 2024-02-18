def pytest_addoption(parser):
    parser.addoption(
        "--yaml_location", action="store", help="Location to YAML file"
    )

# pytest -v --yaml_location="src/yaml_configs/config.yml"
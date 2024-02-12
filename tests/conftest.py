def pytest_addoption(parser):
    parser.addoption(
        "--yaml_location", action="store", help="Location to YAML file"
    )
    parser.addoption(
        "--expected_output", action="store", help="Expected output"
    )

# pytest -v --yaml_location="src/yaml_configs/config.yml" --expected_output="{'rest': {'url': 'https://example.com/', 'port': 3001}, 'details': 'A Demo Website'}"
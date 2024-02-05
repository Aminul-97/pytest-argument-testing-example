def pytest_addoption(parser):
    parser.addoption(
        "--yaml_location", action="store", default="10", help="Location to YAML file"
    )
    parser.addoption(
        "--expected_output", action="store", help="Expected output"
    )

# pytest -v --yaml_location="src/yaml_configs/server_config.yml" --expected_output="{'server': {'ip': '172.0.0.1', 'port': 81}}"
# pytest -v --yaml_location="src/yaml_configs/config.yml" --expected_output="{'rest': {'url': 'https://example.com/', 'port': 3001}, 'details': 'A Demo Website'}"
import json
from os import environ

expected_input_files = json.loads(environ["EXPECTED_INPUT_FILES"])
expected_output_files = json.loads(environ["EXPECTED_OUTPUT_FILES"])
actual_input_files = json.loads(environ["ACTUAL_INPUT_FILES"])
actual_output_files = json.loads(environ["ACTUAL_OUTPUT_FILES"])

assert set(expected_input_files) == set(actual_input_files)
assert set(expected_output_files) == set(actual_output_files)

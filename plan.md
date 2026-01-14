# JSON Parser Plan

## Steps

- Get JSON-formatted text
- Create custom object
- Store JSON data as dictionary
- Parse text for colon-separated values
    - Check for nested JSON
    - Create sub-dictionaries
    - Recursively parse for colon-separated values
    - Keys can only be strings
    - Values may be strings, integers, floats, object, array, boolean, null
    - Need to convert values to their corresponding types
- Assume JSON will be valid when testing
- Create helpful functions

## Desired Features

- Convert string in JSON format to custom object
- Give object helpful functions and properties
- Read from string or file

## Anticipated Problems

- Whitespace
- Nested entries
- Mixed data types

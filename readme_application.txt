# Python version: 3.12.1

# Run the application:
	- from the root on the command line run: python application.py --input_file events.json --window_size 10
	- the results are saved in the root in the file output.json

# Run the unit tests:
	- from the root on the command line run: python -m unittest discover

# File structure:

project_root/
│
| application.py # Run the application
| readme.txt # Application description
| setup.py # Modules to install (empty file)
|
├── packages/
│   ├── __init__.py
│   └── calculator.py # Contains the calculation service to calculate the moving average
    └── data_processor.py # Contains the data processor service to process the received json file, preprocess it and save it
│
└── tests/
    ├── __init__.py
    └── test_calculator.py # Test cases for calculation service
    └── test_data_processor.py # Test cases for data processor service
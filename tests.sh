#!/bin/bash

echo "Running Blackbox Tests"
pytest tests/blackboxTests.py -v
echo "Running Step 3: Static Analysis"
prospector
echo "Running Step 5: Static Analysis 2"
python3 -m mccabe --min 5 interviewIterations/interview3.py



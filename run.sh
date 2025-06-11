#!/bin/bash

set +e

CURRENT_DATE_TIME=$(date +"%Y-%m-%d_%H.%M")
echo "Current Date and Time: ${CURRENT_DATE_TIME}"

# Run pytest in headless mode
#python -m pytest -m "sanity or regression" --reruns 2 --browser_name chrome --headless tests/ --html=reports/report_${CURRENT_DATE_TIME}.html

# Run pytest headed mode with the HTML report option including the timestamp
#python -m pytest -m "sanity or regression" --reruns 2 --browser_name chrome tests/ --html=reports/report_${CURRENT_DATE_TIME}.html

# Run pytest in parallel mode with pytest-xdist library
python -m pytest -m "sanity or regression" -n auto --browser_name chrome tests/ --html=reports/report_${CURRENT_DATE_TIME}.html

# Generate allure report single file
allure generate --single-file ./reports/allure-results -o ./reports/allure-reports --clean
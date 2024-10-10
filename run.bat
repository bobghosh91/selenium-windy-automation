@echo off

REM Get current date and time in a format suitable for filenames
set timestamp=%DATE:/=-%_%TIME::=-%
REM Remove milliseconds from the time part
set timestamp=%timestamp:~0,-6%
REM Remove leading spaces from the time part
set timestamp=%timestamp: =%

REM Run pytest with the HTML report option including the timestamp
@REM python -m pytest -m "sanity or regression" --reruns 2 --browser_name chrome tests\ --html=reports/report_%timestamp%.html

REM Run pytest in headless mode
@REM python -m pytest -m "sanity or regression" --reruns 2 --browser_name --headless chrome tests\ --html=reports/report_%timestamp%.html

REM Run pytest headed
python -m pytest -m "sanity or regression" --reruns 2 --browser_name chrome tests\ --html=reports/report_%timestamp%.html
@REM python -m pytest -n auto --browser_name chrome tests\
@REM python -m pytest --browser_name chrome tests\

REM generate allure report single file
allure generate --single-file ./reports/allure-results -o ./reports/allure-reports --clean
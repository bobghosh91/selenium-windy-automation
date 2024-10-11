# Selenium Windy Automation
This project automates the Windy website, showcasing various weather-related functionalities using 
Selenium, Pytest, and other modern Python utilities. 
The framework is built with simplicity, re-usability, and scalability in mind.

## Table of Contents
1. [Selenium Windy Automation](#selenium-windy-automation)
2. [Key Features](#key-features)
   - [Browser Invocation (Builder Pattern)](#browser-invocation-builder-pattern)
   - [Custom Logger](#custom-logger)
   - [Parameterized Testing](#parameterized-testing)
   - [Docker Compose](#docker-compose)
3. [Setup Instructions](#setup-instructions)
4. [Docker Compose Usage](#docker-compose-usage)
5. [Deploying Docker Compose on AWS EC2](#deploying-docker-compose-on-aws-ec2)


## Key Features
### Browser Invocation (Builder Pattern):
The browser instantiation is managed using the Builder Pattern, enhancing code readability and maintainability. 
This design allows the framework to switch easily between Chrome, Edge, and Firefox, minimizing code duplication. 
It also supports headless execution for faster CI pipeline runs or when executing tests remotely

### Custom Logger:

A custom logger has been integrated, which exports logs simultaneously to:
 - A log file
 - The console
 - Allure reports for in-depth analysis and better test traceability.

### Parameterized Testing:

Parameterization is demonstrated using both:
 - *pytest.mark.parametrize*: 
   - For running test cases with multiple input datasets.
 - *openpyxl*: 
   - To handle parameterization from Excel files, making it easy to manage test data for multiple test cases dynamically.

### Docker Compose:

`docker-compose` and `dynamic-docker-compose` configurations have been added to the project, allowing you to choose between these setups based on your preference.
Instructions for deploying the docker-compose on remote engines like AWS EC2 are included below.

## Setup Instructions
1. **Clone or Download the Repository:**
   - Clone or download the repo and open in any IDE of choice(pycharm preferred).
2. **Replace Credentials:**
   - Create a free account on [windy.com](https://windy.com).
   - Make sure to update the config.ini file with your actual email and password to avoid authentication issues during test execution.

3. **Install Dependencies:**
   - Open terminal at root folder.
   - all dependencies required are stored in requirements.txt. Run the following command in terminal.
       ```bat
       pip install -r requirements.txt
       ```
       or, if in bash environment:
       ```bash
       pip3 install -r requirements.txt
       ```
 
   > **Note:** It's recommended to use Python's virtual environment `(venv)` to create an isolated environment and then install the dependencies. This is the preferred approach for managing project dependencies.

4. **Run Tests:**
    ```
    python -m pytest -m "sanity or regression" --browser_name chrome tests\ --alluredir=./reports/allure-results
    ```
    > You can refer to the `run.bat` file in the root directory for additional methods to run tests and generate reports, or simply execute the file to start the tests. If you're using macOS, create a `run.sh` (bash) script to achieve the same functionality.

5. **Generating Allure Reports:**
   - Once the test run is completed, you can generate the Allure report using the following command:

    ```bash
    allure generate --single-file ./reports/allure-results -o ./reports/allure-reports --clean
    ```
   > The `--clean` flag is used to empty the allure-results folder before the next run

## Enable static website hosting on S3 bucket
    `aws s3 website s3://your-bucket-name/ --index-document index.html`

## Set the bucket policy to allow public access to the website
```
aws s3api put-bucket-policy --bucket your-bucket-name --policy '{
  "Version": "2012-10-17",
  "Statement":[
    {
        "Sid": "AllowPublicReadAccess",
        "Effect": "Allow",
        "Principal": "*",
        "Action": [
            "s3:GetObject",
            "s3:GetObjectVersion"
        ],
        "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}'
```
This setup generates a custom URL that can be easily shared with stakeholders, enabling them to access and review the test results. 
Ensure that the AWS CLI is installed on your machine for integration.

### Docker Compose Usage:

- You can deploy this project using Docker Compose, allowing easy setup of testing environments:
  * `docker-compose.yml`: Standard Docker compose file.
  * `dynamic-docker-compose.yml`: Enhanced version with dynamic configurations.

- Execute the following command to start the containers and run the tests:
    > `docker-compose -f docker-compose.yml up -d`

    **Ensure to use `webdriver.Remote` when running tests in a remote environment.**

### Deploying Docker Compose on AWS EC2:
To deploy your Docker Compose setup on an AWS EC2 instance, follow these steps:
1. **SSH into your EC2 Instance:** Connect to your EC2 instance via SSH. Ensure Docker and Docker Compose are pre-installed on your instance.
2. **Copy the Docker Compose File:** Copy the chosen docker-compose file to instance root:
    ```bash
    scp -i /path/to/your-key.pem /path/to/your-file.yml ubuntu@ec2-instance-public-ip:/destination`
    ```
3. **Run the Docker Compose:** Once transferred, run the following command on the EC2 instance:
    ```bash
    docker-compose -f docker-compose.yml up -d`
    ```
4. **Update WebDriver URL:** Make sure to replace `http://localhost:4444/wd/hub` with the actual URL of your remote WebDriver server. For example `http://<ec2-ip-address>:<port>`

You can now run the tests remotely on your EC2 instance.

### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

Happy Testing!
## Table of Contents
1. [Introduction](#selenium-windy-automation)
2. [Key Features](#key-features)
   - [Browser Invocation (Builder Pattern)](#browser-invocation-builder-pattern)
   - [Custom Logger](#custom-logger)
   - [Parameterized Testing](#parameterized-testing)
   - [Allure Report Integration](#allure-reporting-integration)
   - [Docker Compose](#docker-compose)
3. [Prerequisites](#prerequisites)
4. [Setup Instructions](#setup-instructions)
5. [Docker Compose Usage](#docker-compose-usage)
6. [Deploying Docker Compose on AWS EC2](#deploying-docker-compose-on-aws-ec2)
7. [Uploading Allure Report to S3](#uploading-allure-report-to-s3)
8. [Contributing](#contributing)


# Selenium Windy Automation
This project automates the Windy website, showcasing various weather-related functionalities using 
Selenium, Pytest, and other modern Python utilities. 
The framework is built with simplicity, re-usability, and scalability in mind.
---
## Key Features

---
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

### Allure Reporting Integration:

`Allure Reports` have been integrated into the framework to provide visually rich and interactive test reports. 
It helps track test execution history, view detailed step-by-step test results, and debug failures more efficiently.
Allure reports can be generated post-test execution, providing stakeholders with easy access to the results in an intuitive format.

### Docker Compose:

`docker-compose` and `dynamic-docker-compose` configurations have been added to the project, allowing you to choose between these setups based on your preference.
Instructions for deploying the docker-compose on remote engines like AWS EC2 are included below.

## Prerequisites

---
Before setting up and running the project, ensure you have the following installed:

1. **Python:** (<u>strictly version 3.10 and above</u>)
2. **pip:**
   - Comes with Python 3.x installations. Verify it using:
     ```bash
     pip --version
     ```
3. **Allure Command Line**
   - Used for generating and viewing Allure reports.
   - Install via the command line:
     - For MacOS:
       ```bash
       brew install allure
       ```
     - For Windows: Download the [Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline) and follow the installation steps.

4. **Docker** and **Docker Compose** (for running the Docker setup)
   - Install Docker and Docker-Compose from their [official](https://docs.docker.com/) website.

5. **AWS CLI** (for uploading reports to S3, optional)
   - You can install the AWS CLI from [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

Ensure that all dependencies are installed before proceeding to the [Setup Instructions](#setup-instructions).

## Setup Instructions

---
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


## Docker Compose Usage:

---
- You can deploy this project using Docker Compose, allowing easy setup of testing environments:
  * `docker-compose.yml`: Standard Docker compose file.
  * `dynamic-docker-compose.yml`: Enhanced version with dynamic configurations.

- Execute the following command to start the containers and run the tests:
    > `docker-compose -f docker-compose.yml up -d`

    **Ensure to use `webdriver.Remote` when running tests in a remote environment.**

## Deploying Docker Compose on AWS EC2:

---
To deploy your Docker Compose setup on an AWS EC2 instance, follow these steps:
1. **Copy the Docker Compose File:** Copy the chosen docker-compose file to instance root:
    ```bash
    scp -i /path/to/your-key.pem /path/to/your-file.yml ubuntu@ec2-instance-public-ip:/destination`
    ```
2. **SSH into your EC2 Instance:** Connect to your EC2 instance via SSH. Ensure Docker and Docker Compose are pre-installed on your instance.
    ```bash
    ssh -i /path/to/your-key.pem ubuntu@ec2-public-ip
    ```
   
3. **Run the Docker Compose:** Once transferred, run the following command on the EC2 instance:
    ```bash
    docker-compose -f docker-compose.yml up -d`
    ```
4. **Update WebDriver URL:** Make sure to replace `http://localhost:4444/wd/hub` with the actual URL of your remote WebDriver server. For example `http://<ec2-ip-address>:<port>`

5. **Running Tests from Jenkins**:
    - From your Jenkins pipeline, ensure the remote WebDriver URL is correctly configured to point to the EC2 instance.
    - Trigger the Jenkins job to run tests remotely on the AWS EC2 instance.

You can now run the tests remotely on your EC2 instance.

### Running Tests in Jenkins

---
This project includes a ready-to-use Jenkins pipeline configuration to automate test execution.
Follow these steps to set up and run tests using Jenkins:

### Prerequisites for Jenkins
1. **Jenkins Installation**: Ensure Jenkins is installed and running on your system or server. Refer to the official Jenkins installation guide for setup instructions.
2. **Jenkins Plugins**: Make sure the following plugins are installed:
   - Allure Jenkins Plugin (for Allure reporting)
   - Docker Pipeline Plugin (for Docker Compose execution)
   - SSH Agent Plugin (for deploying on AWS EC2)
   - Python Plugin (if you’re executing Python scripts directly)
   
### Configuring the Jenkins Pipeline

1. **Add the Jenkinsfile**: Copy the content of  `Jenkinsfile` from the project’s root directory into your Jenkins job. The pipeline job is already configured with steps to run tests, generate Allure reports, and archive the results.
   
2. **Pipeline Job Execution**:
    - After setting up your pipeline, trigger the job manually or set up a schedule for automated runs.
    - The tests will execute based on the configurations provided, and Allure reports will be generated for visual representation of the results.
    
3. **Viewing Results**:
   - Once the job is complete, you can view the Allure reports directly in Jenkins.
   - Navigate to the `Allure Report` link in the Jenkins build console.

## Uploading Allure Report to S3

---
To easily share Allure reports with stakeholders, you can upload the generated report to an S3 bucket and enable public access via a static website. Follow these steps to configure S3 for hosting and sharing your Allure report.

1. Enable Static Website Hosting
   -    First, enable static website hosting on your S3 bucket. This will allow the report to be accessed via a public URL.

    ```bash
    aws s3 website s3://your-bucket-name/ --index-document index.html
    ```

2. Set Public Access Policy
    ```bash
   aws s3api put-bucket-policy --bucket your-bucket-name --policy '{
    "Version": "2012-10-17",
    "Statement": [
    {
      "Sid": "PublicReadGetObject",
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

3. Share the URL:
   - Once the tests are completed and the Allure report is generated, you can upload the single-file Allure report to an S3 bucket for easy sharing and access.

   - The steps to upload the Allure report to S3 are already included in the `Jenkinsfile`. Ensure the bucket access policy is set to public, as explained [above](#uploading-allure-report-to-s3).

    > For example: http://my-bucket-name.s3.website-region.amazonaws.com


### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

Happy Testing!
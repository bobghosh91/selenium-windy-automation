# Selenium Windy Automation
This project automates the Windy website, showcasing various weather-related functionalities using 
Selenium, Pytest, and other modern Python utilities. 
The framework is built with simplicity, re-usability, and scalability in mind.

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
 - pytest.mark.parametrize: 
   - For running test cases with multiple input datasets.
 - openpyxl: 
   - To handle parameterization from Excel files, making it easy to manage test data for multiple test cases dynamically.

### Docker Compose:

docker-compose and dynamic-docker-compose configurations have been added to the project, allowing you to choose between these setups based on your preference.
Instructions for deploying the docker-compose on remote engines like AWS EC2 are included below.

# Setup Instructions
1. Replace Credentials:

 - Create a free account in windy.com
 - Make sure to update the config.ini file with your actual email and password to avoid authentication issues during test execution.

2. How to Run:

 - Clone or download the repo and open in any IDE of choice(pycharm preferred).
 - Open terminal at root folder.
 - all dependencies required are stored in requirements.txt. Run the following command in terminal.
   > pip install -r requirements.txt
   ---
   > pip3 install - r requirements.txt
 
Note: The following dependencies will be installed globally on your system. However, it's recommended to use Python's virtual environment `(venv)` to create an isolated environment and then install the dependencies. This is the preferred approach for managing project dependencies.
 - To execute tests with parameterization:
   >python -m pytest -m "sanity or regression" --browser_name chrome tests\ --alluredir=./reports/allure-results

You can also refer to the `run.bat` file in the root directory for more ways to run tests and generate report.

Once the test run is completed, Allure will generate a single HTML report in the /reports/allure-reports folder.
This file is useful for sharing reports with stakeholders or can be uploaded to cloud storage services like an S3 bucket. The S3 bucket can also be customized to act as a static web hosting location. By enabling web hosting, S3 will provide a custom URL that can be shared with stakeholders or other parties, allowing them to view the results.

```
# Enable static website hosting on S3 bucket
aws s3 website s3://your-bucket-name/ --index-document index.html --error-document error.html

# Set the bucket policy to allow public access to the website
aws s3api put-bucket-policy --bucket your-bucket-name --policy '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}'
```
### Docker Compose Usage:

- You can deploy this project using Docker Compose, allowing easy setup of testing environments:
   - docker-compose.yml: Standard Docker compose file.
   - dynamic-docker-compose.yml: Enhanced version with dynamic configurations.

- Ensure to use webdriver.remote for remote execution.

- Run the following command to bring up the containers:
    > `docker-compose -f docker-compose.yml up -d`

### Deploying Docker Compose on AWS EC2:
- Connect to your EC2 instance via SSH. As a pre-requisite docker and docker-compose is required in your instance
- Copy the chosen docker-compose file to instance root:
  >`scp -i /path/to/your-key.pem /path/to/your-file.yml ubuntu@ec2-instance-public-ip:/destination`
  > 
  >`docker-compose -f docker-compose.yml up -d`
- Make sure to replace `http://localhost:4444/wd/hub` with the actual URL of your remote WebDriver server. For example `http://<ec2-ip-address>:<port>`

You can now run the tests remotely on your EC2 instance.
Happy Testing!
# Schedule Checker

## Overview

The Schedule Checker project consists of several Python scripts that perform various tasks such as scraping schedules, comparing them, taking screenshots, and sending alerts via Discord. Each script has its specific functionality contributing to the overall goal of the project.

## Scripts

- **[dbConn.py]**: Establishes a connection to MongoDB to store schedule data.
- **[seleniumScreenshot.py]**: Utilizes Selenium to take screenshots of schedule webpages.
- **[scheduleChecker.py]**: Checks for schedule changes, scrapes schedules, and sends alerts.
- **[discordAlerts.py]**: Sends alerts to Discord channels when schedule changes are detected.
- **[utils.py]**: Contains utility functions for scraping schedules and computing differences.
- **[main.py]**: Entry point script to execute the schedule checking process.

## Installation and Setup

### Requirements

- pymongo
- python-dotenv
- undetected-chromedriver
- selenium
- requests
- beautifulsoup4
- deepdiff

### Installation

To install the necessary dependencies, run the following command in your terminal:

```
pip install -r requirements.txt
```

### Configuration

Before running the scripts, ensure you have set up the necessary environment variables. Refer to the `.env.example` file for the required variables.

Configure the environment variables in your .env file as needed

## Usage

To execute the schedule checker, run the `main.py` script:

```
py main.py
```

## Contributing

Contributions to the Schedule Checker project are welcome! If you'd like to contribute, feel free to submit pull requests or open issues on the GitHub repository.


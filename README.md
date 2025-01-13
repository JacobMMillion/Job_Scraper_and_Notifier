# Job Scraper and Notifier

This project consists of two Python scripts that work together to scrape the Teach For America (TFA) Learning Stream website for available tutoring positions and send an email notification when a new position is added.

## Files:
1. **send_message.py**: Handles sending email notifications to a specified email address.
2. **job_scraper.py**: Scrapes the TFA Learning Stream website for new tutoring positions and calls the `send_email_driver()` function from `send_message.py` to notify the user when a new position is added.

## Requirements:
- Python 3.x
- [Selenium](https://www.selenium.dev/documentation/webdriver/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

You can install the necessary libraries using pip:

```bash
pip install selenium webdriver-manager python-dotenv
```

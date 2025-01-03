from dotenv import dotenv_values

config = dotenv_values(".env")
EMAIL = config.get("EMAIL")
PASSWORD = config.get("PASSWORD")

# Playwright
MODE = "no-login"
LINKEDIN_HOME = "https://www.linkedin.com"
URL_LOGIN = "https://www.linkedin.com/uas/login"
LINKEDIN_KEYWORDS = ["python"]
LOCATION = "Brazil"
LINKEDIN_URL_SEARCH = f"https://www.linkedin.com/jobs/search/?keywords={" ".join(LINKEDIN_KEYWORDS)}&location={LOCATION}&refresh=false"
USER_DATA_DIR = 'playwright-context-data/'
MAX_TRIES = 20

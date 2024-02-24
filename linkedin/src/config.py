from dotenv import dotenv_values

config = dotenv_values(".env")
EMAIL = config.get("EMAIL")
PASSWORD = config.get("PASSWORD")
SESSION_STORAGE = config.get("SESSION_STORAGE")

URL_LOGIN = "https://www.linkedin.com/uas/login"

LINKEDIN_KEYWORDS = ["python"]
LOCATION = "Brazil"
LINKEDIN_URL_SEARCH = f"https://www.linkedin.com/jobs/search/?keywords={" ".join(LINKEDIN_KEYWORDS)}&location={LOCATION}&refresh=false"
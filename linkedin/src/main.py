from asyncio import run, sleep
from playwright.async_api import Page, async_playwright
from playwright._impl._errors import Error
from src.config import URL_LOGIN, EMAIL, PASSWORD, LINKEDIN_URL_SEARCH, USER_DATA_DIR, LINKEDIN_HOME, MAX_TRIES
import os
from rich import print


async def login(page: Page, email: str, password: str) -> Page:
	await page.goto(URL_LOGIN)
	await page.wait_for_load_state("domcontentloaded")

	await page.get_by_label("Email or phone").click()
	await page.get_by_label("Email or phone").fill(email)
	await page.get_by_label("Password").click()
	await page.get_by_label("Password").fill(password)
	await (
		page.locator("#organic-div form")
		.get_by_role("button", name="Sign in")
		.click()
	)
	await page.wait_for_load_state("load")
	return page


async def linkedin_load_search(page: Page) -> Page:
	for _ in range(MAX_TRIES):
		try:
			await page.goto(LINKEDIN_URL_SEARCH)
			await page.wait_for_load_state("networkidle")
			title = await page.title()
			print(f"Title of LINKEDIN_URL_SEARCH: {title}")
			if "Jobs in Brazil".lower() in title.lower():
				return page
		except Error as e:
			print(e)
			return page


def start_new_context() -> bool:
	if not os.path.exists(USER_DATA_DIR):
		os.mkdir(USER_DATA_DIR)
		return True
	return False


async def main() -> None:
	async with async_playwright() as p:
		start_new_context()

		browser = await p.chromium.launch_persistent_context(USER_DATA_DIR, headless=False)
		page = await browser.new_page()

		await linkedin_load_search(page)

		# await page.goto(LINKEDIN_URL_SEARCH)
		# # await page.wait_for_load_state()
		# await page.wait_for_load_state("networkidle")
		# title = await page.title()
		#
		# if "Jobs in Brazil" not in title:
		# 	await page.goto(LINKEDIN_URL_SEARCH)
		# 	await page.wait_for_load_state("networkidle")

		elements = await page.query_selector_all('.base-card')
		print(elements)
		print(len(elements))

		# Get the list of job ids
		# job_ids = [element.get_attribute('data-occludable-job-id') for element in elements]
		# print(job_ids)

		await sleep(120)

		# browser = await p.chromium.launch_persistent_context(USER_DATA_DIR, headless=False)
		# browser = await p.chromium.launch(headless=False)
		# page = await browser.new_page()

		# page = await login(page, EMAIL, PASSWORD)
		# await sleep(10)
		#
		# await page.goto(LINKEDIN_URL_SEARCH)
		# await sleep(20)


if __name__ == "__main__":
	run(main())

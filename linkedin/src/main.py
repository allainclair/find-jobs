from asyncio import run, sleep
from playwright.async_api import Page, async_playwright
from src.config import URL_LOGIN, EMAIL, PASSWORD, LINKEDIN_URL_SEARCH, SESSION_STORAGE


async def login(page: Page, email: str, password: str) -> Page:
	await page.goto(URL_LOGIN)
	await page.wait_for_load_state("load")

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


async def main() -> None:
	async with async_playwright() as p:
		user_data_dir = 'playwright-context-data/'
		browser = await p.chromium.launch_persistent_context(user_data_dir, headless=False)
		# browser = await p.chromium.launch(headless=False)
		page = await browser.new_page()

		# page = await login(page, EMAIL, PASSWORD)
		# await sleep(10)

		await page.goto(LINKEDIN_URL_SEARCH)
		await sleep(20)


if __name__ == "__main__":
	run(main())

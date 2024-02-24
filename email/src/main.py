from asyncio import run
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from datetime import datetime
from email.mime.text import MIMEText

from aiosmtplib import send

from src.config import config
from src.models import JobLinkedIn
from src.templating import template

# Examples only
job1 = JobLinkedIn(
	company="Google",
	date="2021-10-01",
	description="We are looking for a Python Developer to join our team.",
	location="Remote",
	matching_keywords=["Python", "Django"],
	title="Python Developer",
	url="https://www.linkedin.com/jobs/view/123456",
)
job2 = JobLinkedIn(
	title="JavaScript Developer",
	company="Facebook",
	location="Remote",
	matching_keywords=["JavaScript", "React"],
	description="We are looking for a JavaScript Developer to join our team.",
	date="2021-10-01",
	url="https://www.linkedin.com/jobs/view/123457",
)
linkedin_jobs = [job1, job2]


async def send_email() -> None:
	smtp_host = config["SMTP_HOST"]
	smtp_port = int(config.get("SMTP_PORT"))
	# assert isinstance(smtp_port, int), "SMTP_PORT must be an integer"

	sender_email = config.get("SENDER_EMAIL") or ""
	sender_password = config.get("SENDER_PASSWORD", "")
	recipient_email = config.get("RECIPIENT_EMAIL") or ""

	message = await build_mime_multipart_message(
		sender_email,
		recipient_email,
		linkedin_jobs,
	)
	await send(
		message,
		hostname=smtp_host,
		port=smtp_port,
		use_tls=True,
		username=sender_email,
		password=sender_password,
	)


async def build_mime_multipart_message(
	sender_email: str,
	recipient_email: str,
	jobs: list[JobLinkedIn],
) -> MIMEMultipart:
	message = MIMEMultipart("alternative")
	message["From"] = sender_email
	message["To"] = recipient_email
	message["Subject"] = "Welcome"
	html_message = template.render(jobs=jobs)

	attachment = MIMEBase('application', 'octet-stream')
	attachment.set_payload(html_message.encode("utf-8"))
	today_date = datetime.today().strftime('%Y-%m-%d')
	file_name = f"job-list-{today_date}.html"
	attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')

	body = MIMEText(
		f'Open the "{file_name}" file in a browser using internet to bring the styles.',
		"html",
		"utf-8",
	)

	message.attach(body)
	message.attach(attachment)

	return message


if __name__ == "__main__":
	run(send_email())

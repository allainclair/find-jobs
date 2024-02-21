from dataclasses import dataclass


@dataclass
class JobLinkedIn:
	company: str
	date: str
	description: str
	location: str
	matching_keywords: list[str]
	title: str
	url: str

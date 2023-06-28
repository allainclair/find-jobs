from pydantic import BaseModel, validator, AnyHttpUrl
from humps import camelize
from logging import getLogger

logger = getLogger(__name__)


class Summary(BaseModel):
    job_summary: str
    job_title_snippet: str
    search_text_snippet: str


class GoogleLocation(BaseModel):
    city: str
    country: str


class Job(BaseModel):
    google_locations: list[GoogleLocation]
    title: str
    primary_city: str
    primary_country: str
    url: AnyHttpUrl
    location_type: str | None = None


class SearchResult(BaseModel):
    summary: Summary
    job: Job


class PinterestSchema(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
    total_hits: int
    next_page_token: str | None = None
    search_results: list[SearchResult]

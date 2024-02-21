from pydantic import BaseModel
from apps.app.pinterest.pinterest_schema import PinterestSchema, SearchResult


class JobSchema(BaseModel):
    job_title: str
    country: str
    url: str
    city: str | None = None
    location_type: str | None = None  # Remote, On-site, Hybrid.


def map_pinterest_result_to_job_schema(result: SearchResult) -> JobSchema:
    return JobSchema(
        job_title=result.job.title,
        country=result.job.primary_country,
        url=result.job.url,
        city=result.job.primary_city,
        location_type=result.job.location_type,
    )


def map_pinterest_to_job_schema(pinterest_schema: PinterestSchema) -> list[JobSchema]:
    return [
        map_pinterest_result_to_job_schema(result)
        for result in pinterest_schema.search_results
    ]

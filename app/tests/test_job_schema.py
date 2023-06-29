from app.job_schema import map_pinterest_to_job_schema, map_pinterest_result_to_job_schema, JobSchema
from app.pinterest.pinterest_schema import PinterestSchema, SearchResult


def assert_job_schema_to_pinterest_search_result(job: JobSchema, search_result: SearchResult) -> None:
    assert job.job_title == search_result.job.title
    assert job.country == search_result.job.primary_country
    assert job.url == search_result.job.url
    assert job.city == search_result.job.primary_city
    assert job.location_type == search_result.job.location_type


def test_map_pinterest_result_to_job_schema(pinterest_schema: PinterestSchema) -> None:
    search_result = pinterest_schema.search_results[0]
    job = map_pinterest_result_to_job_schema(search_result)
    assert_job_schema_to_pinterest_search_result(job, search_result)


def test_map_pinterest_to_job_schema(pinterest_schema: PinterestSchema) -> None:
    # Limit to 3 results to not make too many calls.
    new_pinterest_schema = PinterestSchema(search_results=pinterest_schema.search_results[:3], total_hits=3)
    jobs = map_pinterest_to_job_schema(new_pinterest_schema)
    assert len(jobs) == len(new_pinterest_schema.search_results)
    for job, search_result in zip(jobs, new_pinterest_schema.search_results):
        assert_job_schema_to_pinterest_search_result(job, search_result)

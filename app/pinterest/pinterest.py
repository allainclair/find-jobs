from app.httpx_async_client import get_httpx_async_client
from httpx import Response
from app.pinterest.pinterest_schema import PinterestSchema
from app.pinterest.config import URL_TEMPLATE, TIMEOUT, PAGE_SIZE, QUERY
from urllib.parse import quote


def format_main_url() -> str:
    return URL_TEMPLATE.format(page_size=PAGE_SIZE, query=quote(QUERY))


async def get_all_jobs() -> PinterestSchema:
    url = format_main_url()
    do_request = True
    next_page_token: str | None = None
    pinterest_schemas = []
    while do_request:
        url = f"{url}&pageToken={next_page_token}" if next_page_token else url
        response = await _get(url)
        pinterest_schema = PinterestSchema.parse_obj(response.json())
        pinterest_schemas.append(pinterest_schema)
        next_page_token = pinterest_schema.next_page_token
        do_request = next_page_token is not None

    return _merge_schemas(pinterest_schemas)


async def _get(url: str, timeout: int = TIMEOUT) -> Response:
    async with get_httpx_async_client() as client:
        response = await client.get(url, timeout=timeout)
    response.raise_for_status()
    return response


def _merge_schemas(pinterest_schemas: list[PinterestSchema]) -> PinterestSchema:
    search_results = []
    for schema in pinterest_schemas:
        search_results += schema.search_results
    return PinterestSchema(total_hits=pinterest_schemas[0].total_hits, search_results=search_results)

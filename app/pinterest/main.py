import json
from asyncio import run
from app.httpx_async_client import get_httpx_async_client
from app.pinterest.config import URL, TIMEOUT
from app.pinterest.pinterest_schema import PinterestSchema

from icecream import ic


def clean_response_text(response: str):
    return response.lstrip("jobsCallback(").rstrip(")")


async def main() -> None:
    async with get_httpx_async_client() as client:
        response = await client.get(URL, timeout=TIMEOUT)

    response.raise_for_status()
    response_text = clean_response_text(response.text)
    response_object = json.loads(response_text)
    ic(response_object)
    pinterest_schema_1 = PinterestSchema.parse_obj(response_object)
    ic(pinterest_schema_1)
    print(pinterest_schema_1.total_hits)
    print(len(pinterest_schema_1.search_results))

    async with get_httpx_async_client() as client:
        response = await client.get(f"{URL}&pageToken={pinterest_schema_1.next_page_token}", timeout=TIMEOUT)
    ic(response)
    response.raise_for_status()
    response_text = clean_response_text(response.text)
    response_object = json.loads(response_text)
    pinterest_schema_2 = PinterestSchema.parse_obj(response_object)
    ic(pinterest_schema_2)
    print(pinterest_schema_2.total_hits)
    print(len(pinterest_schema_2.search_results))

    if pinterest_schema_1 == pinterest_schema_2:
        print("Equal...")


if __name__ == '__main__':
    run(main())

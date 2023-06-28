from app.pinterest.pinterest_schema import PinterestSchema
from app.pinterest.pinterest import _get, _merge_schemas, get_all_jobs, format_main_url
from httpx import Response, HTTPStatusError
import respx
from pytest import raises


@respx.mock
async def test_get_all_jobs(
        pinterest_schema_with_next_page_token: PinterestSchema,
        pinterest_schema: PinterestSchema,
        pinterest_merged_schemas: PinterestSchema,
) -> None:
    url = format_main_url()

    # First call with a next_page_token.
    route_1 = respx.get(url).mock(
        return_value=Response(200, json=pinterest_schema_with_next_page_token.dict(by_alias=True, exclude_none=True))
    )
    # Second call without a next_page_token.
    route_2 = respx.get(f"{url}&pageToken={pinterest_schema_with_next_page_token.next_page_token}").mock(
        return_value=Response(200, json=pinterest_schema.dict(by_alias=True, exclude_none=True))
    )

    pinterest_schema = await get_all_jobs()
    assert route_1.called
    assert route_2.called
    assert pinterest_schema == pinterest_merged_schemas


def test__merge_schemas(pinterest_schemas: list[PinterestSchema], pinterest_merged_schemas: PinterestSchema) -> None:
    assert _merge_schemas(pinterest_schemas) == pinterest_merged_schemas


@respx.mock
async def test__get_200() -> None:
    url = format_main_url()
    route = respx.get(url).mock(return_value=Response(200))
    response = await _get(url)
    assert route.called
    assert response.status_code == 200


@respx.mock
async def test__get_raise_for_status() -> None:
    url = format_main_url()
    respx.get(url).mock(return_value=Response(400))
    with raises(HTTPStatusError):
        await _get(url)

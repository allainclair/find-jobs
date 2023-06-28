from app.pinterest.pinterest_schema import PinterestSchema
from pytest import fixture

PATH = "app/pinterest/tests/fixture_pinterest_schema_1.json"


@fixture
def pinterest_schema() -> PinterestSchema:
    return PinterestSchema.parse_file(PATH)


@fixture
def pinterest_schema_with_next_page_token(pinterest_schema: PinterestSchema) -> PinterestSchema:
    return pinterest_schema.copy(update={"next_page_token": "next_page_token"})


@fixture
def pinterest_schemas(
        pinterest_schema_with_next_page_token: PinterestSchema,
        pinterest_schema: PinterestSchema
) -> list[PinterestSchema]:
    return [pinterest_schema_with_next_page_token, pinterest_schema]


@fixture
def pinterest_merged_schemas(
        pinterest_schema_with_next_page_token: PinterestSchema,
        pinterest_schema: PinterestSchema,
) -> PinterestSchema:
    return PinterestSchema(
        total_hits=pinterest_schema_with_next_page_token.total_hits,
        search_results=pinterest_schema_with_next_page_token.search_results + pinterest_schema.search_results
    )

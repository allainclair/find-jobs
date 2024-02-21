from asyncio import run
from app.pinterest.pinterest import get_all_jobs

from icecream import ic


async def main() -> None:
    pinterest_schema = await get_all_jobs()
    ic(pinterest_schema.dict(exclude_none=True))
    ic(len(pinterest_schema.search_results))


if __name__ == '__main__':
    run(main())

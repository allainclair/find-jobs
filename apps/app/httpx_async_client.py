from httpx import AsyncClient
from logging import getLogger

logger = getLogger(__name__)

_httpx_async_client: AsyncClient | None = None


def get_httpx_async_client() -> AsyncClient:
    """Returning the same global instance of httpx.AsyncClient if exists or create a new one."""
    global _httpx_async_client

    if _httpx_async_client is None or _httpx_async_client.is_closed:
        _httpx_async_client = AsyncClient()
        logger.info("AsyncClient has been created successfully.")

    return _httpx_async_client


async def close_httpx_async_client() -> None:
    """Closing global instance of httpx.AsyncClient if it exists or not closed."""
    global _httpx_async_client

    if _httpx_async_client is not None:
        await _httpx_async_client.aclose()
        logger.info("httpx.AsyncClient session has been closed successfully.")
        _httpx_async_client = None

    return None

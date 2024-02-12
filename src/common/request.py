from asyncio.exceptions import TimeoutError
from datetime import datetime
from typing import Any
from uuid import UUID

from aiohttp import ClientResponse, ClientSession
from aiohttp.client_exceptions import ClientConnectionError, ContentTypeError
from loguru import logger

from src.common.logger import LoggerManager
from src.config import settings


class RequestManager:
    _timeout: int = settings.request.TIMEOUT

    _logger: logger = LoggerManager.get_request_logger()

    @staticmethod
    def _process_params(params: dict) -> dict:
        processed_params = {}
        for param in params.keys():
            param_value = params[param]
            if param_value is not None:
                if isinstance(param_value, UUID) or isinstance(param_value, datetime):
                    param_value = str(param_value)
                processed_params[param] = param_value
        return processed_params

    @staticmethod
    def _process_payload(payload: dict | list) -> dict | list:
        if isinstance(payload, dict):
            processed_payload = {}
            for param in payload.keys():
                param_value = payload[param]
                if isinstance(param_value, UUID) or isinstance(param_value, datetime):
                    param_value = str(param_value)
                processed_payload[param] = param_value
        else:
            processed_payload = []
            for i in range(len(payload)):
                params = payload[i]
                if hasattr(params, "model_dump"):
                    params = params.model_dump()
                if hasattr(params, "dict"):
                    params = params.dict()
                processed_params = {}
                for param in params.keys():
                    param_value = params[param]
                    if isinstance(param_value, UUID) or isinstance(
                        param_value, datetime
                    ):
                        param_value = str(param_value)
                    processed_params[param] = param_value
                processed_payload.append(processed_params)
        return processed_payload

    @classmethod
    def _get_params(
        cls, params: dict | None, unprocessed_params: dict | None
    ) -> dict | None:
        if unprocessed_params:
            if not params:
                params = {}
            params.update(cls._process_params(params=unprocessed_params))
        return params

    @classmethod
    def _get_payload(
        cls, payload: dict | list | str | None, unprocessed_payload: dict | list | None
    ) -> dict | None:
        if unprocessed_payload:
            if not payload:
                if isinstance(unprocessed_payload, dict):
                    payload = {}
                if isinstance(unprocessed_payload, list):
                    payload = []
            if isinstance(payload, dict):
                payload.update(cls._process_payload(payload=unprocessed_payload))
            if isinstance(payload, list):
                payload.extend(cls._process_payload(payload=unprocessed_payload))
        return payload

    @classmethod
    async def aio_get(
        cls,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        unprocessed_params: dict | None = None,
    ) -> tuple[ClientResponse | None, Any | None]:
        params = cls._get_params(
            params=params,
            unprocessed_params=unprocessed_params,
        )

        client = ClientSession()

        response = None
        content = None

        try:
            response = await client.get(
                url=url, headers=headers, params=params, timeout=cls._timeout
            )
            content = await response.json(encoding="utf-8")
        except ClientConnectionError:
            cls._logger.error(
                f"Connect request exception From: {url} with Params: {params}"
            )
        except ContentTypeError:
            cls._logger.error(
                f"Content request exception From: {url} with Params: {params}"
            )
        except TimeoutError:
            cls._logger.error(
                f"Timeout request exception From: {url} with Params: {params}"
            )
        except Exception as e:
            cls._logger.error(f"Exception: {e} From: {url} with Params: {params}")
        finally:
            await client.close()

        return response, content

    @classmethod
    async def aio_post(
        cls,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        unprocessed_params: dict | None = None,
        payload: dict | list | str | None = None,
        unprocessed_payload: dict | list | None = None,
    ) -> tuple[ClientResponse | None, Any | None]:
        params = cls._get_params(
            params=params,
            unprocessed_params=unprocessed_params,
        )
        payload = cls._get_payload(
            payload=payload,
            unprocessed_payload=unprocessed_payload,
        )

        client = ClientSession()

        response = None
        content = None

        try:
            response = await client.post(
                url=url,
                headers=headers,
                params=params,
                json=payload,
                timeout=cls._timeout,
            )
            content = await response.json(encoding="utf-8")
        except ClientConnectionError:
            cls._logger.error(
                f"Connect request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except ContentTypeError:
            cls._logger.error(
                f"Content request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except TimeoutError:
            cls._logger.error(
                f"Timeout request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except Exception as e:
            cls._logger.error(
                f"Exception: {e} From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        finally:
            await client.close()

        return response, content

    @classmethod
    async def aio_put(
        cls,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        unprocessed_params: dict | None = None,
        payload: dict | list | str | None = None,
        unprocessed_payload: dict | list | None = None,
    ) -> tuple[ClientResponse | None, Any | None]:
        params = cls._get_params(
            params=params,
            unprocessed_params=unprocessed_params,
        )
        payload = cls._get_payload(
            payload=payload,
            unprocessed_payload=unprocessed_payload,
        )

        client = ClientSession()

        response = None
        content = None

        try:
            response = await client.put(
                url=url,
                headers=headers,
                params=params,
                json=payload,
                timeout=cls._timeout,
            )
            content = await response.json(encoding="utf-8")
        except ClientConnectionError:
            cls._logger.error(
                f"Connect request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except ContentTypeError:
            cls._logger.error(
                f"Content request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except TimeoutError:
            cls._logger.error(
                f"Timeout request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except Exception as e:
            cls._logger.error(
                f"Exception: {e} From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        finally:
            await client.close()

        return response, content

    @classmethod
    async def aio_patch(
        cls,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        unprocessed_params: dict | None = None,
        payload: dict | list | str | None = None,
        unprocessed_payload: dict | list | None = None,
    ) -> tuple[ClientResponse | None, Any | None]:
        params = cls._get_params(
            params=params,
            unprocessed_params=unprocessed_params,
        )
        payload = cls._get_payload(
            payload=payload,
            unprocessed_payload=unprocessed_payload,
        )

        client = ClientSession()

        response = None
        content = None

        try:
            response = await client.patch(
                url=url,
                headers=headers,
                params=params,
                json=payload,
                timeout=cls._timeout,
            )
            content = await response.json(encoding="utf-8")
        except ClientConnectionError:
            cls._logger.error(
                f"Connect request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except ContentTypeError:
            cls._logger.error(
                f"Content request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except TimeoutError:
            cls._logger.error(
                f"Timeout request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except Exception as e:
            cls._logger.error(
                f"Exception: {e} From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        finally:
            await client.close()

        return response, content

    @classmethod
    async def aio_delete(
        cls,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        unprocessed_params: dict | None = None,
        payload: dict | list | str | None = None,
        unprocessed_payload: dict | list | None = None,
    ) -> tuple[ClientResponse | None, Any | None]:
        params = cls._get_params(
            params=params,
            unprocessed_params=unprocessed_params,
        )
        payload = cls._get_payload(
            payload=payload,
            unprocessed_payload=unprocessed_payload,
        )

        client = ClientSession()

        response = None
        content = None

        try:
            response = await client.delete(
                url=url,
                headers=headers,
                params=params,
                json=payload,
                timeout=cls._timeout,
            )
            content = await response.json(encoding="utf-8")
        except ClientConnectionError:
            cls._logger.error(
                f"Connect request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except ContentTypeError:
            cls._logger.error(
                f"Content request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except TimeoutError:
            cls._logger.error(
                f"Timeout request exception From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        except Exception as e:
            cls._logger.error(
                f"Exception: {e} From: {url}"
                f" with Params: {params} and Payload: {payload}"
            )
        finally:
            await client.close()

        return response, content

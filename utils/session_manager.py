import requests
import logging
from typing import Optional
from datetime import datetime, timedelta
from dify_plugin.config.logger_format import plugin_logger_handler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(plugin_logger_handler)


class ZoomInfoSessionManager:
    def __init__(self, username: str, password: str, storage):
        self.username = username
        self.password = password
        self.storage = storage
        self.token_key = f"zoominfo_jwt_{username}"
        self.token_expiry_key = f"zoominfo_jwt_expiry_{username}"

        logger.info(f"Initialized ZoomInfo session manager for user: {username[:3]}***")

    def _authenticate(self) -> Optional[str]:
        logger.info(f"Starting authentication for user: {self.username[:3]}***")

        try:
            auth_payload = {
                "username": self.username,
                "password": self.password
            }

            headers = {
                "Content-Type": "application/json"
            }

            logger.info("Sending authentication request to ZoomInfo API")
            response = requests.post(
                "https://api.zoominfo.com/authenticate",
                headers=headers,
                json=auth_payload,
                timeout=30
            )

            logger.info(f"Authentication response status: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                token = result.get("jwt")
                if token:
                    expiry_time = datetime.now() + timedelta(minutes=55)
                    logger.info(f"Authentication successful, token expires at: {expiry_time.isoformat()}")
                    self._store_token(token, expiry_time)
                    return token
                else:
                    logger.error("Authentication response missing JWT token")
                    raise Exception("Authentication response missing JWT token")
            elif response.status_code == 401:
                logger.error("Authentication failed: Invalid username or password")
                raise Exception("Invalid ZoomInfo username or password")
            else:
                logger.error(f"Authentication failed with status {response.status_code}: {response.text}")
                raise Exception(f"Authentication failed with status {response.status_code}: {response.text}")

        except requests.exceptions.Timeout as e:
            logger.error(f"ZoomInfo authentication request timed out: {e}")
            raise Exception(
                f"ZoomInfo authentication request timed out after 30 seconds. Check your network connection: {e}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Failed to connect to ZoomInfo API: {e}")
            raise Exception(f"Failed to connect to ZoomInfo API. Check your network connection: {e}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error during ZoomInfo authentication: {e}")
            raise Exception(f"Network error during ZoomInfo authentication: {e}")
        except Exception as e:
            if "Invalid ZoomInfo" in str(e) or "Authentication failed" in str(e):
                raise e
            else:
                logger.error(f"Unexpected error during ZoomInfo authentication: {e}")
                raise Exception(f"Unexpected error during ZoomInfo authentication: {e}")

        return None

    def _store_token(self, token: str, expiry_time: datetime) -> None:
        try:
            logger.info("Storing JWT token in persistent storage")

            token_size = len(token.encode('utf-8'))
            expiry_str = expiry_time.isoformat()
            expiry_size = len(expiry_str.encode('utf-8'))
            total_size = token_size + expiry_size

            logger.info(
                f"JWT token size: {token_size} bytes, expiry size: {expiry_size} bytes, total: {total_size} bytes")

            self.storage.set(self.token_key, token.encode('utf-8'))
            self.storage.set(self.token_expiry_key, expiry_str.encode('utf-8'))

            logger.info("JWT token successfully stored in persistent storage")

        except Exception as e:
            logger.warning(f"Failed to store JWT token in persistent storage: {e}")
            logger.info("Plugin will authenticate on each request when storage is unavailable")
            pass

    def _get_stored_token(self) -> Optional[str]:
        logger.info("Checking for stored JWT token")

        try:
            token_bytes = self.storage.get(self.token_key)
            if not token_bytes:
                logger.info("No stored JWT token found")
                return None

            token = token_bytes.decode('utf-8')

            expiry_bytes = self.storage.get(self.token_expiry_key)
            if not expiry_bytes:
                logger.warning("Stored token found but no expiry information, considering invalid")
                return None

            expiry_str = expiry_bytes.decode('utf-8')
            expiry_time = datetime.fromisoformat(expiry_str)

            current_time = datetime.now()
            if current_time + timedelta(minutes=1) < expiry_time:
                logger.info(f"Valid stored token found, expires at: {expiry_time.isoformat()}")
                return token
            else:
                logger.info(f"Stored token expired at: {expiry_time.isoformat()}, cleaning up")
                self._clear_stored_token()
                return None

        except Exception as e:
            logger.warning(f"Error reading stored token: {e}")
            return None

    def _clear_stored_token(self) -> None:
        try:
            logger.info("Clearing stored JWT token from persistent storage")
            self.storage.delete(self.token_key)
            self.storage.delete(self.token_expiry_key)
            logger.info("Successfully cleared stored JWT token")
        except Exception as e:
            logger.warning(f"Error clearing stored token: {e}")
            pass

    def get_valid_token(self) -> str:
        logger.info("Getting valid JWT token")

        token = self._get_stored_token()
        if token:
            logger.info("Using cached JWT token")
            return token

        logger.info("No valid cached token, authenticating for new token")
        token = self._authenticate()
        if not token:
            logger.error("Failed to obtain JWT token from ZoomInfo")
            raise Exception("Failed to obtain JWT token from ZoomInfo")

        logger.info("Successfully obtained new JWT token")
        return token

    def refresh_token(self) -> str:
        logger.info("Force refreshing JWT token")

        self._clear_stored_token()

        new_token = self.get_valid_token()
        logger.info("JWT token successfully refreshed")
        return new_token

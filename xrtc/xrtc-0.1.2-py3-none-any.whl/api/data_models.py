"""Data Models for XRTC: connection, login, set/get API. Pydantic is used for parsing."""
from pydantic import BaseSettings, BaseModel, Field


class ConnectionConfiguration(BaseSettings):
    """Connection configuration"""

    # Connection URL
    login_url: str = Field("https://api.xrtc.org/v1/auth/login", env="LOGIN_URL")
    set_url: str = Field("https://api.xrtc.org/v1/item/set", env="SET_URL")
    get_url: str = Field("https://api.xrtc.org/v1/item/get", env="GET_URL")

    # Default timeouts and connection limits

    # aiohttp
    # Duration of the whole operation incl connection establishment, request sending & response reading, seconds
    aiohttp_timeout_total: int = 20

    # Duration of new connection or for waiting for a free connection from a pool if limits are exceeded, seconds
    aiohttp_timeout_connect: float = 5

    # Duration of connecting to a peer for a new connection, not given from a pool, seconds
    aiohttp_timeout_sock_connect: float = 5

    # Duration of the period between reading a new data portion from a peer, seconds
    aiohttp_timeout_sock_read: float = 10

    # Duration of the DNS entries expiry, seconds
    aiohttp_timeout_dns_cache: int = 3600

    # Total number simultaneous connections to any hosts
    aiohttp_limit_connections: int = 100

    # Total number of concurrent requests
    aiohttp_limit_concurrent_requests: int = 5

    # requests
    # Duration the client will wait to establish a connection to a remote machine
    requests_connect: float = 5.0

    # Duration the client will wait for the server to send a response and in between of the bytes, seconds
    requests_read: float = 10.0

    class Config:
        """Read configuration from default .env"""

        env_file = "xrtc.env"


class LoginCredentials(BaseSettings):
    """Loging configuration"""

    accountid: int = Field(..., env="ACCOUNT_ID")
    apikey: str = Field(..., env="API_KEY")

    class Config:
        """Read configuration from default .env"""

        env_file = "xrtc.env"


class Item(BaseModel):
    """Data model for API element Item"""

    portalid: str
    payload: str
    servertimestamp: int = 0


class Portal(BaseModel):
    """Data model for API element Portal"""

    portalid: str
    servertimestamp: int = 0


class SetItemRequest(BaseModel):
    """Data model for API request item/set"""

    items: list[Item]


class GetItemRequest(BaseModel):
    """Data model for API request item/get"""

    portals: list[Portal] = None
    polling: int = 0


class ReceivedData(BaseModel):
    """Data model for API response item/get"""

    items: list[Item] = None


class Error(BaseModel):
    """Data model for API response item/get"""

    errorgroup: int = 0
    errorcode: int = 0
    errormessage: str = None


class ReceivedError(BaseModel):
    """Data model for API response item/get"""

    error: Error = None


class XRTCException(Exception):
    """Custom XRTC exception."""

    def __init__(self, message: str = "error occured", url = None):
        """Add custom message formatting."""
        if url is not None:
            self.message = "XRTC URL: " + url + ": " + message
        else:
            self.message = "XRTC: " + message

        super().__init__(self.message)

# 400   Bad Request -  Your request is invalid.
import requests.models


# requests
class BadRequestError(Exception):
    def __init__(self, message: str = None, resp: requests.models.Response = None):
        self.message = f"400 - {message}" if message else f"400 - Your request is invalid"
        self.message += f"\n\t{resp.url}" if resp else ""

    def __str__(self):
        return self.message


# 401   Unauthorized - Your API key is wrong.
class UnauthorizedError(Exception):
    def __init__(self, message: str = None, resp: requests.models.Response = None):
        self.message = f"401 - {message}" if message else "401 - Your API key is wrong"
        self.message += f"\n\t{resp.url}" if resp else ""

    def __str__(self):
        return self.message


# 404   Not Found - The specified link could not be found.
class NotFoundError(Exception):
    def __init__(self, message: str = None, resp: requests.models.Response = None):
        self.message = f"404 - {message}" if message else "404 - The specified link could not be found"
        self.message += f"\n\t{resp.url}" if resp else ""

    def __str__(self):
        return self.message


# 429   Too Many Requests - You're making too many API calls
class TooManyRequestsError(Exception):
    def __init__(self, message: str = None, resp: requests.models.Response = None):
        self.message = f"429 - {message}" if message else "429 - You're making too many API calls"
        self.message += f"\n\t{resp.url}" if resp else ""

    def __str__(self):
        return self.message


# 500   Internal Server Error - We had a problem with our server. Try again later.
class InternalServerError(Exception):
    def __init__(self, message: str = None, resp: requests.models.Response = None):
        self.message = f"500 - {message}" if message else '500 - We had a problem with our server. Try again later'
        self.message += f"\n\t{resp.url}" if resp else ""

    def __str__(self):
        return self.message


# 503   Service Unavailable - We're temporarily offline for maintenance. Please try again later.
class ServiceUnavailableError(Exception):
    def __init__(self, message: str = None, resp: requests.models.Response = None):
        self.message = f"503 - {message}" if message else '503 - We\'re temporarily offline for maintenance. Please ' \
                                                          'try again later '
        self.message += f"\n\t{resp.url}" if resp else ""

    def __str__(self):
        return self.message


class CurrencyNotFound(Exception):
    """
    Error raise when currency (eg: USDT) is not found when searching/looping through balances or others
    """
    pass


# class


if __name__ == "__main__":
    pass

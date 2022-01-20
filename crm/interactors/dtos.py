from dataclasses import dataclass


@dataclass()
class TokenDetailsDTO:
    access_token: str
    refresh_token: str

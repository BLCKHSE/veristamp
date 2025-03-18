from dataclasses import dataclass


@dataclass
class User:

    email: str
    email_verified: bool = False

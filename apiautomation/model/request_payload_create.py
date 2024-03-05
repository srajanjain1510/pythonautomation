from dataclasses import dataclass


@dataclass
class RequestPayload:
    name: str
    job: str

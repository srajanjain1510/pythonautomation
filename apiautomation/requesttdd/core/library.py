"""This module has reusuable methods"""
import os
from typing import Any

import requests

PI = 3.14


def area_circle(radius: float) -> float:
    """
    area_circle will calculate the area of circle
    :param radius:
    :return: area
    """
    return PI * radius * radius


def remove_file(filename: str) -> None:
    os.remove(filename)


def get_jokes_yo_mamma_api() -> Any | None:
    response = requests.get("https://reqres.in/api/users/2")
    return response.json()

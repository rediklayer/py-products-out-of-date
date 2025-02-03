import datetime
from unittest.mock import patch
from typing import List, Dict, Any
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, products, expected_output",
    [
        (
            datetime.date(2022, 2, 2),  # Mock today's date
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["duck"],
        ),

        (
            datetime.date(2022, 1, 1),  # Mock today's date
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            [],
        ),

        (
            datetime.date(2022, 2, 15),  # Mock today's date
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["salmon", "chicken", "duck"],
        ),

        (
            datetime.date(2022, 2, 2),  # Mock today's date
            [],
            [],
        ),
    ],
)
def test_outdated_products(
    today_date: datetime.date,
    products: List[Dict[str, Any]],
    expected_output: List[str],
) -> None:

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        mock_date.side_effect = lambda *args, **kw: datetime.date(*args, **kw)
        assert outdated_products(products) == expected_output

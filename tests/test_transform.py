from src.etl.transform import cleaning_csv, transform, transform_run


def test_cleaning_csv():
    fake_df = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "customer_name": "Morgan Berka",
            "items": "Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9",
            "payment_type": "CASH",
            "total_amount": "8.40",
            "card_details": "None",
        }
    ]
    expected = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": "Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9",
            "payment_type": "CASH",
            "total_amount": "8.40",
        }
    ]
    actual = cleaning_csv(fake_df)
    assert actual == expected


def test_transform():
    fake_df = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": "Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9",
            "payment_type": "CASH",
            "total_amount": "8.40",
        }
    ]
    expected = [
        {
            "Date-Time": 1614070848,
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
                {"size": "Large", "type": "", "name": "Chai latte", "price": "2.6"},
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
        }
    ]

    actual = transform(fake_df)
    print(actual)
    assert actual == expected


def test_transform_run():
    fake_df = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "customer_name": "Morgan Berka",
            "items": "Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9",
            "payment_type": "CASH",
            "total_amount": "8.40",
            "card_details": "None",
        }
    ]

    expected = [
        {
            "Date-Time": 1614070848,
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
                {"size": "Large", "type": "", "name": "Chai latte", "price": "2.6"},
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
        }
    ]

    actual = transform_run(fake_df)
    assert actual == expected

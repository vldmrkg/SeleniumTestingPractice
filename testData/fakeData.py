from faker import Faker
fake = Faker()


class HomePageData:
    # Lista sa test podacima za HomePage
    test_homePage_data = [
        {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "email": fake.email(),
            "password": fake.password()
        }
    ]


class CheckOutPageData:
    # Lista sa test podacima za CheckOutPage
    test_checkOutPage_data = [
        {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "email": fake.email(),
            "password": fake.password(),
            "street": fake.street_address(),
            "city": fake.city(),
            "company": fake.company(),
            "zipCode": fake.zipcode(),
            "phoneNumber": fake.phone_number()
        }
    ]





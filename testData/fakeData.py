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

class SignInPageData:
    # Lista sa test podacima za SignInPage
    test_signInPage_data = [
        {
            "correct_email": "vldmr@gmail.comm",
            "correct_password": "Lalalala123123",
            "incorrect_email": "vldmra@gmail.comm",
            "incorrect_password": "Lalalala123123sa"
        }
    ]

    @classmethod
    def get_correct_signin_data(cls):
        return cls.test_signInPage_data[0]["correct_email"], cls.test_signInPage_data[0]["correct_password"]

    @classmethod
    def get_incorrect_signin_data(cls):
        return cls.test_signInPage_data[0]["incorrect_email"], cls.test_signInPage_data[0]["incorrect_password"]



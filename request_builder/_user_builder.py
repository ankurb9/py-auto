from faker import Faker


class UserBuilder:
    _MISSING = object()

    def __init__(self, seed=None):
        self._obj = {}
        self.fake = Faker()
        if seed:
            self.fake.seed_instance(seed)

    def set_name(self, name=_MISSING):
        self._obj["name"] = self.fake.name() if name is self._MISSING else name
        return self

    def set_username(self, username=_MISSING):
        self._obj["username"] = self.fake.user_name() if username is self._MISSING else username
        return self

    def set_email(self, email=_MISSING):
        self._obj["email"] = self.fake.email() if email is self._MISSING else email
        return self

    def set_phone(self, phone=_MISSING):
        self._obj["phone"] = self.fake.phone_number() if phone is self._MISSING else phone
        return self

    def set_street(self, street=_MISSING):
        self._obj.setdefault("address", {})["street"] = (
            self.fake.street_address() if street is self._MISSING else street
        )
        return self

    def set_city(self, city=_MISSING):
        self._obj.setdefault("address", {})["city"] = (
            self.fake.city() if city is self._MISSING else city
        )
        return self

    def set_state(self, state=_MISSING):
        self._obj.setdefault("address", {})["state"] = (
            self.fake.state() if state is self._MISSING else state
        )
        return self

    def set_zipcode(self, zipcode=_MISSING):
        self._obj.setdefault("address", {})["zipcode"] = (
            self.fake.zipcode() if zipcode is self._MISSING else zipcode
        )
        return self

    def build(self):

        return self._obj
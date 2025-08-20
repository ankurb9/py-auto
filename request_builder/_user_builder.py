
class UserBuilder:
    def __init__(self, exclude_none: bool= True):
        self._name = None
        self._username = None
        self._email = None
        self._phone = None
        self._street = None
        self._city = None
        self._state = None
        self._zipcode = None
        self._obj = dict()
        self._exclude_none = exclude_none

    def set_name(self, name):
        self._name = name
        return self

    def set_username(self, username):
        self._username = username
        return self

    def set_email(self, email):
        self._email = email
        return self

    def set_phone(self, phone):
        self._phone = phone
        return self
    
    def set_street(self, street):
        self._street = street
        return self
    
    def set_city(self, city):
        self._city = city
        return self
    
    def set_state(self, state):
        self._state = state
        return self
    
    def set_zipcode(self, zipcode):
        self._zipcode = zipcode
        return self
        
    def build(self):

        user = {
            "name": self._name,
            "username": self._username,
            "email": self._email,
            "phone": self._phone,
            "address": {
                "street": self._street,
                "city": self._city,
                "state": self._state,
                "zipcode": self._zipcode
            }
        }

        if self._exclude_none:
            user = self._clean(user)

        return user

    def _clean(self, d):
        if isinstance(d, dict):
            cleaned = {}
            for k, v in d.items():
                if v is None:
                    continue
                val = self._clean(v)
                if val != {}:
                    cleaned[k] = val
            return cleaned
        return d





class UserBuilder:
    def __init__(self):

        self._obj = dict()

    def set_name(self, name):
        self._obj["name"] = name
        return self

    def set_username(self, username):
        self._obj["username"] = username
        return self

    def set_email(self, email):
        self._obj["email"] = email
        return self

    def set_phone(self, phone):
        self._obj["phone"] = phone
        return self
    
    def set_street(self, street):
        self._obj.setdefault("address", {})["street"] = street
        return self
    
    def set_city(self, city):
        self._obj.setdefault("address", {})["city"] = city
        return self
    
    def set_state(self, state):
        self._obj.setdefault("address", {})["state"] = state
        return self
    
    def set_zipcode(self, zipcode):
        self._obj.setdefault("address", {})["zipcode"] = zipcode
        return self
        
    def build(self):
        return self._obj




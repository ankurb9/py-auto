from utils.faker import get_faker

class UserResponse:

    @staticmethod
    def response(users: int = 5):

        return {
            "page": 2,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [
                {
                    "id": i,
                    "email": get_faker(i).email(),
                    "first_name": get_faker(i).first_name(),
                    "last_name": get_faker(i).last_name()
                }
                for i in range(users)

            ],
            "support": {
                "url": get_faker().url()
            }
        }

    @property
    def schema(self):
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "Mock Users Schema",
            "type": "object",
            "properties": {
                "page": {"type": "integer"},
                "per_page": {"type": "integer"},
                "total": {"type": "integer"},
                "total_pages": {"type": "integer"},
                "data": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "email": {"type": "string", "format": "email"},
                            "first_name": {"type": "string"},
                            "last_name": {"type": "string"}
                        },
                        "required": ["id", "email", "first_name", "last_name"]
                    }
                }
            },
            "required": ["page", "per_page", "total", "total_pages", "data"]
        }

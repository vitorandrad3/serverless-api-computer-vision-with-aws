class APIError(Exception):

    def __init__(self, status_code: int, message: str):
        super().__init__(f"API error: {status_code} - {message}")
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return self.message

from string import punctuation


class PhoneNumber:
    def __init__(self, number: str):
        self.number = self.clean(number)
        self.area_code, self.exchange_code, self.subscriber_number = self.number[:3], self.number[3:6], self.number[6:]
    
    def pretty(self) -> str:
        """Returns phone number formatted as '(NXX)-NXX-XXXX'."""
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
    
    def clean(self, number: str) ->  str:
        """Returns cleaned and validated phone number or raises ValueError"""
        number = "".join(char for char in number if char not in "()+-. ")

        # Reject Invalid Characters
        if any(item for item in number if item.isalpha()):
            raise ValueError("letters not permitted")
        if any(item for item in number if item in punctuation):
            raise ValueError("punctuations not permitted")
        
        # Reject incorrect length or incorrect country code
        length = len(number)
        if length < 10:
            raise ValueError("must not be fewer than 10 digits")
        if length > 11:
            raise ValueError("must not be greater than 11 digits")
        if length == 11 and number[0] != "1":
            raise ValueError("11 digits must start with 1")
        
        # Discard country code
        if length == 11:
            number = number[1:]

        # Reject invalid area and exchange codes
        if number[0] in "01":
            raise ValueError(f"area code cannot start with {'zero' if number[0] == '0' else 'one'}")
        if number[3] in "01":
            raise ValueError(f"exchange code cannot start with {'zero' if number[3] == '0' else 'one'}")
        
        return number
    
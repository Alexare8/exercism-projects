class PhoneNumber:
    def __init__(self, number: str):
        # Reject invalid characters and clean number
        if number[6].isalpha(): raise ValueError("letters not permitted")
        if any(sym in number for sym in "@:!"): raise ValueError("punctuations not permitted")
        self.number = "".join(digit for digit in number if digit.isdigit())
        
        # Reject incorrect length or incorrect country code
        if (length := len(self.number)) < 10: raise ValueError("must not be fewer than 10 digits")
        if length > 11: raise ValueError("must not be greater than 11 digits")
        if length == 11 and self.number[0] != "1": raise ValueError("11 digits must start with 1")

        # Save final number without country code
        if length == 11: self.number = self.number[1:]
        self.area_code = self.number[:3]

        # Reject invalid area and exchange codes
        if self.area_code[0] in "01":
            raise ValueError(f"area code cannot start with {'zero' if self.area_code[0] == '0' else 'one'}")
        if self.number[3] in "01":
            raise ValueError(f"exchange code cannot start with {'zero' if self.number[3] == '0' else 'one'}")
    
    def pretty(self) -> str:
        """Returns phone number formatted as '(NXX)-NXX-XXXX'."""
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
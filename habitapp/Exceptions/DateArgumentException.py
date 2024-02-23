class DateArgumentException(Exception):
    """Exception raised for invalid date arguments.

    Attributes:
        message (str): Explanation of the error.
        
    """
    
    def __init__(self, message, errors):            
        super().__init__(message)
        self.errors = errors
    

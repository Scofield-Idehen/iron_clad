# pragma version 0.4.0
# @license MIT

fav_scofield: uint256
my_bool: bool  # Changed from String to bool

@deploy 
def __init__():
    self.fav_scofield = 24
    self.my_bool = False  # Initialize with default value

@external 
def new_store(_value: uint256):
    self.fav_scofield = _value

@external
def set_bool(_new_value: bool):
    #set bool to whatever is passed but what if bool is set to something othern than true or false
    #how do i catch this error?
    self.my_bool = _new_value

@external
@view
def get_bool() -> bool:
    return self.my_bool

    

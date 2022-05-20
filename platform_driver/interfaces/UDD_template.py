from platform_driver.interfaces.driver_wrapper import WrapperInterface, WrapperRegister
from platform_driver.interfaces.driver_wrapper import ImplementedRegister, RegisterValue
from typing import List, Optional


# TODO-developer: Your code here
# Add dependency as needed, and update in requirements


# TODO-developer: Your code here
# Change the classname "UserDevelopRegister" as needed
class UserDevelopRegister(WrapperRegister):
    # boilerplate code. Don't touch me.  # TODO: find a better way to expose this
    # def __init__(self,
    #              driver_config: dict,
    #              point_name: str,
    #              data_type: RegisterValue,
    #              units: str, read_only: bool,
    #              default_value: Optional[RegisterValue] = None,
    #              description: str = ""):  # re-define for readability
    #     super().__init__(driver_config, point_name, data_type, units, default_value, description)  # base class1
    #     super().__init__("byte", read_only, point_name, units, description='')  # base class2

    def get_register_value(self) -> RegisterValue:
        # TODO-developer: Your code here
        # Implement get-register-value logic here
        # Note: Keep the method name as it is including the signatures.
        # Use a helper method if needed.

        # EXAMPLE:
        # def get_register_value(self) -> RegisterValue:
        #    return _get_register_value_helper(url=self.driver_config.get("url"))
        # def _get_register_value_helper(self, url: str):
        #    ...
        pass


# TODO-developer: Your code here
# fill in register_types with register types accordingly
# EXAMPLE:
# register_types = [UserDevelopRegister, UserDevelopRegister2]
register_types: List[ImplementedRegister]
register_types = []


# boilerplate code. Don't touch me.
class Interface(WrapperInterface):
    def pass_register_types(self):
        return register_types



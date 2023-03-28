"""Sample user/role pairings."""

from . import organizations
from . import users

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

pairs = [
    (users.sol_student, organizations.org1),
    (users.merritt_manager, organizations.org1),
    (users.merritt_manager, organizations.org2),
    (users.sol_student, organizations.org2),
    (users.arden_ambassador, organizations.org3)
]

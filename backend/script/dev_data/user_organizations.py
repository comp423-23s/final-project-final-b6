"""Sample user/role pairings."""

from . import organizations
from . import users

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

pairs = [
    (users.sol_student, organizations.org1),
    (users.sol_student, organizations.org9),
    (users.sol_student, organizations.org10),
    (users.sol_student, organizations.org5),
    (users.sol_student, organizations.org2),
    (users.sol_student, organizations.org15),
    (users.sol_student, organizations.org12),
    (users.sol_student, organizations.org11),

    (users.merritt_manager, organizations.org1),
    (users.merritt_manager, organizations.org3),
    (users.merritt_manager, organizations.org6),
    (users.merritt_manager, organizations.org13),
    
    (users.arden_ambassador, organizations.org3),
    (users.arden_ambassador, organizations.org4),
    (users.arden_ambassador, organizations.org8),
    (users.arden_ambassador, organizations.org9),
    (users.arden_ambassador, organizations.org10),
    (users.arden_ambassador, organizations.org14),

    (users.root, organizations.org1),
    (users.root, organizations.org2),
    (users.root, organizations.org3),
    (users.root, organizations.org4),
    (users.root, organizations.org5),
    (users.root, organizations.org6),
    (users.root, organizations.org7),
    (users.root, organizations.org8),
    (users.root, organizations.org9),
    (users.root, organizations.org10),
    (users.root, organizations.org11),
    (users.root, organizations.org12),
    (users.root, organizations.org13),
    (users.root, organizations.org14),
    (users.root, organizations.org15)
]

"""Sample permissions."""

from ...models import Permission
from . import roles

__authors__ = ["Kris Jordan", "Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

pairs = [
    (roles.sudoer, Permission(action="*", resource="*")),
    (roles.staff, Permission(action="admin.*", resource="*")),
    (roles.staff, Permission(action="user.*", resource="*")),
    (roles.staff, Permission(action="role.*", resource="*")),
    (roles.staff, Permission(action="checkin.*", resource="*")),
    #the two additions below allow managers to do everything associted with events/ organizations
    #if they should have some restrictions like not being able to create/delete, I can fix that in a PR
    (roles.staff, Permission(action="organization.*", resource="*")),
    (roles.staff, Permission(action="event.*", resource="*")),

    # An ambassador should be able to:
        # Do everything a student is able to do.
        # Search for users.
        # Checkin a user to the CSXL.
        # Edit organization detials.
        # Edit event details.
        # Create an organization.
        # Create an event for an organizaiton.

    (roles.ambassador, Permission(action="user.search", resource="*")),
    (roles.ambassador, Permission(action="checkin.*", resource="*")),
    (roles.ambassador, Permission(action="organization.edit_organization", resource="*")),
    (roles.ambassador, Permission(action="event.edit_event", resource="*")),
    #(roles.ambassador, Permission(action="organization.create_organization", resource="*")),
    #(roles.ambassador, Permission(action="event.create_event", resource="*")),



]

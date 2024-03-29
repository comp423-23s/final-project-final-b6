"""Reset the database by dropping all tables, creating tables, and inserting demo data.

Usage: python3 -m backend.script.reset_database."""

import sys
from sqlalchemy import text
from sqlalchemy.orm import Session
from ..database import engine
from ..env import getenv
from .. import entities

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


# Insert Dev Data from `script.dev_data`
def reset_database():
    if getenv("MODE") != "development":
        print("This script can only be run in development mode.", file=sys.stderr)
        print("Add MODE=development to your .env file in workspace's `backend/` directory")
        exit(1)

    # Reset Tables
    entities.EntityBase.metadata.drop_all(engine)
    entities.EntityBase.metadata.create_all(engine)


    # Add Users
    with Session(engine) as session:
        from .dev_data import users
        to_entity = entities.UserEntity.from_model
        session.add_all([to_entity(model) for model in users.models])
        session.execute(text(f'ALTER SEQUENCE {entities.UserEntity.__table__}_id_seq RESTART WITH {len(users.models) + 1}'))
        session.commit()

    # Add Roles
    with Session(engine) as session:
        from .dev_data import roles
        to_entity = entities.RoleEntity.from_model
        session.add_all([to_entity(model) for model in roles.models])
        session.execute(text(f'ALTER SEQUENCE {entities.RoleEntity.__table__}_id_seq RESTART WITH {len(roles.models) + 1}'))
        session.commit()

    # Add Users to Roles
    with Session(engine) as session:
        from ..entities import UserEntity, RoleEntity
        from .dev_data import user_roles
        for user, role in user_roles.pairs:
            user_entity = session.get(UserEntity, user.id)
            role_entity = session.get(RoleEntity, role.id)
            user_entity.roles.append(role_entity)
        session.commit()

    # Add Permissions to Users/Roles
    with Session(engine) as session:
        from ..entities import PermissionEntity
        from .dev_data import permissions
        for role, permission in permissions.pairs:
            entity = PermissionEntity.from_model(permission)
            entity.role = session.get(RoleEntity, role.id)
            session.add(entity)
        session.execute(text(f'ALTER SEQUENCE permission_id_seq RESTART WITH {len(permissions.pairs) + 1}'))
        session.commit()

    # Add Organizations
    with Session(engine) as session:
        from .dev_data import organizations
        to_entity = entities.OrganizationEntity.from_model
        session.add_all([to_entity(model) for model in organizations.models])
        session.execute(text(f'ALTER SEQUENCE {entities.OrganizationEntity.__table__}_id_seq RESTART WITH {1}'))
        session.commit()

    # Add Users to Organizations
    with Session(engine) as session:
        from ..entities import UserEntity, OrganizationEntity
        from .dev_data import user_organizations
        for user, organization in user_organizations.pairs:
            user_entity = session.get(UserEntity, user.id)
            organization_entity = session.get(OrganizationEntity, organization.id)
            user_entity.organizations.append(organization_entity)
        session.commit()

    # Add events to organizations
    with Session(engine) as session:
        from .dev_data import events
        from ..entities import EventEntity, OrganizationEntity
        to_entity = entities.EventEntity.from_model
        session.add_all([to_entity(model) for model in events.models])
        session.execute(text(f'ALTER SEQUENCE {entities.EventEntity.__table__}_id_seq RESTART WITH {len(events.models) + 1}'))
        session.commit()

reset_database()

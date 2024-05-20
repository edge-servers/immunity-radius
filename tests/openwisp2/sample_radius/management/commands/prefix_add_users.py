from immunity_radius.management.commands.base import BatchAddMixin
from immunity_radius.management.commands.base.prefix_add_users import (
    BasePrefixAddUsersCommand,
)


class Command(BatchAddMixin, BasePrefixAddUsersCommand):
    pass

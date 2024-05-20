from immunity_radius.management.commands.base import BatchAddMixin
from immunity_radius.management.commands.base.batch_add_users import (
    BaseBatchAddUsersCommand,
)


class Command(BatchAddMixin, BaseBatchAddUsersCommand):
    pass

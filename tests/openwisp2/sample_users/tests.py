from immunity_radius.tests.mixins import GetEditFormInlineMixin
from immunity_users.tests.test_admin import (
    TestBasicUsersIntegration as BaseTestBasicUsersIntegration,
)
from immunity_users.tests.test_admin import (
    TestMultitenantAdmin as BaseTestMultitenantAdmin,
)
from immunity_users.tests.test_admin import TestUsersAdmin as BaseTestUsersAdmin
from immunity_users.tests.test_models import TestUsers as BaseTestUsers

additional_fields = [
    ('social_security_number', '123-45-6789'),
]


class TestUsersAdmin(GetEditFormInlineMixin, BaseTestUsersAdmin):
    app_label = 'sample_users'
    is_integration_test = True
    _additional_user_fields = additional_fields


class TestBasicUsersIntegration(GetEditFormInlineMixin, BaseTestBasicUsersIntegration):
    app_label = 'sample_users'
    is_integration_test = True
    _additional_user_fields = additional_fields


class TestMultitenantAdmin(BaseTestMultitenantAdmin):
    app_label = 'sample_users'


class TestUsers(BaseTestUsers):
    pass


del BaseTestUsersAdmin
del BaseTestBasicUsersIntegration
del BaseTestMultitenantAdmin
del BaseTestUsers

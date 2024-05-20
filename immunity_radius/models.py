import logging

from swapper import swappable_setting

from .base.models import (
    AbstractNas,
    AbstractOrganizationRadiusSettings,
    AbstractPhoneToken,
    AbstractRadiusAccounting,
    AbstractRadiusBatch,
    AbstractRadiusCheck,
    AbstractRadiusGroup,
    AbstractRadiusGroupCheck,
    AbstractRadiusGroupReply,
    AbstractRadiusPostAuth,
    AbstractRadiusReply,
    AbstractRadiusToken,
    AbstractRadiusUserGroup,
    AbstractRegisteredUser,
)

logger = logging.getLogger(__name__)


class RadiusCheck(AbstractRadiusCheck):
    class Meta(AbstractRadiusCheck.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusCheck')


class RadiusReply(AbstractRadiusReply):
    class Meta(AbstractRadiusReply.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusReply')


class RadiusAccounting(AbstractRadiusAccounting):
    class Meta(AbstractRadiusAccounting.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusAccounting')


class RadiusGroup(AbstractRadiusGroup):
    class Meta(AbstractRadiusGroup.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusGroup')


class RadiusGroupCheck(AbstractRadiusGroupCheck):
    class Meta(AbstractRadiusGroupCheck.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusGroupCheck')


class RadiusGroupReply(AbstractRadiusGroupReply):
    class Meta(AbstractRadiusGroupReply.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusGroupReply')


class RadiusUserGroup(AbstractRadiusUserGroup):
    class Meta(AbstractRadiusUserGroup.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusUserGroup')


class RadiusPostAuth(AbstractRadiusPostAuth):
    class Meta(AbstractRadiusPostAuth.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusPostAuth')


class Nas(AbstractNas):
    class Meta(AbstractNas.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'Nas')


class RadiusBatch(AbstractRadiusBatch):
    class Meta(AbstractRadiusBatch.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusBatch')


class RadiusToken(AbstractRadiusToken):
    class Meta(AbstractRadiusToken.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RadiusToken')


class OrganizationRadiusSettings(AbstractOrganizationRadiusSettings):
    class Meta(AbstractOrganizationRadiusSettings.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'OrganizationRadiusSettings')


class PhoneToken(AbstractPhoneToken):
    class Meta(AbstractPhoneToken.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'PhoneToken')


class RegisteredUser(AbstractRegisteredUser):
    class Meta(AbstractRegisteredUser.Meta):
        abstract = False
        swappable = swappable_setting('immunity_radius', 'RegisteredUser')

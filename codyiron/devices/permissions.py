from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Lamp


class LampPermissions:

    @classmethod
    def assign_create_lamp_permission(cls, user):
        cls._assign_permission(user, 'add_lamp')

    @classmethod
    def assign_view_lamp_permission(cls, user):
        cls._assign_permission(user, 'view_lamp')

    @classmethod
    def assign_change_lamp_permission(cls, user):
        cls._assign_permission(user, 'change_lamp')

    @classmethod
    def assign_delete_lamp_permission(cls, user):
        cls._assign_permission(user, 'delete_lamp')

    @classmethod
    def _assign_permission(cls, user, codename):
        content_type = ContentType.objects.get_for_model(Lamp)
        permission, created = Permission.objects.get_or_create(
            codename=codename,
            content_type=content_type,
        )
        user.user_permissions.add(permission)

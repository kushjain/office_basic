from . import integration


class Settings(integration.Settings):
    """
    Settings for production environment
    """

    ADMIN_USER_ACCOUNTS = [
        {
            "email": 'kushj@admin.com',
            "username": "nucleus",
            "password": "pbkdf2_sha256$24000$Xb1psndpkbdu$Zu/S1dFzm/sh2q0pNcZisonGKf9XFD++U4VQuUKMfjg=",
            "force_update_password": False
        }
    ]

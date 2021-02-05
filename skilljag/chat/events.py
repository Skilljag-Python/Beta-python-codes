import snitch
from snitch.backends import PushNotificationBackend, EmailNotificationBackend

ACTIVATED_EVENT = "activated"
CONFIRMED_EVENT = "confirmed"

@snitch.register(ACTIVATED_EVENT)
class ActivatedHandler(snitch.EventHandler):
    title = "Activated!"


@snitch.register(CONFIRMED_EVENT)
class ConfirmedHandler(snitch.EventHandler):
    title = "Confirmed!"
    notification_backends = [PushNotificationBackend]

    def audience(self):
        return get_user_model().objects.all()
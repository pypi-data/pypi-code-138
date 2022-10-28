from office365.runtime.paths.resource_path import ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery
from office365.sharepoint.base_entity import BaseEntity
from office365.sharepoint.base_entity_collection import BaseEntityCollection
from office365.sharepoint.translation.notification_recipient_set_request \
    import TranslationNotificationRecipientSetRequest
from office365.sharepoint.translation.notification_recipient_users import TranslationNotificationRecipientUsers


class MultilingualSettings(BaseEntity):

    def set_notification_recipients(self, notification_recipients):
        """
        :param list notification_recipients:
        """
        request = TranslationNotificationRecipientSetRequest(notification_recipients)
        qry = ServiceOperationQuery(self, "SetNotificationRecipients", None, request)
        self.context.add_query(qry)
        return self

    @property
    def recipients(self):
        return self.properties.get('Recipients',
                                   BaseEntityCollection(self.context, TranslationNotificationRecipientUsers,
                                                        ResourcePath("Recipients", self.resource_path)))

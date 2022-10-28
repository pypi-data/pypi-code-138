from office365.runtime.client_object import ClientObject


class SpoOperation(ClientObject):
    """Represents an operation on a site collection."""

    @property
    def is_complete(self):
        """Gets a value that indicates whether the operation has completed."""
        if self.is_property_available("IsComplete"):
            return bool(self.properties["IsComplete"])
        return None

    @property
    def polling_interval_secs(self):
        """Gets the recommended interval to poll for the IsComplete property."""
        if self.is_property_available("PollingInterval"):
            return int(self.properties["PollingInterval"]) / 1000
        return None

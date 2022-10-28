from office365.directory.identities.providers.base import IdentityProviderBase


class BuiltInIdentityProvider(IdentityProviderBase):
    """
    Represents built-in identity providers with External Identities for an Azure Active Directory tenant.
    """

    @property
    def identity_provider_type(self):
        """
        The identity provider type. For a B2B scenario, possible values: AADSignup, MicrosoftAccount, EmailOTP.

        :rtype: str
        """
        return self.properties.get("identityProviderType", None)

from office365.sharepoint.base_entity import BaseEntity


class SuiteNavData(BaseEntity):

    @property
    def entity_type_name(self):
        return "Microsoft.SharePoint.Portal.SuiteNavData"

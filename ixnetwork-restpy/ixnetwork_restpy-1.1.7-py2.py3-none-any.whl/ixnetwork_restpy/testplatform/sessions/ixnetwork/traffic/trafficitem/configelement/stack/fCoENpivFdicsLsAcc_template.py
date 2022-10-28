from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoENpivFdicsLsAcc(Base):
    __slots__ = ()
    _SDM_NAME = "fCoENpivFdicsLsAcc"
    _SDM_ATT_MAP = {
        "FcoeHeaderVersion": "fCoENpivFdicsLsAcc.header.fcoeHeader.version-1",
        "FcoeHeaderReserved": "fCoENpivFdicsLsAcc.header.fcoeHeader.reserved-2",
        "FcoeHeaderESOF": "fCoENpivFdicsLsAcc.header.fcoeHeader.eSOF-3",
        "ExtendedLinkServicesExtendedLinkServiceInfo": "fCoENpivFdicsLsAcc.header.fcHeader.RCtl.extendedLinkServices.extendedLinkServiceInfo-4",
        "FcHeaderDId": "fCoENpivFdicsLsAcc.header.fcHeader.DId-5",
        "FcHeaderCsCtlPriority": "fCoENpivFdicsLsAcc.header.fcHeader.CsCtlPriority-6",
        "FcHeaderSId": "fCoENpivFdicsLsAcc.header.fcHeader.SId-7",
        "FcHeaderType": "fCoENpivFdicsLsAcc.header.fcHeader.Type-8",
        "FCtlExchangeContext": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.exchangeContext-9",
        "FCtlSequenceContext": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.sequenceContext-10",
        "FCtlFirstSequence": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.firstSequence-11",
        "FCtlLastSequence": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.lastSequence-12",
        "FCtlEndSequence": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.endSequence-13",
        "FCtlEndConnection": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.endConnection-14",
        "FCtlCsCtlPriority": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.csCtlPriority-15",
        "FCtlSequenceInitiative": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.sequenceInitiative-16",
        "FCtlFcXidReassigned": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.fcXidReassigned-17",
        "FCtlFcInvalidateXid": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.fcInvalidateXid-18",
        "FCtlAckForm": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.ackForm-19",
        "FCtlFcDataCompression": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.fcDataCompression-20",
        "FCtlFcDataEncryption": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.fcDataEncryption-21",
        "FCtlRetransmittedSequence": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.retransmittedSequence-22",
        "FCtlUnidirectionalTransmit": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.unidirectionalTransmit-23",
        "FCtlContinueSeqCondition": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.continueSeqCondition-24",
        "FCtlAbortSeqCondition": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.abortSeqCondition-25",
        "FCtlRelativeOffsetPresent": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.relativeOffsetPresent-26",
        "FCtlExchangeReassembly": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.exchangeReassembly-27",
        "FCtlFillBytes": "fCoENpivFdicsLsAcc.header.fcHeader.FCtl.fCtl.fillBytes-28",
        "FcHeaderSeqId": "fCoENpivFdicsLsAcc.header.fcHeader.SeqId-29",
        "FcHeaderDfCtl": "fCoENpivFdicsLsAcc.header.fcHeader.DfCtl-30",
        "FcHeaderSeqCnt": "fCoENpivFdicsLsAcc.header.fcHeader.SeqCnt-31",
        "FcHeaderOxId": "fCoENpivFdicsLsAcc.header.fcHeader.OxId-32",
        "FcHeaderRxId": "fCoENpivFdicsLsAcc.header.fcHeader.RxId-33",
        "FcHeaderParameter": "fCoENpivFdicsLsAcc.header.fcHeader.Parameter-34",
        "FcElsCommandCodeFcElsCommandCodeLsAcc": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommandCode.FcElsCommandCodeLsAcc-35",
        "FcElsRequestAcceptRejectFcElsRequestReserved": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsRequestReserved-36",
        "FcElsCommonServiceParametersFcElsCommonServiceParametersFc-phVersion": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommonServiceParameters.FcElsCommonServiceParametersFc-phVersion-37",
        "FcElsCommonServiceParametersFcElsCommonServiceParametersBuffer-to-bufferCredit": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommonServiceParameters.FcElsCommonServiceParametersBuffer-to-bufferCredit-38",
        "FcElsCommonServiceParametersFcElsCommonServiceParametersCommonFeatures": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommonServiceParameters.FcElsCommonServiceParametersCommonFeatures-39",
        "FcElsCommonServiceParametersFcElsCommonServiceParametersBbScNumber": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommonServiceParameters.FcElsCommonServiceParametersBbScNumber-40",
        "FcElsCommonServiceParametersFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommonServiceParameters.FcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize-41",
        "FcElsCommonServiceParametersFcElsCommonServiceParametersRATov": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommonServiceParameters.FcElsCommonServiceParametersRATov-42",
        "FcElsCommonServiceParametersFcElsCommonServiceParametersEDTov": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommonServiceParameters.FcElsCommonServiceParametersEDTov-43",
        "FcElsCommonServiceParametersFcElsCommonServiceParametersNPortPortName": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommonServiceParameters.FcElsCommonServiceParametersNPortPortName-44",
        "FcElsCommonServiceParametersFcElsCommonServiceParametersFabricNodeName": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsCommonServiceParameters.FcElsCommonServiceParametersFabricNodeName-45",
        "FcElsRequestAcceptRejectFcElsClass1SvcParameters": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass1SvcParameters-46",
        "FcElsRequestAcceptRejectFcElsClass2SvcParameters": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass2SvcParameters-47",
        "FcElsClass3SvcParametersFcElsClass3SvcParametersServiceOptions": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass3SvcParameters.FcElsClass3SvcParametersServiceOptions-48",
        "FcElsClass3SvcParametersFcElsClass3SvcParametersInitiatorControl": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass3SvcParameters.FcElsClass3SvcParametersInitiatorControl-49",
        "FcElsClass3SvcParametersFcElsClass3SvcParametersRecipientControl": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass3SvcParameters.FcElsClass3SvcParametersRecipientControl-50",
        "FcElsClass3SvcParametersFcElsClass3SvcParametersClassReceiveSize": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass3SvcParameters.FcElsClass3SvcParametersClassReceiveSize-51",
        "FcElsClass3SvcParametersFcElsClass3SvcParametersTotalConcurrentSequence": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass3SvcParameters.FcElsClass3SvcParametersTotalConcurrentSequence-52",
        "FcElsClass3SvcParametersFcElsClass3SvcParametersEnd-to-endCredit": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass3SvcParameters.FcElsClass3SvcParametersEnd-to-endCredit-53",
        "FcElsClass3SvcParametersFcElsClass3SvcParametersOpenSeqPerExchange": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass3SvcParameters.FcElsClass3SvcParametersOpenSeqPerExchange-54",
        "FcElsClass3SvcParametersFcElsClass3SvcParametersCrTov": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsClass3SvcParameters.FcElsClass3SvcParametersCrTov-55",
        "FcElsRequestAcceptRejectClass4SvcParameters": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.Class4SvcParameters-56",
        "FcElsRequestAcceptRejectFcElsVendorVersion": "fCoENpivFdicsLsAcc.header.FcEls.FcElsRequestAcceptReject.FcElsVendorVersion-57",
    }

    def __init__(self, parent, list_op=False):
        super(FCoENpivFdicsLsAcc, self).__init__(parent, list_op)

    @property
    def FcoeHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeHeaderVersion"])
        )

    @property
    def FcoeHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeHeaderReserved"])
        )

    @property
    def FcoeHeaderESOF(self):
        """
        Display Name: E-SOF
        Default Value: 54
        Value Format: decimal
        Available enum values: SOFf - Fabric, 40, SOFi4 - Initiate Class 4, 41, SOFi2 - Initiate Class 2, 45, SOFi3 - Initiate Class 3, 46, SOFn4 - Normal Class 4, 49, SOFn2 - Normal Class 2, 53, SOFn3 - Normal Class 3, 54, SOFc4 - Connect Class 4, 57, SOFn1 - Normal Class 1 or 6, 250
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeHeaderESOF"])
        )

    @property
    def ExtendedLinkServicesExtendedLinkServiceInfo(self):
        """
        Display Name: Information
        Default Value: 35
        Value Format: decimal
        Available enum values: Solicited Data, 33, Request, 34, Reply, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ExtendedLinkServicesExtendedLinkServiceInfo"]
            ),
        )

    @property
    def FcHeaderDId(self):
        """
        Display Name: D_ID
        Default Value: 00.00.01
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderDId"]))

    @property
    def FcHeaderCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderCsCtlPriority"])
        )

    @property
    def FcHeaderSId(self):
        """
        Display Name: S_ID
        Default Value: FF.FF.FE
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSId"]))

    @property
    def FcHeaderType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderType"]))

    @property
    def FCtlExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlExchangeContext"])
        )

    @property
    def FCtlSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlSequenceContext"])
        )

    @property
    def FCtlFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFirstSequence"])
        )

    @property
    def FCtlLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlLastSequence"])
        )

    @property
    def FCtlEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlEndSequence"])
        )

    @property
    def FCtlEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlEndConnection"])
        )

    @property
    def FCtlCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority Enable, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlCsCtlPriority"])
        )

    @property
    def FCtlSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 1
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlSequenceInitiative"])
        )

    @property
    def FCtlFcXidReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcXidReassigned"])
        )

    @property
    def FCtlFcInvalidateXid(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcInvalidateXid"])
        )

    @property
    def FCtlAckForm(self):
        """
        Display Name: ACK
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCtlAckForm"]))

    @property
    def FCtlFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcDataCompression"])
        )

    @property
    def FCtlFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcDataEncryption"])
        )

    @property
    def FCtlRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlRetransmittedSequence"])
        )

    @property
    def FCtlUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlUnidirectionalTransmit"])
        )

    @property
    def FCtlContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlContinueSeqCondition"])
        )

    @property
    def FCtlAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlAbortSeqCondition"])
        )

    @property
    def FCtlRelativeOffsetPresent(self):
        """
        Display Name: Relative offset present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlRelativeOffsetPresent"])
        )

    @property
    def FCtlExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlExchangeReassembly"])
        )

    @property
    def FCtlFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCtlFillBytes"]))

    @property
    def FcHeaderSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSeqId"]))

    @property
    def FcHeaderDfCtl(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderDfCtl"]))

    @property
    def FcHeaderSeqCnt(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSeqCnt"])
        )

    @property
    def FcHeaderOxId(self):
        """
        Display Name: OX_ID
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderOxId"]))

    @property
    def FcHeaderRxId(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderRxId"]))

    @property
    def FcHeaderParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderParameter"])
        )

    @property
    def FcElsCommandCodeFcElsCommandCodeLsAcc(self):
        """
        Display Name: LS_ACC
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsCommandCodeFcElsCommandCodeLsAcc"]
            ),
        )

    @property
    def FcElsRequestAcceptRejectFcElsRequestReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsRequestAcceptRejectFcElsRequestReserved"]
            ),
        )

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersFcphVersion(self):
        """
        Display Name: FC-PH Version
        Default Value: 0x2020
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsCommonServiceParametersFcElsCommonServiceParametersFc-phVersion"
                ]
            ),
        )

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersBuffertobufferCredit(
        self,
    ):
        """
        Display Name: Buffer-to-Buffer Credit
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsCommonServiceParametersFcElsCommonServiceParametersBuffer-to-bufferCredit"
                ]
            ),
        )

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersCommonFeatures(self):
        """
        Display Name: Common Features
        Default Value: 0x8000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsCommonServiceParametersFcElsCommonServiceParametersCommonFeatures"
                ]
            ),
        )

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersBbScNumber(self):
        """
        Display Name: BB_SC_Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsCommonServiceParametersFcElsCommonServiceParametersBbScNumber"
                ]
            ),
        )

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersBuffertobufferReceiveDataFieldSize(
        self,
    ):
        """
        Display Name: Buffer-to-Buffer Receive Data Field Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsCommonServiceParametersFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize"
                ]
            ),
        )

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersRATov(self):
        """
        Display Name: R_A_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsCommonServiceParametersFcElsCommonServiceParametersRATov"
                ]
            ),
        )

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersEDTov(self):
        """
        Display Name: E_D_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsCommonServiceParametersFcElsCommonServiceParametersEDTov"
                ]
            ),
        )

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersNPortPortName(self):
        """
        Display Name: N_Port Port Name
        Default Value: 0x2000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsCommonServiceParametersFcElsCommonServiceParametersNPortPortName"
                ]
            ),
        )

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersFabricNodeName(self):
        """
        Display Name: Fabric/Node Name
        Default Value: 0x1000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsCommonServiceParametersFcElsCommonServiceParametersFabricNodeName"
                ]
            ),
        )

    @property
    def FcElsRequestAcceptRejectFcElsClass1SvcParameters(self):
        """
        Display Name: Class 1 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsRequestAcceptRejectFcElsClass1SvcParameters"]
            ),
        )

    @property
    def FcElsRequestAcceptRejectFcElsClass2SvcParameters(self):
        """
        Display Name: Class 2 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsRequestAcceptRejectFcElsClass2SvcParameters"]
            ),
        )

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersServiceOptions(self):
        """
        Display Name: Service Options
        Default Value: 0x8800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsClass3SvcParametersFcElsClass3SvcParametersServiceOptions"
                ]
            ),
        )

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersInitiatorControl(self):
        """
        Display Name: Initiator Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsClass3SvcParametersFcElsClass3SvcParametersInitiatorControl"
                ]
            ),
        )

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersRecipientControl(self):
        """
        Display Name: Recipient Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsClass3SvcParametersFcElsClass3SvcParametersRecipientControl"
                ]
            ),
        )

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersClassReceiveSize(self):
        """
        Display Name: Class Receive Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsClass3SvcParametersFcElsClass3SvcParametersClassReceiveSize"
                ]
            ),
        )

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersTotalConcurrentSequence(self):
        """
        Display Name: Total Concurrent Sequence
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsClass3SvcParametersFcElsClass3SvcParametersTotalConcurrentSequence"
                ]
            ),
        )

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersEndtoendCredit(self):
        """
        Display Name: End-to-End Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsClass3SvcParametersFcElsClass3SvcParametersEnd-to-endCredit"
                ]
            ),
        )

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersOpenSeqPerExchange(self):
        """
        Display Name: Open Seq Per Exchange
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsClass3SvcParametersFcElsClass3SvcParametersOpenSeqPerExchange"
                ]
            ),
        )

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersCrTov(self):
        """
        Display Name: CR_TOV
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FcElsClass3SvcParametersFcElsClass3SvcParametersCrTov"
                ]
            ),
        )

    @property
    def FcElsRequestAcceptRejectClass4SvcParameters(self):
        """
        Display Name: Class 4 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsRequestAcceptRejectClass4SvcParameters"]
            ),
        )

    @property
    def FcElsRequestAcceptRejectFcElsVendorVersion(self):
        """
        Display Name: Vendor Version
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsRequestAcceptRejectFcElsVendorVersion"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

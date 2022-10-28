# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.dkcreturns.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.dkcreturns.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.dkcreturns.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.dkcreturns.archetypes.PlayerCommonData import PlayerCommonData
from retro_data_structures.properties.dkcreturns.archetypes.PlayerMountData import PlayerMountData
from retro_data_structures.properties.dkcreturns.archetypes.PlayerMountRiderList import PlayerMountRiderList
from retro_data_structures.properties.dkcreturns.archetypes.ShadowData import ShadowData
from retro_data_structures.properties.dkcreturns.archetypes.UnknownStruct import UnknownStruct
from retro_data_structures.properties.dkcreturns.archetypes.UnknownStruct297 import UnknownStruct297
from retro_data_structures.properties.dkcreturns.core.Vector import Vector


@dataclasses.dataclass()
class VerticalRocketBarrel(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties)
    patterned: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef)
    shadow_data: ShadowData = dataclasses.field(default_factory=ShadowData)
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters)
    unknown_struct: UnknownStruct = dataclasses.field(default_factory=UnknownStruct)
    common: PlayerCommonData = dataclasses.field(default_factory=PlayerCommonData)
    mount_data: PlayerMountData = dataclasses.field(default_factory=PlayerMountData)
    rider_list_data: PlayerMountRiderList = dataclasses.field(default_factory=PlayerMountRiderList)
    unknown_struct297: UnknownStruct297 = dataclasses.field(default_factory=UnknownStruct297)

    @classmethod
    def game(cls) -> Game:
        return Game.DKCRETURNS

    @classmethod
    def object_type(cls) -> str:
        return 'VRBR'

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None, default_override: typing.Optional[dict] = None):
        struct_id, size, property_count = struct.unpack(">LHH", data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = struct.unpack(">LH", data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, property_size)
            except KeyError:
                data.read(property_size)  # skip unknown property
            assert data.tell() - start == property_size

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    def to_stream(self, data: typing.BinaryIO, default_override: typing.Optional[dict] = None):
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\t')  # 9 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, default_override={'collision_radius': 0.5, 'collision_offset': Vector(x=0.0, y=0.0, z=-0.699999988079071)})
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\xbf\x81\xc8>')  # 0xbf81c83e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shadow_data.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'~9\x7f\xed')  # 0x7e397fed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.actor_information.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\x00c\xf68')  # 0x63f638
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'<8I\x8d')  # 0x3c38498d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.common.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\x97\x8e[\xd8')  # 0x978e5bd8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mount_data.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\x7fh\x14\x11')  # 0x7f681411
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rider_list_data.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'E\xb5\xb7T')  # 0x45b5b754
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct297.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            editor_properties=EditorProperties.from_json(data['editor_properties']),
            patterned=PatternedAITypedef.from_json(data['patterned']),
            shadow_data=ShadowData.from_json(data['shadow_data']),
            actor_information=ActorParameters.from_json(data['actor_information']),
            unknown_struct=UnknownStruct.from_json(data['unknown_struct']),
            common=PlayerCommonData.from_json(data['common']),
            mount_data=PlayerMountData.from_json(data['mount_data']),
            rider_list_data=PlayerMountRiderList.from_json(data['rider_list_data']),
            unknown_struct297=UnknownStruct297.from_json(data['unknown_struct297']),
        )

    def to_json(self) -> dict:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'shadow_data': self.shadow_data.to_json(),
            'actor_information': self.actor_information.to_json(),
            'unknown_struct': self.unknown_struct.to_json(),
            'common': self.common.to_json(),
            'mount_data': self.mount_data.to_json(),
            'rider_list_data': self.rider_list_data.to_json(),
            'unknown_struct297': self.unknown_struct297.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, property_size: int):
    return EditorProperties.from_stream(data, property_size)


def _decode_patterned(data: typing.BinaryIO, property_size: int):
    return PatternedAITypedef.from_stream(data, property_size, default_override={'collision_radius': 0.5, 'collision_offset': Vector(x=0.0, y=0.0, z=-0.699999988079071)})


def _decode_shadow_data(data: typing.BinaryIO, property_size: int):
    return ShadowData.from_stream(data, property_size)


def _decode_actor_information(data: typing.BinaryIO, property_size: int):
    return ActorParameters.from_stream(data, property_size)


def _decode_unknown_struct(data: typing.BinaryIO, property_size: int):
    return UnknownStruct.from_stream(data, property_size)


def _decode_common(data: typing.BinaryIO, property_size: int):
    return PlayerCommonData.from_stream(data, property_size)


def _decode_mount_data(data: typing.BinaryIO, property_size: int):
    return PlayerMountData.from_stream(data, property_size)


def _decode_rider_list_data(data: typing.BinaryIO, property_size: int):
    return PlayerMountRiderList.from_stream(data, property_size)


def _decode_unknown_struct297(data: typing.BinaryIO, property_size: int):
    return UnknownStruct297.from_stream(data, property_size)


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0xbf81c83e: ('shadow_data', _decode_shadow_data),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x63f638: ('unknown_struct', _decode_unknown_struct),
    0x3c38498d: ('common', _decode_common),
    0x978e5bd8: ('mount_data', _decode_mount_data),
    0x7f681411: ('rider_list_data', _decode_rider_list_data),
    0x45b5b754: ('unknown_struct297', _decode_unknown_struct297),
}

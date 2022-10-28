# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.dkcreturns.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.dkcreturns.archetypes.BehaviorsData import BehaviorsData
from retro_data_structures.properties.dkcreturns.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.dkcreturns.archetypes.GenericCreatureData import GenericCreatureData
from retro_data_structures.properties.dkcreturns.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.dkcreturns.archetypes.RetronomeMessage import RetronomeMessage
from retro_data_structures.properties.dkcreturns.archetypes.ShadowData import ShadowData
from retro_data_structures.properties.dkcreturns.archetypes.UnknownStruct140 import UnknownStruct140


@dataclasses.dataclass()
class GenericCreature(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties)
    shadow_data: ShadowData = dataclasses.field(default_factory=ShadowData)
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters)
    patterned: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef)
    generic_creature: GenericCreatureData = dataclasses.field(default_factory=GenericCreatureData)
    behaviors: BehaviorsData = dataclasses.field(default_factory=BehaviorsData)
    unknown_struct140: UnknownStruct140 = dataclasses.field(default_factory=UnknownStruct140)
    retronome_message: RetronomeMessage = dataclasses.field(default_factory=RetronomeMessage)

    @classmethod
    def game(cls) -> Game:
        return Game.DKCRETURNS

    @classmethod
    def object_type(cls) -> str:
        return 'GCTR'

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
        data.write(b'\x00\x08')  # 8 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data)
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

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, default_override={'collision_height': 1.0})
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'c?\xa4\xa9')  # 0x633fa4a9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.generic_creature.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'U\xa74\x03')  # 0x55a73403
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.behaviors.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'W\x1e\xb1\xef')  # 0x571eb1ef
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct140.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\x89\x91c\x95')  # 0x89916395
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.retronome_message.to_stream(data)
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
            shadow_data=ShadowData.from_json(data['shadow_data']),
            actor_information=ActorParameters.from_json(data['actor_information']),
            patterned=PatternedAITypedef.from_json(data['patterned']),
            generic_creature=GenericCreatureData.from_json(data['generic_creature']),
            behaviors=BehaviorsData.from_json(data['behaviors']),
            unknown_struct140=UnknownStruct140.from_json(data['unknown_struct140']),
            retronome_message=RetronomeMessage.from_json(data['retronome_message']),
        )

    def to_json(self) -> dict:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'shadow_data': self.shadow_data.to_json(),
            'actor_information': self.actor_information.to_json(),
            'patterned': self.patterned.to_json(),
            'generic_creature': self.generic_creature.to_json(),
            'behaviors': self.behaviors.to_json(),
            'unknown_struct140': self.unknown_struct140.to_json(),
            'retronome_message': self.retronome_message.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, property_size: int):
    return EditorProperties.from_stream(data, property_size)


def _decode_shadow_data(data: typing.BinaryIO, property_size: int):
    return ShadowData.from_stream(data, property_size)


def _decode_actor_information(data: typing.BinaryIO, property_size: int):
    return ActorParameters.from_stream(data, property_size)


def _decode_patterned(data: typing.BinaryIO, property_size: int):
    return PatternedAITypedef.from_stream(data, property_size, default_override={'collision_height': 1.0})


def _decode_generic_creature(data: typing.BinaryIO, property_size: int):
    return GenericCreatureData.from_stream(data, property_size)


def _decode_behaviors(data: typing.BinaryIO, property_size: int):
    return BehaviorsData.from_stream(data, property_size)


def _decode_unknown_struct140(data: typing.BinaryIO, property_size: int):
    return UnknownStruct140.from_stream(data, property_size)


def _decode_retronome_message(data: typing.BinaryIO, property_size: int):
    return RetronomeMessage.from_stream(data, property_size)


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xbf81c83e: ('shadow_data', _decode_shadow_data),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xb3774750: ('patterned', _decode_patterned),
    0x633fa4a9: ('generic_creature', _decode_generic_creature),
    0x55a73403: ('behaviors', _decode_behaviors),
    0x571eb1ef: ('unknown_struct140', _decode_unknown_struct140),
    0x89916395: ('retronome_message', _decode_retronome_message),
}

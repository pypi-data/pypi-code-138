# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.BasicSwarmProperties import BasicSwarmProperties
from retro_data_structures.properties.echoes.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters


@dataclasses.dataclass()
class MetareeSwarm(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties)
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters)
    animation_information: AnimationParameters = dataclasses.field(default_factory=AnimationParameters)
    active: bool = dataclasses.field(default=True)
    basic_swarm_properties: BasicSwarmProperties = dataclasses.field(default_factory=BasicSwarmProperties)
    unknown_0x7399abbb: int = dataclasses.field(default=-1)
    unknown_0x734d923b: int = dataclasses.field(default=-1)
    max_attack_angle: float = dataclasses.field(default=30.0)
    into_attack_speed: float = dataclasses.field(default=1.0)
    attack_speed: float = dataclasses.field(default=1.0)

    @classmethod
    def game(cls) -> Game:
        return Game.ECHOES

    @classmethod
    def object_type(cls) -> str:
        return 'MSWM'

    @classmethod
    def modules(cls) -> typing.List[str]:
        return ['SwarmBasics.rel', 'MetareeSwarm.rel']

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
        data.write(b'\x00\n')  # 10 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data)
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

        data.write(b'\xe2_\xb0\x8c')  # 0xe25fb08c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.animation_information.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\xc6\xbb/E')  # 0xc6bb2f45
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.active))

        data.write(b'\xe1\xecsF')  # 0xe1ec7346
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.basic_swarm_properties.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b's\x99\xab\xbb')  # 0x7399abbb
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x7399abbb))

        data.write(b'sM\x92;')  # 0x734d923b
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x734d923b))

        data.write(b'\xf1\x1fs\x84')  # 0xf11f7384
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.max_attack_angle))

        data.write(b'\xcav\x1d\xcd')  # 0xca761dcd
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.into_attack_speed))

        data.write(b'l\n+\xc8')  # 0x6c0a2bc8
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.attack_speed))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            editor_properties=EditorProperties.from_json(data['editor_properties']),
            actor_information=ActorParameters.from_json(data['actor_information']),
            animation_information=AnimationParameters.from_json(data['animation_information']),
            active=data['active'],
            basic_swarm_properties=BasicSwarmProperties.from_json(data['basic_swarm_properties']),
            unknown_0x7399abbb=data['unknown_0x7399abbb'],
            unknown_0x734d923b=data['unknown_0x734d923b'],
            max_attack_angle=data['max_attack_angle'],
            into_attack_speed=data['into_attack_speed'],
            attack_speed=data['attack_speed'],
        )

    def to_json(self) -> dict:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'actor_information': self.actor_information.to_json(),
            'animation_information': self.animation_information.to_json(),
            'active': self.active,
            'basic_swarm_properties': self.basic_swarm_properties.to_json(),
            'unknown_0x7399abbb': self.unknown_0x7399abbb,
            'unknown_0x734d923b': self.unknown_0x734d923b,
            'max_attack_angle': self.max_attack_angle,
            'into_attack_speed': self.into_attack_speed,
            'attack_speed': self.attack_speed,
        }


def _decode_editor_properties(data: typing.BinaryIO, property_size: int):
    return EditorProperties.from_stream(data, property_size)


def _decode_actor_information(data: typing.BinaryIO, property_size: int):
    return ActorParameters.from_stream(data, property_size)


def _decode_animation_information(data: typing.BinaryIO, property_size: int):
    return AnimationParameters.from_stream(data, property_size)


def _decode_active(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_basic_swarm_properties(data: typing.BinaryIO, property_size: int):
    return BasicSwarmProperties.from_stream(data, property_size)


def _decode_unknown_0x7399abbb(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x734d923b(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_max_attack_angle(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_into_attack_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_attack_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xe25fb08c: ('animation_information', _decode_animation_information),
    0xc6bb2f45: ('active', _decode_active),
    0xe1ec7346: ('basic_swarm_properties', _decode_basic_swarm_properties),
    0x7399abbb: ('unknown_0x7399abbb', _decode_unknown_0x7399abbb),
    0x734d923b: ('unknown_0x734d923b', _decode_unknown_0x734d923b),
    0xf11f7384: ('max_attack_angle', _decode_max_attack_angle),
    0xca761dcd: ('into_attack_speed', _decode_into_attack_speed),
    0x6c0a2bc8: ('attack_speed', _decode_attack_speed),
}

# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.Spline import Spline
from retro_data_structures.properties.corruption.core.Vector import Vector


@dataclasses.dataclass()
class TriggerInfo(BaseProperty):
    unknown_0x97c0611f: int = dataclasses.field(default=127)  # Flagset
    unknown_0x50224907: int = dataclasses.field(default=0)
    unknown_0x46cc1b48: bool = dataclasses.field(default=False)
    damage_spline: Spline = dataclasses.field(default_factory=Spline)
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo)
    force_field: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0))

    @classmethod
    def game(cls) -> Game:
        return Game.CORRUPTION

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None, default_override: typing.Optional[dict] = None):
        property_count = struct.unpack(">H", data.read(2))[0]
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

        return cls(**present_fields)

    def to_stream(self, data: typing.BinaryIO, default_override: typing.Optional[dict] = None):
        default_override = default_override or {}
        data.write(b'\x00\x06')  # 6 properties

        data.write(b'\x97\xc0a\x1f')  # 0x97c0611f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack(">L", self.unknown_0x97c0611f))

        data.write(b'P"I\x07')  # 0x50224907
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x50224907))

        data.write(b'F\xcc\x1bH')  # 0x46cc1b48
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0x46cc1b48))

        data.write(b'\xfa\x87:g')  # 0xfa873a67
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_spline.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b' \x92~\x9b')  # 0x20927e9b
        data.write(b'\x00\x0c')  # size
        self.force_field.to_stream(data)

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            unknown_0x97c0611f=data['unknown_0x97c0611f'],
            unknown_0x50224907=data['unknown_0x50224907'],
            unknown_0x46cc1b48=data['unknown_0x46cc1b48'],
            damage_spline=Spline.from_json(data['damage_spline']),
            damage=DamageInfo.from_json(data['damage']),
            force_field=Vector.from_json(data['force_field']),
        )

    def to_json(self) -> dict:
        return {
            'unknown_0x97c0611f': self.unknown_0x97c0611f,
            'unknown_0x50224907': self.unknown_0x50224907,
            'unknown_0x46cc1b48': self.unknown_0x46cc1b48,
            'damage_spline': self.damage_spline.to_json(),
            'damage': self.damage.to_json(),
            'force_field': self.force_field.to_json(),
        }


def _decode_unknown_0x97c0611f(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">L", data.read(4))[0]


def _decode_unknown_0x50224907(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x46cc1b48(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_damage_spline(data: typing.BinaryIO, property_size: int):
    return Spline.from_stream(data, property_size)


def _decode_damage(data: typing.BinaryIO, property_size: int):
    return DamageInfo.from_stream(data, property_size)


def _decode_force_field(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x97c0611f: ('unknown_0x97c0611f', _decode_unknown_0x97c0611f),
    0x50224907: ('unknown_0x50224907', _decode_unknown_0x50224907),
    0x46cc1b48: ('unknown_0x46cc1b48', _decode_unknown_0x46cc1b48),
    0xfa873a67: ('damage_spline', _decode_damage_spline),
    0x337f9524: ('damage', _decode_damage),
    0x20927e9b: ('force_field', _decode_force_field),
}

# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class SwampBossStage2Struct(BaseProperty):
    unknown_0x95e7a2c2: float = dataclasses.field(default=3.0)
    unknown_0x76ba1c18: float = dataclasses.field(default=7.0)
    unknown_0x29e6ead6: float = dataclasses.field(default=1.0)
    unknown_0x1753225e: float = dataclasses.field(default=2.0)
    dash_chance: float = dataclasses.field(default=0.20000000298023224)
    taunt_chance: float = dataclasses.field(default=0.20000000298023224)
    first_attack: int = dataclasses.field(default=0)
    second_attack: int = dataclasses.field(default=0)
    third_attack: int = dataclasses.field(default=0)
    fourth_attack: int = dataclasses.field(default=7)
    fifth_attack: int = dataclasses.field(default=7)
    health: float = dataclasses.field(default=10.0)
    unknown_0x2e7e55f2: int = dataclasses.field(default=5)
    unknown_0xef3efec0: int = dataclasses.field(default=2)
    unknown_0x2b0bfd51: int = dataclasses.field(default=10)

    @classmethod
    def game(cls) -> Game:
        return Game.ECHOES

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None, default_override: typing.Optional[dict] = None):
        property_count = struct.unpack(">H", data.read(2))[0]
        if default_override is None and (result := _fast_decode(data, property_count)) is not None:
            return result

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
        data.write(b'\x00\x0f')  # 15 properties

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x95e7a2c2))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x76ba1c18))

        data.write(b')\xe6\xea\xd6')  # 0x29e6ead6
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x29e6ead6))

        data.write(b'\x17S"^')  # 0x1753225e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x1753225e))

        data.write(b'\xbe\x1a\xfb\xf8')  # 0xbe1afbf8
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.dash_chance))

        data.write(b'\xa7\x7fb\x12')  # 0xa77f6212
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.taunt_chance))

        data.write(b'\x9c\xfa\x9a\xcb')  # 0x9cfa9acb
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.first_attack))

        data.write(b'\x18\x0f\x81\xdd')  # 0x180f81dd
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.second_attack))

        data.write(b'Ba|\xfd')  # 0x42617cfd
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.third_attack))

        data.write(b'\xc3\x9f\x86N')  # 0xc39f864e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.fourth_attack))

        data.write(b'\x19\x94\xd5\x06')  # 0x1994d506
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.fifth_attack))

        data.write(b'\xf0f\x89\x19')  # 0xf0668919
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.health))

        data.write(b'.~U\xf2')  # 0x2e7e55f2
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x2e7e55f2))

        data.write(b'\xef>\xfe\xc0')  # 0xef3efec0
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0xef3efec0))

        data.write(b'+\x0b\xfdQ')  # 0x2b0bfd51
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x2b0bfd51))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            unknown_0x95e7a2c2=data['unknown_0x95e7a2c2'],
            unknown_0x76ba1c18=data['unknown_0x76ba1c18'],
            unknown_0x29e6ead6=data['unknown_0x29e6ead6'],
            unknown_0x1753225e=data['unknown_0x1753225e'],
            dash_chance=data['dash_chance'],
            taunt_chance=data['taunt_chance'],
            first_attack=data['first_attack'],
            second_attack=data['second_attack'],
            third_attack=data['third_attack'],
            fourth_attack=data['fourth_attack'],
            fifth_attack=data['fifth_attack'],
            health=data['health'],
            unknown_0x2e7e55f2=data['unknown_0x2e7e55f2'],
            unknown_0xef3efec0=data['unknown_0xef3efec0'],
            unknown_0x2b0bfd51=data['unknown_0x2b0bfd51'],
        )

    def to_json(self) -> dict:
        return {
            'unknown_0x95e7a2c2': self.unknown_0x95e7a2c2,
            'unknown_0x76ba1c18': self.unknown_0x76ba1c18,
            'unknown_0x29e6ead6': self.unknown_0x29e6ead6,
            'unknown_0x1753225e': self.unknown_0x1753225e,
            'dash_chance': self.dash_chance,
            'taunt_chance': self.taunt_chance,
            'first_attack': self.first_attack,
            'second_attack': self.second_attack,
            'third_attack': self.third_attack,
            'fourth_attack': self.fourth_attack,
            'fifth_attack': self.fifth_attack,
            'health': self.health,
            'unknown_0x2e7e55f2': self.unknown_0x2e7e55f2,
            'unknown_0xef3efec0': self.unknown_0xef3efec0,
            'unknown_0x2b0bfd51': self.unknown_0x2b0bfd51,
        }


_FAST_FORMAT = None
_FAST_IDS = (0x95e7a2c2, 0x76ba1c18, 0x29e6ead6, 0x1753225e, 0xbe1afbf8, 0xa77f6212, 0x9cfa9acb, 0x180f81dd, 0x42617cfd, 0xc39f864e, 0x1994d506, 0xf0668919, 0x2e7e55f2, 0xef3efec0, 0x2b0bfd51)


def _fast_decode(data: typing.BinaryIO, property_count: int) -> typing.Optional[SwampBossStage2Struct]:
    if property_count != 15:
        return None

    global _FAST_FORMAT
    if _FAST_FORMAT is None:
        _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHlLHlLHlLHlLHlLHfLHlLHlLHl')

    dec = _FAST_FORMAT.unpack(data.read(150))
    if (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[33], dec[36], dec[39], dec[42]) != _FAST_IDS:
        return None

    return SwampBossStage2Struct(
        dec[2],
        dec[5],
        dec[8],
        dec[11],
        dec[14],
        dec[17],
        dec[20],
        dec[23],
        dec[26],
        dec[29],
        dec[32],
        dec[35],
        dec[38],
        dec[41],
        dec[44],
    )


def _decode_unknown_0x95e7a2c2(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x76ba1c18(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x29e6ead6(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x1753225e(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_dash_chance(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_taunt_chance(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_first_attack(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_second_attack(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_third_attack(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_fourth_attack(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_fifth_attack(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_health(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x2e7e55f2(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0xef3efec0(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x2b0bfd51(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x95e7a2c2: ('unknown_0x95e7a2c2', _decode_unknown_0x95e7a2c2),
    0x76ba1c18: ('unknown_0x76ba1c18', _decode_unknown_0x76ba1c18),
    0x29e6ead6: ('unknown_0x29e6ead6', _decode_unknown_0x29e6ead6),
    0x1753225e: ('unknown_0x1753225e', _decode_unknown_0x1753225e),
    0xbe1afbf8: ('dash_chance', _decode_dash_chance),
    0xa77f6212: ('taunt_chance', _decode_taunt_chance),
    0x9cfa9acb: ('first_attack', _decode_first_attack),
    0x180f81dd: ('second_attack', _decode_second_attack),
    0x42617cfd: ('third_attack', _decode_third_attack),
    0xc39f864e: ('fourth_attack', _decode_fourth_attack),
    0x1994d506: ('fifth_attack', _decode_fifth_attack),
    0xf0668919: ('health', _decode_health),
    0x2e7e55f2: ('unknown_0x2e7e55f2', _decode_unknown_0x2e7e55f2),
    0xef3efec0: ('unknown_0xef3efec0', _decode_unknown_0xef3efec0),
    0x2b0bfd51: ('unknown_0x2b0bfd51', _decode_unknown_0x2b0bfd51),
}

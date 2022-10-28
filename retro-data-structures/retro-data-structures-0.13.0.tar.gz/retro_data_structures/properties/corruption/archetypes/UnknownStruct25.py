# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class UnknownStruct25(BaseProperty):
    start_on_task: bool = dataclasses.field(default=False)
    cover_search_radius: float = dataclasses.field(default=25.0)
    unknown_0x95e7a2c2: float = dataclasses.field(default=2.0)
    unknown_0x76ba1c18: float = dataclasses.field(default=5.0)
    min_attack_time: float = dataclasses.field(default=1.0)
    max_attack_time: float = dataclasses.field(default=2.0)
    unknown_0x1109ad02: float = dataclasses.field(default=1.0)
    unknown_0x15939c28: float = dataclasses.field(default=2.0)
    unknown_0x761ed7af: int = dataclasses.field(default=0)

    @classmethod
    def game(cls) -> Game:
        return Game.CORRUPTION

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
        data.write(b'\x00\t')  # 9 properties

        data.write(b'\x01\xc8\x1f\x07')  # 0x1c81f07
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.start_on_task))

        data.write(b'\x82\x0c\xf2\xde')  # 0x820cf2de
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.cover_search_radius))

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x95e7a2c2))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x76ba1c18))

        data.write(b'.\xdf3h')  # 0x2edf3368
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.min_attack_time))

        data.write(b'}y+\x8c')  # 0x7d792b8c
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.max_attack_time))

        data.write(b'\x11\t\xad\x02')  # 0x1109ad02
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x1109ad02))

        data.write(b'\x15\x93\x9c(')  # 0x15939c28
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x15939c28))

        data.write(b'v\x1e\xd7\xaf')  # 0x761ed7af
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x761ed7af))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            start_on_task=data['start_on_task'],
            cover_search_radius=data['cover_search_radius'],
            unknown_0x95e7a2c2=data['unknown_0x95e7a2c2'],
            unknown_0x76ba1c18=data['unknown_0x76ba1c18'],
            min_attack_time=data['min_attack_time'],
            max_attack_time=data['max_attack_time'],
            unknown_0x1109ad02=data['unknown_0x1109ad02'],
            unknown_0x15939c28=data['unknown_0x15939c28'],
            unknown_0x761ed7af=data['unknown_0x761ed7af'],
        )

    def to_json(self) -> dict:
        return {
            'start_on_task': self.start_on_task,
            'cover_search_radius': self.cover_search_radius,
            'unknown_0x95e7a2c2': self.unknown_0x95e7a2c2,
            'unknown_0x76ba1c18': self.unknown_0x76ba1c18,
            'min_attack_time': self.min_attack_time,
            'max_attack_time': self.max_attack_time,
            'unknown_0x1109ad02': self.unknown_0x1109ad02,
            'unknown_0x15939c28': self.unknown_0x15939c28,
            'unknown_0x761ed7af': self.unknown_0x761ed7af,
        }


_FAST_FORMAT = None
_FAST_IDS = (0x1c81f07, 0x820cf2de, 0x95e7a2c2, 0x76ba1c18, 0x2edf3368, 0x7d792b8c, 0x1109ad02, 0x15939c28, 0x761ed7af)


def _fast_decode(data: typing.BinaryIO, property_count: int) -> typing.Optional[UnknownStruct25]:
    if property_count != 9:
        return None

    global _FAST_FORMAT
    if _FAST_FORMAT is None:
        _FAST_FORMAT = struct.Struct('>LH?LHfLHfLHfLHfLHfLHfLHfLHl')

    dec = _FAST_FORMAT.unpack(data.read(87))
    if (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24]) != _FAST_IDS:
        return None

    return UnknownStruct25(
        dec[2],
        dec[5],
        dec[8],
        dec[11],
        dec[14],
        dec[17],
        dec[20],
        dec[23],
        dec[26],
    )


def _decode_start_on_task(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_cover_search_radius(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x95e7a2c2(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x76ba1c18(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_min_attack_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_max_attack_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x1109ad02(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x15939c28(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x761ed7af(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x1c81f07: ('start_on_task', _decode_start_on_task),
    0x820cf2de: ('cover_search_radius', _decode_cover_search_radius),
    0x95e7a2c2: ('unknown_0x95e7a2c2', _decode_unknown_0x95e7a2c2),
    0x76ba1c18: ('unknown_0x76ba1c18', _decode_unknown_0x76ba1c18),
    0x2edf3368: ('min_attack_time', _decode_min_attack_time),
    0x7d792b8c: ('max_attack_time', _decode_max_attack_time),
    0x1109ad02: ('unknown_0x1109ad02', _decode_unknown_0x1109ad02),
    0x15939c28: ('unknown_0x15939c28', _decode_unknown_0x15939c28),
    0x761ed7af: ('unknown_0x761ed7af', _decode_unknown_0x761ed7af),
}

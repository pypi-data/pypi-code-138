# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class UnknownStruct4(BaseProperty):
    center_x: float = dataclasses.field(default=320.0)
    center_y: float = dataclasses.field(default=224.0)
    min_radius: float = dataclasses.field(default=0.0)
    max_radius: float = dataclasses.field(default=64.0)
    initial_angle: float = dataclasses.field(default=45.0)
    arc_angle: float = dataclasses.field(default=90.0)

    @classmethod
    def game(cls) -> Game:
        return Game.DKCRETURNS

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
        data.write(b'\x00\x06')  # 6 properties

        data.write(b'\x8c\x93\x8c?')  # 0x8c938c3f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.center_x))

        data.write(b'G\xcf_\x9a')  # 0x47cf5f9a
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.center_y))

        data.write(b"|\xbf'\xca")  # 0x7cbf27ca
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.min_radius))

        data.write(b'\xc5\x99\xbc\xbb')  # 0xc599bcbb
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.max_radius))

        data.write(b'\x90\xac\x80A')  # 0x90ac8041
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.initial_angle))

        data.write(b'\xb5\x88\x90\xfb')  # 0xb58890fb
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.arc_angle))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            center_x=data['center_x'],
            center_y=data['center_y'],
            min_radius=data['min_radius'],
            max_radius=data['max_radius'],
            initial_angle=data['initial_angle'],
            arc_angle=data['arc_angle'],
        )

    def to_json(self) -> dict:
        return {
            'center_x': self.center_x,
            'center_y': self.center_y,
            'min_radius': self.min_radius,
            'max_radius': self.max_radius,
            'initial_angle': self.initial_angle,
            'arc_angle': self.arc_angle,
        }


_FAST_FORMAT = None
_FAST_IDS = (0x8c938c3f, 0x47cf5f9a, 0x7cbf27ca, 0xc599bcbb, 0x90ac8041, 0xb58890fb)


def _fast_decode(data: typing.BinaryIO, property_count: int) -> typing.Optional[UnknownStruct4]:
    if property_count != 6:
        return None

    global _FAST_FORMAT
    if _FAST_FORMAT is None:
        _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHf')

    dec = _FAST_FORMAT.unpack(data.read(60))
    if (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15]) != _FAST_IDS:
        return None

    return UnknownStruct4(
        dec[2],
        dec[5],
        dec[8],
        dec[11],
        dec[14],
        dec[17],
    )


def _decode_center_x(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_center_y(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_min_radius(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_max_radius(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_initial_angle(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_arc_angle(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x8c938c3f: ('center_x', _decode_center_x),
    0x47cf5f9a: ('center_y', _decode_center_y),
    0x7cbf27ca: ('min_radius', _decode_min_radius),
    0xc599bcbb: ('max_radius', _decode_max_radius),
    0x90ac8041: ('initial_angle', _decode_initial_angle),
    0xb58890fb: ('arc_angle', _decode_arc_angle),
}

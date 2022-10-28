# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class Misc(BaseProperty):
    eye_offset: float = dataclasses.field(default=0.20000000298023224)
    normal_turn_factor: float = dataclasses.field(default=1.0)
    free_look_turn_factor: float = dataclasses.field(default=1.0)
    free_look_max_x: float = dataclasses.field(default=100.0)
    free_look_max_z: float = dataclasses.field(default=70.0)
    free_look_speed: float = dataclasses.field(default=100.0)
    free_look_snap_speed: float = dataclasses.field(default=200.0)
    free_look_fade_angle: float = dataclasses.field(default=5.0)
    free_look_min_angle: float = dataclasses.field(default=0.10000000149011612)
    free_look_centered_time: float = dataclasses.field(default=0.25)
    free_look_dampen_factor: float = dataclasses.field(default=80.0)
    null_analog_scales: bool = dataclasses.field(default=False)
    unknown_0xfb909bc3: float = dataclasses.field(default=5.0)
    left_analog_max: float = dataclasses.field(default=1.0)
    right_analog_max: float = dataclasses.field(default=1.0)
    unknown_0x88297760: bool = dataclasses.field(default=True)

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
        data.write(b'\x00\x10')  # 16 properties

        data.write(b'\xb4\x9b\x00\x8e')  # 0xb49b008e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.eye_offset))

        data.write(b'\xb0)\x14p')  # 0xb0291470
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.normal_turn_factor))

        data.write(b'(x\x92\xab')  # 0x287892ab
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.free_look_turn_factor))

        data.write(b'y\xf8\xef\x93')  # 0x79f8ef93
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.free_look_max_x))

        data.write(b'40N\x98')  # 0x34304e98
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.free_look_max_z))

        data.write(b"\xba'Uo")  # 0xba27556f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.free_look_speed))

        data.write(b'\xd7\xd7\x82\x8e')  # 0xd7d7828e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.free_look_snap_speed))

        data.write(b'\x0e\x0cC\x1e')  # 0xe0c431e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.free_look_fade_angle))

        data.write(b',\x1d\xa0\xec')  # 0x2c1da0ec
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.free_look_min_angle))

        data.write(b'\xe1\x17\x88\xe4')  # 0xe11788e4
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.free_look_centered_time))

        data.write(b'\xc9\x82uN')  # 0xc982754e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.free_look_dampen_factor))

        data.write(b'\xfb\\\x81\xa9')  # 0xfb5c81a9
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.null_analog_scales))

        data.write(b'\xfb\x90\x9b\xc3')  # 0xfb909bc3
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xfb909bc3))

        data.write(b'\xf1\xf08\xde')  # 0xf1f038de
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.left_analog_max))

        data.write(b'+\x1fP\x94')  # 0x2b1f5094
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.right_analog_max))

        data.write(b'\x88)w`')  # 0x88297760
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0x88297760))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            eye_offset=data['eye_offset'],
            normal_turn_factor=data['normal_turn_factor'],
            free_look_turn_factor=data['free_look_turn_factor'],
            free_look_max_x=data['free_look_max_x'],
            free_look_max_z=data['free_look_max_z'],
            free_look_speed=data['free_look_speed'],
            free_look_snap_speed=data['free_look_snap_speed'],
            free_look_fade_angle=data['free_look_fade_angle'],
            free_look_min_angle=data['free_look_min_angle'],
            free_look_centered_time=data['free_look_centered_time'],
            free_look_dampen_factor=data['free_look_dampen_factor'],
            null_analog_scales=data['null_analog_scales'],
            unknown_0xfb909bc3=data['unknown_0xfb909bc3'],
            left_analog_max=data['left_analog_max'],
            right_analog_max=data['right_analog_max'],
            unknown_0x88297760=data['unknown_0x88297760'],
        )

    def to_json(self) -> dict:
        return {
            'eye_offset': self.eye_offset,
            'normal_turn_factor': self.normal_turn_factor,
            'free_look_turn_factor': self.free_look_turn_factor,
            'free_look_max_x': self.free_look_max_x,
            'free_look_max_z': self.free_look_max_z,
            'free_look_speed': self.free_look_speed,
            'free_look_snap_speed': self.free_look_snap_speed,
            'free_look_fade_angle': self.free_look_fade_angle,
            'free_look_min_angle': self.free_look_min_angle,
            'free_look_centered_time': self.free_look_centered_time,
            'free_look_dampen_factor': self.free_look_dampen_factor,
            'null_analog_scales': self.null_analog_scales,
            'unknown_0xfb909bc3': self.unknown_0xfb909bc3,
            'left_analog_max': self.left_analog_max,
            'right_analog_max': self.right_analog_max,
            'unknown_0x88297760': self.unknown_0x88297760,
        }


_FAST_FORMAT = None
_FAST_IDS = (0xb49b008e, 0xb0291470, 0x287892ab, 0x79f8ef93, 0x34304e98, 0xba27556f, 0xd7d7828e, 0xe0c431e, 0x2c1da0ec, 0xe11788e4, 0xc982754e, 0xfb5c81a9, 0xfb909bc3, 0xf1f038de, 0x2b1f5094, 0x88297760)


def _fast_decode(data: typing.BinaryIO, property_count: int) -> typing.Optional[Misc]:
    if property_count != 16:
        return None

    global _FAST_FORMAT
    if _FAST_FORMAT is None:
        _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLH?LHfLHfLHfLH?')

    dec = _FAST_FORMAT.unpack(data.read(154))
    if (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[33], dec[36], dec[39], dec[42], dec[45]) != _FAST_IDS:
        return None

    return Misc(
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
        dec[47],
    )


def _decode_eye_offset(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_normal_turn_factor(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_free_look_turn_factor(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_free_look_max_x(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_free_look_max_z(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_free_look_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_free_look_snap_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_free_look_fade_angle(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_free_look_min_angle(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_free_look_centered_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_free_look_dampen_factor(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_null_analog_scales(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0xfb909bc3(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_left_analog_max(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_right_analog_max(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x88297760(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0xb49b008e: ('eye_offset', _decode_eye_offset),
    0xb0291470: ('normal_turn_factor', _decode_normal_turn_factor),
    0x287892ab: ('free_look_turn_factor', _decode_free_look_turn_factor),
    0x79f8ef93: ('free_look_max_x', _decode_free_look_max_x),
    0x34304e98: ('free_look_max_z', _decode_free_look_max_z),
    0xba27556f: ('free_look_speed', _decode_free_look_speed),
    0xd7d7828e: ('free_look_snap_speed', _decode_free_look_snap_speed),
    0xe0c431e: ('free_look_fade_angle', _decode_free_look_fade_angle),
    0x2c1da0ec: ('free_look_min_angle', _decode_free_look_min_angle),
    0xe11788e4: ('free_look_centered_time', _decode_free_look_centered_time),
    0xc982754e: ('free_look_dampen_factor', _decode_free_look_dampen_factor),
    0xfb5c81a9: ('null_analog_scales', _decode_null_analog_scales),
    0xfb909bc3: ('unknown_0xfb909bc3', _decode_unknown_0xfb909bc3),
    0xf1f038de: ('left_analog_max', _decode_left_analog_max),
    0x2b1f5094: ('right_analog_max', _decode_right_analog_max),
    0x88297760: ('unknown_0x88297760', _decode_unknown_0x88297760),
}

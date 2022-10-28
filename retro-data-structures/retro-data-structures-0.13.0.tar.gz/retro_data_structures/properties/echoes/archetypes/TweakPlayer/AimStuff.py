# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class AimStuff(BaseProperty):
    aim_min_time: float = dataclasses.field(default=0.10000000149011612)
    aim_max_time: float = dataclasses.field(default=0.25)
    aim_max_distance: float = dataclasses.field(default=100.0)
    aim_max_angle_left: float = dataclasses.field(default=30.0)
    aim_max_angle_right: float = dataclasses.field(default=30.0)
    aim_max_angle_up: float = dataclasses.field(default=50.0)
    aim_max_angle_down: float = dataclasses.field(default=60.0)
    aim_angle_per_second: float = dataclasses.field(default=110.0)
    aim_threshold_distance: float = dataclasses.field(default=5.0)
    aim_turn_angle_per_second: float = dataclasses.field(default=360.0)
    unknown: float = dataclasses.field(default=10.0)
    aim_box_width: float = dataclasses.field(default=20.0)
    aim_box_height: float = dataclasses.field(default=10.0)
    aim_target_timer: float = dataclasses.field(default=0.009999999776482582)
    aim_assist_horizontal_angle: float = dataclasses.field(default=5.0)
    aim_assist_vertical_angle: float = dataclasses.field(default=5.0)

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
        data.write(b'\x00\x10')  # 16 properties

        data.write(b"'\xc6\r\n")  # 0x27c60d0a
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_min_time))

        data.write(b'\xb7\xb5\x1d\xe0')  # 0xb7b51de0
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_max_time))

        data.write(b'\xf7}\x03Y')  # 0xf77d0359
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_max_distance))

        data.write(b'\xde\x88|\xca')  # 0xde887cca
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_max_angle_left))

        data.write(b'\xb4\xb0}]')  # 0xb4b07d5d
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_max_angle_right))

        data.write(b'\xe5\xf8\xc5g')  # 0xe5f8c567
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_max_angle_up))

        data.write(b'\x97tt\x9d')  # 0x9774749d
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_max_angle_down))

        data.write(b'\x13?0\x02')  # 0x133f3002
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_angle_per_second))

        data.write(b'\x96\xfa\xb6\x02')  # 0x96fab602
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_threshold_distance))

        data.write(b'\x94\x16J/')  # 0x94164a2f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_turn_angle_per_second))

        data.write(b'T5L\x80')  # 0x54354c80
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown))

        data.write(b'Sa\xce\x18')  # 0x5361ce18
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_box_width))

        data.write(b'K.\x92`')  # 0x4b2e9260
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_box_height))

        data.write(b';\x9a7\x89')  # 0x3b9a3789
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_target_timer))

        data.write(b'8\xdd\x0b\x85')  # 0x38dd0b85
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_assist_horizontal_angle))

        data.write(b'\x11W\x88>')  # 0x1157883e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.aim_assist_vertical_angle))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            aim_min_time=data['aim_min_time'],
            aim_max_time=data['aim_max_time'],
            aim_max_distance=data['aim_max_distance'],
            aim_max_angle_left=data['aim_max_angle_left'],
            aim_max_angle_right=data['aim_max_angle_right'],
            aim_max_angle_up=data['aim_max_angle_up'],
            aim_max_angle_down=data['aim_max_angle_down'],
            aim_angle_per_second=data['aim_angle_per_second'],
            aim_threshold_distance=data['aim_threshold_distance'],
            aim_turn_angle_per_second=data['aim_turn_angle_per_second'],
            unknown=data['unknown'],
            aim_box_width=data['aim_box_width'],
            aim_box_height=data['aim_box_height'],
            aim_target_timer=data['aim_target_timer'],
            aim_assist_horizontal_angle=data['aim_assist_horizontal_angle'],
            aim_assist_vertical_angle=data['aim_assist_vertical_angle'],
        )

    def to_json(self) -> dict:
        return {
            'aim_min_time': self.aim_min_time,
            'aim_max_time': self.aim_max_time,
            'aim_max_distance': self.aim_max_distance,
            'aim_max_angle_left': self.aim_max_angle_left,
            'aim_max_angle_right': self.aim_max_angle_right,
            'aim_max_angle_up': self.aim_max_angle_up,
            'aim_max_angle_down': self.aim_max_angle_down,
            'aim_angle_per_second': self.aim_angle_per_second,
            'aim_threshold_distance': self.aim_threshold_distance,
            'aim_turn_angle_per_second': self.aim_turn_angle_per_second,
            'unknown': self.unknown,
            'aim_box_width': self.aim_box_width,
            'aim_box_height': self.aim_box_height,
            'aim_target_timer': self.aim_target_timer,
            'aim_assist_horizontal_angle': self.aim_assist_horizontal_angle,
            'aim_assist_vertical_angle': self.aim_assist_vertical_angle,
        }


_FAST_FORMAT = None
_FAST_IDS = (0x27c60d0a, 0xb7b51de0, 0xf77d0359, 0xde887cca, 0xb4b07d5d, 0xe5f8c567, 0x9774749d, 0x133f3002, 0x96fab602, 0x94164a2f, 0x54354c80, 0x5361ce18, 0x4b2e9260, 0x3b9a3789, 0x38dd0b85, 0x1157883e)


def _fast_decode(data: typing.BinaryIO, property_count: int) -> typing.Optional[AimStuff]:
    if property_count != 16:
        return None

    global _FAST_FORMAT
    if _FAST_FORMAT is None:
        _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHf')

    dec = _FAST_FORMAT.unpack(data.read(160))
    if (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[33], dec[36], dec[39], dec[42], dec[45]) != _FAST_IDS:
        return None

    return AimStuff(
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


def _decode_aim_min_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_max_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_max_distance(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_max_angle_left(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_max_angle_right(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_max_angle_up(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_max_angle_down(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_angle_per_second(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_threshold_distance(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_turn_angle_per_second(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_box_width(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_box_height(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_target_timer(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_assist_horizontal_angle(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_aim_assist_vertical_angle(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x27c60d0a: ('aim_min_time', _decode_aim_min_time),
    0xb7b51de0: ('aim_max_time', _decode_aim_max_time),
    0xf77d0359: ('aim_max_distance', _decode_aim_max_distance),
    0xde887cca: ('aim_max_angle_left', _decode_aim_max_angle_left),
    0xb4b07d5d: ('aim_max_angle_right', _decode_aim_max_angle_right),
    0xe5f8c567: ('aim_max_angle_up', _decode_aim_max_angle_up),
    0x9774749d: ('aim_max_angle_down', _decode_aim_max_angle_down),
    0x133f3002: ('aim_angle_per_second', _decode_aim_angle_per_second),
    0x96fab602: ('aim_threshold_distance', _decode_aim_threshold_distance),
    0x94164a2f: ('aim_turn_angle_per_second', _decode_aim_turn_angle_per_second),
    0x54354c80: ('unknown', _decode_unknown),
    0x5361ce18: ('aim_box_width', _decode_aim_box_width),
    0x4b2e9260: ('aim_box_height', _decode_aim_box_height),
    0x3b9a3789: ('aim_target_timer', _decode_aim_target_timer),
    0x38dd0b85: ('aim_assist_horizontal_angle', _decode_aim_assist_horizontal_angle),
    0x1157883e: ('aim_assist_vertical_angle', _decode_aim_assist_vertical_angle),
}

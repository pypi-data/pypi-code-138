# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.corruption.archetypes.EditorProperties import EditorProperties


@dataclasses.dataclass()
class AITaskPoint(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties)
    stay_forever: bool = dataclasses.field(default=False)
    unknown_0xb553cda1: float = dataclasses.field(default=1.0)
    unknown_0x53336240: float = dataclasses.field(default=30.0)
    unknown_0x12341132: bool = dataclasses.field(default=False)
    unknown_0xaaccd7cd: int = dataclasses.field(default=-1)
    idle_animation: int = dataclasses.field(default=-1)
    unknown_0x799f6f58: int = dataclasses.field(default=-1)
    unknown_0x121045f5: float = dataclasses.field(default=5.0)
    unknown_0xf470ea14: float = dataclasses.field(default=10.0)
    unknown_0x7aa31371: int = dataclasses.field(default=-1)
    unknown_0x0ac4d7ad: int = dataclasses.field(default=-1)
    unknown_0x03d511b9: int = dataclasses.field(default=-1)
    unknown_0x2bd321da: int = dataclasses.field(default=-1)
    unknown_0x2b3bd997: int = dataclasses.field(default=-1)
    unknown_0xc36101f6: int = dataclasses.field(default=-1)
    unknown_0x3fa8c740: int = dataclasses.field(default=-1)
    unknown_0x3aca31d7: int = dataclasses.field(default=-1)
    unknown_0xe5d4d300: int = dataclasses.field(default=8)
    is_combat_task: bool = dataclasses.field(default=False)
    unknown_0x2cf6f605: bool = dataclasses.field(default=False)
    unknown_0x81591346: bool = dataclasses.field(default=False)
    unknown_0xf874aa52: bool = dataclasses.field(default=True)
    align_ai: bool = dataclasses.field(default=False)
    unknown_0x2340b043: bool = dataclasses.field(default=True)

    @classmethod
    def game(cls) -> Game:
        return Game.CORRUPTION

    @classmethod
    def object_type(cls) -> str:
        return 'AITP'

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
        data.write(b'\x00\x19')  # 25 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'V\x94\x1e\xb7')  # 0x56941eb7
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.stay_forever))

        data.write(b'\xb5S\xcd\xa1')  # 0xb553cda1
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xb553cda1))

        data.write(b'S3b@')  # 0x53336240
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x53336240))

        data.write(b'\x124\x112')  # 0x12341132
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0x12341132))

        data.write(b'\xaa\xcc\xd7\xcd')  # 0xaaccd7cd
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0xaaccd7cd))

        data.write(b'\xa2\xa5\xb3\x8f')  # 0xa2a5b38f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.idle_animation))

        data.write(b'y\x9foX')  # 0x799f6f58
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x799f6f58))

        data.write(b'\x12\x10E\xf5')  # 0x121045f5
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x121045f5))

        data.write(b'\xf4p\xea\x14')  # 0xf470ea14
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xf470ea14))

        data.write(b'z\xa3\x13q')  # 0x7aa31371
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x7aa31371))

        data.write(b'\n\xc4\xd7\xad')  # 0xac4d7ad
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x0ac4d7ad))

        data.write(b'\x03\xd5\x11\xb9')  # 0x3d511b9
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x03d511b9))

        data.write(b'+\xd3!\xda')  # 0x2bd321da
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x2bd321da))

        data.write(b'+;\xd9\x97')  # 0x2b3bd997
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x2b3bd997))

        data.write(b'\xc3a\x01\xf6')  # 0xc36101f6
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0xc36101f6))

        data.write(b'?\xa8\xc7@')  # 0x3fa8c740
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x3fa8c740))

        data.write(b':\xca1\xd7')  # 0x3aca31d7
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0x3aca31d7))

        data.write(b'\xe5\xd4\xd3\x00')  # 0xe5d4d300
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.unknown_0xe5d4d300))

        data.write(b'%(\xf4B')  # 0x2528f442
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.is_combat_task))

        data.write(b',\xf6\xf6\x05')  # 0x2cf6f605
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0x2cf6f605))

        data.write(b'\x81Y\x13F')  # 0x81591346
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0x81591346))

        data.write(b'\xf8t\xaaR')  # 0xf874aa52
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0xf874aa52))

        data.write(b'\\ \xcfX')  # 0x5c20cf58
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.align_ai))

        data.write(b'#@\xb0C')  # 0x2340b043
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0x2340b043))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            editor_properties=EditorProperties.from_json(data['editor_properties']),
            stay_forever=data['stay_forever'],
            unknown_0xb553cda1=data['unknown_0xb553cda1'],
            unknown_0x53336240=data['unknown_0x53336240'],
            unknown_0x12341132=data['unknown_0x12341132'],
            unknown_0xaaccd7cd=data['unknown_0xaaccd7cd'],
            idle_animation=data['idle_animation'],
            unknown_0x799f6f58=data['unknown_0x799f6f58'],
            unknown_0x121045f5=data['unknown_0x121045f5'],
            unknown_0xf470ea14=data['unknown_0xf470ea14'],
            unknown_0x7aa31371=data['unknown_0x7aa31371'],
            unknown_0x0ac4d7ad=data['unknown_0x0ac4d7ad'],
            unknown_0x03d511b9=data['unknown_0x03d511b9'],
            unknown_0x2bd321da=data['unknown_0x2bd321da'],
            unknown_0x2b3bd997=data['unknown_0x2b3bd997'],
            unknown_0xc36101f6=data['unknown_0xc36101f6'],
            unknown_0x3fa8c740=data['unknown_0x3fa8c740'],
            unknown_0x3aca31d7=data['unknown_0x3aca31d7'],
            unknown_0xe5d4d300=data['unknown_0xe5d4d300'],
            is_combat_task=data['is_combat_task'],
            unknown_0x2cf6f605=data['unknown_0x2cf6f605'],
            unknown_0x81591346=data['unknown_0x81591346'],
            unknown_0xf874aa52=data['unknown_0xf874aa52'],
            align_ai=data['align_ai'],
            unknown_0x2340b043=data['unknown_0x2340b043'],
        )

    def to_json(self) -> dict:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'stay_forever': self.stay_forever,
            'unknown_0xb553cda1': self.unknown_0xb553cda1,
            'unknown_0x53336240': self.unknown_0x53336240,
            'unknown_0x12341132': self.unknown_0x12341132,
            'unknown_0xaaccd7cd': self.unknown_0xaaccd7cd,
            'idle_animation': self.idle_animation,
            'unknown_0x799f6f58': self.unknown_0x799f6f58,
            'unknown_0x121045f5': self.unknown_0x121045f5,
            'unknown_0xf470ea14': self.unknown_0xf470ea14,
            'unknown_0x7aa31371': self.unknown_0x7aa31371,
            'unknown_0x0ac4d7ad': self.unknown_0x0ac4d7ad,
            'unknown_0x03d511b9': self.unknown_0x03d511b9,
            'unknown_0x2bd321da': self.unknown_0x2bd321da,
            'unknown_0x2b3bd997': self.unknown_0x2b3bd997,
            'unknown_0xc36101f6': self.unknown_0xc36101f6,
            'unknown_0x3fa8c740': self.unknown_0x3fa8c740,
            'unknown_0x3aca31d7': self.unknown_0x3aca31d7,
            'unknown_0xe5d4d300': self.unknown_0xe5d4d300,
            'is_combat_task': self.is_combat_task,
            'unknown_0x2cf6f605': self.unknown_0x2cf6f605,
            'unknown_0x81591346': self.unknown_0x81591346,
            'unknown_0xf874aa52': self.unknown_0xf874aa52,
            'align_ai': self.align_ai,
            'unknown_0x2340b043': self.unknown_0x2340b043,
        }


def _decode_editor_properties(data: typing.BinaryIO, property_size: int):
    return EditorProperties.from_stream(data, property_size)


def _decode_stay_forever(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0xb553cda1(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x53336240(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x12341132(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0xaaccd7cd(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_idle_animation(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x799f6f58(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x121045f5(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0xf470ea14(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x7aa31371(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x0ac4d7ad(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x03d511b9(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x2bd321da(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x2b3bd997(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0xc36101f6(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x3fa8c740(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x3aca31d7(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0xe5d4d300(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_is_combat_task(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0x2cf6f605(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0x81591346(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0xf874aa52(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_align_ai(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0x2340b043(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x56941eb7: ('stay_forever', _decode_stay_forever),
    0xb553cda1: ('unknown_0xb553cda1', _decode_unknown_0xb553cda1),
    0x53336240: ('unknown_0x53336240', _decode_unknown_0x53336240),
    0x12341132: ('unknown_0x12341132', _decode_unknown_0x12341132),
    0xaaccd7cd: ('unknown_0xaaccd7cd', _decode_unknown_0xaaccd7cd),
    0xa2a5b38f: ('idle_animation', _decode_idle_animation),
    0x799f6f58: ('unknown_0x799f6f58', _decode_unknown_0x799f6f58),
    0x121045f5: ('unknown_0x121045f5', _decode_unknown_0x121045f5),
    0xf470ea14: ('unknown_0xf470ea14', _decode_unknown_0xf470ea14),
    0x7aa31371: ('unknown_0x7aa31371', _decode_unknown_0x7aa31371),
    0xac4d7ad: ('unknown_0x0ac4d7ad', _decode_unknown_0x0ac4d7ad),
    0x3d511b9: ('unknown_0x03d511b9', _decode_unknown_0x03d511b9),
    0x2bd321da: ('unknown_0x2bd321da', _decode_unknown_0x2bd321da),
    0x2b3bd997: ('unknown_0x2b3bd997', _decode_unknown_0x2b3bd997),
    0xc36101f6: ('unknown_0xc36101f6', _decode_unknown_0xc36101f6),
    0x3fa8c740: ('unknown_0x3fa8c740', _decode_unknown_0x3fa8c740),
    0x3aca31d7: ('unknown_0x3aca31d7', _decode_unknown_0x3aca31d7),
    0xe5d4d300: ('unknown_0xe5d4d300', _decode_unknown_0xe5d4d300),
    0x2528f442: ('is_combat_task', _decode_is_combat_task),
    0x2cf6f605: ('unknown_0x2cf6f605', _decode_unknown_0x2cf6f605),
    0x81591346: ('unknown_0x81591346', _decode_unknown_0x81591346),
    0xf874aa52: ('unknown_0xf874aa52', _decode_unknown_0xf874aa52),
    0x5c20cf58: ('align_ai', _decode_align_ai),
    0x2340b043: ('unknown_0x2340b043', _decode_unknown_0x2340b043),
}

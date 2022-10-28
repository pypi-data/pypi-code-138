# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.dkcreturns.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.dkcreturns.core.AssetId import AssetId
from retro_data_structures.properties.dkcreturns.core.Color import Color


@dataclasses.dataclass()
class CameraFilterKeyframe(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties)
    filter_type: int = dataclasses.field(default=0)
    filter_shape: int = dataclasses.field(default=0)
    filter_stage: int = dataclasses.field(default=0)
    which_filter_group: int = dataclasses.field(default=0)
    color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0))
    interpolate_in_time: float = dataclasses.field(default=0.0)
    interpolate_out_time: float = dataclasses.field(default=0.0)
    texture: AssetId = dataclasses.field(metadata={'asset_types': ['TXTR']}, default=0xffffffffffffffff)
    model: AssetId = dataclasses.field(metadata={'asset_types': ['CMDL']}, default=0xffffffffffffffff)
    prevent_pause_when_incremented: bool = dataclasses.field(default=False)

    @classmethod
    def game(cls) -> Game:
        return Game.DKCRETURNS

    @classmethod
    def object_type(cls) -> str:
        return 'FILT'

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
        data.write(b'\x00\x0b')  # 11 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'yu\xdb[')  # 0x7975db5b
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.filter_type))

        data.write(b'j>\x9a=')  # 0x6a3e9a3d
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.filter_shape))

        data.write(b'X\xbd\xbd{')  # 0x58bdbd7b
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.filter_stage))

        data.write(b'?\xdcK.')  # 0x3fdc4b2e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.which_filter_group))

        data.write(b'7\xc7\xd0\x9d')  # 0x37c7d09d
        data.write(b'\x00\x10')  # size
        self.color.to_stream(data)

        data.write(b'\xab\xd4\x1a6')  # 0xabd41a36
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.interpolate_in_time))

        data.write(b'>\xafx\xfe')  # 0x3eaf78fe
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.interpolate_out_time))

        data.write(b'\xd1\xf6Xr')  # 0xd1f65872
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.texture))

        data.write(b'\xc2\x7f\xfa\x8f')  # 0xc27ffa8f
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.model))

        data.write(b'\x89\xf7\xf8\xc5')  # 0x89f7f8c5
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.prevent_pause_when_incremented))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            editor_properties=EditorProperties.from_json(data['editor_properties']),
            filter_type=data['filter_type'],
            filter_shape=data['filter_shape'],
            filter_stage=data['filter_stage'],
            which_filter_group=data['which_filter_group'],
            color=Color.from_json(data['color']),
            interpolate_in_time=data['interpolate_in_time'],
            interpolate_out_time=data['interpolate_out_time'],
            texture=data['texture'],
            model=data['model'],
            prevent_pause_when_incremented=data['prevent_pause_when_incremented'],
        )

    def to_json(self) -> dict:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'filter_type': self.filter_type,
            'filter_shape': self.filter_shape,
            'filter_stage': self.filter_stage,
            'which_filter_group': self.which_filter_group,
            'color': self.color.to_json(),
            'interpolate_in_time': self.interpolate_in_time,
            'interpolate_out_time': self.interpolate_out_time,
            'texture': self.texture,
            'model': self.model,
            'prevent_pause_when_incremented': self.prevent_pause_when_incremented,
        }


def _decode_editor_properties(data: typing.BinaryIO, property_size: int):
    return EditorProperties.from_stream(data, property_size)


def _decode_filter_type(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_filter_shape(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_filter_stage(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_which_filter_group(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_interpolate_in_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_interpolate_out_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_texture(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_model(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_prevent_pause_when_incremented(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x7975db5b: ('filter_type', _decode_filter_type),
    0x6a3e9a3d: ('filter_shape', _decode_filter_shape),
    0x58bdbd7b: ('filter_stage', _decode_filter_stage),
    0x3fdc4b2e: ('which_filter_group', _decode_which_filter_group),
    0x37c7d09d: ('color', _decode_color),
    0xabd41a36: ('interpolate_in_time', _decode_interpolate_in_time),
    0x3eaf78fe: ('interpolate_out_time', _decode_interpolate_out_time),
    0xd1f65872: ('texture', _decode_texture),
    0xc27ffa8f: ('model', _decode_model),
    0x89f7f8c5: ('prevent_pause_when_incremented', _decode_prevent_pause_when_incremented),
}

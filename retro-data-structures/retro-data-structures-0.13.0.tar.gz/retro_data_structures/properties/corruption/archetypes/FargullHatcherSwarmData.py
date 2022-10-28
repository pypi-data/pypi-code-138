# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class FargullHatcherSwarmData(BaseProperty):
    unknown_0x3109e1c7: float = dataclasses.field(default=4.0)
    unknown_0xf73a8baa: float = dataclasses.field(default=25.0)

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
        data.write(b'\x00\x02')  # 2 properties

        data.write(b'1\t\xe1\xc7')  # 0x3109e1c7
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x3109e1c7))

        data.write(b'\xf7:\x8b\xaa')  # 0xf73a8baa
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xf73a8baa))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            unknown_0x3109e1c7=data['unknown_0x3109e1c7'],
            unknown_0xf73a8baa=data['unknown_0xf73a8baa'],
        )

    def to_json(self) -> dict:
        return {
            'unknown_0x3109e1c7': self.unknown_0x3109e1c7,
            'unknown_0xf73a8baa': self.unknown_0xf73a8baa,
        }


_FAST_FORMAT = None
_FAST_IDS = (0x3109e1c7, 0xf73a8baa)


def _fast_decode(data: typing.BinaryIO, property_count: int) -> typing.Optional[FargullHatcherSwarmData]:
    if property_count != 2:
        return None

    global _FAST_FORMAT
    if _FAST_FORMAT is None:
        _FAST_FORMAT = struct.Struct('>LHfLHf')

    dec = _FAST_FORMAT.unpack(data.read(20))
    if (dec[0], dec[3]) != _FAST_IDS:
        return None

    return FargullHatcherSwarmData(
        dec[2],
        dec[5],
    )


def _decode_unknown_0x3109e1c7(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0xf73a8baa(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x3109e1c7: ('unknown_0x3109e1c7', _decode_unknown_0x3109e1c7),
    0xf73a8baa: ('unknown_0xf73a8baa', _decode_unknown_0xf73a8baa),
}

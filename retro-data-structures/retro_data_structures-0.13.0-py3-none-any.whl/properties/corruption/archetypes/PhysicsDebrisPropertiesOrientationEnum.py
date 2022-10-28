# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty
import retro_data_structures.enums.corruption as enums


@dataclasses.dataclass()
class PhysicsDebrisPropertiesOrientationEnum(BaseProperty):
    orientation: enums.UnknownEnum1 = dataclasses.field(default=enums.UnknownEnum1.Unknown1)

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
        data.write(b'\x00\x01')  # 1 properties

        data.write(b'\xf4\xbff7')  # 0xf4bf6637
        data.write(b'\x00\x04')  # size
        self.orientation.to_stream(data)

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            orientation=enums.UnknownEnum1.from_json(data['orientation']),
        )

    def to_json(self) -> dict:
        return {
            'orientation': self.orientation.to_json(),
        }


_FAST_FORMAT = None
_FAST_IDS = (0xf4bf6637)


def _fast_decode(data: typing.BinaryIO, property_count: int) -> typing.Optional[PhysicsDebrisPropertiesOrientationEnum]:
    if property_count != 1:
        return None

    global _FAST_FORMAT
    if _FAST_FORMAT is None:
        _FAST_FORMAT = struct.Struct('>LHL')

    dec = _FAST_FORMAT.unpack(data.read(10))
    if (dec[0]) != _FAST_IDS:
        return None

    return PhysicsDebrisPropertiesOrientationEnum(
        enums.UnknownEnum1(dec[2]),
    )


def _decode_orientation(data: typing.BinaryIO, property_size: int):
    return enums.UnknownEnum1.from_stream(data)


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0xf4bf6637: ('orientation', _decode_orientation),
}

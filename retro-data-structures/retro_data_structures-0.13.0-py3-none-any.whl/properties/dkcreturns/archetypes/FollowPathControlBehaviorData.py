# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class FollowPathControlBehaviorData(BaseProperty):
    reverse_movement: bool = dataclasses.field(default=False)

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
        data.write(b'\x00\x01')  # 1 properties

        data.write(b'\xff\xe2\x01\xa7')  # 0xffe201a7
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.reverse_movement))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            reverse_movement=data['reverse_movement'],
        )

    def to_json(self) -> dict:
        return {
            'reverse_movement': self.reverse_movement,
        }


_FAST_FORMAT = None
_FAST_IDS = (0xffe201a7)


def _fast_decode(data: typing.BinaryIO, property_count: int) -> typing.Optional[FollowPathControlBehaviorData]:
    if property_count != 1:
        return None

    global _FAST_FORMAT
    if _FAST_FORMAT is None:
        _FAST_FORMAT = struct.Struct('>LH?')

    dec = _FAST_FORMAT.unpack(data.read(7))
    if (dec[0]) != _FAST_IDS:
        return None

    return FollowPathControlBehaviorData(
        dec[2],
    )


def _decode_reverse_movement(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0xffe201a7: ('reverse_movement', _decode_reverse_movement),
}

# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId


@dataclasses.dataclass()
class UnknownStruct23(BaseProperty):
    loop_duration: float = dataclasses.field(default=0.0)
    destroy_percentage: int = dataclasses.field(default=0)
    shock_wave_info: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo)
    sound: AssetId = dataclasses.field(default=0x0)

    @classmethod
    def game(cls) -> Game:
        return Game.ECHOES

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None, default_override: typing.Optional[dict] = None):
        property_count = struct.unpack(">H", data.read(2))[0]
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
        data.write(b'\x00\x04')  # 4 properties

        data.write(b'\xce\xe6\x87#')  # 0xcee68723
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.loop_duration))

        data.write(b"\x01'Mn")  # 0x1274d6e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.destroy_percentage))

        data.write(b'\x8fG\x87\xcb')  # 0x8f4787cb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shock_wave_info.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'%\xafI\x0e')  # 0x25af490e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack(">L", self.sound))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            loop_duration=data['loop_duration'],
            destroy_percentage=data['destroy_percentage'],
            shock_wave_info=ShockWaveInfo.from_json(data['shock_wave_info']),
            sound=data['sound'],
        )

    def to_json(self) -> dict:
        return {
            'loop_duration': self.loop_duration,
            'destroy_percentage': self.destroy_percentage,
            'shock_wave_info': self.shock_wave_info.to_json(),
            'sound': self.sound,
        }


def _decode_loop_duration(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_destroy_percentage(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_shock_wave_info(data: typing.BinaryIO, property_size: int):
    return ShockWaveInfo.from_stream(data, property_size)


def _decode_sound(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">L", data.read(4))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0xcee68723: ('loop_duration', _decode_loop_duration),
    0x1274d6e: ('destroy_percentage', _decode_destroy_percentage),
    0x8f4787cb: ('shock_wave_info', _decode_shock_wave_info),
    0x25af490e: ('sound', _decode_sound),
}

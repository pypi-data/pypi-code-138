# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.prime.archetypes.ScannableParameters import ScannableParameters
from retro_data_structures.properties.prime.core.Vector import Vector


@dataclasses.dataclass()
class PointOfInterest(BaseObjectType):
    name: str = dataclasses.field(default='')
    position: Vector = dataclasses.field(default_factory=Vector)
    rotation: Vector = dataclasses.field(default_factory=Vector)
    active: bool = dataclasses.field(default=False)
    unnamed: ScannableParameters = dataclasses.field(default_factory=ScannableParameters)
    unknown: float = dataclasses.field(default=0.0)

    @classmethod
    def game(cls) -> Game:
        return Game.PRIME

    @classmethod
    def object_type(cls) -> int:
        return 0x42

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None, default_override: typing.Optional[dict] = None):
        property_size = None  # Atomic
        property_count = struct.unpack(">L", data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b'\x00')).decode("utf-8")
        position = Vector.from_stream(data)
        rotation = Vector.from_stream(data)
        active = struct.unpack('>?', data.read(1))[0]
        unnamed = ScannableParameters.from_stream(data, property_size)
        unknown = struct.unpack('>f', data.read(4))[0]
        return cls(name, position, rotation, active, unnamed, unknown)

    def to_stream(self, data: typing.BinaryIO, default_override: typing.Optional[dict] = None):
        default_override = default_override or {}
        data.write(b'\x00\x00\x00\x06')  # 6 properties
        data.write(self.name.encode("utf-8"))
        data.write(b'\x00')
        self.position.to_stream(data)
        self.rotation.to_stream(data)
        data.write(struct.pack('>?', self.active))
        self.unnamed.to_stream(data)
        data.write(struct.pack('>f', self.unknown))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            name=data['name'],
            position=Vector.from_json(data['position']),
            rotation=Vector.from_json(data['rotation']),
            active=data['active'],
            unnamed=ScannableParameters.from_json(data['unnamed']),
            unknown=data['unknown'],
        )

    def to_json(self) -> dict:
        return {
            'name': self.name,
            'position': self.position.to_json(),
            'rotation': self.rotation.to_json(),
            'active': self.active,
            'unnamed': self.unnamed.to_json(),
            'unknown': self.unknown,
        }

# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId
from retro_data_structures.properties.prime.core.Vector import Vector


@dataclasses.dataclass()
class BloodFlower(BaseObjectType):
    name: str = dataclasses.field(default='')
    position: Vector = dataclasses.field(default_factory=Vector)
    rotation: Vector = dataclasses.field(default_factory=Vector)
    scale: Vector = dataclasses.field(default_factory=Vector)
    unnamed_0x00000004: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef)
    unnamed_0x00000005: ActorParameters = dataclasses.field(default_factory=ActorParameters)
    particle_1: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffff)
    wpsc_1: AssetId = dataclasses.field(metadata={'asset_types': ['WPSC']}, default=0xffffffff)
    wpsc_2: AssetId = dataclasses.field(metadata={'asset_types': ['WPSC']}, default=0xffffffff)
    damage_info_1: DamageInfo = dataclasses.field(default_factory=DamageInfo)
    damage_info_2: DamageInfo = dataclasses.field(default_factory=DamageInfo)
    damage_info_3: DamageInfo = dataclasses.field(default_factory=DamageInfo)
    particle_2: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffff)
    particle_3: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffff)
    particle_4: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffff)
    unknown_1: float = dataclasses.field(default=0.0)
    particle_5: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffff)
    unknown_2: AssetId = dataclasses.field(default=0x0)

    @classmethod
    def game(cls) -> Game:
        return Game.PRIME

    @classmethod
    def object_type(cls) -> int:
        return 0x2D

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None, default_override: typing.Optional[dict] = None):
        property_size = None  # Atomic
        property_count = struct.unpack(">L", data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b'\x00')).decode("utf-8")
        position = Vector.from_stream(data)
        rotation = Vector.from_stream(data)
        scale = Vector.from_stream(data)
        unnamed_0x00000004 = PatternedAITypedef.from_stream(data, property_size)
        unnamed_0x00000005 = ActorParameters.from_stream(data, property_size)
        particle_1 = struct.unpack(">L", data.read(4))[0]
        wpsc_1 = struct.unpack(">L", data.read(4))[0]
        wpsc_2 = struct.unpack(">L", data.read(4))[0]
        damage_info_1 = DamageInfo.from_stream(data, property_size)
        damage_info_2 = DamageInfo.from_stream(data, property_size)
        damage_info_3 = DamageInfo.from_stream(data, property_size)
        particle_2 = struct.unpack(">L", data.read(4))[0]
        particle_3 = struct.unpack(">L", data.read(4))[0]
        particle_4 = struct.unpack(">L", data.read(4))[0]
        unknown_1 = struct.unpack('>f', data.read(4))[0]
        particle_5 = struct.unpack(">L", data.read(4))[0]
        unknown_2 = struct.unpack(">L", data.read(4))[0]
        return cls(name, position, rotation, scale, unnamed_0x00000004, unnamed_0x00000005, particle_1, wpsc_1, wpsc_2, damage_info_1, damage_info_2, damage_info_3, particle_2, particle_3, particle_4, unknown_1, particle_5, unknown_2)

    def to_stream(self, data: typing.BinaryIO, default_override: typing.Optional[dict] = None):
        default_override = default_override or {}
        data.write(b'\x00\x00\x00\x12')  # 18 properties
        data.write(self.name.encode("utf-8"))
        data.write(b'\x00')
        self.position.to_stream(data)
        self.rotation.to_stream(data)
        self.scale.to_stream(data)
        self.unnamed_0x00000004.to_stream(data)
        self.unnamed_0x00000005.to_stream(data)
        data.write(struct.pack(">L", self.particle_1))
        data.write(struct.pack(">L", self.wpsc_1))
        data.write(struct.pack(">L", self.wpsc_2))
        self.damage_info_1.to_stream(data)
        self.damage_info_2.to_stream(data)
        self.damage_info_3.to_stream(data)
        data.write(struct.pack(">L", self.particle_2))
        data.write(struct.pack(">L", self.particle_3))
        data.write(struct.pack(">L", self.particle_4))
        data.write(struct.pack('>f', self.unknown_1))
        data.write(struct.pack(">L", self.particle_5))
        data.write(struct.pack(">L", self.unknown_2))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            name=data['name'],
            position=Vector.from_json(data['position']),
            rotation=Vector.from_json(data['rotation']),
            scale=Vector.from_json(data['scale']),
            unnamed_0x00000004=PatternedAITypedef.from_json(data['unnamed_0x00000004']),
            unnamed_0x00000005=ActorParameters.from_json(data['unnamed_0x00000005']),
            particle_1=data['particle_1'],
            wpsc_1=data['wpsc_1'],
            wpsc_2=data['wpsc_2'],
            damage_info_1=DamageInfo.from_json(data['damage_info_1']),
            damage_info_2=DamageInfo.from_json(data['damage_info_2']),
            damage_info_3=DamageInfo.from_json(data['damage_info_3']),
            particle_2=data['particle_2'],
            particle_3=data['particle_3'],
            particle_4=data['particle_4'],
            unknown_1=data['unknown_1'],
            particle_5=data['particle_5'],
            unknown_2=data['unknown_2'],
        )

    def to_json(self) -> dict:
        return {
            'name': self.name,
            'position': self.position.to_json(),
            'rotation': self.rotation.to_json(),
            'scale': self.scale.to_json(),
            'unnamed_0x00000004': self.unnamed_0x00000004.to_json(),
            'unnamed_0x00000005': self.unnamed_0x00000005.to_json(),
            'particle_1': self.particle_1,
            'wpsc_1': self.wpsc_1,
            'wpsc_2': self.wpsc_2,
            'damage_info_1': self.damage_info_1.to_json(),
            'damage_info_2': self.damage_info_2.to_json(),
            'damage_info_3': self.damage_info_3.to_json(),
            'particle_2': self.particle_2,
            'particle_3': self.particle_3,
            'particle_4': self.particle_4,
            'unknown_1': self.unknown_1,
            'particle_5': self.particle_5,
            'unknown_2': self.unknown_2,
        }

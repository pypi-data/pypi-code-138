# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.PhysicsDebrisPropertiesOrientationEnum import PhysicsDebrisPropertiesOrientationEnum
from retro_data_structures.properties.corruption.core.AssetId import AssetId
from retro_data_structures.properties.corruption.core.Color import Color
from retro_data_structures.properties.corruption.core.Vector import Vector


@dataclasses.dataclass()
class PhysicsDebrisProperties(BaseProperty):
    cone_spread_yaw: float = dataclasses.field(default=180.0)
    cone_spread_pitch: float = dataclasses.field(default=180.0)
    initial_direction: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=1.0))
    position_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0))
    transform_position_offset: bool = dataclasses.field(default=True)
    minimum_speed: float = dataclasses.field(default=5.0)
    maximum_speed: float = dataclasses.field(default=15.0)
    minimum_spin_speed: Vector = dataclasses.field(default_factory=lambda: Vector(x=-1.0, y=-1.0, z=-1.0))
    maximum_spin_speed: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0))
    minimum_lifetime: float = dataclasses.field(default=2.0)
    maximum_lifetime: float = dataclasses.field(default=3.0)
    disable_collision_time: float = dataclasses.field(default=0.0)
    fade_in_end_percentage: float = dataclasses.field(default=10.0)
    fade_out_start_percentage: float = dataclasses.field(default=80.0)
    start_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0))
    middle_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0))
    end_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0))
    scale_start_percentage: float = dataclasses.field(default=80.0)
    final_scale: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0))
    unknown_0x417f4a91: float = dataclasses.field(default=0.375)
    friction: float = dataclasses.field(default=0.10000000149011612)
    gravity: float = dataclasses.field(default=25.0)
    disable_physics_threshold: float = dataclasses.field(default=1.0)
    model: AssetId = dataclasses.field(metadata={'asset_types': ['CMDL']}, default=0xffffffffffffffff)
    bounce_sound: AssetId = dataclasses.field(metadata={'asset_types': ['CAUD']}, default=0xffffffffffffffff)
    max_bounce_sounds: int = dataclasses.field(default=1)
    unknown_0x76c79503: float = dataclasses.field(default=1.0)
    unknown_0x310dfac8: float = dataclasses.field(default=1.0)
    unknown_0x5e9f5215: float = dataclasses.field(default=0.10000000149011612)
    unknown_0x39743618: float = dataclasses.field(default=0.10000000149011612)
    unknown_0x33e0fbb4: float = dataclasses.field(default=0.10000000149011612)
    unknown_0xe82e7ed7: float = dataclasses.field(default=0.10000000149011612)
    unknown_0x855ee21b: float = dataclasses.field(default=0.10000000149011612)
    particle_system1: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    particle_system1_scale: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0))
    particle_system1_uses_global_translation: bool = dataclasses.field(default=False)
    particle_system1_uses_global_orientation: bool = dataclasses.field(default=False)
    particle_system1_wait_for_particles_to_die: bool = dataclasses.field(default=True)
    physics_debris_properties_orientation_enum_0x49286613: PhysicsDebrisPropertiesOrientationEnum = dataclasses.field(default_factory=PhysicsDebrisPropertiesOrientationEnum)
    particle_system2: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    particle_system2_scale: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0))
    particle_system2_uses_global_translation: bool = dataclasses.field(default=False)
    particle_system2_uses_global_orientation: bool = dataclasses.field(default=False)
    particle_system2_wait_for_particles_to_die: bool = dataclasses.field(default=True)
    physics_debris_properties_orientation_enum_0x1e0a4a41: PhysicsDebrisPropertiesOrientationEnum = dataclasses.field(default_factory=PhysicsDebrisPropertiesOrientationEnum)
    is_collider: bool = dataclasses.field(default=True)
    is_shootable: bool = dataclasses.field(default=False)
    die_on_collision: bool = dataclasses.field(default=False)
    unknown_0xbfd82a19: bool = dataclasses.field(default=False)
    unknown_0x723d42d6: bool = dataclasses.field(default=True)
    unknown_0x4edb1d0e: bool = dataclasses.field(default=False)
    unknown_0xbf496273: bool = dataclasses.field(default=False)

    @classmethod
    def game(cls) -> Game:
        return Game.CORRUPTION

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
        data.write(b'\x004')  # 52 properties

        data.write(b'\\<JW')  # 0x5c3c4a57
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.cone_spread_yaw))

        data.write(b'\xa7\x9f\xc5_')  # 0xa79fc55f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.cone_spread_pitch))

        data.write(b'\x01\xa0\xdf\xe6')  # 0x1a0dfe6
        data.write(b'\x00\x0c')  # size
        self.initial_direction.to_stream(data)

        data.write(b'\xef\x90\xf0\x9d')  # 0xef90f09d
        data.write(b'\x00\x0c')  # size
        self.position_offset.to_stream(data)

        data.write(b'\xc4\xb1\xe6\xa1')  # 0xc4b1e6a1
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.transform_position_offset))

        data.write(b'\x01\x85&>')  # 0x185263e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.minimum_speed))

        data.write(b'\x14\x0e\xf2\xcc')  # 0x140ef2cc
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.maximum_speed))

        data.write(b'\xf7\x8c\x8a\xc7')  # 0xf78c8ac7
        data.write(b'\x00\x0c')  # size
        self.minimum_spin_speed.to_stream(data)

        data.write(b'\xb6\x9b\xb5A')  # 0xb69bb541
        data.write(b'\x00\x0c')  # size
        self.maximum_spin_speed.to_stream(data)

        data.write(b'\xd6YF"')  # 0xd6594622
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.minimum_lifetime))

        data.write(b"\xff'\xbb:")  # 0xff27bb3a
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.maximum_lifetime))

        data.write(b'kW\x1b\xa5')  # 0x6b571ba5
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.disable_collision_time))

        data.write(b'P\x05\x1a\x17')  # 0x50051a17
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.fade_in_end_percentage))

        data.write(b'cS\xc4\t')  # 0x6353c409
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.fade_out_start_percentage))

        data.write(b':V4\xd8')  # 0x3a5634d8
        data.write(b'\x00\x10')  # size
        self.start_color.to_stream(data)

        data.write(b'|n\xbe\x98')  # 0x7c6ebe98
        data.write(b'\x00\x10')  # size
        self.middle_color.to_stream(data)

        data.write(b'Z\xf5\x86}')  # 0x5af5867d
        data.write(b'\x00\x10')  # size
        self.end_color.to_stream(data)

        data.write(b'\x88n|\x9f')  # 0x886e7c9f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.scale_start_percentage))

        data.write(b'\x80\xc2*\n')  # 0x80c22a0a
        data.write(b'\x00\x0c')  # size
        self.final_scale.to_stream(data)

        data.write(b'A\x7fJ\x91')  # 0x417f4a91
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x417f4a91))

        data.write(b'\x16\xb7-I')  # 0x16b72d49
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.friction))

        data.write(b'/*\xe3\xe5')  # 0x2f2ae3e5
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.gravity))

        data.write(b')_\x05\xb7')  # 0x295f05b7
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.disable_physics_threshold))

        data.write(b'\xc2\x7f\xfa\x8f')  # 0xc27ffa8f
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.model))

        data.write(b'\xf1\x92Uv')  # 0xf1925576
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.bounce_sound))

        data.write(b'\x99\x12\x02\xc3')  # 0x991202c3
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>l', self.max_bounce_sounds))

        data.write(b'v\xc7\x95\x03')  # 0x76c79503
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x76c79503))

        data.write(b'1\r\xfa\xc8')  # 0x310dfac8
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x310dfac8))

        data.write(b'^\x9fR\x15')  # 0x5e9f5215
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x5e9f5215))

        data.write(b'9t6\x18')  # 0x39743618
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x39743618))

        data.write(b'3\xe0\xfb\xb4')  # 0x33e0fbb4
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x33e0fbb4))

        data.write(b'\xe8.~\xd7')  # 0xe82e7ed7
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xe82e7ed7))

        data.write(b'\x85^\xe2\x1b')  # 0x855ee21b
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x855ee21b))

        data.write(b'G\x8d\n\xa3')  # 0x478d0aa3
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.particle_system1))

        data.write(b'\x19\xa6\xf7\x1f')  # 0x19a6f71f
        data.write(b'\x00\x0c')  # size
        self.particle_system1_scale.to_stream(data)

        data.write(b';\x03\xa0\x1e')  # 0x3b03a01e
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.particle_system1_uses_global_translation))

        data.write(b'\xdb\x1f\xa6\x1c')  # 0xdb1fa61c
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.particle_system1_uses_global_orientation))

        data.write(b';\xdd/\xed')  # 0x3bdd2fed
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.particle_system1_wait_for_particles_to_die))

        data.write(b'I(f\x13')  # 0x49286613
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.physics_debris_properties_orientation_enum_0x49286613.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\xc1\x19x\r')  # 0xc119780d
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.particle_system2))

        data.write(b'n8%\xef')  # 0x6e3825ef
        data.write(b'\x00\x0c')  # size
        self.particle_system2_scale.to_stream(data)

        data.write(b'\xc9TM\xe6')  # 0xc9544de6
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.particle_system2_uses_global_translation))

        data.write(b')HK\xe4')  # 0x29484be4
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.particle_system2_uses_global_orientation))

        data.write(b'\xc9\x8a\xc2\x15')  # 0xc98ac215
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.particle_system2_wait_for_particles_to_die))

        data.write(b'\x1e\nJA')  # 0x1e0a4a41
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.physics_debris_properties_orientation_enum_0x1e0a4a41.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b',{\x18\xdd')  # 0x2c7b18dd
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.is_collider))

        data.write(b'\x8cs\xcb|')  # 0x8c73cb7c
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.is_shootable))

        data.write(b'\r\x7f\xadU')  # 0xd7fad55
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.die_on_collision))

        data.write(b'\xbf\xd8*\x19')  # 0xbfd82a19
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0xbfd82a19))

        data.write(b'r=B\xd6')  # 0x723d42d6
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0x723d42d6))

        data.write(b'N\xdb\x1d\x0e')  # 0x4edb1d0e
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0x4edb1d0e))

        data.write(b'\xbfIbs')  # 0xbf496273
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0xbf496273))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            cone_spread_yaw=data['cone_spread_yaw'],
            cone_spread_pitch=data['cone_spread_pitch'],
            initial_direction=Vector.from_json(data['initial_direction']),
            position_offset=Vector.from_json(data['position_offset']),
            transform_position_offset=data['transform_position_offset'],
            minimum_speed=data['minimum_speed'],
            maximum_speed=data['maximum_speed'],
            minimum_spin_speed=Vector.from_json(data['minimum_spin_speed']),
            maximum_spin_speed=Vector.from_json(data['maximum_spin_speed']),
            minimum_lifetime=data['minimum_lifetime'],
            maximum_lifetime=data['maximum_lifetime'],
            disable_collision_time=data['disable_collision_time'],
            fade_in_end_percentage=data['fade_in_end_percentage'],
            fade_out_start_percentage=data['fade_out_start_percentage'],
            start_color=Color.from_json(data['start_color']),
            middle_color=Color.from_json(data['middle_color']),
            end_color=Color.from_json(data['end_color']),
            scale_start_percentage=data['scale_start_percentage'],
            final_scale=Vector.from_json(data['final_scale']),
            unknown_0x417f4a91=data['unknown_0x417f4a91'],
            friction=data['friction'],
            gravity=data['gravity'],
            disable_physics_threshold=data['disable_physics_threshold'],
            model=data['model'],
            bounce_sound=data['bounce_sound'],
            max_bounce_sounds=data['max_bounce_sounds'],
            unknown_0x76c79503=data['unknown_0x76c79503'],
            unknown_0x310dfac8=data['unknown_0x310dfac8'],
            unknown_0x5e9f5215=data['unknown_0x5e9f5215'],
            unknown_0x39743618=data['unknown_0x39743618'],
            unknown_0x33e0fbb4=data['unknown_0x33e0fbb4'],
            unknown_0xe82e7ed7=data['unknown_0xe82e7ed7'],
            unknown_0x855ee21b=data['unknown_0x855ee21b'],
            particle_system1=data['particle_system1'],
            particle_system1_scale=Vector.from_json(data['particle_system1_scale']),
            particle_system1_uses_global_translation=data['particle_system1_uses_global_translation'],
            particle_system1_uses_global_orientation=data['particle_system1_uses_global_orientation'],
            particle_system1_wait_for_particles_to_die=data['particle_system1_wait_for_particles_to_die'],
            physics_debris_properties_orientation_enum_0x49286613=PhysicsDebrisPropertiesOrientationEnum.from_json(data['physics_debris_properties_orientation_enum_0x49286613']),
            particle_system2=data['particle_system2'],
            particle_system2_scale=Vector.from_json(data['particle_system2_scale']),
            particle_system2_uses_global_translation=data['particle_system2_uses_global_translation'],
            particle_system2_uses_global_orientation=data['particle_system2_uses_global_orientation'],
            particle_system2_wait_for_particles_to_die=data['particle_system2_wait_for_particles_to_die'],
            physics_debris_properties_orientation_enum_0x1e0a4a41=PhysicsDebrisPropertiesOrientationEnum.from_json(data['physics_debris_properties_orientation_enum_0x1e0a4a41']),
            is_collider=data['is_collider'],
            is_shootable=data['is_shootable'],
            die_on_collision=data['die_on_collision'],
            unknown_0xbfd82a19=data['unknown_0xbfd82a19'],
            unknown_0x723d42d6=data['unknown_0x723d42d6'],
            unknown_0x4edb1d0e=data['unknown_0x4edb1d0e'],
            unknown_0xbf496273=data['unknown_0xbf496273'],
        )

    def to_json(self) -> dict:
        return {
            'cone_spread_yaw': self.cone_spread_yaw,
            'cone_spread_pitch': self.cone_spread_pitch,
            'initial_direction': self.initial_direction.to_json(),
            'position_offset': self.position_offset.to_json(),
            'transform_position_offset': self.transform_position_offset,
            'minimum_speed': self.minimum_speed,
            'maximum_speed': self.maximum_speed,
            'minimum_spin_speed': self.minimum_spin_speed.to_json(),
            'maximum_spin_speed': self.maximum_spin_speed.to_json(),
            'minimum_lifetime': self.minimum_lifetime,
            'maximum_lifetime': self.maximum_lifetime,
            'disable_collision_time': self.disable_collision_time,
            'fade_in_end_percentage': self.fade_in_end_percentage,
            'fade_out_start_percentage': self.fade_out_start_percentage,
            'start_color': self.start_color.to_json(),
            'middle_color': self.middle_color.to_json(),
            'end_color': self.end_color.to_json(),
            'scale_start_percentage': self.scale_start_percentage,
            'final_scale': self.final_scale.to_json(),
            'unknown_0x417f4a91': self.unknown_0x417f4a91,
            'friction': self.friction,
            'gravity': self.gravity,
            'disable_physics_threshold': self.disable_physics_threshold,
            'model': self.model,
            'bounce_sound': self.bounce_sound,
            'max_bounce_sounds': self.max_bounce_sounds,
            'unknown_0x76c79503': self.unknown_0x76c79503,
            'unknown_0x310dfac8': self.unknown_0x310dfac8,
            'unknown_0x5e9f5215': self.unknown_0x5e9f5215,
            'unknown_0x39743618': self.unknown_0x39743618,
            'unknown_0x33e0fbb4': self.unknown_0x33e0fbb4,
            'unknown_0xe82e7ed7': self.unknown_0xe82e7ed7,
            'unknown_0x855ee21b': self.unknown_0x855ee21b,
            'particle_system1': self.particle_system1,
            'particle_system1_scale': self.particle_system1_scale.to_json(),
            'particle_system1_uses_global_translation': self.particle_system1_uses_global_translation,
            'particle_system1_uses_global_orientation': self.particle_system1_uses_global_orientation,
            'particle_system1_wait_for_particles_to_die': self.particle_system1_wait_for_particles_to_die,
            'physics_debris_properties_orientation_enum_0x49286613': self.physics_debris_properties_orientation_enum_0x49286613.to_json(),
            'particle_system2': self.particle_system2,
            'particle_system2_scale': self.particle_system2_scale.to_json(),
            'particle_system2_uses_global_translation': self.particle_system2_uses_global_translation,
            'particle_system2_uses_global_orientation': self.particle_system2_uses_global_orientation,
            'particle_system2_wait_for_particles_to_die': self.particle_system2_wait_for_particles_to_die,
            'physics_debris_properties_orientation_enum_0x1e0a4a41': self.physics_debris_properties_orientation_enum_0x1e0a4a41.to_json(),
            'is_collider': self.is_collider,
            'is_shootable': self.is_shootable,
            'die_on_collision': self.die_on_collision,
            'unknown_0xbfd82a19': self.unknown_0xbfd82a19,
            'unknown_0x723d42d6': self.unknown_0x723d42d6,
            'unknown_0x4edb1d0e': self.unknown_0x4edb1d0e,
            'unknown_0xbf496273': self.unknown_0xbf496273,
        }


def _decode_cone_spread_yaw(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_cone_spread_pitch(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_initial_direction(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


def _decode_position_offset(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


def _decode_transform_position_offset(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_minimum_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_maximum_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_minimum_spin_speed(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


def _decode_maximum_spin_speed(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


def _decode_minimum_lifetime(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_maximum_lifetime(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_disable_collision_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_fade_in_end_percentage(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_fade_out_start_percentage(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_start_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_middle_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_end_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_scale_start_percentage(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_final_scale(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


def _decode_unknown_0x417f4a91(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_friction(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_gravity(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_disable_physics_threshold(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_model(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_bounce_sound(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_max_bounce_sounds(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>l', data.read(4))[0]


def _decode_unknown_0x76c79503(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x310dfac8(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x5e9f5215(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x39743618(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x33e0fbb4(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0xe82e7ed7(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x855ee21b(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_particle_system1(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_particle_system1_scale(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


def _decode_particle_system1_uses_global_translation(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_particle_system1_uses_global_orientation(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_particle_system1_wait_for_particles_to_die(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_physics_debris_properties_orientation_enum_0x49286613(data: typing.BinaryIO, property_size: int):
    return PhysicsDebrisPropertiesOrientationEnum.from_stream(data, property_size)


def _decode_particle_system2(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_particle_system2_scale(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


def _decode_particle_system2_uses_global_translation(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_particle_system2_uses_global_orientation(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_particle_system2_wait_for_particles_to_die(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_physics_debris_properties_orientation_enum_0x1e0a4a41(data: typing.BinaryIO, property_size: int):
    return PhysicsDebrisPropertiesOrientationEnum.from_stream(data, property_size)


def _decode_is_collider(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_is_shootable(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_die_on_collision(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0xbfd82a19(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0x723d42d6(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0x4edb1d0e(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0xbf496273(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x5c3c4a57: ('cone_spread_yaw', _decode_cone_spread_yaw),
    0xa79fc55f: ('cone_spread_pitch', _decode_cone_spread_pitch),
    0x1a0dfe6: ('initial_direction', _decode_initial_direction),
    0xef90f09d: ('position_offset', _decode_position_offset),
    0xc4b1e6a1: ('transform_position_offset', _decode_transform_position_offset),
    0x185263e: ('minimum_speed', _decode_minimum_speed),
    0x140ef2cc: ('maximum_speed', _decode_maximum_speed),
    0xf78c8ac7: ('minimum_spin_speed', _decode_minimum_spin_speed),
    0xb69bb541: ('maximum_spin_speed', _decode_maximum_spin_speed),
    0xd6594622: ('minimum_lifetime', _decode_minimum_lifetime),
    0xff27bb3a: ('maximum_lifetime', _decode_maximum_lifetime),
    0x6b571ba5: ('disable_collision_time', _decode_disable_collision_time),
    0x50051a17: ('fade_in_end_percentage', _decode_fade_in_end_percentage),
    0x6353c409: ('fade_out_start_percentage', _decode_fade_out_start_percentage),
    0x3a5634d8: ('start_color', _decode_start_color),
    0x7c6ebe98: ('middle_color', _decode_middle_color),
    0x5af5867d: ('end_color', _decode_end_color),
    0x886e7c9f: ('scale_start_percentage', _decode_scale_start_percentage),
    0x80c22a0a: ('final_scale', _decode_final_scale),
    0x417f4a91: ('unknown_0x417f4a91', _decode_unknown_0x417f4a91),
    0x16b72d49: ('friction', _decode_friction),
    0x2f2ae3e5: ('gravity', _decode_gravity),
    0x295f05b7: ('disable_physics_threshold', _decode_disable_physics_threshold),
    0xc27ffa8f: ('model', _decode_model),
    0xf1925576: ('bounce_sound', _decode_bounce_sound),
    0x991202c3: ('max_bounce_sounds', _decode_max_bounce_sounds),
    0x76c79503: ('unknown_0x76c79503', _decode_unknown_0x76c79503),
    0x310dfac8: ('unknown_0x310dfac8', _decode_unknown_0x310dfac8),
    0x5e9f5215: ('unknown_0x5e9f5215', _decode_unknown_0x5e9f5215),
    0x39743618: ('unknown_0x39743618', _decode_unknown_0x39743618),
    0x33e0fbb4: ('unknown_0x33e0fbb4', _decode_unknown_0x33e0fbb4),
    0xe82e7ed7: ('unknown_0xe82e7ed7', _decode_unknown_0xe82e7ed7),
    0x855ee21b: ('unknown_0x855ee21b', _decode_unknown_0x855ee21b),
    0x478d0aa3: ('particle_system1', _decode_particle_system1),
    0x19a6f71f: ('particle_system1_scale', _decode_particle_system1_scale),
    0x3b03a01e: ('particle_system1_uses_global_translation', _decode_particle_system1_uses_global_translation),
    0xdb1fa61c: ('particle_system1_uses_global_orientation', _decode_particle_system1_uses_global_orientation),
    0x3bdd2fed: ('particle_system1_wait_for_particles_to_die', _decode_particle_system1_wait_for_particles_to_die),
    0x49286613: ('physics_debris_properties_orientation_enum_0x49286613', _decode_physics_debris_properties_orientation_enum_0x49286613),
    0xc119780d: ('particle_system2', _decode_particle_system2),
    0x6e3825ef: ('particle_system2_scale', _decode_particle_system2_scale),
    0xc9544de6: ('particle_system2_uses_global_translation', _decode_particle_system2_uses_global_translation),
    0x29484be4: ('particle_system2_uses_global_orientation', _decode_particle_system2_uses_global_orientation),
    0xc98ac215: ('particle_system2_wait_for_particles_to_die', _decode_particle_system2_wait_for_particles_to_die),
    0x1e0a4a41: ('physics_debris_properties_orientation_enum_0x1e0a4a41', _decode_physics_debris_properties_orientation_enum_0x1e0a4a41),
    0x2c7b18dd: ('is_collider', _decode_is_collider),
    0x8c73cb7c: ('is_shootable', _decode_is_shootable),
    0xd7fad55: ('die_on_collision', _decode_die_on_collision),
    0xbfd82a19: ('unknown_0xbfd82a19', _decode_unknown_0xbfd82a19),
    0x723d42d6: ('unknown_0x723d42d6', _decode_unknown_0x723d42d6),
    0x4edb1d0e: ('unknown_0x4edb1d0e', _decode_unknown_0x4edb1d0e),
    0xbf496273: ('unknown_0xbf496273', _decode_unknown_0xbf496273),
}

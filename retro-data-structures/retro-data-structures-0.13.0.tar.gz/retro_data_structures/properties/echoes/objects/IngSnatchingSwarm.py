# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.core.AssetId import AssetId


@dataclasses.dataclass()
class IngSnatchingSwarm(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties)
    state_machine: AssetId = dataclasses.field(metadata={'asset_types': ['AFSM', 'FSM2']}, default=0xffffffff)
    swarm_particle_system: AssetId = dataclasses.field(metadata={'asset_types': ['PART', 'SRSC']}, default=0xffffffff)
    unknown_0x7cae2ed5: float = dataclasses.field(default=0.5)
    part_0x35a88fa1: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffff)
    unknown_0xf65e7ec5: float = dataclasses.field(default=0.3499999940395355)
    lifetime: float = dataclasses.field(default=15.0)
    max_linear_speed: float = dataclasses.field(default=25.0)
    max_linear_acceleration: float = dataclasses.field(default=10.0)
    max_turn_speed: float = dataclasses.field(default=2000.0)
    unknown_0xdffdf5a2: bool = dataclasses.field(default=False)
    ignore_player: bool = dataclasses.field(default=False)
    unknown_0xe6b57a25: float = dataclasses.field(default=0.5)
    exit_portal_distance: float = dataclasses.field(default=4.0)
    unknown_0x2de5a19a: float = dataclasses.field(default=10.0)
    unknown_0x4e79f717: float = dataclasses.field(default=3.0)
    unknown_0xe8e0b5a6: float = dataclasses.field(default=2.0)
    begin_snatching_range: float = dataclasses.field(default=5.0)
    part_0x2d2afc26: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffff)
    impact_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo)
    sound_impact: AssetId = dataclasses.field(default=0x0)
    sound_idle: AssetId = dataclasses.field(default=0x0)
    sound_move: AssetId = dataclasses.field(default=0x0)
    health: float = dataclasses.field(default=50.0)
    swarm_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability)

    @classmethod
    def game(cls) -> Game:
        return Game.ECHOES

    @classmethod
    def object_type(cls) -> str:
        return 'ISSW'

    @classmethod
    def modules(cls) -> typing.List[str]:
        return ['IngSnatchingSwarm.rel']

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

        data.write(b'UtA`')  # 0x55744160
        data.write(b'\x00\x04')  # size
        data.write(struct.pack(">L", self.state_machine))

        data.write(b'\x83\xcfe\t')  # 0x83cf6509
        data.write(b'\x00\x04')  # size
        data.write(struct.pack(">L", self.swarm_particle_system))

        data.write(b'|\xae.\xd5')  # 0x7cae2ed5
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x7cae2ed5))

        data.write(b'5\xa8\x8f\xa1')  # 0x35a88fa1
        data.write(b'\x00\x04')  # size
        data.write(struct.pack(">L", self.part_0x35a88fa1))

        data.write(b'\xf6^~\xc5')  # 0xf65e7ec5
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xf65e7ec5))

        data.write(b'2\xdcg\xf6')  # 0x32dc67f6
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.lifetime))

        data.write(b'V=m\x13')  # 0x563d6d13
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.max_linear_speed))

        data.write(b'\xf5I\xe73')  # 0xf549e733
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.max_linear_acceleration))

        data.write(b'\x0b\\<\x1a')  # 0xb5c3c1a
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.max_turn_speed))

        data.write(b'\xdf\xfd\xf5\xa2')  # 0xdffdf5a2
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.unknown_0xdffdf5a2))

        data.write(b'wU\xf3I')  # 0x7755f349
        data.write(b'\x00\x01')  # size
        data.write(struct.pack('>?', self.ignore_player))

        data.write(b'\xe6\xb5z%')  # 0xe6b57a25
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xe6b57a25))

        data.write(b'\x83\tf\xd5')  # 0x830966d5
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.exit_portal_distance))

        data.write(b'-\xe5\xa1\x9a')  # 0x2de5a19a
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x2de5a19a))

        data.write(b'Ny\xf7\x17')  # 0x4e79f717
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x4e79f717))

        data.write(b'\xe8\xe0\xb5\xa6')  # 0xe8e0b5a6
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xe8e0b5a6))

        data.write(b'\xfc\xd8\x05{')  # 0xfcd8057b
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.begin_snatching_range))

        data.write(b'-*\xfc&')  # 0x2d2afc26
        data.write(b'\x00\x04')  # size
        data.write(struct.pack(">L", self.part_0x2d2afc26))

        data.write(b'\xb1mU>')  # 0xb16d553e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.impact_damage.to_stream(data, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\x1b\xb1n\xa5')  # 0x1bb16ea5
        data.write(b'\x00\x04')  # size
        data.write(struct.pack(">L", self.sound_impact))

        data.write(b'\xaf8\x96\x8e')  # 0xaf38968e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack(">L", self.sound_idle))

        data.write(b'l\x10\x18T')  # 0x6c101854
        data.write(b'\x00\x04')  # size
        data.write(struct.pack(">L", self.sound_move))

        data.write(b'\xf0f\x89\x19')  # 0xf0668919
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.health))

        data.write(b'\x87\x92\xa2\xb0')  # 0x8792a2b0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.swarm_vulnerability.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            editor_properties=EditorProperties.from_json(data['editor_properties']),
            state_machine=data['state_machine'],
            swarm_particle_system=data['swarm_particle_system'],
            unknown_0x7cae2ed5=data['unknown_0x7cae2ed5'],
            part_0x35a88fa1=data['part_0x35a88fa1'],
            unknown_0xf65e7ec5=data['unknown_0xf65e7ec5'],
            lifetime=data['lifetime'],
            max_linear_speed=data['max_linear_speed'],
            max_linear_acceleration=data['max_linear_acceleration'],
            max_turn_speed=data['max_turn_speed'],
            unknown_0xdffdf5a2=data['unknown_0xdffdf5a2'],
            ignore_player=data['ignore_player'],
            unknown_0xe6b57a25=data['unknown_0xe6b57a25'],
            exit_portal_distance=data['exit_portal_distance'],
            unknown_0x2de5a19a=data['unknown_0x2de5a19a'],
            unknown_0x4e79f717=data['unknown_0x4e79f717'],
            unknown_0xe8e0b5a6=data['unknown_0xe8e0b5a6'],
            begin_snatching_range=data['begin_snatching_range'],
            part_0x2d2afc26=data['part_0x2d2afc26'],
            impact_damage=DamageInfo.from_json(data['impact_damage']),
            sound_impact=data['sound_impact'],
            sound_idle=data['sound_idle'],
            sound_move=data['sound_move'],
            health=data['health'],
            swarm_vulnerability=DamageVulnerability.from_json(data['swarm_vulnerability']),
        )

    def to_json(self) -> dict:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'state_machine': self.state_machine,
            'swarm_particle_system': self.swarm_particle_system,
            'unknown_0x7cae2ed5': self.unknown_0x7cae2ed5,
            'part_0x35a88fa1': self.part_0x35a88fa1,
            'unknown_0xf65e7ec5': self.unknown_0xf65e7ec5,
            'lifetime': self.lifetime,
            'max_linear_speed': self.max_linear_speed,
            'max_linear_acceleration': self.max_linear_acceleration,
            'max_turn_speed': self.max_turn_speed,
            'unknown_0xdffdf5a2': self.unknown_0xdffdf5a2,
            'ignore_player': self.ignore_player,
            'unknown_0xe6b57a25': self.unknown_0xe6b57a25,
            'exit_portal_distance': self.exit_portal_distance,
            'unknown_0x2de5a19a': self.unknown_0x2de5a19a,
            'unknown_0x4e79f717': self.unknown_0x4e79f717,
            'unknown_0xe8e0b5a6': self.unknown_0xe8e0b5a6,
            'begin_snatching_range': self.begin_snatching_range,
            'part_0x2d2afc26': self.part_0x2d2afc26,
            'impact_damage': self.impact_damage.to_json(),
            'sound_impact': self.sound_impact,
            'sound_idle': self.sound_idle,
            'sound_move': self.sound_move,
            'health': self.health,
            'swarm_vulnerability': self.swarm_vulnerability.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, property_size: int):
    return EditorProperties.from_stream(data, property_size)


def _decode_state_machine(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">L", data.read(4))[0]


def _decode_swarm_particle_system(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">L", data.read(4))[0]


def _decode_unknown_0x7cae2ed5(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_part_0x35a88fa1(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">L", data.read(4))[0]


def _decode_unknown_0xf65e7ec5(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_lifetime(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_max_linear_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_max_linear_acceleration(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_max_turn_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0xdffdf5a2(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_ignore_player(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>?', data.read(1))[0]


def _decode_unknown_0xe6b57a25(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_exit_portal_distance(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x2de5a19a(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x4e79f717(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0xe8e0b5a6(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_begin_snatching_range(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_part_0x2d2afc26(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">L", data.read(4))[0]


def _decode_impact_damage(data: typing.BinaryIO, property_size: int):
    return DamageInfo.from_stream(data, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_sound_impact(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">L", data.read(4))[0]


def _decode_sound_idle(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">L", data.read(4))[0]


def _decode_sound_move(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">L", data.read(4))[0]


def _decode_health(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_swarm_vulnerability(data: typing.BinaryIO, property_size: int):
    return DamageVulnerability.from_stream(data, property_size)


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x55744160: ('state_machine', _decode_state_machine),
    0x83cf6509: ('swarm_particle_system', _decode_swarm_particle_system),
    0x7cae2ed5: ('unknown_0x7cae2ed5', _decode_unknown_0x7cae2ed5),
    0x35a88fa1: ('part_0x35a88fa1', _decode_part_0x35a88fa1),
    0xf65e7ec5: ('unknown_0xf65e7ec5', _decode_unknown_0xf65e7ec5),
    0x32dc67f6: ('lifetime', _decode_lifetime),
    0x563d6d13: ('max_linear_speed', _decode_max_linear_speed),
    0xf549e733: ('max_linear_acceleration', _decode_max_linear_acceleration),
    0xb5c3c1a: ('max_turn_speed', _decode_max_turn_speed),
    0xdffdf5a2: ('unknown_0xdffdf5a2', _decode_unknown_0xdffdf5a2),
    0x7755f349: ('ignore_player', _decode_ignore_player),
    0xe6b57a25: ('unknown_0xe6b57a25', _decode_unknown_0xe6b57a25),
    0x830966d5: ('exit_portal_distance', _decode_exit_portal_distance),
    0x2de5a19a: ('unknown_0x2de5a19a', _decode_unknown_0x2de5a19a),
    0x4e79f717: ('unknown_0x4e79f717', _decode_unknown_0x4e79f717),
    0xe8e0b5a6: ('unknown_0xe8e0b5a6', _decode_unknown_0xe8e0b5a6),
    0xfcd8057b: ('begin_snatching_range', _decode_begin_snatching_range),
    0x2d2afc26: ('part_0x2d2afc26', _decode_part_0x2d2afc26),
    0xb16d553e: ('impact_damage', _decode_impact_damage),
    0x1bb16ea5: ('sound_impact', _decode_sound_impact),
    0xaf38968e: ('sound_idle', _decode_sound_idle),
    0x6c101854: ('sound_move', _decode_sound_move),
    0xf0668919: ('health', _decode_health),
    0x8792a2b0: ('swarm_vulnerability', _decode_swarm_vulnerability),
}

# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.GrappleData import GrappleData
from retro_data_structures.properties.corruption.core.AssetId import AssetId


@dataclasses.dataclass()
class UnknownStruct26(BaseProperty):
    scan: AssetId = dataclasses.field(metadata={'asset_types': ['SCAN']}, default=0xffffffffffffffff)
    helmet_l_model: AssetId = dataclasses.field(metadata={'asset_types': ['CMDL']}, default=0xffffffffffffffff)
    helmet_r_model: AssetId = dataclasses.field(metadata={'asset_types': ['CMDL']}, default=0xffffffffffffffff)
    optic_array_model: AssetId = dataclasses.field(metadata={'asset_types': ['CMDL']}, default=0xffffffffffffffff)
    jammer_antenna_model: AssetId = dataclasses.field(metadata={'asset_types': ['CMDL']}, default=0xffffffffffffffff)
    part_0x537f8382: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    jammer_antenna_explosion_effect: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    part_0xad17a036: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    leg_collision_effect: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    visor_electric_effect: AssetId = dataclasses.field(metadata={'asset_types': ['ELSC']}, default=0xffffffffffffffff)
    missile_projectile: AssetId = dataclasses.field(metadata={'asset_types': ['WPSC']}, default=0xffffffffffffffff)
    huge_missile_projectile: AssetId = dataclasses.field(metadata={'asset_types': ['WPSC']}, default=0xffffffffffffffff)
    seeker_bomb_effect: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    part_0xdbf176dd: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    death_gibs: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    part_0xdd6be17f: AssetId = dataclasses.field(metadata={'asset_types': ['PART']}, default=0xffffffffffffffff)
    max_grapple_distance: float = dataclasses.field(default=40.0)
    grapple_data: GrappleData = dataclasses.field(default_factory=GrappleData)
    sound_jump_loop: AssetId = dataclasses.field(metadata={'asset_types': ['CAUD']}, default=0xffffffffffffffff)
    sound_bomb_loop: AssetId = dataclasses.field(metadata={'asset_types': ['CAUD']}, default=0xffffffffffffffff)
    caud_0xb4a84d85: AssetId = dataclasses.field(metadata={'asset_types': ['CAUD']}, default=0xffffffffffffffff)
    caud_0xfef01104: AssetId = dataclasses.field(metadata={'asset_types': ['CAUD']}, default=0xffffffffffffffff)
    caud_0xeb8805bd: AssetId = dataclasses.field(metadata={'asset_types': ['CAUD']}, default=0xffffffffffffffff)
    sound_fireball_loop: AssetId = dataclasses.field(metadata={'asset_types': []}, default=0xffffffffffffffff)
    unknown_0xa99ccb84: AssetId = dataclasses.field(metadata={'asset_types': []}, default=0xffffffffffffffff)
    unknown_0xb60df150: AssetId = dataclasses.field(metadata={'asset_types': []}, default=0xffffffffffffffff)

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
        data.write(b'\x00\x1a')  # 26 properties

        data.write(b'\x7f\xabE*')  # 0x7fab452a
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.scan))

        data.write(b'\xc4zR$')  # 0xc47a5224
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.helmet_l_model))

        data.write(b'8\xfa\xbd\xe9')  # 0x38fabde9
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.helmet_r_model))

        data.write(b'K\xa2\x83>')  # 0x4ba2833e
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.optic_array_model))

        data.write(b'\xc6\x0f\xb9\x11')  # 0xc60fb911
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.jammer_antenna_model))

        data.write(b'S\x7f\x83\x82')  # 0x537f8382
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.part_0x537f8382))

        data.write(b'\x98\xd5\x88=')  # 0x98d5883d
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.jammer_antenna_explosion_effect))

        data.write(b'\xad\x17\xa06')  # 0xad17a036
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.part_0xad17a036))

        data.write(b'?\xef7\xbd')  # 0x3fef37bd
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.leg_collision_effect))

        data.write(b'\xbd2\x158')  # 0xbd321538
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.visor_electric_effect))

        data.write(b'p\xe9qf')  # 0x70e97166
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.missile_projectile))

        data.write(b'\x9e\xefq\xc2')  # 0x9eef71c2
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.huge_missile_projectile))

        data.write(b'\xf9\x8f\xdc\xc9')  # 0xf98fdcc9
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.seeker_bomb_effect))

        data.write(b'\xdb\xf1v\xdd')  # 0xdbf176dd
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.part_0xdbf176dd))

        data.write(b'z\xf4\x88\xb1')  # 0x7af488b1
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.death_gibs))

        data.write(b'\xddk\xe1\x7f')  # 0xdd6be17f
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.part_0xdd6be17f))

        data.write(b'\x1c\xc99\x84')  # 0x1cc93984
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.max_grapple_distance))

        data.write(b'\xf6\t\xc67')  # 0xf609c637
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_data.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b',U\x8c]')  # 0x2c558c5d
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.sound_jump_loop))

        data.write(b'\xb3"\x0bx')  # 0xb3220b78
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.sound_bomb_loop))

        data.write(b'\xb4\xa8M\x85')  # 0xb4a84d85
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.caud_0xb4a84d85))

        data.write(b'\xfe\xf0\x11\x04')  # 0xfef01104
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.caud_0xfef01104))

        data.write(b'\xeb\x88\x05\xbd')  # 0xeb8805bd
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.caud_0xeb8805bd))

        data.write(b"es'\xcd")  # 0x657327cd
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.sound_fireball_loop))

        data.write(b'\xa9\x9c\xcb\x84')  # 0xa99ccb84
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.unknown_0xa99ccb84))

        data.write(b'\xb6\r\xf1P')  # 0xb60df150
        data.write(b'\x00\x08')  # size
        data.write(struct.pack(">Q", self.unknown_0xb60df150))

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            scan=data['scan'],
            helmet_l_model=data['helmet_l_model'],
            helmet_r_model=data['helmet_r_model'],
            optic_array_model=data['optic_array_model'],
            jammer_antenna_model=data['jammer_antenna_model'],
            part_0x537f8382=data['part_0x537f8382'],
            jammer_antenna_explosion_effect=data['jammer_antenna_explosion_effect'],
            part_0xad17a036=data['part_0xad17a036'],
            leg_collision_effect=data['leg_collision_effect'],
            visor_electric_effect=data['visor_electric_effect'],
            missile_projectile=data['missile_projectile'],
            huge_missile_projectile=data['huge_missile_projectile'],
            seeker_bomb_effect=data['seeker_bomb_effect'],
            part_0xdbf176dd=data['part_0xdbf176dd'],
            death_gibs=data['death_gibs'],
            part_0xdd6be17f=data['part_0xdd6be17f'],
            max_grapple_distance=data['max_grapple_distance'],
            grapple_data=GrappleData.from_json(data['grapple_data']),
            sound_jump_loop=data['sound_jump_loop'],
            sound_bomb_loop=data['sound_bomb_loop'],
            caud_0xb4a84d85=data['caud_0xb4a84d85'],
            caud_0xfef01104=data['caud_0xfef01104'],
            caud_0xeb8805bd=data['caud_0xeb8805bd'],
            sound_fireball_loop=data['sound_fireball_loop'],
            unknown_0xa99ccb84=data['unknown_0xa99ccb84'],
            unknown_0xb60df150=data['unknown_0xb60df150'],
        )

    def to_json(self) -> dict:
        return {
            'scan': self.scan,
            'helmet_l_model': self.helmet_l_model,
            'helmet_r_model': self.helmet_r_model,
            'optic_array_model': self.optic_array_model,
            'jammer_antenna_model': self.jammer_antenna_model,
            'part_0x537f8382': self.part_0x537f8382,
            'jammer_antenna_explosion_effect': self.jammer_antenna_explosion_effect,
            'part_0xad17a036': self.part_0xad17a036,
            'leg_collision_effect': self.leg_collision_effect,
            'visor_electric_effect': self.visor_electric_effect,
            'missile_projectile': self.missile_projectile,
            'huge_missile_projectile': self.huge_missile_projectile,
            'seeker_bomb_effect': self.seeker_bomb_effect,
            'part_0xdbf176dd': self.part_0xdbf176dd,
            'death_gibs': self.death_gibs,
            'part_0xdd6be17f': self.part_0xdd6be17f,
            'max_grapple_distance': self.max_grapple_distance,
            'grapple_data': self.grapple_data.to_json(),
            'sound_jump_loop': self.sound_jump_loop,
            'sound_bomb_loop': self.sound_bomb_loop,
            'caud_0xb4a84d85': self.caud_0xb4a84d85,
            'caud_0xfef01104': self.caud_0xfef01104,
            'caud_0xeb8805bd': self.caud_0xeb8805bd,
            'sound_fireball_loop': self.sound_fireball_loop,
            'unknown_0xa99ccb84': self.unknown_0xa99ccb84,
            'unknown_0xb60df150': self.unknown_0xb60df150,
        }


def _decode_scan(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_helmet_l_model(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_helmet_r_model(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_optic_array_model(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_jammer_antenna_model(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_part_0x537f8382(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_jammer_antenna_explosion_effect(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_part_0xad17a036(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_leg_collision_effect(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_visor_electric_effect(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_missile_projectile(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_huge_missile_projectile(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_seeker_bomb_effect(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_part_0xdbf176dd(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_death_gibs(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_part_0xdd6be17f(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_max_grapple_distance(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_grapple_data(data: typing.BinaryIO, property_size: int):
    return GrappleData.from_stream(data, property_size)


def _decode_sound_jump_loop(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_sound_bomb_loop(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_caud_0xb4a84d85(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_caud_0xfef01104(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_caud_0xeb8805bd(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_sound_fireball_loop(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_unknown_0xa99ccb84(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


def _decode_unknown_0xb60df150(data: typing.BinaryIO, property_size: int):
    return struct.unpack(">Q", data.read(8))[0]


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0x7fab452a: ('scan', _decode_scan),
    0xc47a5224: ('helmet_l_model', _decode_helmet_l_model),
    0x38fabde9: ('helmet_r_model', _decode_helmet_r_model),
    0x4ba2833e: ('optic_array_model', _decode_optic_array_model),
    0xc60fb911: ('jammer_antenna_model', _decode_jammer_antenna_model),
    0x537f8382: ('part_0x537f8382', _decode_part_0x537f8382),
    0x98d5883d: ('jammer_antenna_explosion_effect', _decode_jammer_antenna_explosion_effect),
    0xad17a036: ('part_0xad17a036', _decode_part_0xad17a036),
    0x3fef37bd: ('leg_collision_effect', _decode_leg_collision_effect),
    0xbd321538: ('visor_electric_effect', _decode_visor_electric_effect),
    0x70e97166: ('missile_projectile', _decode_missile_projectile),
    0x9eef71c2: ('huge_missile_projectile', _decode_huge_missile_projectile),
    0xf98fdcc9: ('seeker_bomb_effect', _decode_seeker_bomb_effect),
    0xdbf176dd: ('part_0xdbf176dd', _decode_part_0xdbf176dd),
    0x7af488b1: ('death_gibs', _decode_death_gibs),
    0xdd6be17f: ('part_0xdd6be17f', _decode_part_0xdd6be17f),
    0x1cc93984: ('max_grapple_distance', _decode_max_grapple_distance),
    0xf609c637: ('grapple_data', _decode_grapple_data),
    0x2c558c5d: ('sound_jump_loop', _decode_sound_jump_loop),
    0xb3220b78: ('sound_bomb_loop', _decode_sound_bomb_loop),
    0xb4a84d85: ('caud_0xb4a84d85', _decode_caud_0xb4a84d85),
    0xfef01104: ('caud_0xfef01104', _decode_caud_0xfef01104),
    0xeb8805bd: ('caud_0xeb8805bd', _decode_caud_0xeb8805bd),
    0x657327cd: ('sound_fireball_loop', _decode_sound_fireball_loop),
    0xa99ccb84: ('unknown_0xa99ccb84', _decode_unknown_0xa99ccb84),
    0xb60df150: ('unknown_0xb60df150', _decode_unknown_0xb60df150),
}

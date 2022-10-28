# Generated File
import dataclasses
import struct
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.core.Color import Color
from retro_data_structures.properties.echoes.core.Spline import Spline
from retro_data_structures.properties.echoes.core.Vector import Vector


@dataclasses.dataclass()
class LogBook(BaseProperty):
    main_window_border_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    main_window_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    main_window_selected_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0xfe98f30e: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x39e57ac0: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    legend_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    node_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    selected_node_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    parent_node_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x56843943: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    selected_text_cursor_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x905ce2c0: float = dataclasses.field(default=1.5)
    text_scale: float = dataclasses.field(default=1.0)
    selected_text_scale: float = dataclasses.field(default=1.0)
    transition_time: float = dataclasses.field(default=1.0)
    node_collapse_motion: Spline = dataclasses.field(default_factory=Spline)
    selected_node_collapse_motion: Spline = dataclasses.field(default_factory=Spline)
    node_expand_motion: Spline = dataclasses.field(default_factory=Spline)
    rotation_speed: float = dataclasses.field(default=2.0)
    node_scale: float = dataclasses.field(default=1.0)
    selected_node_scale: float = dataclasses.field(default=1.0)
    selected_text_cursor_scale: float = dataclasses.field(default=1.0)
    scan_model_scale: float = dataclasses.field(default=2.0)
    unknown_0x925b9d4a: Spline = dataclasses.field(default_factory=Spline)
    unknown_0x075a0734: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x8ef43309: float = dataclasses.field(default=2.0)
    fog_near: float = dataclasses.field(default=11.0)
    fog_far: float = dataclasses.field(default=18.0)
    fog_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0xeef15783: float = dataclasses.field(default=12.0)
    unknown_0x78055ab2: float = dataclasses.field(default=0.0)
    unknown_0x09e3197f: float = dataclasses.field(default=0.0)
    unknown_0xfaffce1f: float = dataclasses.field(default=0.0)
    unknown_0xe5280e7c: float = dataclasses.field(default=0.0)
    background_sweep_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    background_sweep_radius: float = dataclasses.field(default=0.6000000238418579)
    background_sweep_time: float = dataclasses.field(default=1.0)
    scan_text_window_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    scan_text_window_border_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    scan_text_window_font_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    legend_window_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    legend_window_border_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    legend_window_font_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    legend_hide_time: float = dataclasses.field(default=1.0)
    unknown_0x7f35c573: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0xe0d77cf1: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x903d9b7e: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x0fdf22fc: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0xbeaf9d6b: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x7e8247d6: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x8b3f7902: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0xdc1abb82: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x306b2b24: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    frame_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    unknown_0x1a4b8068: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    slider_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    slider_selection_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    slider_scale: float = dataclasses.field(default=0.10000000149011612)
    slider_speed: float = dataclasses.field(default=100.0)
    unknown_0x58795865: float = dataclasses.field(default=0.20000000298023224)
    unknown_0x35e0bd31: float = dataclasses.field(default=0.20000000298023224)
    menu_option_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    menu_option_enabled_arrow_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    menu_option_disabled_arrow_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    menu_option_scale: float = dataclasses.field(default=1.0)
    menu_option_arrow_scale: float = dataclasses.field(default=0.10000000149011612)
    model_rotation_speed: float = dataclasses.field(default=120.0)
    unknown_0x60914b79: float = dataclasses.field(default=-80.0)
    unknown_0x1fd44d9b: float = dataclasses.field(default=80.0)
    model_light1_position: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0))
    model_light1_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    model_light2_position: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0))
    model_light2_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))
    model_ambient_light_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0))

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
        data.write(b'\x00J')  # 74 properties

        data.write(b'\xbaZe\xc8')  # 0xba5a65c8
        data.write(b'\x00\x10')  # size
        self.main_window_border_color.to_stream(data)

        data.write(b'\xbf\xf0\xe3{')  # 0xbff0e37b
        data.write(b'\x00\x10')  # size
        self.main_window_text_color.to_stream(data)

        data.write(b'(\xb4\x9a\x88')  # 0x28b49a88
        data.write(b'\x00\x10')  # size
        self.main_window_selected_text_color.to_stream(data)

        data.write(b'\xfe\x98\xf3\x0e')  # 0xfe98f30e
        data.write(b'\x00\x10')  # size
        self.unknown_0xfe98f30e.to_stream(data)

        data.write(b'9\xe5z\xc0')  # 0x39e57ac0
        data.write(b'\x00\x10')  # size
        self.unknown_0x39e57ac0.to_stream(data)

        data.write(b'\xa6\xb63\xfa')  # 0xa6b633fa
        data.write(b'\x00\x10')  # size
        self.legend_background_color.to_stream(data)

        data.write(b'\xac\x80\x01;')  # 0xac80013b
        data.write(b'\x00\x10')  # size
        self.node_color.to_stream(data)

        data.write(b'YF\xb49')  # 0x5946b439
        data.write(b'\x00\x10')  # size
        self.selected_node_color.to_stream(data)

        data.write(b'\xc5\xaar\x8c')  # 0xc5aa728c
        data.write(b'\x00\x10')  # size
        self.parent_node_color.to_stream(data)

        data.write(b'V\x849C')  # 0x56843943
        data.write(b'\x00\x10')  # size
        self.unknown_0x56843943.to_stream(data)

        data.write(b'k\xd4x:')  # 0x6bd4783a
        data.write(b'\x00\x10')  # size
        self.selected_text_cursor_color.to_stream(data)

        data.write(b'\x90\\\xe2\xc0')  # 0x905ce2c0
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x905ce2c0))

        data.write(b'_\xa6Lw')  # 0x5fa64c77
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.text_scale))

        data.write(b'\xaa`\xf9u')  # 0xaa60f975
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.selected_text_scale))

        data.write(b'\x182\x93^')  # 0x1832935e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.transition_time))

        data.write(b'\x16YC\xf6')  # 0x165943f6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.node_collapse_motion.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\x9a\xd0M\xd7')  # 0x9ad04dd7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.selected_node_collapse_motion.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\x08q\x9a\x9c')  # 0x8719a9c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.node_expand_motion.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\x11\xcd\x07o')  # 0x11cd076f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.rotation_speed))

        data.write(b'\xb7\x16w\xd0')  # 0xb71677d0
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.node_scale))

        data.write(b'B\xd0\xc2\xd2')  # 0x42d0c2d2
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.selected_node_scale))

        data.write(b'pB\x0e\xd1')  # 0x70420ed1
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.selected_text_cursor_scale))

        data.write(b'\xc0\xcb96')  # 0xc0cb3936
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.scan_model_scale))

        data.write(b'\x92[\x9dJ')  # 0x925b9d4a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_0x925b9d4a.to_stream(data)
        after = data.tell()
        data.seek(before)
        data.write(struct.pack(">H", after - before - 2))
        data.seek(after)

        data.write(b'\x07Z\x074')  # 0x75a0734
        data.write(b'\x00\x10')  # size
        self.unknown_0x075a0734.to_stream(data)

        data.write(b'\x8e\xf43\t')  # 0x8ef43309
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x8ef43309))

        data.write(b'A\x94b.')  # 0x4194622e
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.fog_near))

        data.write(b'95\xa7V')  # 0x3935a756
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.fog_far))

        data.write(b'\xe5x\xc0\xdd')  # 0xe578c0dd
        data.write(b'\x00\x10')  # size
        self.fog_color.to_stream(data)

        data.write(b'\xee\xf1W\x83')  # 0xeef15783
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xeef15783))

        data.write(b'x\x05Z\xb2')  # 0x78055ab2
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x78055ab2))

        data.write(b'\t\xe3\x19\x7f')  # 0x9e3197f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x09e3197f))

        data.write(b'\xfa\xff\xce\x1f')  # 0xfaffce1f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xfaffce1f))

        data.write(b'\xe5(\x0e|')  # 0xe5280e7c
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0xe5280e7c))

        data.write(b'd}\x9f\x91')  # 0x647d9f91
        data.write(b'\x00\x10')  # size
        self.background_sweep_color.to_stream(data)

        data.write(b'q \xf1\x8f')  # 0x7120f18f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.background_sweep_radius))

        data.write(b'M\xeff\r')  # 0x4def660d
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.background_sweep_time))

        data.write(b'\xc7\xc1\x96{')  # 0xc7c1967b
        data.write(b'\x00\x10')  # size
        self.scan_text_window_background_color.to_stream(data)

        data.write(b'\xf7K\xba\xd2')  # 0xf74bbad2
        data.write(b'\x00\x10')  # size
        self.scan_text_window_border_color.to_stream(data)

        data.write(b'\xe3\x14!\xe2')  # 0xe31421e2
        data.write(b'\x00\x10')  # size
        self.scan_text_window_font_color.to_stream(data)

        data.write(b'\x0b\x8f\r\xdb')  # 0xb8f0ddb
        data.write(b'\x00\x10')  # size
        self.legend_window_background_color.to_stream(data)

        data.write(b'\nzAU')  # 0xa7a4155
        data.write(b'\x00\x10')  # size
        self.legend_window_border_color.to_stream(data)

        data.write(b'Rz\x0b\x10')  # 0x527a0b10
        data.write(b'\x00\x10')  # size
        self.legend_window_font_color.to_stream(data)

        data.write(b"y'\xcag")  # 0x7927ca67
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.legend_hide_time))

        data.write(b'\x7f5\xc5s')  # 0x7f35c573
        data.write(b'\x00\x10')  # size
        self.unknown_0x7f35c573.to_stream(data)

        data.write(b'\xe0\xd7|\xf1')  # 0xe0d77cf1
        data.write(b'\x00\x10')  # size
        self.unknown_0xe0d77cf1.to_stream(data)

        data.write(b'\x90=\x9b~')  # 0x903d9b7e
        data.write(b'\x00\x10')  # size
        self.unknown_0x903d9b7e.to_stream(data)

        data.write(b'\x0f\xdf"\xfc')  # 0xfdf22fc
        data.write(b'\x00\x10')  # size
        self.unknown_0x0fdf22fc.to_stream(data)

        data.write(b'\xbe\xaf\x9dk')  # 0xbeaf9d6b
        data.write(b'\x00\x10')  # size
        self.unknown_0xbeaf9d6b.to_stream(data)

        data.write(b'~\x82G\xd6')  # 0x7e8247d6
        data.write(b'\x00\x10')  # size
        self.unknown_0x7e8247d6.to_stream(data)

        data.write(b'\x8b?y\x02')  # 0x8b3f7902
        data.write(b'\x00\x10')  # size
        self.unknown_0x8b3f7902.to_stream(data)

        data.write(b'\xdc\x1a\xbb\x82')  # 0xdc1abb82
        data.write(b'\x00\x10')  # size
        self.unknown_0xdc1abb82.to_stream(data)

        data.write(b'0k+$')  # 0x306b2b24
        data.write(b'\x00\x10')  # size
        self.unknown_0x306b2b24.to_stream(data)

        data.write(b'\xa4\x857,')  # 0xa485372c
        data.write(b'\x00\x10')  # size
        self.frame_color.to_stream(data)

        data.write(b'\x1aK\x80h')  # 0x1a4b8068
        data.write(b'\x00\x10')  # size
        self.unknown_0x1a4b8068.to_stream(data)

        data.write(b'\xcc/%\xf1')  # 0xcc2f25f1
        data.write(b'\x00\x10')  # size
        self.slider_background_color.to_stream(data)

        data.write(b'\xcb\x8d\\\xaf')  # 0xcb8d5caf
        data.write(b'\x00\x10')  # size
        self.slider_selection_color.to_stream(data)

        data.write(b'?D%O')  # 0x3f44254f
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.slider_scale))

        data.write(b'p\x87\xc3w')  # 0x7087c377
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.slider_speed))

        data.write(b'XyXe')  # 0x58795865
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x58795865))

        data.write(b'5\xe0\xbd1')  # 0x35e0bd31
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x35e0bd31))

        data.write(b'\xe7\xc2\x83\xbe')  # 0xe7c283be
        data.write(b'\x00\x10')  # size
        self.menu_option_color.to_stream(data)

        data.write(b'\xda\xbc\xb70')  # 0xdabcb730
        data.write(b'\x00\x10')  # size
        self.menu_option_enabled_arrow_color.to_stream(data)

        data.write(b'\x9c!\x95\xd7')  # 0x9c2195d7
        data.write(b'\x00\x10')  # size
        self.menu_option_disabled_arrow_color.to_stream(data)

        data.write(b'\xfcT\xf5U')  # 0xfc54f555
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.menu_option_scale))

        data.write(b'\xefT\x950')  # 0xef549530
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.menu_option_arrow_scale))

        data.write(b'\xfaz\x92\xb8')  # 0xfa7a92b8
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.model_rotation_speed))

        data.write(b'`\x91Ky')  # 0x60914b79
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x60914b79))

        data.write(b'\x1f\xd4M\x9b')  # 0x1fd44d9b
        data.write(b'\x00\x04')  # size
        data.write(struct.pack('>f', self.unknown_0x1fd44d9b))

        data.write(b'\x06\xc9:\xfa')  # 0x6c93afa
        data.write(b'\x00\x0c')  # size
        self.model_light1_position.to_stream(data)

        data.write(b'3\x92J\xfb')  # 0x33924afb
        data.write(b'\x00\x10')  # size
        self.model_light1_color.to_stream(data)

        data.write(b'\x17\xb4P\x83')  # 0x17b45083
        data.write(b'\x00\x0c')  # size
        self.model_light2_position.to_stream(data)

        data.write(b'\xaap,\xfa')  # 0xaa702cfa
        data.write(b'\x00\x10')  # size
        self.model_light2_color.to_stream(data)

        data.write(b'b\xffmr')  # 0x62ff6d72
        data.write(b'\x00\x10')  # size
        self.model_ambient_light_color.to_stream(data)

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            main_window_border_color=Color.from_json(data['main_window_border_color']),
            main_window_text_color=Color.from_json(data['main_window_text_color']),
            main_window_selected_text_color=Color.from_json(data['main_window_selected_text_color']),
            unknown_0xfe98f30e=Color.from_json(data['unknown_0xfe98f30e']),
            unknown_0x39e57ac0=Color.from_json(data['unknown_0x39e57ac0']),
            legend_background_color=Color.from_json(data['legend_background_color']),
            node_color=Color.from_json(data['node_color']),
            selected_node_color=Color.from_json(data['selected_node_color']),
            parent_node_color=Color.from_json(data['parent_node_color']),
            unknown_0x56843943=Color.from_json(data['unknown_0x56843943']),
            selected_text_cursor_color=Color.from_json(data['selected_text_cursor_color']),
            unknown_0x905ce2c0=data['unknown_0x905ce2c0'],
            text_scale=data['text_scale'],
            selected_text_scale=data['selected_text_scale'],
            transition_time=data['transition_time'],
            node_collapse_motion=Spline.from_json(data['node_collapse_motion']),
            selected_node_collapse_motion=Spline.from_json(data['selected_node_collapse_motion']),
            node_expand_motion=Spline.from_json(data['node_expand_motion']),
            rotation_speed=data['rotation_speed'],
            node_scale=data['node_scale'],
            selected_node_scale=data['selected_node_scale'],
            selected_text_cursor_scale=data['selected_text_cursor_scale'],
            scan_model_scale=data['scan_model_scale'],
            unknown_0x925b9d4a=Spline.from_json(data['unknown_0x925b9d4a']),
            unknown_0x075a0734=Color.from_json(data['unknown_0x075a0734']),
            unknown_0x8ef43309=data['unknown_0x8ef43309'],
            fog_near=data['fog_near'],
            fog_far=data['fog_far'],
            fog_color=Color.from_json(data['fog_color']),
            unknown_0xeef15783=data['unknown_0xeef15783'],
            unknown_0x78055ab2=data['unknown_0x78055ab2'],
            unknown_0x09e3197f=data['unknown_0x09e3197f'],
            unknown_0xfaffce1f=data['unknown_0xfaffce1f'],
            unknown_0xe5280e7c=data['unknown_0xe5280e7c'],
            background_sweep_color=Color.from_json(data['background_sweep_color']),
            background_sweep_radius=data['background_sweep_radius'],
            background_sweep_time=data['background_sweep_time'],
            scan_text_window_background_color=Color.from_json(data['scan_text_window_background_color']),
            scan_text_window_border_color=Color.from_json(data['scan_text_window_border_color']),
            scan_text_window_font_color=Color.from_json(data['scan_text_window_font_color']),
            legend_window_background_color=Color.from_json(data['legend_window_background_color']),
            legend_window_border_color=Color.from_json(data['legend_window_border_color']),
            legend_window_font_color=Color.from_json(data['legend_window_font_color']),
            legend_hide_time=data['legend_hide_time'],
            unknown_0x7f35c573=Color.from_json(data['unknown_0x7f35c573']),
            unknown_0xe0d77cf1=Color.from_json(data['unknown_0xe0d77cf1']),
            unknown_0x903d9b7e=Color.from_json(data['unknown_0x903d9b7e']),
            unknown_0x0fdf22fc=Color.from_json(data['unknown_0x0fdf22fc']),
            unknown_0xbeaf9d6b=Color.from_json(data['unknown_0xbeaf9d6b']),
            unknown_0x7e8247d6=Color.from_json(data['unknown_0x7e8247d6']),
            unknown_0x8b3f7902=Color.from_json(data['unknown_0x8b3f7902']),
            unknown_0xdc1abb82=Color.from_json(data['unknown_0xdc1abb82']),
            unknown_0x306b2b24=Color.from_json(data['unknown_0x306b2b24']),
            frame_color=Color.from_json(data['frame_color']),
            unknown_0x1a4b8068=Color.from_json(data['unknown_0x1a4b8068']),
            slider_background_color=Color.from_json(data['slider_background_color']),
            slider_selection_color=Color.from_json(data['slider_selection_color']),
            slider_scale=data['slider_scale'],
            slider_speed=data['slider_speed'],
            unknown_0x58795865=data['unknown_0x58795865'],
            unknown_0x35e0bd31=data['unknown_0x35e0bd31'],
            menu_option_color=Color.from_json(data['menu_option_color']),
            menu_option_enabled_arrow_color=Color.from_json(data['menu_option_enabled_arrow_color']),
            menu_option_disabled_arrow_color=Color.from_json(data['menu_option_disabled_arrow_color']),
            menu_option_scale=data['menu_option_scale'],
            menu_option_arrow_scale=data['menu_option_arrow_scale'],
            model_rotation_speed=data['model_rotation_speed'],
            unknown_0x60914b79=data['unknown_0x60914b79'],
            unknown_0x1fd44d9b=data['unknown_0x1fd44d9b'],
            model_light1_position=Vector.from_json(data['model_light1_position']),
            model_light1_color=Color.from_json(data['model_light1_color']),
            model_light2_position=Vector.from_json(data['model_light2_position']),
            model_light2_color=Color.from_json(data['model_light2_color']),
            model_ambient_light_color=Color.from_json(data['model_ambient_light_color']),
        )

    def to_json(self) -> dict:
        return {
            'main_window_border_color': self.main_window_border_color.to_json(),
            'main_window_text_color': self.main_window_text_color.to_json(),
            'main_window_selected_text_color': self.main_window_selected_text_color.to_json(),
            'unknown_0xfe98f30e': self.unknown_0xfe98f30e.to_json(),
            'unknown_0x39e57ac0': self.unknown_0x39e57ac0.to_json(),
            'legend_background_color': self.legend_background_color.to_json(),
            'node_color': self.node_color.to_json(),
            'selected_node_color': self.selected_node_color.to_json(),
            'parent_node_color': self.parent_node_color.to_json(),
            'unknown_0x56843943': self.unknown_0x56843943.to_json(),
            'selected_text_cursor_color': self.selected_text_cursor_color.to_json(),
            'unknown_0x905ce2c0': self.unknown_0x905ce2c0,
            'text_scale': self.text_scale,
            'selected_text_scale': self.selected_text_scale,
            'transition_time': self.transition_time,
            'node_collapse_motion': self.node_collapse_motion.to_json(),
            'selected_node_collapse_motion': self.selected_node_collapse_motion.to_json(),
            'node_expand_motion': self.node_expand_motion.to_json(),
            'rotation_speed': self.rotation_speed,
            'node_scale': self.node_scale,
            'selected_node_scale': self.selected_node_scale,
            'selected_text_cursor_scale': self.selected_text_cursor_scale,
            'scan_model_scale': self.scan_model_scale,
            'unknown_0x925b9d4a': self.unknown_0x925b9d4a.to_json(),
            'unknown_0x075a0734': self.unknown_0x075a0734.to_json(),
            'unknown_0x8ef43309': self.unknown_0x8ef43309,
            'fog_near': self.fog_near,
            'fog_far': self.fog_far,
            'fog_color': self.fog_color.to_json(),
            'unknown_0xeef15783': self.unknown_0xeef15783,
            'unknown_0x78055ab2': self.unknown_0x78055ab2,
            'unknown_0x09e3197f': self.unknown_0x09e3197f,
            'unknown_0xfaffce1f': self.unknown_0xfaffce1f,
            'unknown_0xe5280e7c': self.unknown_0xe5280e7c,
            'background_sweep_color': self.background_sweep_color.to_json(),
            'background_sweep_radius': self.background_sweep_radius,
            'background_sweep_time': self.background_sweep_time,
            'scan_text_window_background_color': self.scan_text_window_background_color.to_json(),
            'scan_text_window_border_color': self.scan_text_window_border_color.to_json(),
            'scan_text_window_font_color': self.scan_text_window_font_color.to_json(),
            'legend_window_background_color': self.legend_window_background_color.to_json(),
            'legend_window_border_color': self.legend_window_border_color.to_json(),
            'legend_window_font_color': self.legend_window_font_color.to_json(),
            'legend_hide_time': self.legend_hide_time,
            'unknown_0x7f35c573': self.unknown_0x7f35c573.to_json(),
            'unknown_0xe0d77cf1': self.unknown_0xe0d77cf1.to_json(),
            'unknown_0x903d9b7e': self.unknown_0x903d9b7e.to_json(),
            'unknown_0x0fdf22fc': self.unknown_0x0fdf22fc.to_json(),
            'unknown_0xbeaf9d6b': self.unknown_0xbeaf9d6b.to_json(),
            'unknown_0x7e8247d6': self.unknown_0x7e8247d6.to_json(),
            'unknown_0x8b3f7902': self.unknown_0x8b3f7902.to_json(),
            'unknown_0xdc1abb82': self.unknown_0xdc1abb82.to_json(),
            'unknown_0x306b2b24': self.unknown_0x306b2b24.to_json(),
            'frame_color': self.frame_color.to_json(),
            'unknown_0x1a4b8068': self.unknown_0x1a4b8068.to_json(),
            'slider_background_color': self.slider_background_color.to_json(),
            'slider_selection_color': self.slider_selection_color.to_json(),
            'slider_scale': self.slider_scale,
            'slider_speed': self.slider_speed,
            'unknown_0x58795865': self.unknown_0x58795865,
            'unknown_0x35e0bd31': self.unknown_0x35e0bd31,
            'menu_option_color': self.menu_option_color.to_json(),
            'menu_option_enabled_arrow_color': self.menu_option_enabled_arrow_color.to_json(),
            'menu_option_disabled_arrow_color': self.menu_option_disabled_arrow_color.to_json(),
            'menu_option_scale': self.menu_option_scale,
            'menu_option_arrow_scale': self.menu_option_arrow_scale,
            'model_rotation_speed': self.model_rotation_speed,
            'unknown_0x60914b79': self.unknown_0x60914b79,
            'unknown_0x1fd44d9b': self.unknown_0x1fd44d9b,
            'model_light1_position': self.model_light1_position.to_json(),
            'model_light1_color': self.model_light1_color.to_json(),
            'model_light2_position': self.model_light2_position.to_json(),
            'model_light2_color': self.model_light2_color.to_json(),
            'model_ambient_light_color': self.model_ambient_light_color.to_json(),
        }


def _decode_main_window_border_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_main_window_text_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_main_window_selected_text_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0xfe98f30e(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x39e57ac0(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_legend_background_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_node_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_selected_node_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_parent_node_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x56843943(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_selected_text_cursor_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x905ce2c0(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_text_scale(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_selected_text_scale(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_transition_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_node_collapse_motion(data: typing.BinaryIO, property_size: int):
    return Spline.from_stream(data, property_size)


def _decode_selected_node_collapse_motion(data: typing.BinaryIO, property_size: int):
    return Spline.from_stream(data, property_size)


def _decode_node_expand_motion(data: typing.BinaryIO, property_size: int):
    return Spline.from_stream(data, property_size)


def _decode_rotation_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_node_scale(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_selected_node_scale(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_selected_text_cursor_scale(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_scan_model_scale(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x925b9d4a(data: typing.BinaryIO, property_size: int):
    return Spline.from_stream(data, property_size)


def _decode_unknown_0x075a0734(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x8ef43309(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_fog_near(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_fog_far(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_fog_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0xeef15783(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x78055ab2(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x09e3197f(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0xfaffce1f(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0xe5280e7c(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_background_sweep_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_background_sweep_radius(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_background_sweep_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_scan_text_window_background_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_scan_text_window_border_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_scan_text_window_font_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_legend_window_background_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_legend_window_border_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_legend_window_font_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_legend_hide_time(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x7f35c573(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0xe0d77cf1(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x903d9b7e(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x0fdf22fc(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0xbeaf9d6b(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x7e8247d6(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x8b3f7902(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0xdc1abb82(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x306b2b24(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_frame_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_unknown_0x1a4b8068(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_slider_background_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_slider_selection_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_slider_scale(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_slider_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x58795865(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x35e0bd31(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_menu_option_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_menu_option_enabled_arrow_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_menu_option_disabled_arrow_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_menu_option_scale(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_menu_option_arrow_scale(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_model_rotation_speed(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x60914b79(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_unknown_0x1fd44d9b(data: typing.BinaryIO, property_size: int):
    return struct.unpack('>f', data.read(4))[0]


def _decode_model_light1_position(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


def _decode_model_light1_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_model_light2_position(data: typing.BinaryIO, property_size: int):
    return Vector.from_stream(data)


def _decode_model_light2_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


def _decode_model_ambient_light_color(data: typing.BinaryIO, property_size: int):
    return Color.from_stream(data)


_property_decoder: typing.Dict[int, typing.Tuple[str, typing.Callable[[typing.BinaryIO, int], typing.Any]]] = {
    0xba5a65c8: ('main_window_border_color', _decode_main_window_border_color),
    0xbff0e37b: ('main_window_text_color', _decode_main_window_text_color),
    0x28b49a88: ('main_window_selected_text_color', _decode_main_window_selected_text_color),
    0xfe98f30e: ('unknown_0xfe98f30e', _decode_unknown_0xfe98f30e),
    0x39e57ac0: ('unknown_0x39e57ac0', _decode_unknown_0x39e57ac0),
    0xa6b633fa: ('legend_background_color', _decode_legend_background_color),
    0xac80013b: ('node_color', _decode_node_color),
    0x5946b439: ('selected_node_color', _decode_selected_node_color),
    0xc5aa728c: ('parent_node_color', _decode_parent_node_color),
    0x56843943: ('unknown_0x56843943', _decode_unknown_0x56843943),
    0x6bd4783a: ('selected_text_cursor_color', _decode_selected_text_cursor_color),
    0x905ce2c0: ('unknown_0x905ce2c0', _decode_unknown_0x905ce2c0),
    0x5fa64c77: ('text_scale', _decode_text_scale),
    0xaa60f975: ('selected_text_scale', _decode_selected_text_scale),
    0x1832935e: ('transition_time', _decode_transition_time),
    0x165943f6: ('node_collapse_motion', _decode_node_collapse_motion),
    0x9ad04dd7: ('selected_node_collapse_motion', _decode_selected_node_collapse_motion),
    0x8719a9c: ('node_expand_motion', _decode_node_expand_motion),
    0x11cd076f: ('rotation_speed', _decode_rotation_speed),
    0xb71677d0: ('node_scale', _decode_node_scale),
    0x42d0c2d2: ('selected_node_scale', _decode_selected_node_scale),
    0x70420ed1: ('selected_text_cursor_scale', _decode_selected_text_cursor_scale),
    0xc0cb3936: ('scan_model_scale', _decode_scan_model_scale),
    0x925b9d4a: ('unknown_0x925b9d4a', _decode_unknown_0x925b9d4a),
    0x75a0734: ('unknown_0x075a0734', _decode_unknown_0x075a0734),
    0x8ef43309: ('unknown_0x8ef43309', _decode_unknown_0x8ef43309),
    0x4194622e: ('fog_near', _decode_fog_near),
    0x3935a756: ('fog_far', _decode_fog_far),
    0xe578c0dd: ('fog_color', _decode_fog_color),
    0xeef15783: ('unknown_0xeef15783', _decode_unknown_0xeef15783),
    0x78055ab2: ('unknown_0x78055ab2', _decode_unknown_0x78055ab2),
    0x9e3197f: ('unknown_0x09e3197f', _decode_unknown_0x09e3197f),
    0xfaffce1f: ('unknown_0xfaffce1f', _decode_unknown_0xfaffce1f),
    0xe5280e7c: ('unknown_0xe5280e7c', _decode_unknown_0xe5280e7c),
    0x647d9f91: ('background_sweep_color', _decode_background_sweep_color),
    0x7120f18f: ('background_sweep_radius', _decode_background_sweep_radius),
    0x4def660d: ('background_sweep_time', _decode_background_sweep_time),
    0xc7c1967b: ('scan_text_window_background_color', _decode_scan_text_window_background_color),
    0xf74bbad2: ('scan_text_window_border_color', _decode_scan_text_window_border_color),
    0xe31421e2: ('scan_text_window_font_color', _decode_scan_text_window_font_color),
    0xb8f0ddb: ('legend_window_background_color', _decode_legend_window_background_color),
    0xa7a4155: ('legend_window_border_color', _decode_legend_window_border_color),
    0x527a0b10: ('legend_window_font_color', _decode_legend_window_font_color),
    0x7927ca67: ('legend_hide_time', _decode_legend_hide_time),
    0x7f35c573: ('unknown_0x7f35c573', _decode_unknown_0x7f35c573),
    0xe0d77cf1: ('unknown_0xe0d77cf1', _decode_unknown_0xe0d77cf1),
    0x903d9b7e: ('unknown_0x903d9b7e', _decode_unknown_0x903d9b7e),
    0xfdf22fc: ('unknown_0x0fdf22fc', _decode_unknown_0x0fdf22fc),
    0xbeaf9d6b: ('unknown_0xbeaf9d6b', _decode_unknown_0xbeaf9d6b),
    0x7e8247d6: ('unknown_0x7e8247d6', _decode_unknown_0x7e8247d6),
    0x8b3f7902: ('unknown_0x8b3f7902', _decode_unknown_0x8b3f7902),
    0xdc1abb82: ('unknown_0xdc1abb82', _decode_unknown_0xdc1abb82),
    0x306b2b24: ('unknown_0x306b2b24', _decode_unknown_0x306b2b24),
    0xa485372c: ('frame_color', _decode_frame_color),
    0x1a4b8068: ('unknown_0x1a4b8068', _decode_unknown_0x1a4b8068),
    0xcc2f25f1: ('slider_background_color', _decode_slider_background_color),
    0xcb8d5caf: ('slider_selection_color', _decode_slider_selection_color),
    0x3f44254f: ('slider_scale', _decode_slider_scale),
    0x7087c377: ('slider_speed', _decode_slider_speed),
    0x58795865: ('unknown_0x58795865', _decode_unknown_0x58795865),
    0x35e0bd31: ('unknown_0x35e0bd31', _decode_unknown_0x35e0bd31),
    0xe7c283be: ('menu_option_color', _decode_menu_option_color),
    0xdabcb730: ('menu_option_enabled_arrow_color', _decode_menu_option_enabled_arrow_color),
    0x9c2195d7: ('menu_option_disabled_arrow_color', _decode_menu_option_disabled_arrow_color),
    0xfc54f555: ('menu_option_scale', _decode_menu_option_scale),
    0xef549530: ('menu_option_arrow_scale', _decode_menu_option_arrow_scale),
    0xfa7a92b8: ('model_rotation_speed', _decode_model_rotation_speed),
    0x60914b79: ('unknown_0x60914b79', _decode_unknown_0x60914b79),
    0x1fd44d9b: ('unknown_0x1fd44d9b', _decode_unknown_0x1fd44d9b),
    0x6c93afa: ('model_light1_position', _decode_model_light1_position),
    0x33924afb: ('model_light1_color', _decode_model_light1_color),
    0x17b45083: ('model_light2_position', _decode_model_light2_position),
    0xaa702cfa: ('model_light2_color', _decode_model_light2_color),
    0x62ff6d72: ('model_ambient_light_color', _decode_model_ambient_light_color),
}

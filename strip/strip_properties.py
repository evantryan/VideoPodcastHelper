import bpy

class StripModeSettings(bpy.types.PropertyGroup):

    modes = [
        ("IGNORE", "Ignore", "", 1),
        ("A", "a", "", 2),
        ("B", "b", "", 3),
        ("C", "c", "", 4),
    ]
    
    mode: bpy.props.EnumProperty(items=modes, options={'ANIMATABLE'},)

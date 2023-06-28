import bpy
from .strip_properties import  StripModeSettings

classes = [
    StripModeSettings,
]

modes = [
        ("IGNORE", "Ignore", "", 1),
        ("A", "a", "", 2),
        ("B", "b", "", 3),
        ("C", "c", "", 4),
    ]
    

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    # bpy.types.Sequence.video_podcast_helper = bpy.props.PointerProperty(type=StripModeSettings)
    bpy.types.Sequence.video_podcast_helper_modes = bpy.props.EnumProperty(items=modes, options={'ANIMATABLE'},)
    
def unregister():
    del bpy.types.Sequence.video_podcast_helper

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

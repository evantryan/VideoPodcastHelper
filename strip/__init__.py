import bpy
from .strip_properties import  StripModeSettings
from ..core import app_handlers

classes = [
    StripModeSettings,
]

modes = [
        ("IGNORE", "Ignore", "", 1),
        ("A", "a", "", 2),
        ("B", "b", "", 3),
        ("C", "c", "", 4),
    ]

def enum_update(enum, context):
    app_handlers.update_helper_modes(context.scene, depsgraph=None)
    

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.Sequence.video_podcast_helper_modes = bpy.props.EnumProperty(items=modes, options={'ANIMATABLE'}, update=enum_update)
    
def unregister():
    del bpy.types.Sequence.video_podcast_helper_modes

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

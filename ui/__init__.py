import bpy
from .strip_modes import SEQUENCER_PT_podcast_modes

classes = (
    SEQUENCER_PT_podcast_modes,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    try:
        unregister()
    except Exception as e:
        print(e)
    
    register()

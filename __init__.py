from . import core
from . import strip
from . import ui

bl_info = {
    "name": "VideoPodcastEditHelper",
    "author": "Evan Ryan",
    "version": (0, 0, 0),
    "blender": (3, 3, 0),
    "location": "Video Sequence Editor",
    "category": "VSE",
    "description": "Attributes for automagically enabling or disabling strips inside a metastrip",
    "warning": ""
}

VERSION = 'v0.0.0' 

def register():
    strip.register()
    core.register()
    ui.register()

def unregister():
    ui.unregister()
    core.unregister()
    strip.unregister()
    
if __name__ == "__main__":
    try:
        unregister()
    except Exception as e:
        print(e)
    
    register()
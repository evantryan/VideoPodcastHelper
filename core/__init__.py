import bpy
from . import app_handlers

def register():
    bpy.app.handlers.frame_change_pre.append(app_handlers.frame_change_pre)
    
def unregister():
    bpy.app.handlers.frame_change_pre.remove(app_handlers.frame_change_pre)
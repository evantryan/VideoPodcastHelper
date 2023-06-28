import bpy
from . import app_handlers

def register():
    bpy.app.handlers.frame_change_post.append(app_handlers.update_helper_modes)
    bpy.app.handlers.render_pre.append(app_handlers.update_helper_modes)
    
def unregister():
    bpy.app.handlers.render_pre.remove(app_handlers.update_helper_modes)
    bpy.app.handlers.frame_change_post.remove(app_handlers.update_helper_modes)
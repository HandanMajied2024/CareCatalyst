import bpy, sys, os, traceback
log = open(r"C:\Users\tutuh\Documents\Hackjuntion_Finnland_2026\3d-hands\b-blender\inst.log", "w", encoding="utf-8")
sys.stdout = sys.stderr = log
try:
    zp = r"C:\Users\tutuh\Documents\Hackjuntion_Finnland_2026\3d-hands\b-blender\dl\mpfb.zip"
    print(bpy.ops.extensions.package_install_files(filepath=zp, repo="user_default", enable_on_install=True))
    bpy.ops.wm.save_userpref()
    import addon_utils
    print([m.__name__ for m in addon_utils.modules() if 'mpfb' in m.__name__])
    print("enabled:", [a for a in bpy.context.preferences.addons.keys()])
    print("ext dir:", bpy.utils.user_resource('EXTENSIONS'))
except Exception:
    traceback.print_exc()
log.flush()

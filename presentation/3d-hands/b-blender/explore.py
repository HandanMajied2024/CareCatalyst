import bpy, sys, os, traceback
from mathutils import Vector
B = r"C:\Users\tutuh\Documents\Hackjuntion_Finnland_2026\3d-hands\b-blender"
log = open(os.path.join(B, "work", "explore.log"), "w", encoding="utf-8"); sys.stdout = sys.stderr = log
try:
    from bl_ext.user_default.mpfb.services.humanservice import HumanService
    [bpy.data.objects.remove(o) for o in list(bpy.data.objects)]
    bm = HumanService.create_human()
    print("basemesh", bm.name, len(bm.data.vertices), bm.dimensions[:])
    rig = HumanService.add_builtin_rig(bm, "default")
    print("rig", rig.name, len(rig.data.bones))
    mh = os.path.join(B, r"assets\mh_system\skins\young_caucasian_male\young_caucasian_male.mhmat")
    HumanService.set_character_skin(mh, bm, skin_type="ENHANCED_SSS")
    print("mats", [m.name for m in bm.data.materials])
    print("mods", [(m.name, m.type) for m in bm.modifiers])
    for n in ["lowerarm01.R","lowerarm02.R","wrist.R","metacarpal2.R","finger3-1.R","finger3-3.R","finger1-1.R","finger1-3.R","finger5-1.R"]:
        b = rig.data.bones[n]
        print(n, "head", tuple(round(x,3) for x in (rig.matrix_world @ b.head_local)), "tail", tuple(round(x,3) for x in (rig.matrix_world @ b.tail_local)), "parent", b.parent.name if b.parent else None, "x", tuple(round(x,2) for x in b.matrix_local.col[0][:3]), "z", tuple(round(x,2) for x in b.matrix_local.col[2][:3]))
    print("vgroups sample", [g.name for g in bm.vertex_groups][:400])
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(B, "work", "explore.blend"))
except Exception:
    traceback.print_exc()
log.flush()

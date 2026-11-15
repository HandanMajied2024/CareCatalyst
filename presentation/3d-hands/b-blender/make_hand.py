# make_hand.py - MPFB human -> forearm+hand holding a phone, Apple-style studio shot.
# Usage (headless):  blender -b -P make_hand.py -- <mode> [frame] [res%]
#   mode: still  -> renders one EEVEE frame to work/preview_<frame>.png
#         anim   -> renders all frames to out/frames/####.png
#         cycles -> renders one Cycles still to out/still.png
#         build  -> only builds + saves work/scene.blend
import bpy, bmesh, sys, os, math, time, traceback
import numpy as np
from mathutils import Vector, Matrix, Euler

B = r"C:\Users\tutuh\Documents\Hackjuntion_Finnland_2026\3d-hands\b-blender"
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
MODE = argv[0] if argv else "still"
FRAME = int(argv[1]) if len(argv) > 1 and argv[1].isdigit() else 72
RES = int(argv[2]) if len(argv) > 2 else 100
os.makedirs(os.path.join(B, "work"), exist_ok=True)
log = open(os.path.join(B, "work", f"log_{MODE}.txt"), "w", encoding="utf-8")
sys.stdout = sys.stderr = log
T0 = time.time()

# ---------------- tunables ----------------
SKIN = r"assets\mh_system\skins\young_caucasian_female\young_caucasian_female.mhmat"
MACRO = {"gender": 0.35, "age": 0.45, "muscle": 0.45, "weight": 0.38}
PW, PH, PT = 0.0715, 0.1467, 0.0080      # phone width, height, thickness (m)
GRIP_ANGLE = math.radians(0)            # roll of phone long axis vs finger direction (about palm normal)
TIP_OVER = 0.004                         # fingertips peek this far over the top edge
X_SHIFT = 0.003                            # sideways phone offset
ADDUCT = {2: 14, 4: 6, 5: 12}              # deg finger spread closing
D_H = 0.088                              # phone centre along wrist->knuckle axis
D_A = 0.018                              # phone centre along pinky->index axis
PALM = 0.016                             # palm half-thickness (wrist axis to palm skin)
TIP_DEPTH = 0.0                          # fingertip depth relative to phone mid-plane
TIP_OUT = 0.0045                         # fingertip bone tail outside the phone edge
Y_TIPS = -0.018                          # mean fingertip height on the phone (phone-local Y)
FOREARM_ANGLE = 70                       # forearm leaves the phone going down at this angle (deg)
FPS, NFR = 24, 72


def say(*a):
    print(f"[{time.time()-T0:6.1f}s]", *a); log.flush()


def norm(v):
    v = Vector(v); return v.normalized()


# ---------------- scene reset ----------------
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o)
scn = bpy.context.scene
scn.render.fps = FPS
scn.frame_start, scn.frame_end = 1, NFR

# ---------------- MPFB human ----------------
from bl_ext.user_default.mpfb.services.humanservice import HumanService
from bl_ext.user_default.mpfb.services.targetservice import TargetService
macro = TargetService.get_default_macro_info_dict()
macro.update(MACRO)
bm_obj = HumanService.create_human(macro_detail_dict=macro)
TD = os.path.join(os.path.dirname(TargetService.target_full_path.__code__.co_filename), "..", "data", "targets", "hands")
for side in ("l", "r"):
    for tname, w in [("hand-fingers-diameter-decr", 0.7), ("hand-fingers-length-incr", 0.45), ("hand-scale-decr", 0.15)]:
        TargetService.load_target(bm_obj, os.path.join(TD, f"{side}-{tname}.target.gz"), weight=w)
rig = HumanService.add_builtin_rig(bm_obj, "default")
HumanService.set_character_skin(os.path.join(B, SKIN), bm_obj, skin_type="ENHANCED_SSS")
sk = bm_obj.data.materials[0].node_tree.nodes["Human.body"]
for k, v in [("Pore strength", 0.35), ("Roughness", 0.5), ("SSS strength", 0.35), ("colorMixInStrength", 0.08), ("Contrast", 0.08)]:
    try: sk.inputs[k].default_value = v
    except Exception as ex: say("skin input skip", k, ex)
say("human+rig+skin done", bm_obj.name, rig.name)

# keep only right forearm + hand (mask everything else)
KEEP_BONES = [b.name for b in rig.data.bones if b.name.endswith(".R") and (
    b.name.startswith(("lowerarm", "wrist", "metacarpal", "finger")))]
keep_idx = {bm_obj.vertex_groups[n].index for n in KEEP_BONES if n in bm_obj.vertex_groups}
body_idx = bm_obj.vertex_groups["body"].index
vg = bm_obj.vertex_groups.new(name="keep_arm")
sel = []
for v in bm_obj.data.vertices:
    gs = {g.group: g.weight for g in v.groups}
    if body_idx in gs and sum(w for gi, w in gs.items() if gi in keep_idx) > 0.5:
        sel.append(v.index)
vg.add(sel, 1.0, 'REPLACE')
bm_obj.modifiers["Hide helpers"].vertex_group = "keep_arm"
sub = bm_obj.modifiers.new("Subsurf", 'SUBSURF'); sub.levels = 1; sub.render_levels = 2
say("kept verts", len(sel))

# ---------------- hand frame (armature space, rest pose) ----------------
bones = rig.data.bones
def head(n): return bones[n].head_local.copy()
def tail(n): return bones[n].tail_local.copy()
W = head("wrist.R")
K_mid, K_idx, K_pnk = head("finger3-1.R"), head("finger2-1.R"), head("finger5-1.R")
h = norm(K_mid - W)
across = K_idx - K_pnk; across = norm(across - across.dot(h) * h)
n = norm(h.cross(across))
# palm side = direction of natural rest curl of the middle finger
v1 = norm(tail("finger3-1.R") - head("finger3-1.R")); v3 = norm(tail("finger3-3.R") - head("finger3-3.R"))
curv = v3 - v1
if curv.dot(n) < 0:
    n = -n
say("hand frame h", tuple(h), "across", tuple(across), "palm n", tuple(n), "curv.n", curv.dot(n))

# ---------------- FK finger curl fitted to the phone, wrist bent so forearm enters bottom-right ----------
P = rig.pose.bones
for pb in P: pb.rotation_mode = 'XYZ'
def upd(): bpy.context.view_layer.update()
curl_sign = {}
for f in (2, 3, 4, 5):
    for seg in (1, 2, 3):
        bn = f"finger{f}-{seg}.R"; upd(); t0 = P[f"finger{f}-3.R"].tail.copy()
        P[bn].rotation_euler.x = 0.4; upd()
        curl_sign[bn] = 1 if (P[f"finger{f}-3.R"].tail - t0).dot(n) > 0 else -1
        P[bn].rotation_euler.x = 0.0
BASE_CURL = (40, 50, 30)   # deg, proximal/middle/distal at c=1
def set_curl(f, c):
    for seg, a in zip((1, 2, 3), BASE_CURL):
        bn = f"finger{f}-{seg}.R"; P[bn].rotation_euler.x = curl_sign[bn] * math.radians(a * c)
# palm skin depth from mesh vertices (shape keys applied)
kbs = bm_obj.data.shape_keys.key_blocks if bm_obj.data.shape_keys else []
def vco(i):
    if not kbs: return bm_obj.data.vertices[i].co.copy()
    b = kbs[0].data[i].co.copy(); v = b.copy()
    for kb in kbs[1:]:
        if kb.value: v += (kb.data[i].co - b) * kb.value
    return v
mc_idx = {bm_obj.vertex_groups[f"metacarpal{i}.R"].index for i in (1, 2, 3, 4)}
palm_d = sorted((vco(v.index) - W).dot(n) for v in bm_obj.data.vertices
                if any(g.group in mc_idx and g.weight > 0.5 for g in v.groups))
Dp = palm_d[int(len(palm_d) * 0.92)]
D_C = Dp + PT / 2 + 0.0008                     # phone centre depth (back of phone touches palm)
say("palm depth", round(Dp, 4), "n palm verts", len(palm_d))
# phone long axis = finger direction (phone stands upright in the hand, fingers behind it)
u = norm(h - h.dot(n) * n)
u = norm(Matrix.Rotation(GRIP_ANGLE, 3, n) @ u)
xax = norm(u.cross(n))
# close the finger spread (adduction about bone Z towards the middle finger)
for f, ang in ADDUCT.items():
    bn = f"finger{f}-1.R"; upd()
    d0 = (P[f"finger{f}-3.R"].tail - P["finger3-3.R"].tail).length
    P[bn].rotation_euler.z = 0.1; upd()
    sg = 1 if (P[f"finger{f}-3.R"].tail - P["finger3-3.R"].tail).length < d0 else -1
    P[bn].rotation_euler.z = sg * math.radians(ang)
upd()
# fingers rest flat against the phone back: tip depth = phone back - finger radius
D_T = D_C - PT / 2 - 0.0065
curl_c = {}
for f in (2, 3, 4, 5):
    lo, hi = -0.8, 1.5
    for _ in range(30):
        mid = (lo + hi) / 2; set_curl(f, mid); upd()
        d = (P[f"finger{f}-3.R"].tail - W).dot(n)
        if d < D_T: lo = mid
        else: hi = mid
    curl_c[f] = round((lo + hi) / 2, 3); set_curl(f, curl_c[f])
upd()
say("curl factors", curl_c)
T = {f: P[f"finger{f}-3.R"].tail.copy() for f in (2, 3, 4, 5)}
ytop = max((T[f] - W).dot(u) for f in T)
xs = [(T[f] - W).dot(xax) for f in T]
C = W + u * (ytop - PH / 2 - TIP_OVER) + xax * ((max(xs) + min(xs)) / 2 + X_SHIFT) + n * D_C
M_phone_rest = Matrix(((xax.x, u.x, n.x, C.x), (xax.y, u.y, n.y, C.y), (xax.z, u.z, n.z, C.z), (0, 0, 0, 1)))
thumb_side = 1 if (P["finger1-3.R"].tail - C).dot(xax) > 0 else -1
sx = -thumb_side
say("thumb side", thumb_side, "tips(phone-local)", {f: tuple(round(x, 3) for x in (M_phone_rest.inverted() @ T[f])) for f in T})
# wrist search
Mw_rest = bones["wrist.R"].matrix_local.copy()
want = Vector((thumb_side * math.cos(math.radians(FOREARM_ANGLE)), -math.sin(math.radians(FOREARM_ANGLE)), 0)).normalized()
best = None
for rx in range(-35, 36, 5):
    for rz in range(-35, 36, 5):
        P["wrist.R"].rotation_euler = (math.radians(rx), 0, math.radians(rz)); upd()
        Rel = P["wrist.R"].matrix @ Mw_rest.inverted()
        Mp = Rel @ M_phone_rest
        fa = (P["lowerarm01.R"].head - P["wrist.R"].head).normalized()
        fl = Mp.to_3x3().transposed() @ fa
        fl2 = Vector((fl.x, fl.y, 0)).normalized()
        score = fl2.dot(want) - 0.002 * (abs(rx) + abs(rz)) - 0.3 * max(0, fl.z)
        if best is None or score > best[0]: best = (score, rx, rz, Mp.copy(), tuple(round(x, 2) for x in fl))
say("wrist best", best[:3], "forearm(phone-local)", best[4])
P["wrist.R"].rotation_euler = (math.radians(best[1]), 0, math.radians(best[2])); upd()
M_phone_arm = best[3]

# ---------------- controller empty ----------------
ctrl = bpy.data.objects.new("HandCtrl", None); scn.collection.objects.link(ctrl)
rig.parent = ctrl
rig.matrix_parent_inverse = Matrix.Identity(4)
rig.matrix_basis = M_phone_arm.inverted()
bm_obj.parent = rig  # already

# ---------------- materials ----------------
def principled(name, base, rough=0.4, metal=0.0, emis=None, emis_s=0.0, coat=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    p = m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = (*base, 1)
    p.inputs["Roughness"].default_value = rough
    p.inputs["Metallic"].default_value = metal
    if coat: p.inputs["Coat Weight"].default_value = coat
    if emis is not None:
        p.inputs["Emission Color"].default_value = (*emis, 1)
        p.inputs["Emission Strength"].default_value = emis_s
    return m

m_frame = principled("Frame", (0.80, 0.79, 0.77), rough=0.22, metal=1.0)
m_back = principled("BackGlass", (0.86, 0.85, 0.83), rough=0.45, coat=0.3)
m_glass = principled("FrontGlass", (0.004, 0.004, 0.005), rough=0.04, coat=1.0)

# screen texture (procedural wallpaper: airbrush blobs + glass cards)
SW, SH = 600, 1240
yy, xx = np.mgrid[0:SH, 0:SW].astype(np.float32)
xn, yn = xx / SW, yy / SH          # yn=0 bottom
img = np.ones((SH, SW, 3), np.float32) * np.array([0.97, 0.97, 0.99], np.float32)
def blob(cx, cy, r, col, a):
    d = ((xn - cx) ** 2 + ((yn - cy) * SH / SW) ** 2) / (r * r)
    w = (np.exp(-d) * a)[..., None]
    return w, np.array(col, np.float32)
for cx, cy, r, col, a in [(0.15, 0.85, 0.55, (0.55, 0.70, 1.00), 0.85),
                          (0.95, 0.60, 0.55, (0.85, 0.65, 1.00), 0.75),
                          (0.30, 0.15, 0.60, (1.00, 0.78, 0.62), 0.70),
                          (0.80, 0.05, 0.40, (1.00, 0.60, 0.75), 0.5)]:
    w, c = blob(cx, cy, r, col, a); img = img * (1 - w) + c * w
def rrect(x0, y0, x1, y1, r, col, a):
    global img
    px, py = xx, yy
    cx, cy = np.clip(px, x0 + r, x1 - r), np.clip(py, y0 + r, y1 - r)
    d = np.sqrt((px - cx) ** 2 + (py - cy) ** 2) - r
    w = (np.clip(0.5 - d, 0, 1) * a)[..., None]
    img = img * (1 - w) + np.array(col, np.float32) * w
rrect(225, SH - 60, 375, SH - 22, 19, (0, 0, 0), 1.0)                 # dynamic island
rrect(40, SH - 380, SW - 40, SH - 130, 44, (1, 1, 1), 0.72)            # card 1
rrect(70, SH - 200, 330, SH - 175, 12, (0.15, 0.15, 0.2), 0.85)        # "text" lines
rrect(70, SH - 250, 440, SH - 232, 9, (0.55, 0.55, 0.62), 0.6)
rrect(70, SH - 340, 200, SH - 280, 30, (0.30, 0.55, 1.0), 0.95)        # icon
rrect(40, SH - 700, SW - 40, SH - 420, 44, (1, 1, 1), 0.62)            # card 2
for i in range(3):
    rrect(70, SH - 480 - i * 70, 70 + 380 - i * 90, SH - 455 - i * 70, 11, (0.3, 0.3, 0.38), 0.55)
rrect(230, 18, 370, 28, 5, (0.1, 0.1, 0.1), 0.9)                       # home bar
rgba = np.concatenate([img, np.ones((SH, SW, 1), np.float32)], axis=2)
im = bpy.data.images.new("ScreenUI", SW, SH, alpha=False)
im.colorspace_settings.name = "sRGB"
im.pixels.foreach_set(rgba.ravel())
im.pack()

m_screen = bpy.data.materials.new("Screen"); m_screen.use_nodes = True
nt = m_screen.node_tree; p = nt.nodes["Principled BSDF"]
tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = im
nt.links.new(tex.outputs["Color"], p.inputs["Emission Color"])
p.inputs["Emission Strength"].default_value = 1.6
p.inputs["Base Color"].default_value = (0, 0, 0, 1)
p.inputs["Roughness"].default_value = 0.05
p.inputs["Coat Weight"].default_value = 1.0

m_btn = principled("Button", (0, 0, 0), rough=0.1, emis=(0.02, 0.02, 0.025), emis_s=1.0)

# ---------------- phone geometry ----------------
def rrect_verts(w, hgt, r, seg=12):
    pts = []
    for cx, cy, a0 in [(w/2 - r, hgt/2 - r, 0), (-w/2 + r, hgt/2 - r, 90), (-w/2 + r, -hgt/2 + r, 180), (w/2 - r, -hgt/2 + r, 270)]:
        for i in range(seg + 1):
            a = math.radians(a0 + 90 * i / seg)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts

def slab(name, w, hgt, r, thick, mats, bevel=0.0):
    me = bpy.data.meshes.new(name); bmm = bmesh.new()
    pts = rrect_verts(w, hgt, r)
    vb = [bmm.verts.new((x, y, -thick/2)) for x, y in pts]
    vt = [bmm.verts.new((x, y, thick/2)) for x, y in pts]
    ftop = bmm.faces.new(vt); ftop.material_index = 0
    fbot = bmm.faces.new(list(reversed(vb))); fbot.material_index = 1
    k = len(pts)
    for i in range(k):
        f = bmm.faces.new((vb[i], vb[(i+1) % k], vt[(i+1) % k], vt[i])); f.material_index = 2
    bmm.normal_update(); bmm.to_mesh(me); bmm.free()
    ob = bpy.data.objects.new(name, me); scn.collection.objects.link(ob)
    for m in mats: me.materials.append(m)
    if bevel:
        bv = ob.modifiers.new("Bevel", 'BEVEL'); bv.width = bevel; bv.segments = 5
        bv.limit_method = 'ANGLE'; bv.angle_limit = math.radians(40); bv.harden_normals = False
    for poly in me.polygons: poly.use_smooth = True
    return ob

def plate(name, w, hgt, r, z, mat):
    me = bpy.data.meshes.new(name); bmm = bmesh.new()
    vs = [bmm.verts.new((x, y, z)) for x, y in rrect_verts(w, hgt, r)]
    f = bmm.faces.new(vs); bmm.to_mesh(me); bmm.free()
    ob = bpy.data.objects.new(name, me); scn.collection.objects.link(ob)
    me.materials.append(mat)
    # UVs from xy
    uv = me.uv_layers.new(name="UVMap")
    for li, loop in enumerate(me.loops):
        co = me.vertices[loop.vertex_index].co
        uv.data[li].uv = (co.x / w + 0.5, co.y / hgt + 0.5)
    return ob

phone = slab("Phone", PW, PH, 0.0105, PT, [m_glass, m_back, m_frame], bevel=0.0016)
bez = 0.0022
screen = plate("Screen", PW - 2*bez, PH - 2*bez, 0.0085, PT/2 + 0.00015, m_screen)
button = plate("Button", 0.050, 0.0125, 0.00625, 0.0, m_btn)
button.location = (thumb_side * 0.006, -0.040, PT/2 + 0.0003)
for ob in (phone, screen):
    ob.parent = ctrl
screen.parent = phone; button.parent = phone
# camera bump on the back
bump = slab("CamBump", 0.030, 0.030, 0.007, 0.0016, [m_back, m_back, m_frame], bevel=0.0005)
bump.parent = phone; bump.location = (-sx * (PW/2 - 0.019), PH/2 - 0.019, -PT/2 - 0.0008)

# ---------------- finger IK (targets on the phone edge) ----------------
def flex_axis(bn):
    b = bones[bn]; M = b.matrix_local.to_3x3()
    ax = {"x": M.col[0], "z": M.col[2]}
    return max(ax, key=lambda k: abs(ax[k].dot(across)))

def add_target(name, loc):
    e = bpy.data.objects.new(name, None); scn.collection.objects.link(e)
    e.empty_display_size = 0.005; e.parent = phone; e.location = loc
    return e

# thumb: tip over the front bezel of the near edge
THUMB_REST = Vector((thumb_side * (PW/2 - 0.003), -0.030, PT/2 + 0.0070))
THUMB_TAP = Vector((thumb_side * 0.012, -0.040, PT/2 + 0.0055))
tthumb = add_target("tgt_thumb", THUMB_REST)
c = rig.pose.bones["finger1-3.R"].constraints.new('IK'); c.target = tthumb; c.chain_count = 3; c.use_stretch = False
for seg in (1, 2, 3):
    rig.pose.bones[f"finger1-{seg}.R"].lock_ik_y = True

# ---------------- final placement in world ----------------
# phone local Z (screen) -> world -Y (towards camera), local Y -> world +Z
BASE_ROT = Euler((math.radians(90), 0, 0), 'XYZ')
YAW = math.radians(-14)
FINAL = Euler((math.radians(90 - 4), math.radians(-7), YAW), 'XYZ')
ctrl.rotation_mode = 'XYZ'

def key_ctrl(fr, loc, rot, interp='BEZIER', easing='AUTO', back=None):
    ctrl.location = loc; ctrl.rotation_euler = rot
    ctrl.keyframe_insert("location", frame=fr); ctrl.keyframe_insert("rotation_euler", frame=fr)

START_LOC = Vector((0.30, 0.10, -0.34))
START_ROT = Euler((math.radians(90 - 35), math.radians(25), YAW + math.radians(40)), 'XYZ')
key_ctrl(1, START_LOC, START_ROT)
key_ctrl(16, Vector((0, 0, 0)), FINAL)
DRIFT = Euler((FINAL.x + math.radians(1.5), FINAL.y, FINAL.z + math.radians(3)), 'XYZ')
key_ctrl(NFR, Vector((-0.004, 0, 0.004)), DRIFT)
ad = ctrl.animation_data.action
fcs = ad.fcurves if hasattr(ad, "fcurves") else [fc for l in ad.layers for s in l.strips for cb in s.channelbags for fc in cb.fcurves]
for fc in fcs:
    for kp in fc.keyframe_points:
        if int(round(kp.co.x)) == 1:
            kp.interpolation = 'BACK'; kp.easing = 'EASE_OUT'
            kp.back = 0.9 if fc.data_path == "location" else 2.0
        elif int(round(kp.co.x)) == 16:
            kp.interpolation = 'BEZIER'; kp.easing = 'AUTO'

# thumb tap (fast in, quick release) + button reaction
def key_loc(ob, fr, loc, interp):
    ob.location = loc; ob.keyframe_insert("location", frame=fr)
    a = ob.animation_data.action
    fl = a.fcurves if hasattr(a, "fcurves") else [fc for l in a.layers for s in l.strips for cb in s.channelbags for fc in cb.fcurves]
    for fc in fl:
        for kp in fc.keyframe_points:
            if int(round(kp.co.x)) == fr: kp.interpolation = interp
TAP = 46
key_loc(tthumb, 1, THUMB_REST, 'CONSTANT')
key_loc(tthumb, TAP - 8, THUMB_REST, 'EXPO')
key_loc(tthumb, TAP, THUMB_TAP, 'BEZIER')
key_loc(tthumb, TAP + 3, THUMB_TAP, 'QUART')
key_loc(tthumb, TAP + 14, THUMB_REST, 'CONSTANT')
for fr, s, col in [(TAP - 1, 1.0, (0.02, 0.02, 0.025)), (TAP + 1, 0.93, (0.10, 0.45, 1.0)), (TAP + 6, 1.0, (0.10, 0.45, 1.0))]:
    button.scale = (s, s, 1); button.keyframe_insert("scale", frame=fr)
    em = m_btn.node_tree.nodes["Principled BSDF"].inputs["Emission Color"]
    em.default_value = (*col, 1); em.keyframe_insert("default_value", frame=fr)

# ---------------- camera, lights, world, backdrop ----------------
cam_d = bpy.data.cameras.new("Cam"); cam_d.lens = 50; cam_d.dof.use_dof = False
cam_d.dof.focus_distance = 0.58; cam_d.dof.aperture_fstop = 2.8
cam = bpy.data.objects.new("Cam", cam_d); scn.collection.objects.link(cam); scn.camera = cam
def look_at(ob, target):
    d = Vector(target) - ob.location
    ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
cam.location = (0.03, -0.62, 0.02); look_at(cam, (0.03, 0, 0.0))
cam.keyframe_insert("location", frame=1)
cam.location = (0.029, -0.595, 0.02); cam.keyframe_insert("location", frame=NFR)

def area(name, loc, size, energy, target=(0, 0, 0), color=(1, 1, 1)):
    ld = bpy.data.lights.new(name, 'AREA'); ld.shape = 'DISK'; ld.size = size; ld.energy = energy; ld.color = color
    lo = bpy.data.objects.new(name, ld); scn.collection.objects.link(lo); lo.location = loc; look_at(lo, target)
    return lo
area("Key", (-0.6, -0.45, 0.5), 0.8, 75, color=(1.0, 0.98, 0.95))
area("Fill", (0.7, -0.5, 0.0), 1.2, 6, color=(0.95, 0.97, 1.0))
area("Rim", (0.35, 0.35, 0.35), 0.4, 45)
area("Top", (0.0, -0.1, 0.8), 1.5, 6)

back_me = bpy.data.meshes.new("Backdrop")
back_me.from_pydata([(-3, 0.22, -3), (3, 0.22, -3), (3, 0.22, 3), (-3, 0.22, 3)], [], [(0, 1, 2, 3)])
backdrop = bpy.data.objects.new("Backdrop", back_me); scn.collection.objects.link(backdrop)
m_bd = principled("BackdropMat", (0.92, 0.92, 0.93), rough=0.9, emis=(0.96, 0.96, 0.97), emis_s=3.0)
back_me.materials.append(m_bd)

world = bpy.data.worlds.new("W"); scn.world = world; world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = (1, 1, 1, 1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.12

# ---------------- render settings ----------------
r = scn.render
r.resolution_x, r.resolution_y, r.resolution_percentage = 1280, 720, RES
scn.view_settings.view_transform = 'AgX'
try: scn.view_settings.look = 'AgX - Punchy'
except Exception as ex: say('look fail', ex)
say('look', scn.view_settings.look)
scn.view_settings.exposure = -0.85
r.use_motion_blur = True
r.motion_blur_shutter = 0.5
if MODE == "cycles":
    r.engine = 'CYCLES'; scn.cycles.samples = int(os.environ.get("CYCLES_SAMPLES", "128")); scn.cycles.use_denoising = True
    try:
        prefs = bpy.context.preferences.addons["cycles"].preferences
        for dt in ("OPTIX", "CUDA", "HIP", "ONEAPI"):
            try:
                prefs.compute_device_type = dt; prefs.get_devices()
                if any(d.type == dt for d in prefs.devices):
                    for d in prefs.devices: d.use = True
                    scn.cycles.device = 'GPU'; say("cycles device", dt); break
            except Exception: pass
    except Exception as e: say("gpu setup fail", e)
else:
    r.engine = 'BLENDER_EEVEE_NEXT'
    e = scn.eevee
    e.taa_render_samples = int(os.environ.get("EEVEE_SAMPLES", "32"))
    for k, v in [("use_raytracing", True), ("use_shadows", True), ("shadow_ray_count", 2), ("shadow_step_count", 8),
                 ("use_fast_gi", False), ("fast_gi_method", 'GLOBAL_ILLUMINATION')]:
        try: setattr(e, k, v)
        except Exception as ex: say("eevee setting skip", k, ex)
r.image_settings.file_format = 'PNG'
r.image_settings.color_mode = 'RGB'

bpy.ops.wm.save_as_mainfile(filepath=os.path.join(B, "work", "scene.blend"))
say("scene built + saved")

# ---------------- render ----------------
try:
    if MODE == "debug":
        r.engine = 'BLENDER_WORKBENCH'; scn.display.shading.light = 'STUDIO'; scn.display.shading.color_type = 'MATERIAL'
        r.use_motion_blur = False; scn.render.resolution_percentage = 50
        views = {"front": None, "back": ((0.0, 0.6, 0.0)), "side": ((-0.6, -0.05, 0.0)), "top": ((0.0, -0.05, 0.6))}
        backdrop.hide_render = True
        cam.animation_data_clear(); cam_d.dof.use_dof = False
        if os.environ.get("DBG_FRONT"): views = {"front": None}
        for fr in [int(x) for x in argv[1].split(",")]:
            scn.frame_set(fr)
            for vn, loc in views.items():
                if loc is None:
                    cam.location = (0.03, -0.62, 0.02); look_at(cam, (0.03, 0, 0.0))
                else:
                    cam.location = loc; look_at(cam, (0, 0, 0))
                r.filepath = os.path.join(B, "work", f"dbg_{fr:03d}_{vn}.png")
                bpy.ops.render.render(write_still=True)
        say("debug views done")
    elif MODE == "still":
        for fr in (FRAME, FRAME + 1):
            scn.frame_set(fr)
            r.filepath = os.path.join(B, "work", f"preview_{fr:03d}.png")
            bpy.ops.render.render(write_still=True); say("rendered", r.filepath)
    elif MODE == "cycles":
        scn.frame_set(FRAME)
        os.makedirs(os.path.join(B, "out"), exist_ok=True)
        r.filepath = os.path.join(B, "out", "still.png")
        bpy.ops.render.render(write_still=True); say("rendered cycles", r.filepath)
    elif MODE == "anim":
        os.makedirs(os.path.join(B, "out", "frames"), exist_ok=True)
        r.filepath = os.path.join(B, "out", "frames", "")
        bpy.ops.render.render(animation=True); say("rendered anim")
except Exception:
    traceback.print_exc()
say("done")
log.flush()

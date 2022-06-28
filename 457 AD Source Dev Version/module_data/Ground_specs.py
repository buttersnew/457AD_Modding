gtf_overlay = 0x00000001 #deprecated
gtf_dusty   = 0x00000002 #controls dustiness of the ground for foot dust particle systems 
gtf_has_color  = 0x00000004 #you can overwrite the ambient color of the ground spec (default: 0.61, 0.72, 0.15)

#IMPORTANT NOTE: Ground_specs have dependency on mnodule system and the engine c++ code!
#                You cannot add new ground types as they are hardcoded in the engine code.
#                Make sure you have updated your module's header_ground_types.py file 

#arguments:
#spec_name, flags, material, uv_scale, multitex_material_name, gtf_has_color->color
ground_specs = [
    ("gray_stone",gtf_has_color,"stone_a",4.0,"none",(0.431, 0.380, 0.247)),
    ("brown_stone",gtf_has_color,"patch_rock",2.0,"none",(0.419, 0.419, 0.419)),
    ("turf",gtf_overlay|gtf_has_color,"grassy_ground",3.3,"ground_earth_under_grass",(0.160, 0.462, 0.078)),
    ("steppe",gtf_overlay|gtf_dusty|gtf_has_color,"ground_steppe",3.0,"ground_earth_under_steppe",(0.321, 0.396, 0.164)),
    ("snow",gtf_overlay|gtf_has_color,"snow",5.2,"none",(0.219, 0.376, 0.062)),
    ("earth",gtf_overlay|gtf_dusty|gtf_has_color,"ground_earth",4.5,"none",(0.388, 0.282, 0.094)),
    ("desert",gtf_overlay|gtf_dusty|gtf_has_color,"ground_desert", 3.5,"none",(0.611, 0.568, 0.227)),
    ("forest",gtf_overlay|gtf_has_color,"ground_forest",4.2,"ground_forest_under_grass",(0.301, 0.368, 0.168)),
    ("pebbles",gtf_overlay|gtf_has_color,"pebbles",4.1,"none",(0.250, 0.447, 0.447)),
    ("village",gtf_overlay|gtf_has_color,"ground_village",7.0,"none",(0.556, 0.525, 0.501)),
    ("path",gtf_overlay|gtf_dusty|gtf_has_color,"ground_path",6.0,"none",(0.572, 0.396, 0.090)),
]

def write_vec(file,vec):
  file.write(" %f %f %f "%vec)
  
def save_ground_specs():
  file = open("./ground_specs.txt","w")
  for ground_spec in ground_specs:
    file.write(" %s %d %s %f %s"%(ground_spec[0],ground_spec[1],ground_spec[2],ground_spec[3],ground_spec[4]))
    if (ground_spec[1] & gtf_has_color):
      file.write(" %f %f %f"%ground_spec[5])
    file.write("\n")
  file.close()

def save_c_header():
  file = open("./ground_spec_codes.h","w")
  file.write("#ifndef _GROUND_SPEC_CODES_H\n")
  file.write("#define _GROUND_SPEC_CODES_H\n\n")
  file.write("typedef enum {\n")
  for ground_spec in ground_specs:
    file.write("  ground_%s,\n"%ground_spec[0])
  file.write("}Ground_spec_codes;\n")
  file.write("const int num_ground_specs = %d;\n"%(len(ground_specs)))
  file.write("\n\n")
  file.write("\n#endif\n")
  file.close()
  
def save_python_header():
  file = open("../Module_system/header_ground_types.py","w")
  for ig in xrange(len(ground_specs)):
    ground_spec = ground_specs[ig]
    file.write("ground_%s = %d\n"%(ground_spec[0], ig))
  file.write("\n\n")
  file.close()

print "Exporting ground_spec data..."
save_ground_specs()
save_c_header()
save_python_header()
#print "Finished."
  

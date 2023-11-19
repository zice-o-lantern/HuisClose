init offset = -4

layeredimage ammon:
    zoom 0.4
    anchor (0.5, 0.6)
    group body:
        attribute body default "ammon_body_neutral" 
    group head:
        attribute front default "ammon_face_front"
        attribute right "ammon_face_right"

    group jaw if_any["right"]:
        attribute j_neutral default "ammon_face_right_jaw_neutral"
        attribute j_disgusted "ammon_face_right_jaw_disgusted"
        attribute j_noway "ammon_face_right_jaw_noway"
        attribute j_smug "ammon_face_right_jaw_smug"
        attribute j_happy "ammon_face_right_jaw_happy"
        attribute j_growl "ammon_face_right_jaw_growl"
        attribute j_surprised "ammon_face_right_jaw_surprised"
    group jaw if_any["front"]:
        attribute j_neutral default "ammon_face_front_jaw_neutral"
        attribute j_disgusted "ammon_face_front_jaw_disgusted"
        attribute j_noway "ammon_face_front_jaw_noway"
        attribute j_smug "ammon_face_front_jaw_smug"
        attribute j_happy "ammon_face_front_jaw_happy"
        attribute j_growl "ammon_face_front_jaw_growl"
        attribute j_yell "ammon_face_front_jaw_yell"
    
    group pupils if_any["right"]:
        attribute pupils default "ammon_face_right_pupils"
    group pupils if_any["front"]:
        attribute pupils default "ammon_face_front_pupils"

    group eyes if_any["right"]:
        attribute e_neutral default "ammon_face_right_eyes_neutral"
        attribute e_noway "ammon_face_right_eyes_noway"
        attribute e_disgusted "ammon_face_right_eyes_disgusted"
        attribute e_smug "ammon_face_right_eyes_smug"
        attribute e_happy "ammon_face_right_eyes_happy"
        attribute e_angry "ammon_face_right_eyes_angry"
        attribute e_closed "ammon_face_right_eyes_closed"
    group eyes if_any["front"]:
        attribute e_neutral default "ammon_face_front_eyes_neutral"
        attribute e_noway "ammon_face_front_eyes_noway"
        attribute e_disgusted "ammon_face_front_eyes_disgusted"
        attribute e_smug "ammon_face_front_eyes_smug"
        attribute e_happy "ammon_face_front_eyes_happy"
        attribute e_angry "ammon_face_front_eyes_angry"
        attribute e_closed "ammon_face_front_eyes_closed"
    
    group clothes:
        attribute no_clothes null 
        attribute biker default "ammon_clothes_biker"
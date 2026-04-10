################################################################################
## VOID Home Screen — Monochromatic Deep Space
################################################################################

transform void_bg_drift:
    yoffset 0
    linear 22.0 yoffset -40
    linear 22.0 yoffset 0
    repeat

transform void_title_glitch:
    alpha 1.0
    xoffset 0
    pause 3.8
    linear 0.04 xoffset 5
    linear 0.03 xoffset -5
    linear 0.03 xoffset 3
    linear 0.04 xoffset 0
    linear 0.06 alpha 0.80
    linear 0.06 alpha 1.0
    pause 2.0
    linear 0.04 xoffset -4
    linear 0.04 xoffset 4
    linear 0.04 xoffset 0
    repeat

transform void_breathe:
    alpha 0.55
    linear 2.8 alpha 0.95
    linear 2.8 alpha 0.55
    repeat

transform void_bracket:
    alpha 0.35
    linear 2.2 alpha 0.85
    linear 2.2 alpha 0.35
    repeat

transform void_scanlines:
    yoffset 0
    linear 8.0 yoffset 8
    yoffset 0
    repeat

transform void_rule_in:
    alpha 0.0
    linear 0.8 alpha 0.55

transform void_datacol:
    alpha 0.0
    linear 1.2 alpha 1.0


screen void_btn(label_text, btn_action):
    button:
        action btn_action
        xsize 330
        ysize 56
        background None
        hover_background Solid("#ffffff")
        padding (0, 0, 0, 0)

        hbox:
            xsize 330
            ysize 56

            frame:
                xsize 3
                yfill True
                background Solid("#ffffff")

            null width 14

            text ">":
                size 20
                color "#888888"
                hover_color "#000000"
                yalign 0.5
                font "DejaVuSans.ttf"

            null width 12

            text label_text:
                size 24
                bold True
                color "#cccccc"
                hover_color "#000000"
                kerning 3.5
                yalign 0.5
                font "DejaVuSans.ttf"
                substitute False


screen main_menu():

    tag menu

    ## Video background — size=(w,h) is the Movie constructor param for render size
    add Movie(play="homepage.webm", loop=True, size=(1920, 1080)):
        xpos 0
        ypos 0


    add Solid("#ffffff"):
        xpos 0
        ypos 0
        xsize 1920
        ysize 2
        alpha 0.50

    text "SYS://VOID.EXE  >  SIGNAL: LOCKED":
        xpos 52
        ypos 16
        size 14
        color "#ffffff6b"
        font "DejaVuSans.ttf"
        kerning 2.0

    text "COORDS: ???AU // CLASS: UNKNOWN // STATUS: ACTIVE":
        xalign 1.0
        xoffset -52
        ypos 16
        size 13
        color "#ffffff4c"
        font "DejaVuSans.ttf"
        kerning 1.5

    fixed:
        xpos 40
        ypos 40
        xsize 52
        ysize 52
        at void_bracket
        add Solid("#ffffff") xpos 0 ypos 0 xsize 52 ysize 2
        add Solid("#ffffff") xpos 0 ypos 0 xsize 2 ysize 52

    fixed:
        xalign 1.0
        xoffset -40
        ypos 40
        xsize 52
        ysize 52
        at void_bracket
        add Solid("#ffffff") xpos 0 ypos 0 xsize 52 ysize 2
        add Solid("#ffffff") xpos 50 ypos 0 xsize 2 ysize 52

    fixed:
        xpos 40
        yalign 1.0
        yoffset -40
        xsize 52
        ysize 52
        at void_bracket
        add Solid("#ffffff") xpos 0 ypos 50 xsize 52 ysize 2
        add Solid("#ffffff") xpos 0 ypos 0 xsize 2 ysize 52

    fixed:
        xalign 1.0
        xoffset -40
        yalign 1.0
        yoffset -40
        xsize 52
        ysize 52
        at void_bracket
        add Solid("#ffffff") xpos 0 ypos 50 xsize 52 ysize 2
        add Solid("#ffffff") xpos 50 ypos 0 xsize 2 ysize 52

    add Solid("#ffffff"):
        xpos 116
        ypos 90
        xsize 1
        ysize 880
        alpha 0.16

    vbox:
        xpos 152
        yalign 0.5
        yoffset -30
        spacing 0

        text "// DEEP SPACE NARRATIVE ENGINE":
            size 15
            color "#ffffff66"
            kerning 4.5
            font "DejaVuSans.ttf"

        null height 20

        fixed:
            xsize 560
            ysize 185

            text "VOID":
                xoffset 4
                yoffset 5
                size 158
                bold True
                color "#00000099"
                font "DejaVuSans.ttf"

            text "VOID":
                size 158
                bold True
                color "#ffffff"
                font "DejaVuSans.ttf"
                at void_title_glitch

        add Transform(Solid("#ffffff"), alpha=0.50):
            xsize 340
            ysize 1
            at void_rule_in

        null height 22

        text "AN INTERACTIVE EXPERIENCE":
            size 22
            color "#ffffffb3"
            kerning 3.5
            font "DejaVuSans.ttf"
            at void_breathe

        null height 6

        text "VER 1.0  --  SECTOR UNKNOWN  --  SIGNAL ACTIVE":
            size 13
            color "#ffffff4c"
            kerning 2.0
            font "DejaVuSans.ttf"

        null height 68

        use void_btn("[[ START ]]", Start())

        null height 18

        use void_btn("[[ LOAD ]]", ShowMenu("load"))

        null height 18

        use void_btn("[[ SETTINGS ]]", ShowMenu("preferences"))

        null height 18

        use void_btn("[[ QUIT ]]", Quit(confirm=True))

    vbox:
        xalign 1.0
        xoffset -78
        yalign 0.5
        yoffset 50
        spacing 10
        at void_datacol

        text "// SECTOR DATA FEED":
            size 13
            color "#ffffff47"
            kerning 2.0
            font "DejaVuSans.ttf"

        add Transform(Solid("#ffffff"), alpha=0.18):
            xsize 200
            ysize 1

        null height 4

        text "OBJECT CLASS  : UNKNOWN":
            size 13
            color "#ffffff38"
            kerning 1.5
            font "DejaVuSans.ttf"

        text "MASS          : ??? SOLAR":
            size 13
            color "#ffffff38"
            kerning 1.5
            font "DejaVuSans.ttf"

        text "SIGNAL ORIGIN : VOID":
            size 13
            color "#ffffff38"
            kerning 1.5
            font "DejaVuSans.ttf"

        text "TIME DILATION : ACTIVE":
            size 13
            color "#ffffff38"
            kerning 1.5
            font "DejaVuSans.ttf"

        text "CREW STATUS   : MISSING":
            size 13
            color "#ffffff38"
            kerning 1.5
            font "DejaVuSans.ttf"

        text "MISSION LOG   : --CORRUPTED--":
            size 13
            color "#ffffff38"
            kerning 1.5
            font "DejaVuSans.ttf"

        null height 20

        add Transform(Solid("#ffffff"), alpha=0.10):
            xsize 200
            ysize 1

        text "// END DATA":
            size 11
            color "#ffffff24"
            kerning 2.0
            font "DejaVuSans.ttf"

    add Solid("#ffffff"):
        xpos 0
        yalign 1.0
        xsize 1920
        ysize 2
        alpha 0.50

    text "SIGNAL LOCK: ESTABLISHED | UPLINK STABLE":
        xpos 52
        yalign 1.0
        yoffset -20
        size 13
        color "#ffffff52"
        font "DejaVuSans.ttf"

    text "AUDIO: ACTIVE":
        xalign 1.0
        xoffset -52
        yalign 1.0
        yoffset -20
        size 13
        color "#ffffff52"
        font "DejaVuSans.ttf"

    on "show" action Play("music", "ryzen.wav", loop=True, fadein=2.5)
    on "replace" action Play("music", "ryzen.wav", loop=True, fadein=2.5)

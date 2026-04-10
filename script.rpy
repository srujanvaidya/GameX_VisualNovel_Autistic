## ═══════════════════════════════════════════════════════════════════════════
##  V O I D  —  Complete Script
## ═══════════════════════════════════════════════════════════════════════════

define flash       = Fade(0.1, 0.0, 0.5, color="#fff")
define flash_black = Fade(0.1, 0.0, 0.8, color="#000")
define flash_blue  = Fade(0.1, 0.0, 0.7, color="#0a0a2e")
define flash_red   = Fade(0.1, 0.0, 0.6, color="#1a0000")

## Far-right position — character's right edge flush with screen edge
transform far_right:
    xalign 1.0
    xanchor 1.0
    yalign 1.0

## ─── Characters ──────────────────────────────────────────────────────────────

define verma      = Character("Dr. Verma",        color="#c0a060")
define das        = Character("Dr. Das",           color="#60a0c0")
define isro_dir   = Character("ISRO Director",     color="#e8c96a")
define anika      = Character("Anika",             color="#9b59b6",
                               what_prefix="{i}", what_suffix="{/i}")
define anika_dist = Character("Anika ~distorted~", color="#7a3fa0",
                               what_prefix="{i}", what_suffix="{/i}")
define mir        = Character("Mir",               color="#3498db")
define ground     = Character("Ground Control",    color="#2ecc71")
define comm       = Character("Comm Officer",      color="#f39c12")

## ─── Variables ───────────────────────────────────────────────────────────────

default trust_anika  = 0
default mir_courage = 0

## ─── Images ──────────────────────────────────────────────────────────────────

image bg_lab           = Transform("lab.png",                      xysize=(1920,1080), fit="cover")
image bg_lab_blast     = Transform("lab blast.png",                xysize=(1920,1080), fit="cover")
image bg_rocket        = Transform("isro rocket.png",              xysize=(1920,1080), fit="cover")
image bg_isro          = Transform("home.png",                     xysize=(1920,1080), fit="cover")
image bg_power         = Transform("power.png",                    xysize=(1920,1080), fit="cover")
image bg_wormhole_in   = Transform("spaceship enters wormhole.png",xysize=(1920,1080), fit="cover")
image bg_wormhole_ins  = Transform("inside wormhole.png",          xysize=(1920,1080), fit="cover")

image scientist_verma  = Transform("nuclear scientist 1.png", ysize=1030, fit="scale-down", yalign=1.0)
image scientist_das    = Transform("nuclear scientist 2.png", ysize=1030, fit="scale-down", yalign=1.0)
image char_anika       = Transform("Anika.png",               ysize=1680, fit="scale-down", yalign=1.0)
image char_mir         = Transform("lassi.png",               ysize=1680, fit="scale-down", yalign=1.0)
image char_isro_dir    = Transform("Isro director.png",       ysize=1680, fit="scale-down", yalign=1.0)

## ─── Video displayables (size forces fullscreen stretch) ────────────────────
image vid_anki_stuck   = Movie(play="anki stuck.webm",     loop=True, size=(1920, 1080))
image vid_wormhole     = Movie(play="wormhole travel.webm", loop=True, size=(1920, 1080))

## ═══════════════════════════════════════════════════════════════════════════
##  S T A R T
## ═══════════════════════════════════════════════════════════════════════════

label start:

    ## ─── ACT I TITLE ─────────────────────────────────────────────────────────
    scene black with dissolve
    pause 0.5
    show text "{size=80}{b}ACT  I{/b}{/size}\n{size=36}{color=#888}The Experiment{/color}{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    pause 0.3

    ## ─── Lab — Verma & Das ───────────────────────────────────────────────────
    scene bg_lab with dissolve
    show scientist_verma at left  with dissolve
    show scientist_das   at far_right with dissolve
    pause 0.3

    "ISRO Quantum Research Division — Bengaluru, India."
    "A room that hums. Banks of servers. Light bending around the containment sphere at the centre."

    verma "Containment field locked at 97 percent. Das — three points from ignition. Tonight we change history."

    das "The committee has not cleared phase three. We skipped four safety benchmarks—"

    verma "History does not remember the ones who waited for permission. Look at it. Zero-point quantum energy. Clean. Infinite. Every light on Earth burning forever."

    das "Or every light going out. The models show a resonance feedback loop at this energy density. If containment fails—"

    verma "The field is holding. The Shunya Core is stable. We proceed."

    "Das stares at the readout. His hand moves toward the emergency stop."

    ## ─── CHOICE 1 ────────────────────────────────────────────────────────────
    menu:
        "Stop him. This is not safe.":
            das "Verma, I am pulling the override. This is not safe."
            verma "Das — do NOT touch that panel—"
            das "I am ending this. Now."
            "They struggle. In the confusion — the stabiliser input drops by 0.3 percent."
            $ trust_anika += 3
            jump lab_explosion

        "Let Verma proceed.":
            das "...Alright. But the moment telemetry spikes, I am pulling the brake."
            verma "It will not spike. Watch."
            $ mir_courage += 2
            jump lab_explosion

label lab_explosion:

    scene bg_lab with dissolve
    show scientist_verma at left with dissolve
    show scientist_das   at far_right with dissolve

    verma "Initiating ignition sequence."

    das "Verma — the resonance is climbing. Past threshold—"

    verma "Normal fluctuation — compensate with secondary dampeners!"

    das "Nothing is responding! The field is INVERTING — the containment sphere is folding in—"

    verma "Kill the power! Manual override — kill EVERYTHING—"

    das "The console is fused! The metal is liquefying! WE HAVE TO RUN!"

    ## ─── Explosion ───────────────────────────────────────────────────────────
    hide scientist_verma
    hide scientist_das
    scene bg_lab_blast with flash
    pause 1.2

    scene bg_lab_blast with dissolve
    show scientist_das at far_right with dissolve

    "Silence."
    "Then a sound with no name — a low, tidal groan passing through walls, floor, bone."

    das "...Verma."

    das "Surface telemetry. The rift went up. Through the ceiling. Through the stratosphere."

    das "It is above the Earth."

    pause 0.8

    das "What have we done?"

    ## ─── Earth Destruction — VIDEO + AUDIO ───────────────────────────────────
    hide scientist_das
    scene black with dissolve
    pause 0.4

    show text "{size=60}{b}2 years later.{/b}{/size}\n{size=28}{color=#888}The Void spreads.{/color}{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    pause 0.3

    stop music fadeout 0.5
    play sound "earff destroy.mp3" fadein 1.0
    $ renpy.movie_cutscene("earth_destroyed.webm", loops=0)
    ## Sound plays until it naturally ends — no forced stop

    scene bg_power with dissolve
    pause 0.3

    "The wormhole did not close."
    "It grew."
    "Cities along the equator went dark first. Then coastlines. Then everything within a thousand kilometres of the rift."
    "Billions watched the sky turn violet."
    "Then the sky disappeared."

    ## ─── ACT II TITLE ────────────────────────────────────────────────────────
    scene black with flash_black
    pause 0.3
    show text "{size=80}{b}ACT  II{/b}{/size}\n{size=36}{color=#888}Anirva{/color}{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    pause 0.3

    ## ─── ISRO Mission briefing ───────────────────────────────────────────────
    scene bg_isro with dissolve
    show scientist_das at left with dissolve
    show char_isro_dir at far_right with dissolve
    pause 0.3

    "ISRO Mission Control. Sriharikota. Two years after the rift."

    isro_dir "Project Anirva. One pilot. Approach the wormhole. Deploy sensors. Transmit everything back."

    das "And if the approach destabilises the rift further?"

    isro_dir "Then we know more than we do now. Our pilot understands the risk."

    das "Who volunteered?"

    isro_dir "Anika. She did not hesitate for a single second."

    ## ─── CHOICE 2 ────────────────────────────────────────────────────────────
    menu:
        "Approve the mission. Earth needs answers.":
            das "Then God help her. Approve it."
            $ trust_anika += 2

        "Raise objections. It is too dangerous.":
            das "We are sending one woman towards a hole in spacetime with no extraction plan."
            isro_dir "We have no better options, Das."
            das "...then may she come back."
            $ mir_courage += 1

    ## ─── Anirva Launch ───────────────────────────────────────────────────────
    hide scientist_das
    hide char_isro_dir
    scene bg_rocket with dissolve
    show char_anika at left with dissolve
    pause 0.3

    "T-minus thirty seconds. Sriharikota Launch Pad Alpha."
    "The rocket was named Anirva — the Sanskrit word for limitless."
    "Inside, a single astronaut breathed slowly and watched the countdown."

    ground "Anika, all systems nominal. You are go for launch."

    "She did not reply. She had already said her goodbyes."

    hide char_anika
    scene bg_rocket with flash_black
    pause 0.5

    "Ignition. The world shook."
    "Anirva climbed through the stratosphere like a prayer aimed at God's eye."
    "And at four hundred kilometres — the wormhole was waiting."

    ## ─── Anirva gets TRAPPED ─────────────────────────────────────────────────
    scene bg_wormhole_in with dissolve
    pause 0.5

    "The sensor array deployed perfectly."
    "The data was extraordinary — gravitational readings that broke every instrument."
    "Anika reached for the thrusters to pull back."

    pause 0.8

    "The thrusters did not fire."

    pause 1.0

    "Anirva was pulled into the gravitational gradient — not consumed, but held."
    "Suspended at the threshold. Like a fly caught in amber."

    ground "Anirva — we are not reading your thrusters. Anika — respond."

    "Static."

    ground "Anika — respond. Please respond."

    "The rocket sat at the edge of spacetime. Fully intact. Completely unreachable."
    "Two weeks passed."

    ## ─── ACT III TITLE ───────────────────────────────────────────────────────
    scene black with flash_black
    pause 0.3
    show text "{size=80}{b}ACT  III{/b}{/size}\n{size=36}{color=#888}The Signal{/color}{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    pause 0.3

    ## ─── Day 14 — ground control ─────────────────────────────────────────────
    scene bg_isro with dissolve
    show scientist_das at left with dissolve
    pause 0.3

    "Day 14. 03:47 AM. Ground Control has not slept."

    comm "Sir. A signal — coming from the Anirva frequency. It is her."

    das "Put it on."

    ## ─── Anika's first transmission — anki stuck.webm (video-only, muted) ───────
    ## Use image alias for the Movie displayable; audio muted via set_volume
    $ renpy.music.set_volume(0.0, channel="movie")
    scene vid_anki_stuck with dissolve

    anika_dist "Still alive. Anirva is locked in the gradient field. I am not alone here."

    scene bg_isro with dissolve
    $ renpy.music.set_volume(1.0, channel="movie")
    show scientist_das at left with dissolve

    das "{i}(under his breath){/i} Anika."

    ## Second glimpse
    $ renpy.music.set_volume(0.0, channel="movie")
    scene vid_anki_stuck with dissolve

    anika_dist "I can see things. I cannot explain it. The past — I can see the past. Moments playing back. 2026. I can see the lab. I can see you, Dr. Das. I can also see forward. Fragments."

    scene bg_isro with dissolve
    $ renpy.music.set_volume(1.0, channel="movie")
    show scientist_das at left with dissolve

    comm "The signal is fading—"

    ## Third glimpse
    $ renpy.music.set_volume(0.0, channel="movie")
    scene vid_anki_stuck with dissolve

    anika_dist "There is something beyond this wormhole. Another side. Connected to ours. But it is twenty years behind. I am standing at the edge of two different nows. Send someone. Please—"

    ## Restore movie channel volume
    $ renpy.music.set_volume(1.0, channel="movie")

    scene bg_isro with dissolve
    show scientist_das at left with dissolve

    "Signal lost."

    pause 1.0

    das "..."

    comm "Sir — what does she mean? Twenty years behind?"

    das "{i}(slowly){/i} She means the wormhole is not just a bridge through space."

    comm "Sir?"

    das "It is a bridge through time."

    ## ─── CHOICE 3 ────────────────────────────────────────────────────────────
    menu:
        "Believe Anika. Act immediately.":
            das "Get me the Director. This changes everything."
            $ trust_anika += 5

        "Be sceptical. Need verification.":
            das "I need a second source before I take this further."
            comm "But sir — she said to send someone—"
            das "And I need certainty before I send someone to their death."
            $ mir_courage -= 2

    hide scientist_das
    scene bg_power with dissolve
    pause 0.3

    "Das called the Director."
    "The Director called the Prime Minister."
    "By dawn, the decision was made."

    ## ─── ACT IV TITLE ────────────────────────────────────────────────────────
    scene black with flash_black
    pause 0.3
    show text "{size=80}{b}ACT  IV{/b}{/size}\n{size=36}{color=#888}Vikrant — The Last Hope{/color}{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    pause 0.3

    ## ─── Vikrant mission briefing ────────────────────────────────────────────
    scene bg_isro with dissolve
    show char_mir      at far_right with dissolve
    show scientist_das at left  with dissolve
    show char_isro_dir at far_right with dissolve
    pause 0.3

    "ISRO's fastest mission turnaround. Eighteen days. Zero sleep."
    "The rocket was named Vikrant — courageous."
    "Mission: reach Anirva's coordinates, re-establish contact, understand the gateway."

    isro_dir "One pilot. Operates alone inside a quantum anomaly."

    "The room went quiet."

    mir "That is me, sir."

    isro_dir "The mission profile does not guarantee return."

    mir "Neither does staying on Earth."

    das "Mir — you understand what Anika said? If this works — if you go beyond—"

    mir "I understand perfectly, Dr. Das. That is exactly why I am the one who should go."

    ## ─── CHOICE 4 ────────────────────────────────────────────────────────────
    menu:
        "Mir: I am ready. Let us go now.":
            mir "Stop wasting time. Launch the mission."
            $ mir_courage += 5

        "Mir: Run me through the entry parameters first.":
            mir "I need full trajectory data before we commit."
            das "Of course. Here—"
            $ trust_anika += 2

    ## ─── Vikrant Launch ──────────────────────────────────────────────────────
    hide scientist_das
    hide char_isro_dir
    hide char_mir
    scene bg_rocket with dissolve
    show char_mir at center with dissolve
    pause 0.3

    "Vikrant launched at 04:00 AM. No public broadcast."
    "The only light in the sky was the rocket — and the wound above it."

    mir "Systems green. Hull integrity nominal. Approaching boundary."

    ground "Vikrant, you are holding at the boundary. Anirva is at your eleven o'clock — forty-two kilometres."

    mir "Copy. Deploying long-range comms array. Matching Anirva's frequency."

    ## ─── Vikrant contacts Anika ──────────────────────────────────────────────
    hide char_mir
    scene bg_wormhole_in with dissolve
    pause 0.5

    "Eleven minutes after deployment — the comms array locked on."

    anika_dist "Vikrant? Is that a signal from—"

    mir "Anika. This is Mir. We received your transmissions. We are here."

    anika_dist "{i}(voice breaking){/i} Mir. You came."

    mir "Tell me everything about the other side."

    anika_dist "The wormhole connects to our universe. Not another dimension — the same universe. Our Earth. But the exit is displaced in time. By twenty years. If you fly through — you arrive in our world twenty years ago. Before the experiment. Before any of this."

    mir "{i}(long pause){/i} Twenty years. That means someone could go back and stop it."

    anika_dist "Stop Dr. Verma before he presses ignition. Das already had doubts — he had his hand near the override. He just needed someone to say what he could not say himself."

    scene bg_isro with dissolve
    show scientist_das at left with dissolve

    das "If someone goes through — they have a chance to change the past. To prevent the rift from ever forming."

    scene bg_wormhole_in with dissolve

    anika_dist "But the wormhole is not stable. The threshold will not stay open long. Mir — it could be days."

    ## ─── CHOICE 5 ────────────────────────────────────────────────────────────
    menu:
        "Mir: I trust you. Tell me what to do when I get through.":
            mir "Anika, I trust you completely. What do I need to do on the other side?"
            anika_dist "Find Dr. Das. Give him the courage to act on what he already knows."
            mir "Then I will say it."
            $ trust_anika += 5
            $ mir_courage += 5

        "Mir: This is a suicide mission. We need more data.":
            mir "Going in without an exit plan — that is not bravery, that is—"
            anika_dist "The exit plan is: the past changes. The rift disappears. You find your way back through a world that was never broken."
            $ trust_anika += 2
            $ mir_courage -= 3

        "Mir: Someone else should go. Not me.":
            mir "This does not have to be me. We can send someone else, or a probe—"
            anika_dist "Mir. I can see fragments of what happens on the other side. It has to be you."
            "Mir had no answer."
            $ mir_courage -= 5

    ## ─── ACT V TITLE ─────────────────────────────────────────────────────────
    scene black with flash_black
    pause 0.3
    show text "{size=80}{b}ACT  V{/b}{/size}\n{size=36}{color=#888}Into the Wormhole{/color}{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    pause 0.3

    ## ─── Ground Control debate ───────────────────────────────────────────────
    scene bg_isro with dissolve
    show scientist_das at left with dissolve
    show char_isro_dir at far_right with dissolve
    pause 0.3

    das "We cannot authorise wormhole entry. We do not know if Vikrant survives transit."

    isro_dir "We do not know anything, Das. That has always been the situation."

    comm "Sir — Anika's signal is degrading. The window is compressing. If we are going to decide—"

    isro_dir "The question is simple. We do nothing — or we send him in."

    das "Or he dies in an event horizon and nothing changes."

    isro_dir "Or he goes through. Twenty years back. And he changes everything."

    isro_dir "Mir — are you still on comms?"

    hide scientist_das
    hide char_isro_dir
    scene bg_rocket with dissolve
    show char_mir at center with dissolve

    mir "I have been listening to every word."

    isro_dir "The decision is yours. You are the one in the seat."

    "Mir looked at the wormhole through the observation port."
    "Violet. Enormous. Turning slowly — as if breathing."

    scene bg_wormhole_in with dissolve

    anika_dist "Mir. You do not have to do this."

    scene bg_rocket with dissolve
    show char_mir at center with dissolve

    mir "Someone does."

    anika_dist "It is a one-way door. If the wormhole closes after you transit—"

    ## ─── CHOICE 6 — THE FINAL CHOICE ────────────────────────────────────────
    menu:
        "Fly Vikrant straight into the wormhole. No hesitation.":
            mir "Then I will be in the past with twenty years to find another way home."
            mir "Dr. Das — if you ever hear this recording — you were right. I am coming."
            ground "Mir — we have no clearance protocol for this—"
            mir "Tell my record to say: mission completed."
            $ mir_courage += 10
            jump ending_hero

        "Ask Ground Control for official clearance first.":
            mir "I need Ground Control to give clear authorisation. I will not do this alone."
            das "Give him the clearance. I take responsibility. Approved."
            $ trust_anika += 2
            $ mir_courage += 5
            jump ending_bittersweet

        "Turn back. The risk is too great.":
            mir "Anika... I cannot. I am sorry. I cannot go in without certainty."
            anika_dist "{i}(long silence){/i} I understand, Mir."
            ground "Vikrant, begin return trajectory."
            $ mir_courage -= 10
            jump ending_failure

## ═══════════════════════════════════════════════════════════════════════════
##  E N D I N G S
## ═══════════════════════════════════════════════════════════════════════════

label ending_hero:

    scene bg_wormhole_in with flash_blue
    pause 0.5

    "Vikrant does not hesitate."
    "Mir pushes the throttle to maximum and flies straight — arrow-straight — into the wormhole."

    ## ─── Wormhole travel video (webm) + rumble for 15s ────────────────────
    stop music fadeout 0.3
    ## Rumble plays on 'sound' channel (separate from music/movie) so it
    ## is audible throughout the full wormhole sequence
    play sound "rumble.mp3" fadein 0.5 loop
    $ renpy.music.set_volume(0.0, channel="movie")
    scene vid_wormhole with dissolve
    pause 15.0
    $ renpy.music.set_volume(1.0, channel="movie")
    stop sound fadeout 1.5
    scene black with dissolve

    "The hull sings. The instruments go white."
    "Time becomes visible — not as clocks, but as layered, overlapping light."
    "He sees the lab. He sees 2026. He sees Dr. Das, hand frozen over the manual override."
    "The exact moment before everything went wrong."

    mir "{i}(to himself){/i} I see you."

    show char_mir at center with dissolve

    "The wormhole folds closed behind him."

    pause 1.0

    hide char_mir
    scene bg_lab with dissolve
    show scientist_das at far_right with dissolve
    pause 0.3

    "Bengaluru. 2026. The air smells of rain."
    "The Shunya Lab hums. Verma is at the console. Das has his hand near the override."

    mir "Dr. Das!"

    das "{i}(startled){/i} Who are you? How did you get inside—"

    mir "There is no time. My name is Mir. I flew through a wormhole your experiment is about to create. You have your hand near that override for a reason. You already know something is wrong. Pull it. Right now."

    "Das stared at him. Then at his hand. Then at the readout."

    show scientist_verma at left with dissolve

    "Verma reached for the ignition."

    das "{b}STOP.{/b}"

    hide scientist_verma
    "Das slammed the manual override."
    "The Shunya Core went dark."

    scene bg_power with dissolve
    pause 0.5

    "The experiment never fired."
    "The rift never formed."
    "In 2028 — above Sriharikota — the sky simply cleared."

    pause 0.8

    scene bg_isro with dissolve
    show scientist_das at left with dissolve

    "ISRO command watched their screens as the wormhole signature vanished."

    anika_dist "{i}(barely a whisper){/i} It worked."

    pause 1.0

    hide scientist_das
    scene bg_wormhole_ins with dissolve
    pause 0.5

    "One astronaut. Twenty-eight years. Two timelines. One decision."

    scene black with dissolve
    pause 1.0

    show text "{size=90}{b}V O I D{/b}{/size}\n{size=28}{color=#9b59b6}Ending — The Hero's Return{/color}{/size}" at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    return

## ─────────────────────────────────────────────────────────────────────────────

label ending_bittersweet:

    scene bg_wormhole_in with flash_blue
    pause 0.5

    "Vikrant enters the wormhole with official clearance."
    "The transit is violent — far more than Anika described."

    scene bg_wormhole_ins with dissolve
    show char_mir at center with dissolve
    pause 0.4

    "Three seconds of impossible geometry. Then — air. Rain. Bengaluru, 2026."

    hide char_mir
    scene bg_lab with dissolve
    show scientist_das at far_right with dissolve
    pause 0.3

    "Mir reaches the lab. The experiment has already started."
    "The resonance is climbing. Das watches the readout with wide eyes."

    mir "Das — pull the override! The containment is going to fail—"

    das "Security! There is an intruder—"

    mir "Look at the readout! You KNOW something is wrong!"

    "Das looked. The resonance was at 89 percent. Rising."

    hide scientist_das
    scene bg_lab_blast with flash_red
    pause 0.4
    scene bg_lab_blast with dissolve

    "The core fractured — smaller than it would have been. A contained explosion."
    "Not nothing. But not everything."
    "The rift formed — a fraction of the original size."

    scene bg_power with dissolve
    pause 0.4

    "In 2028, the wormhole stopped growing."
    "The violet fields retreated from the cities. Slowly. Imperfectly."
    "The world was damaged — but alive."

    scene bg_isro with dissolve
    show scientist_das at left with dissolve

    anika_dist "He made it. It was not perfect. But the world survives."

    hide scientist_das
    scene black with dissolve
    pause 1.0

    show text "{size=90}{b}V O I D{/b}{/size}\n{size=28}{color=#60a0c0}Ending — A Flawed Salvation{/color}{/size}" at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    return

## ─────────────────────────────────────────────────────────────────────────────

label ending_failure:

    scene bg_rocket with dissolve
    show char_mir at center with dissolve
    pause 0.3

    "Vikrant turned."
    "The engines fired in the opposite direction."
    "Mir flew home."

    hide char_mir
    scene bg_isro with dissolve
    show char_mir at center with dissolve
    pause 0.3

    "He docked. He climbed out of the cockpit."
    "He stood in Mission Control surrounded by exhausted faces looking at him for an answer."

    mir "{i}(quietly){/i} I could not do it. I am sorry."

    show scientist_das at left with dissolve

    das "Then we find another way."

    "But above the Earth — the wormhole threshold widened by another half-kilometre."

    "And Anika's signal — they had been watching it the whole time Mir flew home."

    scene bg_wormhole_in with dissolve
    pause 0.5

    "It went silent at the exact moment Vikrant turned."

    pause 0.8

    scene bg_power with dissolve

    "They never heard from Anika again."
    "The wormhole grew by 20 kilometres over the next three months."

    pause 0.5

    "Sometimes Mir goes to the roof of Mission Control and watches the violet spiral turn in the night sky."
    "He tells himself there is still time."

    pause 0.8

    "He is not sure he believes it anymore."

    scene black with dissolve
    pause 1.0

    show text "{size=90}{b}V O I D{/b}{/size}\n{size=28}{color=#888}Ending — The Weight of Turning Back{/color}{/size}" at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    return
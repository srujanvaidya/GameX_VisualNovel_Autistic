## ─── Character Definitions ───────────────────────────────────────────────────

define flash       = Fade(0.1, 0.0, 0.5, color="#fff")
define flash_black = Fade(0.1, 0.0, 0.8, color="#000")

define verma = Character("Dr. Verma",  color="#c0a060")
define das   = Character("Dr. Das",    color="#60a0c0")
define m     = Character("Meera",      color="#3498db")
define a     = Character("Anika",      color="#9b59b6", what_prefix="{i}", what_suffix="{/i}")
define ar    = Character("Arjun",      color="#e67e22")
define p     = Character("Priya",      color="#2ecc71")
define v     = Character("Voice from the Void", color="#ffffff")
define narr  = Character(None,         kind=nvl_narrator)

## ─── Game Variables ──────────────────────────────────────────────────────────

default trust_anika          = 0
default entanglement_stability = 50

## ─── Image Declarations ──────────────────────────────────────────────────────

image bg_lab         = im.Scale("lab.png",          1920, 1080)
image bg_lab_blast   = im.Scale("lab blast.png",     1920, 1080)
image bg_isro_rocket = im.Scale("isro rocket.png",   1920, 1080)
image bg_earth_dead  = im.Scale("power.png",         1920, 1080)  ## swap with earth destroyed.png later
image bg_isro_lab    = im.Scale("home.png",          1920, 1080)  ## swap with isro lab.png later

image scientist_verma = "scientist man.png"
image scientist_das   = "scientist.png"
image astro_arjun     = "man astro.png"
image astro_meera     = "women saree.png"

## ─── START ───────────────────────────────────────────────────────────────────

label start:

    ## ── ACT 1 title card ─────────────────────────────────────────────────────
    scene black with dissolve
    pause 0.6

    show text "{size=72}{b}ACT I{/b}{/size}\n{size=36}{color=#aaaaaa}The Mission and the Trap{/color}{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    pause 0.4

    ## ── Lab scene opens ──────────────────────────────────────────────────────
    scene bg_lab with dissolve
    pause 0.5

    ## establish characters
    show scientist_verma at left  with dissolve
    show scientist_das   at right with dissolve

    pause 0.3

    ## ── Opening dialogue — ambition and hubris ────────────────────────────────

    verma "Containment field is holding at 94%%. Remarkable. Absolutely remarkable, Das."

    das "Verma... we need to dial it back. We are way past the authorized parameters."

    verma "Authorized by who, Das? The committee? They lack vision. {i}Look at it.{/i} We have done it. Zero-point energy. A localized quantum tear."

    das "It is illegal for a reason! If that field fluctuates by even a fraction of a percent, the particle collision will—"

    verma "It is completely stable. The Shunya core is behaving exactly as my models predicted. We are about to rewrite human history."

    das "History? Verma, if we harness this incorrectly we are not writing history — we are {b}ending{/b} it. This much energy could power entire continents."

    verma "Or something greater. Do you understand what a controlled quantum rift means for weapons technology? No missile, no army, nothing stops a tear in spacetime."

    das "You are talking about a weapon of mass destruction. That is why the ethics board shut down the original proposal!"

    verma "The ethics board is afraid of the dark. We are the ones holding the torch, Das. The nation that controls the Void controls the future."

    das "And if we lose control of it?"

    verma "We {i}won't.{/i}"

    ## ── The catastrophe ───────────────────────────────────────────────────────

    das "Warning alarm! Verma — the resonance! It is spiking! The field is fracturing!"

    verma "That is impossible, the dampeners are active! Reroute the secondary grid — pump everything into the magnetic lock!"

    das "I cannot! It is not pulling power — it is {b}emitting{/b} it! It is latching onto the floor! The geometry of the room is shifting!"

    verma "Kill the power! Pull the manual override!"

    das "The console is fused! Verma, the metal is... it is {i}melting{/i} into the glass! It is rewriting the matter around it! WE HAVE TO GET OUT!"

    ## blast scene transition
    scene bg_lab_blast with flash

    pause 0.8

    ## dead silence — bass drop moment
    scene bg_lab_blast with dissolve

    verma "Das... the surface telemetry."

    das "Oh my god..."

    verma "The rift... it did not stay in the containment grid. It is expanding. Upward."

    das "Verma... what have we done?"

    verma "..."

    das "We did not open a door. We tore the {b}bottom out of the world.{/b}"

    verma "The Void... it is self-sustaining now. We cannot stop it."

    das "Millions of people. Verma — {i}millions of people.{/i}"

    verma "{i}(barely a whisper){/i} I know."

    ## ── Year 2047 title card ──────────────────────────────────────────────────

    scene black with dissolve
    pause 1.0

    show text "{size=64}{b}2047{/b}{/size}\n{size=28}{color=#888888}Twenty-one years later.{/color}{/size}" at truecenter with dissolve
    pause 3.0
    hide text with dissolve
    pause 0.4

    ## ── Earth destroyed ──────────────────────────────────────────────────────

    scene bg_earth_dead with dissolve
    pause 0.5

    "Year 2047. Earth is dying."
    "Black swirls — The Void — consume the horizon. Oceans fold into nothing. Cities vanish in silence."
    "Two billion people gone. The rest watch the sky and wait."

    ## ── ISRO lab — last hope ─────────────────────────────────────────────────

    scene bg_isro_lab with dissolve
    pause 0.3

    show astro_arjun at left  with dissolve
    show astro_meera at right with dissolve

    m "The wormhole above the stratosphere — scientists believe it is the rift's origin point. If we go through, if we find the source..."

    ar "We shut it down. Or we die trying. Either way, Earth gets one last shot."

    m "The Vikram is ready. India built her in four years — the fastest spacecraft ever made. She will hold."

    ar "She had better. I have a daughter back in Chennai.\n{i}(grins){/i} She made me promise to bring her back a piece of the void."

    m "{i}(soft laugh){/i} Tell her I will wrap it in a saree."

    ar "She would love that."

    ## ── Launch from Sriharikota ───────────────────────────────────────────────

    scene bg_isro_rocket with flash_black
    pause 0.5

    show astro_arjun at left  with dissolve
    show astro_meera at right with dissolve

    "Sriharikota Launch Centre. T-minus sixty seconds."
    "The ground shakes. Three thousand people stand in silence at the perimeter fence."
    "No cheering. Everyone knows this is goodbye — one way or another."

    m "Arjun. Farewell message recorded?"

    ar "Short one. Told my daughter the stars looked like her mother's eyes. Cried like an idiot for ten minutes after."

    m "Mine took four attempts. I kept apologising."

    ar "Do not apologise. We chose this."

    m "Systems green across the board. Vikram — go for launch."

    "T-minus ten. Nine. Eight."
    "The rocket breathes fire into the earth."
    "Seven. Six. Five."

    ar "For Earth."

    m "For everyone."

    "Ignition."

    ## ── Wormhole entry ───────────────────────────────────────────────────────

    scene black with flash
    pause 0.2

    scene bg_isro_rocket with dissolve
    pause 0.3

    "The Vikram punches through the upper atmosphere. The wormhole yawns open — vast, violet, alive."
    "It does not look like science. It looks like a mouth."

    ar "Captain — hull stress at 60%%. 70%%. Radiation spiking—"

    m "Hold course."

    ar "80%%. 85%%—"

    m "{b}Hold course, Arjun.{/b}"

    "The ship enters the wormhole."
    "Time becomes a texture. Space folds like paper."
    "Stars smear into ribbons. Arjun's voice stretches and slows."

    ar "{i}Capt— we are— losing— com—{/i}"

    scene black with dissolve
    pause 1.5

    "Silence."
    "Complete, impossible silence."
    "Then — a frequency. Something that is not sound but arrives like it."

    ## ── Anika's voice ────────────────────────────────────────────────────────

    show astro_meera at center with dissolve

    a "Meera... I am alive. The ship is trapped but stable. Something happened... the particles... we are entangled now."

    m "Anika? That is impossible — your pod was pulled into the event horizon—"

    a "I know what it looks like from your side. From mine... I can see it all. Past, future, the other side. I can see {b}why the Void started.{/b}"

    m "Anika, nobody else can hear you. Where are you? What do you mean you can see—"

    a "Listen to me. We do not have much time before the signal degrades. 2026, Meera. A lab. Two scientists and their hubris."

    a "The Void did not come from nowhere. {i}We made it.{/i} Humans made it. And you — only you — can go back and stop it."

    m "Go {b}back?{/b}"

    a "The wormhole is not just a rift in space. It is a rift in {i}time.{/i} The Vikram is stuck — but you are not. Listen to me carefully."

    menu:
        "I trust you. Tell me what to do.":
            m "Anika — I trust you. Tell me everything."
            $ trust_anika += 5
            a "Then listen. The Shunya Lab, Bengaluru. Find Dr. Das — the younger one. He already has doubts. You just need to give him the courage to act on them."

        "I need a scientific explanation first.":
            m "Anika — how is this possible? None of this makes sense."
            a "I know. It does not obey the physics we were taught. But you are inside a quantum rift, Meera. You {i}are{/i} the physics now. Trust the signal."
            $ entanglement_stability -= 5

    jump act_1_wormhole

## ─── Continuation labels (carried over) ────────────────────────────────────

label act_1_wormhole:
    scene black with dissolve
    "Darkness. Silence. Then..."
    v "Meera... can you... hear me?"
    m "Anika? Is that you? We saw your pod get sucked into the event horizon!"
    show astro_meera at center with dissolve
    a "I am here, Meera. But I am... everywhere else, too. I see the threads of time. I see the end of our world."

    menu:
        "Trust the voice immediately.":
            m "Anika, tell me what to do. I trust you."
            $ trust_anika += 5
            a "Then listen. The Vikram is stuck, but we can use the entanglement. You must go back."
        "Demand a scientific explanation.":
            m "How is this possible? Priya, are you hearing this?"
            a "Priya cannot hear me, Meera. Only you. Our particles are linked. We are two sides of the same coin now."
            $ entanglement_stability -= 5

    jump act_2_guidance

label act_2_guidance:
    scene bg_isro_lab
    "The crew is frantic, but Meera stands still, listening to the ghost in her ear."
    a "Meera, in ten seconds, a debris cloud will hit the port side. Tell Arjun to bank right. Now."

    menu:
        "Command Arjun to bank right.":
            m "Arjun! Hard right, now!"
            ar "What? There is nothing on the—"
            "A massive chunk of frozen time slams past where the ship just was."
            ar "How did you...?"
            $ trust_anika += 2
        "Wait for Priya's scan.":
            m "Priya, scan for debris!"
            p "Scanning... wait, there is—!"
            "The ship jolts violently as debris clips the wing."
            $ entanglement_stability -= 10
            a "You have to listen to me, Meera. Logic will not save us here."

    jump act_3_past_world

label act_3_past_world:
    scene bg_lab with dissolve
    "Meera steps out of the landing craft. The air smells of rain and coal smoke — Bengaluru, 2026."
    a "You are at the Shunya Lab. Das is inside. He already suspects something is wrong. You just need to be the voice he listens to."
    m "And if I fail?"
    a "Then nothing changes. And everything ends."
    m "I am at the door. Anika... what if I fail?"

    if trust_anika > 10 and entanglement_stability > 40:
        jump ending_true
    elif trust_anika < 5:
        jump ending_bad
    else:
        jump ending_bittersweet

label ending_true:
    "Meera convinces Das to pull the override before the field fractures."
    "The rift never forms. The Void never grows."
    "In 2047 — the sky clears. Slowly. Then all at once."
    a "We did it, Meera. I can feel the tether pulling me back."
    "One particle. Two worlds. Both saved."
    return

label ending_bittersweet:
    "Das hesitates too long. The rift forms — but smaller. Containable."
    "The Void in 2047 slows. Stops. Does not heal, but does not grow."
    a "It is not perfect. But the world survives, Meera. That is enough."
    return

label ending_bad:
    "The confrontation goes wrong. The lab explodes."
    "The entanglement snaps."
    a "Meera? I cannot... see... anything..."
    "The Void consumes everything."
    return
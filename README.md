# VOID (Visual Novel)

VOID is a sci-fi visual novel built on the Ren'Py engine. It explores themes of quantum causality, fragmented timelines, and the profound consequences of human ambition pushed beyond theoretical limits.

## Narrative Overview
Set within a classified ISRO quantum research facility in 2026, the story follows Dr. Verma and Dr. Das during the activation of the "Shunya Core". When the experiment breaches the boundaries of physics, causality shatters, tearing a permanent rift into space-time. The resulting narrative is highly branching, following an astronaut's perilous journey through the anomaly and the harrowing decisions left to the survivors on Earth.

## Core Features
- Canonical Branching Storyline: A meticulously crafted script with high stakes, multiple dialogue paths, and severe consequences for failure.
- Cinematic Asset Integration: Heavy utilization of scalable, fullscreen WebM video cutscenes, immersive orbital audio loops, and environmental sound design. 
- Custom UI/UX Design: A completely overhauled monochromatic Ren'Py interface, featuring specialized quick menus and choice screens designed for a minimalist, modern aesthetic.

## "Infinite Outcomes" Generative AI Mode
In addition to the standard canonical script, VOID features an isolated, experimental subsystem called Infinite Outcomes. 

This mode is an advanced integration that connects the Ren'Py visual framework directly to a local Large Language Model. The Python codebase parses the AI's textual outputs and directly interfaces them into the visual novel's standard dialogue boxes and character sprites. By inputting custom text instructions, players can interact with Dr. Verma and Dr. Das to shape a completely unscripted, endless visual novel sandbox.

## Requirements and Installation

### Base Game Setup
1. Download or clone this repository.
2. Install the Ren'Py SDK (version 8.5+ recommended).
3. Select the project directory from the Ren'Py launcher and execute the game.

### AI Integration Requirements
To utilize the Infinite Outcomes feature, the host machine must run a local inference node.
1. Install Ollama on your machine.
2. Download the Llama 3.2 model via terminal by running: `ollama pull llama3.2`
3. Ensure the Ollama server is active and running locally on port 11434 prior to clicking the feature in the visual novel main menu.
4. The custom Python layer (`ai_interface.rpy`) handles all API requests natively.

## Code Architecture
- `script.rpy`: Contains the primary branching narrative, variable tracking structures, and audio/video pipeline declarations.
- `screens.rpy`: Contains the custom aesthetic modifications to the UI, including a modified scrollable viewport designed to dynamically handle massive blocks of LLM-generated text.
- `homescreen.rpy`: Provides the structural UI logic for the specialized main menu and entry points.
- `ai_interface.rpy`: The pure Python networking layer built to handle formatted API POST requests to the local Ollama instance and parse the data arrays back into the Ren'Py dialogue format.

## Licensing
This project is open-source. It serves as a demonstration of bridging advanced generative AI networking capabilities directly into interactive, static game engines.

Made by team Autistic for MMCOE Hackathon 2026
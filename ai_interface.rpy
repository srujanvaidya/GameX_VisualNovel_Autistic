init python:
    import requests
    import json

    def get_structured_llama_dialogue(prompt):
        """
        Sends a POST request to Llama 3.2 forcing a strict speaker parsing format.
        Returns a tuple of (Speaker_Name, Dialogue_Text)
        """
        url = "http://localhost:11434/api/generate"
        
        system_prompt = (
            "You are writing a sci-fi visual novel. You must output EXACTLY ONE line. "
            "You MUST format your response EXACTLY like this: [SPEAKER]|||[TEXT] "
            "where [SPEAKER] can ONLY be VERMA, DAS, or NARRATOR. "
            "[TEXT] is the spoken dialogue or narrative action. "
            "Example: VERMA|||The quantum core is destabilizing!"
        )
        
        payload = {
            "model": "llama3.2",
            "prompt": system_prompt + "\n\n" + prompt,
            "stream": False
        }
        
        try:
            response = requests.post(url, json=payload, timeout=45)
            if response.status_code == 200:
                raw_text = response.json().get("response", "NARRATOR|||Error: Empty response").strip()
                
                # Parse the strict format
                if "|||" in raw_text:
                    speaker, text = raw_text.split("|||", 1)
                    return speaker.strip().upper(), text.strip()
                else:
                    return "NARRATOR", raw_text
            else:
                return "NARRATOR", f"Error: Ollama returned HTTP {response.status_code}"
                
        except requests.exceptions.ConnectionError:
            return "NARRATOR", "CRITICAL ERROR: Could not connect. Please ensure Ollama is running on port 11434."
        except Exception as e:
            return "NARRATOR", f"Error communicating with AI: {str(e)}"

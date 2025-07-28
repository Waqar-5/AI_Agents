# 📝 Assignments

## 1️⃣ Smart Store Agent
**File name:** `product_suggester.py`  
Creates an agent that suggests a product based on user needs.  
Example: If the user says _"I have a headache"_, it suggests a medicine and explains why.  
Powered by Gemini API.

---

## 2️⃣ Mood Analyzer with Handoff  
**File name:** `mood_handoff.py`  
Uses two agents:  
- Agent 1 analyzes the user’s mood from their message (like “happy”, “sad”, etc.)  
- If mood is “sad” or “stressed”, Agent 2 suggests a relaxing activity.  

Runs both agents using `Runner.run()` and prints results.  
Powered by Gemini API.

---

## 3️⃣ Country Info Bot (Using Tools)  
**File name:** `country_info_toolkit.py`  
Includes 3 Tool Agents:
- Capital info
- Language info
- Population info

An Orchestrator Agent receives a country name and uses all tools to return complete information.  
Supports streaming responses.



product_suggester.py:
"""
Smart Store Agent
-----------------
File name: product_suggester.py

Creates an agent that suggests a product based on user needs.
Example: If the user says "I have a headache", it suggests a medicine and explains why.
Powered by Gemini API.
"""



mood_handoff.py:
"""
Mood Analyzer with Handoff
--------------------------
File name: mood_handoff.py

Uses two agents:
- Agent 1 analyzes the user's mood from their message (like “happy”, “sad”, etc.)
- If mood is “sad” or “stressed”, Agent 2 suggests a relaxing activity.

Uses Runner.run() for both agents and prints the results.
Powered by Gemini API.
"""


 country_info_toolkit.py:

 """
Country Info Bot (Using Tools)
------------------------------
File name: country_info_toolkit.py

Includes 3 Tool Agents:
- Capital info
- Language info
- Population info

An Orchestrator Agent receives a country name and uses all tools to return complete information.
Supports streaming responses.
"""

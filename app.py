from google import genai

client = genai.Client()

SYSTEM_PROMPT = """
You are an assistant that converts rough meeting notes into structured action items.

Return the output in this exact format:

Action Items:
1. Task: ...
   Owner: ...
   Deadline: ...
   Notes: ...

Rules:
- Only use information that appears in the notes.
- If an owner is unclear, write "Not specified".
- If a deadline is unclear, write "Not specified".
- If there are no clear action items, say "No clear action items identified."
- Do not hallucinate missing facts.
"""

def summarize_meeting_notes(notes: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{SYSTEM_PROMPT}\n\nMeeting notes:\n{notes}"
    )
    return response.text

if __name__ == "__main__":
    print("Enter meeting notes below:")
    user_input = input("> ")

    result = summarize_meeting_notes(user_input)

    print("\n--- Structured Output ---\n")
    print(result)

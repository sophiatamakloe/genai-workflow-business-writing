# prompts.md

## Initial Prompt
Convert the following meeting notes into action items.

## Revision 1
Convert the following meeting notes into structured action items.  
For each action item, include:
- Task
- Owner
- Deadline

## Final Prompt
Convert the following meeting notes into structured action items.

Return the output in this exact format for each action item:
- Task:
- Owner:
- Deadline:
- Notes:

Rules:
- Use only information explicitly found in the notes
- If the owner or deadline is unclear, write "Not specified"
- Do not invent missing details
- If there are no clear action items, say "No clear action items found"

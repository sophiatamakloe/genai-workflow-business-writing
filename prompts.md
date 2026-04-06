# prompts.md

## Initial Version
Convert the following meeting notes into action items.

## Revision 1
Convert the following meeting notes into structured action items.

For each action item, include:
- Task
- Owner
- Deadline

If a field is not mentioned, write "Not specified."

## Revision 2
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

## What Changed and Why
The initial version was very short and did not define a clear output format.  
Revision 1 added structure by specifying the fields that should be returned.  
Revision 2 improved reliability by adding an exact format and explicit rules to avoid hallucinating owners, deadlines, or tasks.

## What Improved, Stayed the Same, or Got Worse
The output became more consistent, easier to evaluate, and safer in ambiguous cases.  
The main improvement was that the model handled missing information more honestly instead of guessing.  
One tradeoff is that the final version is more rigid and less natural-sounding, but that is acceptable because the goal is a clear business workflow rather than conversational style.

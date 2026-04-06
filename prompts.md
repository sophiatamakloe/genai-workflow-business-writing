# report.md

## Workflow Summary
This project automates the task of turning rough meeting notes into structured action items.  
The workflow is useful because many business teams take messy notes during meetings and then spend extra time manually organizing next steps afterward.  
This prototype helps reduce that friction by extracting tasks, owners, and deadlines into a clean format.

## Why This Workflow Matters
This workflow is valuable because it saves time, improves clarity, and reduces the chance that important follow-up items are forgotten.  
It is especially useful for project managers, business analysts, startup teams, and team leads who regularly work with notes, planning, and execution.  
Instead of rewriting notes manually, the user can quickly turn raw text into a usable summary.

## Prototype Overview
The prototype was built using Python and the Google Gemini API.  
The system accepts plain text meeting notes as input and returns structured action items as output.  
The prototype runs in the terminal and demonstrates a realistic GenAI workflow that could later be expanded into a web or internal business tool.

## Prompting Iteration Process
The prompt went through multiple versions to improve consistency and reliability.

### Initial Version
The first prompt was very simple:
> Convert the following meeting notes into action items.

This worked in basic cases, but it often produced inconsistent formatting and sometimes omitted useful fields.

### Revision 1
The second version added more structure by asking for:
- Task
- Owner
- Deadline

This improved consistency, but still left room for the model to guess or vary the format.

### Revision 2
The final version added:
- an exact response structure
- instructions to avoid hallucinating missing facts
- fallback behavior such as writing "Not specified"

This made the workflow much more dependable and easier to evaluate.

## Evaluation Process
The workflow was tested using five evaluation examples in `eval_set.json`.

These included:
- normal business meeting notes
- notes with missing owners or deadlines
- ambiguous action items
- a case with no clear action items

The outputs were reviewed based on whether the system:
1. identified the correct tasks,
2. assigned the right owner when available,
3. captured deadlines when available,
4. avoided inventing information.

## Key Findings
The strongest result was that the model successfully transformed rough business notes into a structured and readable summary.  
It performed especially well when the notes clearly mentioned owners and deadlines.

The biggest challenge was ambiguity.  
If notes were vague or incomplete, the model sometimes had to decide whether to leave a field blank or infer meaning from context.  
The final prompt reduced this problem by explicitly instructing the model not to hallucinate missing information.

## Strengths
- Saves time on a repetitive business task
- Produces clean, structured outputs
- Useful for real workplace workflows
- Easy to extend into a more advanced tool

## Limitations
- Depends on the quality of the input notes
- May miss nuance if the notes are too vague
- Currently runs only in the terminal
- Does not yet export to email, Slack, or task management tools

## Future Improvements
Possible next steps for this project include:
- exporting action items to email or Slack
- generating follow-up summaries automatically
- integrating with project management tools like Asana or Trello
- adding a simple web interface for non-technical users

## Conclusion
This prototype demonstrates a realistic and practical GenAI workflow for business writing.  
It shows how a large language model can turn rough, unstructured notes into a structured output that saves time and improves execution.  
Overall, the workflow is simple, useful, and highly relevant to real business operations.

# report.md

## Workflow Summary
This project automates the task of turning rough meeting notes into structured action items.  
The workflow is useful because many business teams take messy notes during meetings and then spend extra time manually organizing next steps afterward.  
This prototype helps reduce that friction by extracting tasks, owners, and deadlines into a clean format.

## Business Use Case
This workflow is designed for business teams that need to quickly turn rough meeting notes into clear next steps.  
It is especially useful for project managers, business analysts, startup teams, operations leads, and team coordinators who regularly leave meetings with incomplete or unorganized notes.  
Instead of manually reviewing meeting notes and deciding what needs to happen next, the user can use this workflow to automatically generate structured action items that are easier to review and execute.

## Why This Workflow Matters
This workflow is valuable because it saves time, improves clarity, and reduces the chance that important follow-up items are forgotten.  
It is especially useful for project managers, business analysts, startup teams, and team leads who regularly work with notes, planning, and execution.  
Instead of rewriting notes manually, the user can quickly turn raw text into a usable summary.

## Model Choice and Why
The prototype was built using Python and the Google Gemini API.  
I chose **Google Gemini** because it was easy to access through the Gemini API, integrated cleanly with Python, and performed well for structured business-writing tasks.  
It was a strong fit for converting unstructured notes into organized, readable action items.

I did not formally compare multiple models for this prototype, but Gemini was sufficient for this use case and produced reliable structured outputs after prompt iteration.  
Instead, I focused on improving reliability through prompt iteration, evaluation design, and output consistency.

## Prototype Overview
The prototype was built using Python and the Google Gemini API.  
The system accepts plain text meeting notes as input and returns structured action items as output.  
The prototype currently runs in the terminal and demonstrates a realistic GenAI workflow that could later be expanded into a web or internal business tool.

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

## Baseline vs. Final Design Comparison

### Baseline Prompt
The original baseline prompt was:
> Convert the following meeting notes into action items.

This version worked for very simple examples, but it often produced inconsistent formatting and sometimes left out important information such as owners or deadlines.  
It also made evaluation harder because the outputs were not always structured the same way.

### Final Prompt
The final version of the prompt was more explicit and structured.  
It instructed the model to return the output in a fixed format with:
- Task  
- Owner  
- Deadline  
- Notes  

It also instructed the model to:
- use only information found in the notes  
- write **"Not specified"** if a field was unclear  
- avoid hallucinating missing details  

### Improvement from Iteration
Compared to the baseline version, the final design produced outputs that were more consistent, easier to read, and easier to evaluate.  
The final prompt significantly reduced hallucinated assumptions and made the workflow more reliable for business use.

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

## Where the Prototype Still Fails or Requires Human Review
The prototype still struggles when meeting notes are highly ambiguous, incomplete, or written in shorthand.  
In these cases, the model may not always know whether a phrase is a true action item or simply part of a discussion.  
It may also miss nuance when ownership or deadlines are only implied rather than directly stated.

Because of this, the output should still be reviewed by a human before being shared or acted on in a real business environment.  
This is especially important when the notes involve important deadlines, accountability, or decisions that affect execution.

## Deployment Recommendation
I would recommend deploying this workflow **only as a draft-support tool**, not as a fully autonomous system.  
It is useful for saving time and improving note organization, but it should still be reviewed by a human before action items are finalized or distributed.

Under those conditions, I believe this workflow would be practical and valuable in real business operations.  
It is especially well-suited for internal productivity support, where speed and structure are helpful but human oversight is still available.

## Future Improvements
Possible next steps for this project include:
- exporting action items to email or Slack  
- generating follow-up summaries automatically  
- integrating with project management tools like Asana or Trello  
- adding a simple web interface for non-technical users  
- adding a confidence or review flag for uncertain outputs  

## Conclusion
This prototype demonstrates a realistic and practical GenAI workflow for business writing.  
It shows how a large language model can turn rough, unstructured notes into a structured output that saves time and improves execution.  
Overall, the workflow is simple, useful, and highly relevant to real business operations.

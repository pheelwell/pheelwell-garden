---
PromptInfo:
  author: Philip
  description: null
  id: sum_todos
  name: "\U0001F4DC summerize Todos"
dg-publish: true
title: reveal_todos

---




I am running a Dungeons and Dragons Adventure 

Prompt to extract Party ToDos from:
{{selection}}

Task:
Extract all necessary Todos from the Party  
The summary should follow this format (including the brackets):

- [ ] Find out that [[{{title}}\|{{title}}]] is XXX
- [ ] Find out about the connection of [[{{title}}\|{{title}}]] to XXXX
- [ ] etc...


Keep the Todos to a minimum for the party to lift all misterys.
If possible oder them by importance.
Don't add unimportant or known lore information, just keep the secrets. 

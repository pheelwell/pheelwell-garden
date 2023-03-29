---
PromptInfo:
  author: Philip
  description: null
  id: rewrite
  name: "\U0001F9D9\U0001F3FB\u200D\u2642 rewrite paragraph"
dg-publish: true
title: rewrite
type: template

---





# Task
rewrite the given section in the style of J. R. R. Tolkien
# Facts to consider
The following CAN be included if context misses, but just should give some guidance on how characters or places feel and behave.  
{{#each children}}
{{this.context}}
{{/each}}

# Prompt to rewrite
{{selection}}

# Rewritten prompt

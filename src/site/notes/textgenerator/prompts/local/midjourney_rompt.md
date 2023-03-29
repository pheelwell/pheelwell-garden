---
PromptInfo:
  author: Philip
  description: null
  id: midjourney_prompt
  name: "\U0001F5BC\uFE0F generate midjourney prompt"
dg-publish: true
title: midjourney_rompt

---





Generate a Picture with Midjourney with the given context:
Additional information for Context
(DONT INCLUDE INTO PROMPT! THIS IS JUST CONTEXT!):
{{title}} ({{type}}): 
{{#each sum}}
-  {{this}}
{{/each}}
{{#each children}}
{{this.basename}}:
{{#each frontmatter.sum}}
-  {{this}}
{{/each}}

{{/each}}

The above text is just lore information, use it for context on how characters or environments  could look or feel like in the picture, but don't reiterate the bullet points.
Instructions:
- Write a literal image description on what to depict. 
- Don't use any terms or names that are not common knowlege to someone not affiliated with the lore would know. 
- No names, just describe how it looks assuming the viewer doesn't know the name.
- Don't explain, just describe
- Don't include everything, just depict a single scene or concept
- Keep it short, ca 20 words

For example:
Wrong:
Painting of Ransden holding a torch infront of Herbstbog
Right: 
Painting of a undead librarian in purple robes holding a torch Infront of a magical city with white walls and brass rounded roofs 

Scenario to depict:
{{selection}}

Literal Image description (describe scene without mentioning names or lore):


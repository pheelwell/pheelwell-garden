---
PromptInfo:
  author: Philip
  description: null
  id: find_summary_tags
  name: "\U0001F4DC summerize facts"
dg-publish: true
title: summerize_facts

---





Prompt to extract facts from:
{{selection}}

Task:
summarize the given document into a obsidian frontmatter to be used as context for other text genreations.
The summary should follow this format (including the --) : 

"type" can be one of : Region, Settlement, Locality, NPC, SideNPC, Faction, History, Arc,Plot, Scene,Thing

--
type: string
sum:
  - fact 1 
  - fact 2
  - fact 4
--

The facts should include all important information of the Document. leave out unnecessary details or flavor

summerized facts in condensed bulletpoints:
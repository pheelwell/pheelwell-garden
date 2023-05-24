---
{"dg-publish":true,"permalink":"/skoria/meta/note-structure-guidelines/","noteIcon":"Meta","created":"2023-05-19T20:38:31.632+02:00","updated":"2023-05-21T18:28:28.394+02:00"}
---

# Folder Structure
Obsidian notes in this Repo are structured this way:

```
├── Meta
├── Bestiary
│   └── Subclasses
├── Adventuring
│   ├── [Adventure Name]
│   │   ├── Journal
│   │   └── Other Things Related to the Campain
│   └── ...
└── Worldbuilding
    ├── Global
    │   ├── Concepts
    │   ├── Factions
    │   └── Things
    └── [Plane Name]
        ├── [Region Name]
	 │   ├── Factions
	 │   │   ├── [Faction Name]
	 │   │   │   ├── [Faction Name] (Main Article)
	 │   │   │   ├── [Person from Faction]
	 │   │   │   └── ...
	 │   ├── Regions
	 │   │   ├── [Region Name]
	 │   │   │   ├── [Region Name] (Main Article)
	 │   │   │   ├── [Location in Region]
	 │   │   │   └── ...
	 │   └── Things
	 │       └── [Thing]
	 └── ...
```

# Frontmatter
Frontmatter helps with the organization and categorization of notes. It should be included at the beginning of each note and follow this general structure:

```yaml
---
aliases: [alternative name, abbreviation]
tags: [tag1, tag2]
type: Region/Settlement, Locality, NPC, SideNPC, Faction, History, Arc, Plot, Scene, Thing, Deity
sum:
- summery of the note in bullet points for refference in gpt templates
- can have multiple bullet points or just one
dg-publish: true/false
owner: your alias
status: seed/sprout/tree/willow
---

Note content goes here.

```

- `aliases`: Alternative names or abbreviations for the note, if applicable.
- `tags`: Keywords that describe the content of the note or its category, which help in organizing and searching for related notes.
- `type`: The general category of the note, such as Region, Settlement, NPC, Faction, etc. This helps in filtering and organizing notes. This is used for the little icons on the website
- `sum`: A brief summary of the note's content in bullet points. These summaries can be used for quick reference or when generating templates with GPT-3.
- `dg-publish`: Indicates whether the note should be published (true) or kept private (false).
- owner`: Specifies the alias of the person who created or owns the note. This helps in attributing credit and maintaining ownership of notes.

- `status`: Indicates the level of completion or development of the note. The categories are:
  - `seed`: A basic idea or concept that needs further development. This topic is up for grabs.
  - `sprout`: A developed concept with some fleshed-out details. Talk to the owner before working on it.
  - `tree`: A fully developed and detailed note, that is deeply rooted into your campain, many secrets exist under the surface.
  - `willow`: a deprecated note that needs trimming or is outdated.

# Formatting
It is a good idea to follow this guideline for writing notes:

- Start with a flavor Text
- Use h1 for chapters- Use h2 for sub-chapters or sections within a chapter
- Use h3 for sub-sections within a section
- Use bullet points or numbered lists for organizing information and details
- Use bold and italic text to emphasize important points or keywords
- Include relevant links to other notes or external sources when necessary
- Break down long paragraphs into smaller, more digestible chunks of text

Example Formatting can be found at [[🌐Skoria/Meta/Example Site\|Example Site]]

# Images and Media

When including Images, include them INSIDE the Repo, otherwise they won't be synced. Please only use selfmade Images that you hold copyright to.
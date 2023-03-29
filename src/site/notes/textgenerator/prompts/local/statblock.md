---
PromptInfo:
  author: Philip
  description: Generates a 5e DnD Statblock given the Description
  id: statblock
  name: "\U0001F409 generate a statblock"
dg-publish: true
title: statblock

---






Goal of this Doc is to build a statblock given the following specification:

# Context: 
This is some information that could be used:
{{#each children}}
{{this.context}}
{{/each}}

# Lore and Combat Mechanics:
{{selection}}

# Format Specification
This is an example 5e statblock, all monsters must obide that yaml format:
```statblock
name: string
size: string
type: string
subtype: string
alignment: string
ac: number
hp: number
hit_dice: string
speed: string
stats: [number, number, number, number, number, number]
saves:
  - <ability-score>: number
skillsaves:
  - <skill-name>: number
damage_vulnerabilities: string
damage_resistances: string
damage_immunities: string
condition_immunities: string
senses: string
languages: string
cr: number
spells:
  - <description>
  - <spell level>: <spell-list>
traits:
  - name: <trait-name>
    desc: <trait-description>
  - ...
actions:
  - name: <trait-name>
    desc: <trait-description>
  - ...
legendary_actions:
  - name: <legendary_actions-name>
    desc: <legendary_actions-description>
  - ...
bonus_actions:
  - name: <trait-name>
    desc: <trait-description>
  - ...
reactions:
  - name: <reaction-name>
    desc: <reaction-description>
  - ...
```

# Statblock for {{title}} 
This is the yaml statblock that includes all given requirements:

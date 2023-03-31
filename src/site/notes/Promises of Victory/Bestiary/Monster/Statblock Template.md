---
{"dg-publish":true,"permalink":"/promises-of-victory/bestiary/monster/statblock-template/","title":"Statblock Template","noteIcon":"Meta","created":"2023-01-25T02:26:54.326+01:00","updated":"2023-03-29T22:31:59.669+02:00"}
---

# Statblock Template:

```statblock
image: [[Wikilink To Image]]
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

# Example Statblock for Magic Guard:
```statblock
name: Magic Guard
size: medium
type: humanoid
subtype: any race
alignment: any alignment
ac: 18 (Magical Armor)
hp: 35 (10d8)
hit_dice: 10d8
speed: 30 ft.
stats: [14, 16, 13, 13, 11, 9]
saves:
  - Perception :5
  - Insight :5
damage_immunities: charm;sleep-by-magic
senses: darkvision 60 ft., passive Perception 15
languages: Common, Elvish, Dwarvish 
cr: 2 (450 XP) 
traits:
  - name : Magical Guard
    desc : "The guard cannot be charmed and it is immune to being put tosleep by magic."
actions :
 - name : "Multiattack"
   desc : "The guard makes two attacks with its spear."   
 - name : "Shock Spear"   
   desc : "*Melee or Ranged Weapon Attack* +4 to hit, reach 5 ft. or range 20 ft., one target. *Hit* 8 (1d8 + 4) piercing damage and the target must make a DC 12  Constitution saving throw, taking 5 (2d4) lightning damage on a failed save, or half as much damage on a successful one." 

 - name : Shield Bash
   desc : "*Melee* Weapon Assault_ +4 to hit, range 5 ft., one goal. *Hit* 5 (1d6 + 2) bludgeoning damage."

 - name : Healing Potion
   desc : The guard has 1d4+1 healing potions which can cure any ailment. The guard can only use 1(one) each day.
```
# Example Statblock for Herstbog Mage:
```statblock name: Herstbog Mage
size: medium
type: humanoid
subtype: any race 
alignment: chaos or evil alignment 
ac: 16 (Spell Mail)
hp: 40 (9d8)
hit_dice: 9d8
speed: 30 ft. 
stats: [9, 14, 11, 17, 12, 9] 
saves: 
  - Arcana : 8  
  - Insight : 5 
damage_immunities: charm;sleep-by-magic  
senses : darkvision 60 ft., passive Perception 15  
languages : Common, Elvish, Dwarvish  
cr : 4 (1,100 XP)  
traits :   
  - name : Mage   
    desc : "The mage cannot be charmed and it is immune to being put to sleep by magic." 

actions :   

 - name : Multiattack   
   desc : "The mage makes two attacks with its staff."  

 - name : Fireball   
   desc : "*Ranged Spell Attack* +8 to hit, range 150 ft., one target. *Hit*  21 (6d6) fire damage." 

 - name : Frostbite   
   desc : "*Ranged Spell Attack* +8 to hit, reach 120 ft., one target. *Hit* 18 (4d8) cold damage, and the target's speed is reduced by 10 feet until the end of the mage's next turn."

 - name : Sleep   
   desc : "*Ranged Spell Attack* +8 to hit, range 90 ft., one target. *Hit* The target falls asleep and is unconscious for 1 minute. The target wakes up if it takes damage, if another creature takes an action to wake it up, or if 1 minute has passed." 

 - name : Shield   
   desc : "*Ranged Spell Attack* +8 to hit, range 30 ft., one target. *Hit* The target has a magical barrier surrounding it for 1 minute that grants it a +5 bonus to AC and immunity to fire damage."

 - name : Mage Armor   
   desc : "*Ranged Spell Attack* +8 to hit, range 30 ft., one target. *Hit* The target has a magical barrier surrounding it for 1 minute that grants it a + 3 bonus to AC."
```

based on [[Promises of Victory/Bestiary/Monster/Statblock Template\|Statblock Template]]

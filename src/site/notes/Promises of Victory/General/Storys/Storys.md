---
{"dg-publish":true,"permalink":"/promises-of-victory/general/storys/storys/","title":"Storys","noteIcon":"Meta","created":"","updated":""}
---



- [[Promises of Victory/General/Storys/Artifact of Chaos\|Artifact of Chaos]]
- [[Promises of Victory/General/Storys/Artifact of Life\|Artifact of Life]]
- [[Promises of Victory/General/Storys/Artifact of Light\|Artifact of Light]]
- [[Promises of Victory/General/Storys/Final Sacrifice\|Final Sacrifice]]
- [[Promises of Victory/General/Storys/Souls of the Dead\|Souls of the Dead]]
- [[Promises of Victory/General/Storys/Titan Forges\|Titan Forges]]


This is BS and outdated ...
```mermaid
graph TD
Start

Start --> Witch_Fight[Player fights the Witch]
Start --> Bwomsamdi[Player find Nosem]
Start --> Death_Energy

Witch_Fight -.-> UNKNOWN[Players find that the Witch channels Energy into Ritual] 


subgraph Adventure_hook_dragons
  Start --> Tavern
  Tavern --> Sturmklau[player gets a quest to hunt a dragon]
  Sturmklau --> Sturmklau_Attack[druid City of Sturmklau gets attacked by the Shaddowhammer Clan]
end

subgraph Life_Artefact
  Forge_of_Life[the player brings the artifact to the forge of life]
  Player_Run_With_artifact[to save the artifact the druids give the artifact to the player]
  Sturmklau -->|time passes| Sturmklau_Attack
  Sturmklau_Attack -->|player fight through the city and reach the artifact| Player_Run_With_artifact
  Player_Run_With_artifact -->|"Players get a fake help call from the Druids"| Forge_of_Life
end


subgraph Jamoke
  Prince_Reveal[Player find out that the player Jamoke is a Prince]
  Dream_Sequence[Player gets Gem of the Dreamer]
  Build_Chain[Player builds the chain to find the Sister]

  Prince_Reveal --> |triggered| Dream_Sequence
  Dream_Sequence --> |Players find a smith that can build the chain| Build_Chain
end


subgraph Chaos_Artefact
    Start --> Player_Has_Chaos_Artefact[Player gets artifact at beginning of game]
    Doctor_Phalandos_Office_raided[Player find Mad Doctor dead & fight Shaddowhammer General]
    Forge_of_Chaos[Player brings artifact to forge of chaos]

    Player_Has_Chaos_Artefact -->|Should be Brought there for Safekeeping| Doctor_Phalandos_Office_raided
    Doctor_Phalandos_Office_raided  -->|Fake Notes to stop Ritual and Bind Chain| Forge_of_Chaos
    Build_Chain --> |look at chain in falk| Forge_of_Chaos
end


Player_Has_Chaos_Artefact

subgraph Light_Artefact
    Herbstbog[Player unveil corruption]
    Düsternest[Player fight the Witch]
    Lichtachte_Cathedral[Player rob Cathedral for Artifact]
    Archaelogy_Site[Player find arcane device]

    Herbstbog -->|Player find Notes| Archaelogy_Site
    Forge_of_Light[Player race to Forge with Volair, fight him, tells his Truth]
    Düsternest --> Lichtachte_Cathedral
    Lichtachte_Cathedral --> Forge_of_Light
    Archaelogy_Site --> Forge_of_Light
end

subgraph Death_Energy
  
end

Forge_of_Life --> Final_Sacrifice

Forge_of_Chaos --> Final_Sacrifice

Forge_of_Light --> Final_Sacrifice

Death_Energy --> Final_Sacrifice

subgraph Final_Sacrifice
    
  Below_Edschmied[Bomb goes down]
  Final_fight_Narun[Player fights Narun]

end

```

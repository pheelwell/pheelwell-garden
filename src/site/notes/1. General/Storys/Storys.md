---
dg-publish: true
title: Storys
type: Meta

---






- [[1. General/Storys/Artifact of Chaos\|Artifact of Chaos]]
- [[1. General/Storys/Artifact of Life\|Artifact of Life]]
- [[1. General/Storys/Artifact of Light\|Artifact of Light]]
- [[1. General/Storys/Final Sacrifice\|Final Sacrifice]]
- [[1. General/Storys/Souls of the Dead\|Souls of the Dead]]
- [[1. General/Storys/Titan Forges\|Titan Forges]]



```plantuml

Witch_Fight: Player fights the Witch
Bwomsamdi: Player find Nosem

Witch_Fight -d-> UNKNOWN : "Players find that the Witch channels Energy into Ritual (witch memories)"

[*] -d-> Death_Energy

state Adventure_hook_dragons{
    Tavern -d-> Sturmklau: player gets a quest to hunt a dragon
}

[*] -d-> Tavern

state Life_Artefact{
    Sturmklau_Attack : druid City of Sturmklau gets attacked by the Shaddowhammer Clan
    Forge_of_Life : the player brings the artifact to the forge of life
    Player_Run_With_artifact : to save the artifact the druids give the artifact to the player

    Sturmklau -d-> Sturmklau_Attack: time passes
    Sturmklau_Attack -d-> Player_Run_With_artifact : player fight through the city and reach the artifact
    Player_Run_With_artifact -d-> Forge_of_Life: Players get a fake help call from the Druids
}

state Jamoke{
    Prince_Reveal: Player find out that the player Jamoke is a Prince
    Dream_Sequence: Player gets Gem of the Dreamer
    Build_Chain: Player builds the chain to find the Sister

    Prince_Reveal -d-> Dream_Sequence: triggered
    Dream_Sequence -d-> Build_Chain: Players find a smith that can build the chain
}

state Chaos_Artefact{
    Doctor_Phalandos_Office_raided : Player find the Mad Doctor dead and fight a Shaddowhammer General
    Forge_of_Chaos : Player brings the artifact to the forge of chaos
    Player_Has_Chaos_Artefact : Player gets the artifact at the beginning of the game

    Player_Has_Chaos_Artefact -d-> Doctor_Phalandos_Office_raided: Should be Brought there for Safekeeping
    Doctor_Phalandos_Office_raided  -d-> Forge_of_Chaos: Fake Notes to stop Ritual and "bind chain"
    Build_Chain -d-> Forge_of_Chaos: look at chain in falk
}
[*] -d-> Player_Has_Chaos_Artefact

state Light_Artefact{
    Herbstbog: Player unveil corruption
    Düsternest: Player fight the Witch
    Lichtachte_Cathedral: Player rob the Cathedral for Artifact
    Archaelogy_Site: Player find the arcane device

    Herbstbog -d-> Archaelogy_Site: Player find Notes
    Forge_of_Light: Player race to Forge with Volair, fight him, tells his Truth
    Düsternest -d-> Lichtachte_Cathedral
    Lichtachte_Cathedral -d-> Forge_of_Light
    Archaelogy_Site -d-> Forge_of_Light
}

state Death_Energy{

    

}

Forge_of_Life -d-> Final_Sacrifice
Forge_of_Chaos -d-> Final_Sacrifice
Forge_of_Light -d-> Final_Sacrifice
Death_Energy -d-> Final_Sacrifice

state Final_Sacrifice{


    Below_[[2. Worldbuilding/2. Regions/🏰Edschmied/Edschmied\|Edschmied]]: Bomb goes down
    Final_fight_Narun: Player fights Narun
}


```


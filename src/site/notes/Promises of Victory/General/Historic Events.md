---
{"dg-publish":true,"permalink":"/promises-of-victory/general/historic-events/","title":"Historic Events","noteIcon":"History","created":"2023-01-25T02:26:52.759+01:00","updated":"2023-03-30T12:51:09.956+02:00"}
---


``` dataviewjs
//CONFIG
const path = '"1. General/Historic Events"'
const title = "Historic Events"

//FUNCTIONS
function genMermaidLine(page, begin, end) {
    return ;
}

function checkfrontmatter(page){
    if (typeof page.gantt != "undefined")
    {
        if (typeof page.gantt.begin != "undefined" && typeof page.gantt.end != "undefined")
        {
            return true;
        }
        if (typeof page.gantt.milestone != "undefined")
        {
            return true;
        }
    }
    return false;
}

function loopPages(pages) {
    let mermaid = ''; 
    console.log(pages)
    pages = pages.filter(page => checkfrontmatter(page))
    console.log(pages)
    //sort pages by gantt.begin
    for (let page of pages) {
        //log to console
        console.log("Processing:"+ page.file.name)
        console.log(page)
        //check if gantt.begin and gantt.end object exists in page
        if (typeof page.gantt != "undefined"){
            if (typeof page.gantt.begin != "undefined" && typeof page.gantt.end != "undefined") {
                let identifier = page.file.name.replace(/ /g, "_");
                //create mermaid line
                mermaid += page.file.name + ' : ' + identifier + ", " + page.gantt.begin + ', ' + page.gantt.end + '\n';
                //make clickable
                mermaid += 'click ' + identifier + ' href "obsidian://open?vault=obsidian&file=' + page.file.path + '"\n';
            }
            //milestone if gantt.milestone exists
            //format:
            // A task           :milestone, identifier, 2014-01-01, 2014-01-01
            if (typeof page.gantt.milestone != "undefined") {
                console.log("milestone:"+ page.file.name)
                let identifier = page.file.name.replace(/ /g, "_");
                //create mermaid line
                mermaid += page.file.name + ' :milestone, ' + identifier + ", " + page.gantt.milestone + ', ' + page.gantt.milestone + '\n';
                //make clickable
                mermaid += 'click ' + identifier + ' href "obsidian://open?vault=obsidian&file=' + page.file.path + '"\n';
            }
        }
    }
    return mermaid;
}
//dates are not related to the actual date but a fantasy date system
//deactivate todayMarker and start with year 0


const Mermaid = `gantt
    title `+title+`
    todayMarker off
    dateFormat DD-MM-YYYY
    axisFormat %Y
    `;

const pages = dv.pages(path)
dv.paragraph('```mermaid\n' + Mermaid +loopPages(pages)+ '\n```');
```
## War History
Those are the most important facts about the War between the [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] and the [[Promises of Victory/Worldbuilding/Factions/League of Arathor/League of Arathor\|League of Arathor]]:
## Year 3014: 

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/attack-on-lichtachte/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





The initial attack on [[Promises of Victory/Worldbuilding/Regions/🏰Lichtachte/Lichtachte\|Lichtachte]] occurred in the year 3014. The attackers were a horde of zombies. The zombies overwhelmed the city's defenses, and many people were killed. To regain the casualties [[Promises of Victory/Worldbuilding/Factions/Defilers/General Malachi\|Malachi]] spread her Plague to rescue the citizens. This is what caused the great divide in [[Promises of Victory/Worldbuilding/Regions/The Basin\|The Basin]]. 
# Behind the Scenes
The Zombies were controlled by [[Promises of Victory/Worldbuilding/Factions/Unaffiliated/Naruun\|Naruun]] who instigated the attack with his last bit of power to get [[Promises of Victory/Worldbuilding/Factions/Defilers/General Malachi\|Malachi]] to use her Ritual. [[Promises of Victory/Worldbuilding/Factions/Unaffiliated/Naruun\|Naruun]], [[Promises of Victory/Worldbuilding/Factions/Defilers/General Malachi\|General Malachi]], instigate, power, Ritual



</div></div>

## Year 3015:

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/the-plague-spreads/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




[[Promises of Victory/Worldbuilding/Things/The Plague\|The Plague]] was a necrotic virus that was spread by the necromancer [[Promises of Victory/Worldbuilding/Factions/Defilers/General Malachi\|Malachi]]. It caused the recently deceased to rise from the dead as zombies with their souls still affixed to them. [[Promises of Victory/Worldbuilding/Things/The Plague\|The Plague]] caused a great divide in [[Promises of Victory/Worldbuilding/Regions/The Basin\|The Basin]], with many people seeing the undead as monsters. The [[Promises of Victory/Worldbuilding/Factions/League of Arathor/League of Arathor\|League of Arathor]] to this day sees the undead as the same monsters that killed many of their kin.
# Behind the Scenes
While Researching [[Promises of Victory/Worldbuilding/Things/The Plague\|The Plague]] [[Promises of Victory/Worldbuilding/Factions/Defilers/General Malachi\|Malachi]] was Influenced by [[Promises of Victory/Worldbuilding/Factions/Unaffiliated/Naruun\|Naruun]]. She didn't intend [[Promises of Victory/Worldbuilding/Things/The Plague\|The Plague]] to be contagious.



</div></div>

## Year 3018: 

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/the-cure/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




The Cure for [[Promises of Victory/Worldbuilding/Things/The Plague\|The Plague]] was found in the year 3018 by the [[paladin\|paladin]] [[Promises of Victory/Worldbuilding/Factions/League of Arathor/High Paladin Erathenar\|Erathenar]]. It was a complicated mixture of holy essences. The Cure was distributed to the people of [[Promises of Victory/Worldbuilding/Regions/The Basin\|The Basin]], and [[Promises of Victory/Worldbuilding/Things/The Plague\|The Plague]] was brought under control. The prevents [[Promises of Victory/Worldbuilding/Things/The Plague\|The Plague]] from going rampage, but didn't revert the already undead.

</div></div>

## Year 3023: 

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/the-founding-of-the-defilers/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




The [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] were founded in the year 3023 by the necromancer [[Promises of Victory/Worldbuilding/Factions/Defilers/General Malachi\|Malachi]]. She united her Undead breathren in the South of [[Promises of Victory/Worldbuilding/Regions/The Basin\|The Basin]] and established her territory. The Orcs of the nearby mountains soon joined her, and the [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] became a powerful force. 

</div></div>

## Year 3024: 

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/the-war-begins/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




The War began in the year 3024 when the [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] attacked multiple cities in the west of [[Promises of Victory/Worldbuilding/Regions/The Basin\|The Basin]]. The [[Promises of Victory/Worldbuilding/Factions/League of Arathor/League of Arathor\|League of Arathor]] was quick to respond, and they pushed the [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] back. The war continued for four years, with neither side gaining an advantage. 


</div></div>

## Year 3028: 

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/the-tides-turn/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




In the year 3028, the [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] conquered the Desecrated Stronghold, a key strategic location in the war. This gave them a major advantage, and they began to push the League back. The League fought bravely, but they were outnumbered. 

</div></div>

## Year 3031: 

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/the-fall-of-the-league/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




In the year 3031, the [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] conquered almost all of [[Promises of Victory/Worldbuilding/Regions/The Basin\|The Basin]]. The League was pushed back to their last stronghold, the city of [[Promises of Victory/Worldbuilding/Regions/Todo/Trollbans Hold\|Trollbans Hold]]. The [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] laid siege to the city, but the League's paladins fought bravely, and they were able to hold the city. 

</div></div>

## Year 3032: 

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/the-tide-turns-again/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




In the year 3032, the tide of the war began to turn. The [[Promises of Victory/Worldbuilding/Factions/League of Arathor/League of Arathor\|League of Arathor]] fought back, and they regained control of the Desecrated Stronghold. This gave them a major advantage, and they began to push the [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] back. 


</div></div>

## Year 3036: 

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/stalemate/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




The war continued for four more years, with neither side gaining an advantage. The [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] were unable to break through the League's defenses, and the League was unable to push the [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] back. The war reached a stalemate. 


</div></div>

## Year 3039: 

<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/promises-of-victory/worldbuilding/historic-events/war/the-defilers-attack-edschmied/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




In the year 3039, the [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] made a push to conquer [[Promises of Victory/Worldbuilding/Regions/The Basin\|The Basin]]. They attacked the city of [[Promises of Victory/Worldbuilding/Regions/🏰Edschmied/Edschmied\|Edschmied]], the League's last stronghold. The League's paladins fought bravely, but they were outnumbered and outmatched. The [[Promises of Victory/Worldbuilding/Factions/Defilers/Defilers\|Defilers]] conquered the city, and the war came to an end. 

</div></div>

![a_Cathedral_concept_art_by_Chris_Rallistrending_on_d.png](/img/user/resources/Pictures/a_Cathedral_concept_art_by_Chris_Rallistrending_on_d.png)
# Naruun Related History
While the war is going on, [[Promises of Victory/Worldbuilding/Factions/Unaffiliated/Naruun\|Naruun]] , [[Promises of Victory/Worldbuilding/Factions/Cult of the Gifted/The Cult of the Gifted\|The Cult of the Gifted]] , [[Promises of Victory/Worldbuilding/Factions/Shaddowhammer/The Shaddowhammer\|The Shaddowhammer]] and [[Promises of Victory/Worldbuilding/Factions/Unaffiliated/The Fulfiller\|The Fulfiller]] also have a History:
Ancient Events: [[Promises of Victory/Worldbuilding/Factions/Unaffiliated/Naruun\|Naruun]] was sealed away by forces of nature
Year 3012: Naruun influence rises in the Basin
Year 3024: [[Promises of Victory/Worldbuilding/Factions/Cult of the Gifted/The Cult of the Gifted\|The Cult of the Gifted]] is founded
Year 3031: [[Promises of Victory/Worldbuilding/Factions/Shaddowhammer/The Shaddowhammer\|The Shaddowhammer]] is formed by cult leader Volar
Year 3038: [[Promises of Victory/Worldbuilding/Factions/Unaffiliated/The Fulfiller\|The Fulfiller]] arrives in the Basin, spreading its influence 

# Volars History
[[Promises of Victory/Worldbuilding/Factions/Shaddowhammer/Volar\|Volar]]s History: 

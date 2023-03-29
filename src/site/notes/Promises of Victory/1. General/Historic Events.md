---
{"dg-publish":true,"permalink":"/promises-of-victory/1-general/historic-events/","title":"Historic Events","noteIcon":"History"}
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
Those are the most important facts about the War between the [[Promises of Victory/2. Worldbuilding/3. Factions/Defilers/Defilers\|Defilers]] and the [[Promises of Victory/2. Worldbuilding/3. Factions/League of Arathor/League of Arathor\|League of Arathor]]:
Year 3014: [[Promises of Victory/1. General/Historic Events/War/Attack on Lichtachte\|Attack on Lichtachte]]
Year 3015: [[Promises of Victory/1. General/Historic Events/War/The Plague spreads\|The Plague spreads]]
Year 3018: [[Promises of Victory/1. General/Historic Events/War/The Cure\|The Cure]]
Year 3023: [[Promises of Victory/1. General/Historic Events/War/The Founding of the Defilers\|The Founding of the Defilers]]
Year 3024: [[Promises of Victory/1. General/Historic Events/War/The War Begins\|The War Begins]]
Year 3028: [[Promises of Victory/1. General/Historic Events/War/The Tides Turn\|The Tides Turn]]
Year 3031: [[Promises of Victory/1. General/Historic Events/War/The Fall of the League\|The Fall of the League]]
Year 3032: [[Promises of Victory/1. General/Historic Events/War/The Tide Turns Again\|The Tide Turns Again]]
Year 3036: [[Promises of Victory/1. General/Historic Events/War/Stalemate\|Stalemate]]
Year 3039: [[Promises of Victory/1. General/Historic Events/War/The Defilers attack Edschmied\|The Defilers attack Edschmied]]

# Naruun Related History
While the war is going on, [[Promises of Victory/2. Worldbuilding/3. Factions/Naruun/Naruun\|Naruun]] , [[Promises of Victory/2. Worldbuilding/3. Factions/Cult of the Gifted/The Cult of the Gifted\|The Cult of the Gifted]] , [[Promises of Victory/2. Worldbuilding/3. Factions/Shaddowhammer/The Shaddowhammer\|The Shaddowhammer]] and [[Promises of Victory/2. Worldbuilding/3. Factions/Fulfiller/The Fulfiller\|The Fulfiller]] also have a History:
Ancient Events: [[Promises of Victory/2. Worldbuilding/3. Factions/Naruun/Naruun\|Naruun]] was sealed away by forces of nature
Year 3012: Naruun influence rises in the Basin
Year 3024: [[Promises of Victory/2. Worldbuilding/3. Factions/Cult of the Gifted/The Cult of the Gifted\|The Cult of the Gifted]] is founded
Year 3031: [[Promises of Victory/2. Worldbuilding/3. Factions/Shaddowhammer/The Shaddowhammer\|The Shaddowhammer]] is formed by cult leader Volar
Year 3038: [[Promises of Victory/2. Worldbuilding/3. Factions/Fulfiller/The Fulfiller\|The Fulfiller]] arrives in the Basin, spreading its influence 

# Volars History
[[Promises of Victory/2. Worldbuilding/3. Factions/Shaddowhammer/Volar\|Volar]]s History: 

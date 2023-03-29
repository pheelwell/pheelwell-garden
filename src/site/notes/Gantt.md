---
{"dg-publish":true,"permalink":"/gantt/","title":"Gantt"}
---






This dataviewjs snippet shows all tagged historic events as a gantt chart using mermaid
Use all notes that have gantt in their frontmatter
gantt.begin -> start date
gantt.end -> ending date
You may change the path of your project folder below

``` dataviewjs
//CONFIG
const path = '"1. General/Historic Events"'
const title = "Historic Events"
const dateFormat = "YYYY-MM-DD"


//FUNCTIONS
function genMermaidLine(page, begin, end) {
    return ;
}

function loopPages(pages) {
    let mermaid = '';
    //filter pages that have gantt.begin and gantt.end (typeof maybeObject != "undefined")

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
            if (typeof page.gantt.milestone != "undefined") {
                //make clickable
                let identifier = page.file.name.replace(/ /g, "_");
                //create mermaid milestone
                mermaid += page.file.name + ' : ' + identifier + ", " + page.gantt.milestone + ', 1d\n';
                mermaid += 'click ' + identifier + ' href "obsidian://open?vault=obsidian&file=' + page.file.path + '"\n';
            }
        }
    }
    return mermaid;
}

const Mermaid = `gantt
    title [[`+title+`]]
    dateFormat `+dateFormat+`
    section Events
    `;

const pages = dv.pages(path)
dv.paragraph('```mermaid\n' + Mermaid +loopPages(pages)+ '\n```');
```

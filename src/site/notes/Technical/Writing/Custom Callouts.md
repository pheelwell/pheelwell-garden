---
{"dg-publish":true,"permalink":"/technical/writing/custom-callouts/","noteIcon":"Technical","created":"2023-03-30T18:01:07.531+02:00","updated":"2023-04-10T13:32:00.427+02:00"}
---

#ADHD 


Documents have custom callouts that are defined in the CSS Snippets as:

>[!read] Read to the Player
>test

>[!secret]- 
> This should not be directly revealed to a player



Read more on callouts on: https://help.obsidian.md/Editing+and+formatting/Callouts

Icons are used from: https://lucide.dev/


```css
.callout[data-callout="read"] {
    --callout-color: 0, 0, 0;
    --callout-icon: lucide-alert-book-open;
}
```
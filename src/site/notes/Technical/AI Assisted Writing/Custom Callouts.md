---
{"dg-publish":true,"permalink":"/technical/ai-assisted-writing/custom-callouts/","noteIcon":"Technical","created":"2023-03-30T18:01:07.531+02:00","updated":"2023-04-10T15:19:24.736+02:00"}
---


One of the powerful features of Obsidian is its ability to customize the appearance using custom CSS snippets. In this tutorial, we will learn how to add a custom CSS snippet to Obsidian and create personalized callouts with unique icons.
The Documents of my Vault have have custom callouts that are defined in the CSS Snippets as:

>[!read] Read to the Player
>test

>[!secret]- 
> This should not be directly revealed to a player


```css
.callout[data-callout="read"] {
    --callout-color: 0, 0, 0;
    --callout-icon: lucide-alert-book-open;
}
```

# Step 1: Enable Custom CSS in Obsidian

Before we start adding custom CSS snippets, we need to enable custom CSS support in Obsidian. Follow these steps:

1. Open Obsidian.
2. Click on the Settings icon (gear) in the left sidebar.
3. In the settings menu, click on "Appearance."
4. Under "Customize," toggle on "Use custom CSS."

Now that we have enabled custom CSS support, let's move on to creating a new custom callout.

# Step 2: Create a Custom Callout

In this example, we are going to create a custom callout called "read" with a specific icon and color.

1. Open your favorite text editor or code editor (e.g., Sublime Text or Visual Studio Code).
2. Copy and paste the following code into your editor:

```
.callout[data-callout="read"] {
    --callout-color: 0, 0, 0;
    --callout-icon: lucide-alert-book-open;
}
```

This code snippet defines a new callout style for elements with `data-callout="read"` attribute and sets the color and icon for that callout.

3. Save this file as `custom-callouts.css` in your preferred folder.

# Step 3: Add Custom Callouts File to Obsidian

Now let's add our newly created `custom-callouts.css` file to Obsidian.

1. Go back to Obsidian.
2. Click on the Settings icon (gear) in the left sidebar.
3. In the settings menu, click on "Appearance."
4. Under "Custom CSS," click on "Open folder."
5. A new file explorer window will open showing your Obsidian's custom CSS folder.
6. Copy and paste the `custom-callouts.css` file into this folder.

# Step 4: Apply Custom Callout

Now that we have added our custom callout style, let's use it in a document.

1. Create a new document or open an existing one in Obsidian.
2. To add the custom callout, type the following syntax:

```
>[!read] Read to the Player
>test
```

This syntax creates a new callout with our custom style applied.

3. Save your document and switch to Preview mode by clicking on the "Preview" button at the top right corner of the editor.

You should now see your custom callout with its unique icon and color.

# Conclusion

In this tutorial, we learned how to enable custom CSS support in Obsidian, create a custom callout with unique icons and colors, and apply it to our documents. With this knowledge, you can further customize your Obsidian experience by creating more personalized callouts or even modifying other parts of your notes' appearance.

Useful resources:
- Obsidian Callouts Documentation: https://help.obsidian.md/Editing+and+formatting/Callouts
- Lucide Icons: https://lucide.dev/
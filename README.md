# Agda syntax highlighting in VS Code

[![Visual Studio Marketplace Version](https://img.shields.io/visual-studio-marketplace/v/FredrikBakke.agda-syntax.svg)](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)
[![Visual Studio Marketplace Downloads](https://img.shields.io/visual-studio-marketplace/d/FredrikBakke.agda-syntax.svg)](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)

A simple syntax highlighting extension for the Agda programming language.

## Features

- Highlight Agda syntax in Agda, Literate Agda (LaTeX), and Markdown files.
- Add keybindings for using [`agda-mode`](https://marketplace.visualstudio.com/items?itemName=banacorn.agda-mode) with Literate Agda and Markdown files.

## Release Notes

### [0.6.7] 2023-09-05

- Remove language configurations, these have now been incorporated in [`agda-mode`](https://marketplace.visualstudio.com/items?itemName=banacorn.agda-mode)

### [0.6.6] 2023-08-24

- Define rules for automatic indentation

### [0.6.5] 2023-08-24

- Define the appropriate word pattern for VS Code

### [0.6.4] 2023-08-21

- Add highlighting for attributes
- Fix some instances where comments were not highlighted as such

### [0.6.2] 2023-08-15

- Update for [`agda-mode`](https://marketplace.visualstudio.com/items?itemName=banacorn.agda-mode) version `0.4.0`

### [0.6.1] 2023-06-10

- Reduce extension size

### [0.6.0] 2023-06-09

- Improve extension logo
- Add file icons based on [Trebor Huang](https://github.com/Trebor-Huang)'s [contribution](https://github.com/banacorn/agda-mode-vscode/pull/123) to `agda-mode`

### [0.5.1] 2023-06-05

- Fix a possible keybinding conflict with `agda-mode`
- Fix a highlighting issue with lambda abstractions
- Exclude line comments from being matched as name parts
- Increase consistency in highlighting inbuilt sorts as such

### [0.5.0] 2023-05-04

- Define the literate agda markdown file format
- Improve hole highlighting
- Fix a collection of issues with lambda abstraction highlighting
- Fix highlighting at the start of a line in `.agda` files

### [0.4.4] 2023-04-18

- Add highlighting for illegal name parts
- Make some accuracy improvements

### [0.4.3] 2023-04-17

- Add syntax highlighting in holes

### [0.4.2] 2023-04-17

- Add highlighting for dot patterns
- Add highlighting for symbols used in `with` patterns
- Add temporary fix for some parameter highlighting

### [0.4.0] 2023-04-16

- Define Literate Agda (LaTeX) files
- Add injection highlighting for Literate Agda files
- Add supporting configuration for Literate Agda files

### [0.3.0] 2023-04-16

- Migrate to Jinja2 templating
- Add many consistency improvements

### [0.2.0]

- Release preview

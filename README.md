# Agda syntax highlighting in VSCode

[![Visual Studio Marketplace Version](https://img.shields.io/visual-studio-marketplace/v/FredrikBakke.agda-syntax.svg)](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)
[![Visual Studio Marketplace Downloads](https://img.shields.io/visual-studio-marketplace/d/FredrikBakke.agda-syntax.svg)](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)

A syntax highlighting extension for the Agda programming language.

## Features

- Highlight Agda syntax in Agda, Literate Agda (LaTeX), and Markdown files.
- Add keybindings for using [`agda-mode`](https://marketplace.visualstudio.com/items?itemName=banacorn.agda-mode) with Literate Agda and Markdown files.

## Setup

The extension works straight out of the box. However, if you are using this extension together with [`agda-mode`](https://marketplace.visualstudio.com/items?itemName=banacorn.agda-mode), there are some settings you may want to change for a better user experience.

You may want to

- set the option `editor.autoClosingPairs` to `"never"` for files used with [`agda-mode`](https://marketplace.visualstudio.com/items?itemName=banacorn.agda-mode) as this function interferes with Agda's input-mode.
- if writing literate Agda LaTeX code, rebind the input-mode key (`agda-mode.input-symbol[Activate]`) from backslash (`\`) to some other key.

## Release Notes

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

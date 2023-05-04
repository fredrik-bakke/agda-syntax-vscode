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
- If you are writing literate Agda LaTeX code, rebind the input-mode key (`agda-mode.input-symbol[Activate]`) from backslash (`\`) to some other key.
- If you are using literate Agda Markdown files, add the following file association to your `settings.json`:
  ```json
  "files.associations": {
      "*.lagda.md": "literate agda markdown"
  }
  ```
  This will make available the appropriate key bindings for using `agda-mode`.

## Release Notes

### [0.5.0] 2023-05-04

- define the literate agda markdown file format
- improve hole highlighting
- a collection of fixes to lambda abstraction highlighting
- fix highlighting at the start of a line in `.agda` files

### [0.4.4] 2023-04-18

- add highlighting for illegal name parts
- some accuracy improvements

### [0.4.3] 2023-04-17

- add syntax highlighting in holes

### [0.4.2] 2023-04-17

- add highlighting for dot patterns
- add highlighting for symbols used in `with` patterns
- temporary fix for some parameter highlighting

### [0.4.0] 2023-04-16

- Define Literate Agda (LaTeX) files
- Add injection highlighting for Literate Agda files
- Add supporting configuration for Literate Agda files

### [0.3.0] 2023-04-16

- Migrate to Jinja2 templating
- Many consistency improvements

### [0.2.0]

- First usable release

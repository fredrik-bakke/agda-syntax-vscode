# Agda syntax highlighting in VSCode

[![Visual Studio Marketplace Version](https://img.shields.io/visual-studio-marketplace/v/FredrikBakke.agda-syntax.svg)](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)
[![Visual Studio Marketplace Downloads](https://img.shields.io/visual-studio-marketplace/d/FredrikBakke.agda-syntax.svg)](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)

A syntax highlighting extension for the Agda programming language.

## Features

- Highlight Agda syntax in Agda, Literate Agda, and Markdown files.
- Add keybindings for using [`agda-mode`](https://marketplace.visualstudio.com/items?itemName=banacorn.agda-mode) with Literate Agda and Markdown files.

## Setup

The extension works straight out of the box. However, if you are using this extension together with [`agda-mode`](https://marketplace.visualstudio.com/items?itemName=banacorn.agda-mode), there are some settings you may want to change for a better user experience.

You may want to

- set the option `editor.autoClosingPairs` to `"never"`, as this function interferes with Agda's input-mode.
- rebind the input-mode key from backslash (`\\`) to some other key, if you are writing literate Agda LaTeX code.

## Release Notes

### [0.4.2] 2023-04-17

- add highlighting dot patterns
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

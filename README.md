# HowrseBot

HowrseBot is a Python-based browser automation project for automating
repetitive horse-management tasks in the browser game Howrse.

The project was originally created as a practical programming project
and has grown into a modular automation system. It uses Selenium
WebDriver to interact with the game UI and separates horse care,
training, competitions, breeding, and BLUP logic into dedicated modules.

> **Note:** This repository is primarily a portfolio/project example
> demonstrating Python, Selenium, modular program design,
> configuration-driven automation, and handling of dynamic web
> interfaces.

## Features

-   Automated horse care
    -   Feeding
    -   Grooming
    -   Watering
    -   Other daily care actions
-   Automated training and riding
    -   Forest and mountain training
    -   Skill-specific training
    -   Age-dependent training plans
-   Automated competitions
    -   Jumping
    -   Dressage
    -   Support for different competition variants
-   Automated BLUP process
    -   Age-based training plans
    -   Breed-specific BLUP schedules
    -   Foal preparation
    -   Aging
    -   Breeding
-   Breed-specific automation
    -   Different BLUP schedules can be selected automatically based on
        the horse's breed
-   Equipment management
    -   Stable changes
    -   Horse specialization
    -   Equipment setup
-   Configuration-driven operation
    -   Accounts and automation settings are kept outside the main logic
    -   Training schedules are represented as data rather than
        hard-coded into the main workflow

## Technologies

-   **Python**
-   **Selenium WebDriver**
-   **JSON**
-   Modular Python architecture
-   CSS selectors and XPath for browser interaction

## Project structure

The project is organized around actions and reusable utilities instead
of putting the entire automation flow into one large file.

``` text
howrsebot/
├── actions/
│   ├── care/
│   │   └── care_actions.py
│   ├── competitions/
│   │   └── competition_actions.py
│   ├── training/
│   │   └── ...
│   └── ...
├── accounts/
│   └── ...
├── blup/
│   ├── blup.py
│   ├── blup_utils.py
│   ├── blup_days_holstein.py
│   └── blup_days_lusitano.py
├── utils/
│   ├── randomTime.py
│   └── ...
├── config.json
├── divines.json
└── main.py
```

The exact structure may evolve as the project is developed further.

## BLUP automation

One of the main parts of the project is the automated BLUP workflow.

Instead of hard-coding every training action directly into the BLUP
algorithm, the schedule is represented as data:

``` python
BLUP_DAYS_LUSITANO = {
    "0y6m": ["metsätalli"],
    "1y6m": ["metsä"],
    "3y0m": ["koulu"],
    "3y10m": ["ravi"],
    # ...
}
```

The correct schedule can then be selected according to the horse's
breed:

``` python
BLUP_DAYS = {
    "Holsteininhevonen": BLUP_DAYS_HOLSTEIN,
    "Lusitano": BLUP_DAYS_LUSITANO,
}
```

This keeps the automation logic separate from the actual training data
and makes it easier to add new breeds or modify existing schedules.

## Browser automation

Selenium is used to interact with the web application.

The project uses reusable helper functions for common interactions, for
example:

``` python
click_divine_button(driver, button_id)
click_button_by_text(driver, text)
```

Selectors are chosen according to the structure of the page, using IDs,
CSS selectors, and XPath where appropriate.

The automation also checks whether elements exist before attempting
actions that may not be available in every horse's current state. This
is important because the page can differ depending on whether a horse
has already been trained, equipped, specialized, or otherwise processed.

## Configuration-driven design

Account-specific and game-specific values are kept in configuration
files instead of being embedded throughout the code.

This makes it possible to change settings without modifying the
automation logic and reduces duplication.

The project also uses structured data for things such as:

-   Horse IDs
-   Amounts of competitions
-   Breed-specific training schedules
-   Special cases in the BLUP process
-   Divine horse configuration

## Handling special cases

A significant part of the project is dealing with exceptions caused by
the dynamic state of the game.

For example, an action may need to behave differently when:

-   A horse is already equipped
-   A horse has already been specialized
-   A competition has a temporary variant available
-   A particular UI element is missing
-   A horse has reached a specific age
-   A breed requires a different BLUP strategy

Rather than assuming that every page is identical, the automation checks
the current state before continuing.

## Why I built it

I built HowrseBot as a practical way to develop my Python and automation
skills.

The project has given me experience with:

-   Breaking a larger problem into smaller modules
-   Designing reusable functions
-   Working with Selenium and dynamic web pages
-   Finding robust CSS and XPath selectors
-   Handling missing elements and different UI states
-   Separating configuration/data from application logic
-   Designing data-driven workflows
-   Debugging automation failures
-   Refactoring code as the project grows

The project is particularly useful as a portfolio example because it has
evolved organically: functionality was first implemented in a simple
form and then refactored into a more maintainable architecture as new
requirements appeared.

## Development approach

The project follows a gradual refactoring approach.

As functionality has grown, responsibilities have been separated into
dedicated modules. For example, the main BLUP workflow is kept
relatively focused, while helper functions and breed-specific schedules
are moved into their own modules.

This makes the codebase easier to extend without turning the main
workflow into a large collection of unrelated functions.

## Future development

Possible future improvements include:

-   More breed-specific BLUP schedules
-   Improved explicit waits instead of fixed delays
-   More robust error handling and recovery
-   Better logging
-   Automated tests for non-Selenium logic
-   More reusable abstractions for different competition types
-   Improved configuration validation
-   A clearer command-line interface for selecting automation tasks

## Project status

The project is an actively developed personal programming project. Its
architecture and functionality are continuously being improved as new
automation requirements arise.

------------------------------------------------------------------------

**Technologies demonstrated:** Python · Selenium · Web automation · JSON
· Modular architecture · Data-driven design · Debugging · Refactoring

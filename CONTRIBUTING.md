# Contribute

Hiii! Thanks for thinking about contributing to this project.

## How the Action Works

The action does the following: 

1. Checks for mermaid definition files

2. Checks for old generated diagrams (svg/png/pdf)

3. If there are diagrams that need to be generated, it:
  - Downloads @mermaid-js/mermaid-cli
  - Generates mermaid diagrams to the desired output

A key detail here is that it only generates mermaid diagrams if the existing, generated diagrams (png/pdf/svg) have older timestamps than their respective mermaid definition files.

As such, a technical challenge arises when checking out a repo, since all timestamps are reset to when the repo was checked out. 

## How the Repo is Structured

I wanted to write my action in Python, and I wanted it to run as fast as possible. I also wanted to unit-test it.

So, I used composite actions, with Python run commands...

But, how do I unit-test them?

I take an unconventional approach by defining standalone, python files that contain the code I want to execute. They're named with the step's ID.

Then, I "bundle" these python files into the action. I take all the python files and (using a YAML JS library) integrate them into the `action.yml`.

This means I can unit-test my Python run commands because they're regular files. I also get to use composite actions (instead of container actions) for speed and readability. Finally, and best of all, I get to use Python to write the logic that I want.

I also added a workflow to check that the files were bundled.

Is it over-engineered? Yes! 

But is it cool? You tell me...

## Next Steps

- I want this action to handle caching generated mermaid files for the user to remove complexity, and to only regenerate the mermaid diagrams that need to be regenerated.

- Support for md can be added

- Support for Yarn berry can be added

- A minimal JS package can be created to preview how the mermaid diagrams will look in production.
# Mermaid-Maker

This action converts [mermaid](https://github.com/mermaid-js/mermaid) definition files into one of the output formats: PNG, SVG, PDf. 

This allows you to create web applications without worrying about how to render static mermaid diagrams in production; this action helps you with that.

## Quickstart

1. Find your deploy workflow, ex. `./.github/workflows/deploy.yml`. 

2. Before you build your web-application, add the following lines: 

```yml
      - name: Generate mermaid diagrams
        uses: "mermaid-maker/actionv1.1.5"
        with:
          pkg_manager: pnpm   # replace with your node pkg manager (npm/pnpm/bun)
          output_file_extension: svg  # replace with your desired output file (svg/png/pdf)
```

3. In your web-application, render simple client-side mermaid diagrams for dev, and refer to the svg/png/pdf files in prod. Here's an example from a Next app:

```js
    let MermaidDiagram = null;

    if (process.env.NODE_ENV == "development"){
        // read mermaid definition file
        const chart_content = await readFile(`${process.cwd()}/public/${chart}.mmd`, "utf-8")
        // generate client-side mermaid diagrams using mermaid-js library
        MermaidDiagram = <ClientMermaid chart={chart_content}/>
    }

    else if (process.env.NODE_ENV == "production") {
        // refer to the static svg in prod
        MermaidDiagram = <Image src={`${process.env.NEXT_PUBLIC_BASEPATH}${chart}.svg`} alt="mermaid_diagram" width={100} height={100}/>
    }

    return (
      <div className="w-100 *:w-full">
        {MermaidDiagram}
      </div>
      )
```

For a full, working example, check out this Next sample app: [mermaid-maker/next-sample-app](https://github.com/mermaid-maker/next-sample-app)

Also, if you want to see how it will look in prod, you can visit [mermaid.ai](https://mermaid.ai) and export PNG/SVG/PDF diagrams that you can test out on your machine.

## Usage

This action takes the following **input** variables:

```yml
input_dir:
  description: |
    The input directory for mermaid files. Defaults to "all",
    i.e. all changed files with input_file_extension across the whole repo.
  required: false
  default: all
input_file_extension:
  description: |
    The extension of the mermaid files. Note: md (markdown) input files are 
    currently not supported, but they could be in the future.
  required: false
  default: mmd
output_dir:
  description: |
    The output directory for generated mermaid files. Defaults to "same",
    i.e. converted files will be placed in the same directory as their source files.
  required: false
  default: same
output_file_extension:
  description: |
    The output format of the generated mermaid files. Only "svg", "png" and "pdf" are accepted. 
  required: false
  default: svg
pkg_manager:
  description: |
    The node package manager to use. Make sure it's setup before using this action.
    Currently, only the following pkg_managers are accepted:
      - "npm"   
      - "pnpm"  
      - "bun"   
    Yarn is not supported due to non-native support for the auto-installation of peer-depenecies like puppeteer. 
  required: false
  default: npm
```

It **outputs** the following variables:

```yml
input_files:
  description: The input files that were used to generate mermaid diagrams
  value: ${{steps.get_files_to_regen.outputs.input_files_to_regen}}
output_files:
  description: The output files that were generate
  value: ${{steps.get_files_to_regen.outputs.output_files_to_regen}}
```

## Why Use This Action?

One key aspect about Mermaid is that it's a client-side library. It uses the DOM to render diagrams.

This means that mermaid diagrams are rendered on the client, adding additional latency to your app. 

So, when you want to render mermaid diagrams, you might come across the following, **possible solutions**: 

#### A. Live the Easy Life

Well, technically, the first solution is to not worry about it... However, a webpage will take longer to load on every rerender.

---

#### B. Async & Caching

One solution is rendering mermaid diagrams asyncronously and caching them between rerenders. This allows you to render most of your webpage while using placeholders/suspense/lazy loading for mermaid diagrams. Then, caching the mermaid diagrams makes it load faster on rerenders. 

This is good enough for use-cases where:

1. Initial speed of loading diagrams isn't a priority

2. A given webpage only contains a few, simpler diagrams

3. You don't mind the added complexity (async, caching, placeholders/suspense). You can even use a library like: [https://github.com/lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) to help you out here.

---

#### C. Diagrams as Static Assets

Another solution is using `mermaid-js/mermaid-cli` to render mermaid diagrams on your machine, before pushing them as static assets to your repo.

This is also good enough for use-cases where:

1. You're working on internal/individual projects. With collaborative (esp. open-source) projects, you need to check and/or protect against scripting attacks with SVGs. You can use PNGs to skip this step.

2. You're willing to figure out how to set up the mermaid cli (downloading headless browsers, sandboxing, generating new mermaid diagrams with every change).

---

### This Solution

Or... **you can use this solution**. This Github action checks for any mermaid definition files, and it renders them to your chosen output. 

This solution is:

1. Simpler. On your dev environment, you can simply load mermaid diagrams on the client without async/placeholders/caching. Then, in prod, your webapp can use the generated SVGs as static assets.

2. You don't need to worry about Mermaid's CLI, sandboxing puppeteer or downloading web browsers.

3. More secure, since SVGs are generated by GitHub Actions rather than individual collaborators.

4. Small overhead. This action only depends on one JS library: `mermaid-js/mermaid-cli`. It's also a composite action, meaning the `action.yml` at the repo's root contains details everything the action does. 

### Drawbacks of This Solution

Here are some of the challenges you might face using this action:

1. Requires basic knowledge of Github Actions. 

2. Can't easily simulate how the diagrams will look in prod. This means that styling mermaid diagrams can create a discrepancy between what you see on dev vs. what ends up on production.

3. Additional latency to deploy applications. There is currently no caching strategy, so static mermaid assets are generated on every deploy.

## So, who's this for?

I'd say this is for hobby projects, and for folks with working knowledge of Github Actions. For more serious projects with larger teams, I'd use [Solution B (detailed above)](#b-async--caching)

## Contributions!! 😀

Check out [CONTRIBUTING.md](./CONTRIBUTING.md) for details on how to contribute to this project!!
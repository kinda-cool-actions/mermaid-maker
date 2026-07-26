import { load, dump } from 'js-yaml'
import { readFileSync, writeFileSync } from 'node:fs'

interface GithubAction {
    name: string
    description?: string
    inputs?: object
    runs: {
        using: string
        steps: {
            name?: string
            id?: string
            run?: string
            if?: string
            uses?: string
            shell?: "bash" | "python"
            env?: object
        }[]
    }
}
// Get document, or throw exception on error

const doc = load(readFileSync('../action.yml', 'utf8')) as GithubAction

// utility to sync action to python files if accidentally editted action instaed of files
export function sync_left() {
    const steps = doc["runs"]["steps"]
    for (const step of steps) {
        if (step['shell'] === "python") {
            const py_id = step['id']
            const py_run = step['run'] as string
            writeFileSync(`../py_files/src/${py_id}.py`, py_run)

        }
    }
}

export function bundle_to_action() {
    const steps = doc["runs"]["steps"]
    for (const step of steps) {
        if (step['shell'] === "python") {
            let py_id = step['id']
            try {
                step['run'] = readFileSync(`../py_files/src/${py_id}.py`, "utf-8")
            }
            catch (error) {
                if (error instanceof Error) {
                    console.log(error.message)
                }
                else {
                    console.log(error)
                }

            }
        }
    }
    writeFileSync("../action.yml", dump(doc, { "lineWidth": -1 }), "utf-8")
}

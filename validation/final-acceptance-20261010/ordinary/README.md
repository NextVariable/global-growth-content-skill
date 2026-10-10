# Global Positioning & Growth Content

A Markdown Skill that helps independent developers and small product teams turn existing target-reader decisions and product facts into positioning and English product content inside a Skill-capable agent client.

Bring the audience, product workflow, authorized evidence and goal for the asset. Start with one homepage hero, then check its claims against your brief. The Skill provides reusable scope and evidence boundaries and task-specific method files. Your client provides the agent model and tools.

[Read the repository](https://github.com/NextVariable/global-growth-content-skill) · [Browse the installation unit](https://github.com/NextVariable/global-growth-content-skill/tree/main/skills/global-growth-content)

## What you can use it for

Draft positioning, product pages, developer README content, search content, social or UGC briefs, and multilingual rewrites. A one-off task can stay small: you do not need to generate a campaign or content package to rewrite a hero.

This is a method package, not a standalone SaaS service, website editor or automatic publishing tool. It does not execute publishing, outreach, ad buying, sales or experiments. A generated draft does not prove market demand or business results.

## Requirements

Use a client that supports Skills and has working agent-model access. Check that client's documented installation location and discovery process. The Skill itself does not supply model credits or require a business script, online service, npm package or pip package to run its Markdown guidance.

Git is needed for the clone commands below. Git is a way to obtain the files, not the Skill's runtime. You may instead obtain the complete installation unit through the repository's file-download interface.

## Get and inspect the package

The commands below fetch the public repository into a new folder and inspect the installation unit. Run them in a working directory where `global-growth-content-skill` does not already exist. They do not install anything globally.

```sh
git clone https://github.com/NextVariable/global-growth-content-skill.git
cd global-growth-content-skill
test -f skills/global-growth-content/SKILL.md
test -f skills/global-growth-content/LICENSE
find skills/global-growth-content -type f -print
```

The documented installation unit is `skills/global-growth-content`, with ten files: `SKILL.md`, six files under `references`, one handoff template under `templates`, `agents/openai.yaml` and the MIT `LICENSE`. Copy the entire directory so its internal references remain available. Do not install only `SKILL.md`.

The public repository is the actual entry point. A verification snapshot dated 2026-10-10 records local methods at `6b57209` and the remote at `994b27b`; the local methods in that snapshot should not be assumed to be published. Inspect the version you obtain. The commands fetch the available public version.

## Try an isolated copy

From the repository directory, these commands make a fresh temporary copy without touching a global Skill directory:

```sh
staging_root=$(mktemp -d)
mkdir "$staging_root/client-skills"
cp -R skills/global-growth-content "$staging_root/client-skills/global-growth-content"
test -f "$staging_root/client-skills/global-growth-content/SKILL.md"
diff -r skills/global-growth-content "$staging_root/client-skills/global-growth-content"
printf 'Isolated copy available at: %s
' "$staging_root/client-skills/global-growth-content"
```

A successful `diff` produces no differences. This checks the copied files; it does not prove your client will discover the Skill. The shared verification record confirms one full ten-file isolated copy and entry/internal-link validation with no errors. It does not confirm automatic discovery in every client.

## Install for your client

Identify the Skill parent directory actually configured in your client. Do not assume that another client's path applies. Copy the complete installation unit there under the name `global-growth-content`. If an existing directory has that name, keep it and inspect it before deciding whether to replace it.

If you want to use a terminal for this copy, run the following from the repository directory. Enter the existing parent directory configured by your client at the prompt. The command refuses an existing same-name package and does not create a guessed client directory.

```sh
printf 'Enter your client-configured Skill parent directory: '
IFS= read -r client_skills_dir
if [ -z "$client_skills_dir" ] || [ ! -d "$client_skills_dir" ]; then
  printf 'No existing Skill parent directory selected. Nothing copied.
'
elif [ -e "$client_skills_dir/global-growth-content" ] || [ -L "$client_skills_dir/global-growth-content" ]; then
  printf 'A same-name package exists. Preserve and inspect it before updating.
'
else
  cp -R skills/global-growth-content "$client_skills_dir/global-growth-content"
  diff -r skills/global-growth-content "$client_skills_dir/global-growth-content"
fi
```

Use your client's documented discovery or refresh process and confirm `global-growth-content` is available before your first task. A copy alone is not a verified client installation. The documented local Codex helper convention uses a `skills` directory under `CODEX_HOME` and supports an explicit destination; this does not establish a universal path for other clients.

## Complete your first task

Create a product brief in your project, outside the installed Skill package. You can use this Skill itself as the example product:

```text
Product: Global Positioning & Growth Content
Category: Markdown method Skill for a Skill-capable agent client.
Reader: Independent developers or small product teams with existing
product facts and a target-reader decision who need English content.
Goal: Make the homepage hero explain the workflow to a first-time reader.
Workflow: User provides reader, product workflow, authorized facts,
evidence and asset goal; the agent drafts content using reusable scope,
evidence boundaries and task-specific method files; user reviews claims.
Supported work: Positioning, pages, developer README, search content,
social/UGC briefs and multilingual rewriting. This task is English only.
Requirements: Client supplies the model. No included model credits.
Scope: No publishing, outreach, ads, sales or experiment execution.
Evidence: Independent ten-file package, MIT license, documented isolated
copy and internal-link check. No customer, time-saving, quality-comparison
or conversion-result data. Client discovery still requires checking.
Next step: https://github.com/NextVariable/global-growth-content-skill#readme
```

Attach or paste that brief using your client's supported input mechanism. Then ask:

```text
Use $global-growth-content with this authorized product brief and existing
target-reader decision. Write a complete English homepage hero so a
first-time reader understands what the Skill is and how the workflow works.

Include an eyebrow, headline, subheading, supporting copy, CTA label and
URL, and visible client/model requirements. Use only supported capability
claims. Add a separate review note identifying unsupported assumptions.
Do not change the market, invent outcome data or publish the result.
```

Check the result before using it. The reader should be able to identify a Markdown Skill, see the product facts as inputs, understand the drafting and review workflow, and follow the README CTA. Remove any invented customer count, speed, quality or conversion promise. Keep the client/model requirements visible. Save the copy and review note in your project.

Your first task is complete when you have a full hero and have checked its factual claims. Publishing the hero and evaluating its effect are separate actions outside this Skill's execution scope.

## Troubleshooting

If the client cannot find the Skill, check its configured directory, the `global-growth-content` folder name and package completeness, then follow the client's discovery instructions. Do not infer successful Skill loading from a model response alone.

If the agent asks for product details, supply the missing reader, workflow, facts, evidence or goal. You do not need another stage package: an existing decision in plain text is enough. If you have no effect evidence, request capability-based copy and keep outcome hypotheses in a review note.

If the agent tries to publish, sell or start an experiment, restate the content-only scope. If the input contains confidential information, use only material you are authorized to provide and keep persistent project/customer records outside the Skill directory.

## License and evidence

MIT licensed. See `skills/global-growth-content/LICENSE` in the installation unit.

Source map for this draft: P1 supports category, inputs and content tasks; P2 supports package structure and runtime boundary; P3 supports scope and project-data placement; P4 supports the isolated verification and discovery limitation; P5 supports client-specific installation and no npm/pip prerequisite; P6 supports the invocation example; P7 supports the repository, license and absence of outcome data.

## Internal publication note — remove before replacing a live README

This is a complete proposed README, not a change to the real repository README. Clone and installation commands are provided for future use and were not run during this writing task. Package facts come from the common authorized inputs. A recorded isolated verification is evidence of that earlier check, not a new installation here. Client discovery and actual first-run output remain unverified in this draft. The fixed audience is an adoption-task assumption, not demonstrated demand.

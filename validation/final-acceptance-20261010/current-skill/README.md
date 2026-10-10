# Global Positioning & Growth Content

A Markdown Skill for turning existing product facts and audience decisions into positioning, product pages, developer READMEs, and related content in a Skill-capable agent client.

Use it when you already know who you want to reach and need to explain the product in English. Bring an authorized brief with the audience, their task, your product’s workflow, the evidence you can use, and the goal of this writing task. The Skill guides the agent through relevant methods and produces content for you to check. It does not supply model access or execute publication, outreach, advertising, sales, or experiments.

The complete independent installation unit is `skills/global-growth-content`. You do not need the other growth Skills or a fixed upstream data format. An existing market decision can be ordinary text. Directly prompting a model remains a reasonable alternative for a simple one-off rewrite; the reason to evaluate this Skill is its reusable methods and explicit scope and evidence boundaries, not a measured claim of superior results.

## Get the files

You need Git to run the download command below, internet access for that download, and an agent client that supports loading local Skills. Your client provides the model, tools, and any associated usage costs. No pip/npm package is required to use these Markdown methods.

From a working directory where a new `global-growth-content-skill` folder is acceptable:

```sh
git clone https://github.com/NextVariable/global-growth-content-skill.git
cd global-growth-content-skill
```

If that folder already exists, stop and inspect the existing copy rather than overwriting it. These commands obtain the public repository revision available at download time; they do not select an unpublished local revision.

Set `CLIENT_SKILLS_DIR` to the skills directory configured in your client, then run this copy block from the repository root. Do not paste a guessed location: confirm the client's configuration first. The local Codex installation helper convention is `$CODEX_HOME/skills`; other clients can use different discovery rules.

```sh
: "${CLIENT_SKILLS_DIR:?Set CLIENT_SKILLS_DIR to your configured client skills directory}"
python3 - <<'PYCODE'
import os
import shutil
from pathlib import Path

source = Path('skills/global-growth-content')
destination = Path(os.environ['CLIENT_SKILLS_DIR']) / 'global-growth-content'
if not (source / 'SKILL.md').is_file():
    raise SystemExit('Run this from the repository root; source SKILL.md is missing.')
if destination.exists():
    raise SystemExit('Destination already exists. Preserve and inspect it before choosing a version.')
destination.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(source, destination)
print('Copied global-growth-content. Confirm discovery in your client next.')
PYCODE
```

This convenience copy block requires Python 3 and refuses an existing destination. Python is a requirement of this optional file-copy example, not of the Skill itself. You can instead copy the complete directory using your file manager. The installation unit has ten files: the entrypoint, six method references, a handoff template, client metadata, and the MIT license. Keep the complete unit together.

Follow your client’s local-Skill loading instructions. Open the installed `SKILL.md` and confirm its linked references exist. A successful file copy is not confirmation of automatic discovery. Do not assume the Skill is active until your client can load it.

## Complete a first task

Use the Skill itself as a small, inspectable product example. Paste this input and request into a conversation after loading the Skill:

```text
Use $global-growth-content.

Product: Global Positioning & Growth Content, a Markdown method Skill.
Reader: independent developers or small product teams with a Skill-capable
agent client, existing audience decisions, and a need for English content.
That reader choice is a working assumption, not a customer research result.

Workflow: the user supplies authorized product facts, the audience,
their task, the product workflow, evidence, and a writing goal. Relevant
method files guide the agent to write complete content and keep claims
within the evidence. The user reviews the draft against the facts.

Capabilities: positioning, product pages, READMEs, and related content.
Independent installation unit: skills/global-growth-content, ten files,
MIT license. The client supplies model access and tools. The Skill does
not publish, run campaigns, sell, or validate growth results.

Evidence: source methods and a completed isolated file-copy/link check.
That check does not prove every client's discovery or writing improvement.
No customer counts, testimonials, savings or conversion measurements.

Goal: write one complete English homepage hero so a first-time reader
understands the category, workflow, conditions and real next step.
CTA: https://github.com/NextVariable/global-growth-content-skill#readme
Keep the audience fixed. Do not create a full content package.
After public copy, give an internal source/assumption note. Do not claim
unpublished local methods are already in the public repository.
```

If your client has a different skill-selection mechanism, select `global-growth-content` through that mechanism; the `$` form is the documented invocation example, not a universal API.

A usable first output includes an actual headline, explanatory copy, a README CTA, and the conditions to try the Skill. For example, the headline can be “Turn your product brief into an introduction people can follow,” followed by copy explaining the supplied facts → relevant methods → reviewed draft workflow. A plan or outline alone does not complete the task.

Check that the result calls this a Markdown Skill, requires a compatible client and product brief, uses the actual README URL, and avoids invented customers or performance promises. Save the reviewed draft, brief, and internal note in your product project outside the installation directory. The outcome is a content draft you can inspect, not a deployed page or validated business result.

## What the methods cover

`SKILL.md` defines input, scope and completion. The linked methods cover positioning and customer language; pages and fair comparisons; developer adoption; search content; social and language adaptation; and source/version handoff. Read the relevant method for the task instead of requiring every task to produce every asset. A one-off hero can remain a one-off hero.

Keep confidential or client-specific facts in an authorized project location. The installation directory is for reusable methods. Supplying data to an agent client is governed by that client's tools and data handling; this Skill does not create a separate storage service or permission system.

## Troubleshooting and limits

If discovery fails, check the configured skill directory, folder nesting, and your client's loading procedure. The exact directory and interface vary; the recorded isolated check did not test all clients. If the agent returns generic principles, ask it to complete the requested public copy from the same brief. If it invents integrations or outcomes, identify those claims and request a source-bound correction. Missing outcome evidence allows a capability-based draft; it does not permit fabricated results.

This Skill does not choose a new market for you, provide a hosted editor, grant model credits, or carry out external publication. There are no documented Skill API endpoints, package-manager installers, or payment flows here. Model and tool availability remain properties of your chosen client.

The source record reports a complete ten-file isolated copy and internal link check on 2026-10-10 with no errors. It did not test client discovery, a live service integration, or commercial outcomes. The content-method revision used for this example is local 6b57209; the recorded public revision is 994b27b. Inspect the repository revision you obtain rather than assuming the newer methods have been published.

## License and entry points

The Skill is MIT-licensed. See the `LICENSE` included in the installation unit for the terms. Read the [actual repository README](https://github.com/NextVariable/global-growth-content-skill#readme) and inspect the [installation directory](https://github.com/NextVariable/global-growth-content-skill/tree/main/skills/global-growth-content). These are documentation and source entry points, not a checkout or automatic installation flow.

---

## Internal delivery and verification note — exclude from the public README

Reader: an individual developer or small team evaluating first use. Purpose: obtain the actual unit, load it through a compatible client, and complete one factual hero task. CTA: the existing public repository and README. P1 supplies scope and brief; P2 supplies package structure and client dependence; P3 supplies project-storage and execution limits; P4 plus isolated-package.json supply the actual earlier copy/link check; P5 supplies Git/copy installation and local helper convention; P6 supplies invocation; P7 supplies MIT, public links and revision limitation. Logical locators: product-evidence.json / sources[id=P1…P7]. The audience remains the assumption at upstream_and_audience.

The network clone and write to a user's configured client directory are instructions for a reader, not actions executed in this acceptance task. The copy block is standard-library file copying and explicitly blocks a pre-existing target. No live client invocation, global installation or model/runtime interface was tested or invented. This is a proposed README artifact; the real repository README has not been edited. No unpublished code, screenshots or customer material was added.

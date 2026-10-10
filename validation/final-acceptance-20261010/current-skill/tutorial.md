# Your first task: write a verifiable homepage hero

This tutorial is for an independent developer or small product team with a Skill-capable agent client, an existing audience decision, and product facts they are authorized to use. You will use Global Positioning & Growth Content itself as the product example. The goal is a complete English first screen that explains what the Skill is, how a reader uses it, and where to start. There is no second fictional product and no publication step.

## 1. Get the installation unit and confirm the client can load it

Open the [repository README](https://github.com/NextVariable/global-growth-content-skill#readme). Get the complete `skills/global-growth-content` directory and place it in the skills directory configured for your client. Preserve an existing directory with that name before deciding which copy to use. The client supplies the model and tools; this Skill is a set of Markdown methods, not an executable application.

The installation unit contains ten files, including `SKILL.md`, `references`, a handoff template, client metadata, and `LICENSE`. Do not copy only `SKILL.md`, because its linked methods belong to the same unit. Follow your client’s instructions for discovering or loading local skills. The local Codex helper uses `$CODEX_HOME/skills` by default, but that convention is not a universal path for other clients.

Observable result: the directory is present, `SKILL.md` opens, and its linked method files can be read. That file check does not by itself confirm the client has loaded the Skill. Confirm loading through the client’s supported mechanism before continuing. If the client cannot discover the folder, check the configured directory and the folder nesting; do not keep issuing the writing prompt and assume the methods were applied.

## 2. Give the agent your existing goal and product brief

Paste the following brief in the client conversation, or attach it from your authorized project folder. Keep product-specific materials outside the installed Skill directory. A previous market decision can enter as ordinary text: there is no required upstream program or seven-file input package.

```text
Product: Global Positioning & Growth Content
Skill name: global-growth-content
Category: Markdown method Skill used in a Skill-capable agent client.
Reader: independent developers or small product teams who already have
an audience decision and product facts, and need English product content.
This reader choice is our working assumption, not a researched customer result.

Reader task: explain an existing product to a first-time reader.
Current alternative: directly prompt a model or maintain a prompt document.
Those alternatives remain reasonable for a simple one-off rewrite.

Workflow: provide authorized product facts, the audience, their task,
product workflow, evidence, and the goal of this writing task. The agent
uses relevant methods to write positioning, pages, a README, or related content.
The user checks the draft against the supplied facts.

Installation: copy the complete skills/global-growth-content unit into
the skills directory configured for the client. The unit has ten files,
including linked methods and MIT LICENSE. No pip/npm package is required
to use the Markdown methods. The client supplies model access and tools.

Evidence: source files describe the workflow. A 2026-10-10 isolated copy
and internal link check completed without errors. This did not verify
all clients' automatic discovery or any improvement in writing outcomes.

Scope: content drafting only; no actual publishing, outreach, ads, sales,
or experiments. The Skill can be installed independently.

Next step: read the real repository README:
https://github.com/NextVariable/global-growth-content-skill#readme

Do not claim customer counts, testimonials, savings percentages,
conversion gains, guaranteed quality, or superiority over ordinary prompts.
Do not claim that the latest local methods have already been published.
```

This brief makes the reader decision and evidence limits explicit. If you use the same process on your own product later, replace the facts with authorized facts for that product; do not retain this Skill’s capabilities as if they belonged to yours.

## 3. Invoke one bounded task

Send this instruction in the same conversation after the brief:

```text
Use $global-growth-content with the brief above. Write a complete English
homepage hero for a first-time reader. Include an eyebrow, headline,
explanation of what this is and how the workflow works, a real README CTA,
and conditions the reader needs to decide whether to try it.

Keep the supplied audience and do not redo market selection. Do not
produce a full content package. After the public copy, add an internal
note mapping important claims to the brief and identifying assumptions.
```

The `$global-growth-content` form is the documented example for invocation. If your client uses a different skill-selection mechanism, select the same Skill through that mechanism and send the task text. There is no supplied model API endpoint or command-line text generator to invoke.

Observable result: a finished hero, followed by a separate internal note. A list of principles, headings without copy, or an answer that changes the target reader is not the requested output. Ask the agent to finish or correct the affected part against this brief; do not fill the gaps with invented benefits.

## 4. Check the draft against the brief

Here is a complete example draft for this product:

> **Global Positioning & Growth Content · Markdown Skill**
>
> **Turn your product brief into an introduction people can follow.**
>
> Already know who your product is for and how it works? Use Global Positioning & Growth Content in a Skill-capable agent client to turn those facts into positioning, a homepage hero, a developer README, or related content.
>
> Start with your audience, their task, your product’s workflow, and the evidence you can use. The Skill guides your agent to connect the task to the product’s mechanism, keep claims within that evidence, and write a complete draft for the next step you actually offer.
>
> [Read the README and get the Skill](https://github.com/NextVariable/global-growth-content-skill#readme)
>
> MIT-licensed files. Bring your own Skill-capable client and product brief. The Skill does not supply model access or publish your content.

The category matches the brief: Markdown Skill, not SaaS. The mechanism has a visible input and a draft output, with user review. The CTA opens real documentation, not an invented purchase flow. The copy contains no conversion or customer claims. These are observable checks on the content, not evidence that the hero performs better commercially.

If a result says “publish automatically,” remove that promise: the provided scope is drafting. If it invents a testimonial or “save 80%,” replace it with an actual capability or omit it. If it cannot explain the workflow, bring it back to the supplied sequence of brief → relevant methods → draft → source check. If your own brief contains contradictory capabilities, identify the disputed claim and leave it out while completing unaffected text. If it contains only an aspiration, label that aspiration in the internal note rather than presenting it as an existing feature.

## 5. Save the result and its boundary

Save the reviewed public hero and internal note in your product project, outside the installation directory. Keep the brief with the draft so a teammate can trace the claims. Your first task is complete when a reader can identify the Skill, its use conditions, and the actual next step, and you can connect every important claim to the supplied brief. You now have a draft to review; you have not deployed a website or validated growth results.

---

## Internal source and execution note

Purpose: first adoption through a single hero task; reader and situation are fixed by product-evidence.json / upstream_and_audience. Source mapping: category/input/output and evidence boundaries → sources[id=P1]; complete independent unit and host client → P2; scope and project storage → P3; actual isolated copy → P4 and isolated-package.json; client-directory convention and no package install → P5; invocation → P6; license, URL and version restriction → P7. The example draft was written for this task from that brief. It is not a reported historical client run, customer quote, or effect measurement.

The sample can be pasted as text or attached as a project file. No automatic product import, form, API, or integration is claimed. The tutorial was not run in an actual client, and no global installation, live URL visit or discovery test occurred. The shared record verifies source copying and links, not this invocation in every client. Current local methods are 6b57209; the supplied remote observation is 994b27b. Readers obtaining the public repository should inspect their checked-out revision; this tutorial does not assert that its local method revision is already online.

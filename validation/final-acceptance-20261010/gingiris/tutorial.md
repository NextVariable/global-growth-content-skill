# Use Global Positioning & Growth Content for your first homepage hero

Global Positioning & Growth Content is a Markdown Skill that guides a compatible agent from an existing product brief to an English content draft. To try it, install the complete Skill directory, supply your reader and evidence, ask for one hero, then check the resulting claims against your brief.

On 10 October 2026, an isolated package check copied this Skill’s 10 files and found no entry or internal-link errors. That establishes a package check—not automatic discovery in your client or a measured writing result. This walkthrough uses the Skill itself as the product, so you can follow every example claim back to an actual source. (A readable draft still needs a factual review.)

| Package fact | Recorded value | Evidence |
|---|---|---|
| Complete installation unit | 10 files | P2, P4 |
| Reference files | 6 | P2 |
| Mandatory business scripts | 0 | P2 |
| Isolated package check | 2026-10-10 | P4 |

## What do you need before using the Skill?

A first-task brief is the material your agent uses to understand the product, reader, workflow and evidence. Have a Skill-compatible client with its own model access ready. The Markdown Skill supplies methods; it does not supply a model subscription, a hosted editor or a publishing service.

Read the [repository README](https://github.com/NextVariable/global-growth-content-skill/blob/main/README.md), obtain the repository, and copy the whole skills/global-growth-content directory into the Skill location configured for your client. Keep an existing same-name directory until you have checked it. Do not install only SKILL.md: its references and supporting files belong to the installation unit. Client directory conventions differ, so follow the client you actually use.

The observable setup result is an intact directory containing SKILL.md, six references, a handoff template, agents/openai.yaml and LICENSE. Then confirm that your client discovers global-growth-content. Copying files and discovering a Skill are separate checks—this example does not claim every client has been tested.

## How do an existing goal and a product brief enter the Skill?

The task request is where your existing goal and authorized product brief enter the agent. Start a conversation in the client that has discovered the Skill. Paste the following request and brief together. You can keep a project brief outside the installed Skill directory and provide its content as context; no separate upstream research repository is required.

```text
Use $global-growth-content to write a complete English homepage hero
for Global Positioning & Growth Content.

Goal: help a first-time developer understand the workflow and try one task.
Do not choose another market. Produce one hero, not a full content package.
Include a headline, subheading, primary CTA, secondary CTA and prerequisites.
Separately list claim-to-source mappings and unsupported assumptions.
Do not publish anything.

Product brief:
Name: Global Positioning & Growth Content.
Skill ID: global-growth-content.
Reader: independent developers or small product teams using a
Skill-compatible agent, with an existing target reader and product facts,
who need English product content.
Situation: they have a product brief but need a homepage first screen
that explains what the product is, how it fits the workflow and how to start.

P1: This is a Markdown methods Skill. It turns existing market/customer
judgments, product value and evidence into positioning, pages, README,
search content, social/UGC briefs and requested language adaptations.
Inputs include product facts, reader, workflow, evidence and current goal.
Unsupported outcome claims cannot be presented as facts.
P2: The independent installation unit is skills/global-growth-content:
10 files including 6 references. It has no mandatory business script,
online service or paid API. The host client provides the model and tools.
P3: It drafts content assets. It does not perform publishing, outreach,
ad buying, sales or experiments. Keep ongoing customer records outside
its installed directory.
P4: A 2026-10-10 isolated copy and source/link check found no package errors.
Automatic discovery in all clients and model outcome quality were not tested.
P5: Obtain the repository with Git and copy the whole installation unit to
your client's configured Skill directory; preserve existing same-name files.
No pip/npm package is needed for the Markdown methods themselves.
P6: A first task can invoke $global-growth-content and request only a hero.
P7: MIT licensed. Real destinations:
https://github.com/NextVariable/global-growth-content-skill
https://github.com/NextVariable/global-growth-content-skill/blob/main/README.md
No customer, conversion, timing, pricing or model-quality statistics supplied.

Mechanism: existing brief -> task-specific Skill methods -> agent draft
-> human checks of capabilities, evidence and CTA.
CTA: get the Skill from the repository; read the README to install and start.
```

## What should a first result look like?

A homepage hero is the opening copy that lets a visitor identify the product, recognize their situation and find a next step. Your agent’s wording may differ. The following is an illustrative target based on the supplied brief, not a claim that your client has already generated it.

> **Turn your product brief into English copy you can check.**
>
> For independent developers and small product teams who already know their target readers: bring your product facts, workflow and evidence to a Skill-compatible agent. Global Positioning & Growth Content guides the agent from those inputs to an English homepage hero or another content draft, with unsupported results kept out of your claims.
>
> [Get the Skill on GitHub](https://github.com/NextVariable/global-growth-content-skill) · [Read the setup instructions](https://github.com/NextVariable/global-growth-content-skill/blob/main/README.md)
>
> MIT licensed. Requires your own Skill-compatible agent and model access. Review the draft before publishing.

The observable result is complete hero text plus a separate claim map. “Markdown Skill” and “brief to content” map to P1; client/model prerequisites map to P2; drafting scope maps to P3; CTA destinations and MIT map to P7. The goal is a reviewable first screen—not proof of conversion uplift.

## How do you check the hero before using it?

A claim check is the comparison between each public statement and the evidence supplied to the agent. Read the headline and subheading without the prompt. Can you identify a Skill rather than a hosted service, its fixed reader, the brief-to-draft mechanism and a real starting point? Then check each capability against P1–P3 and each link against P7.

Reject invented speed percentages, customer counts, “better than ordinary prompts” claims or universal client compatibility. The isolated package result supports packaging only. A generated hero is not customer research or a completed campaign. (The easiest sentence to miss is often a polished promise.)

If a claim has no source, ask: “Revise this hero using only P1–P7. Remove the unsupported result and keep the supported capability.” Save the approved text separately from the installed methods. It becomes your content draft after review—publishing requires its own actual action.

## What if setup or generation fails?

Failure handling is the route from an observable problem to a specific correction. If the Skill is absent in your client, check its configured Skill root, the global-growth-content directory name, the presence of SKILL.md and the complete package. Use the client’s documented refresh or discovery process. The isolated check cannot establish discovery on your machine.

If the agent ignores the Skill, explicitly request $global-growth-content and ask which Skill it used. If it cannot load it, resolve discovery before calling the draft a Skill result. If required references are missing, obtain the complete installation unit again and compare it with the repository; preserve an existing installation before replacing it.

If model access fails, resolve access in your host client; the Skill has no model endpoint to fix. If the draft invents outcomes or changes the audience, resupply the brief and request a source-bounded revision. Your next step is one reviewed hero, then a separately chosen README or content task if needed.

---

# Internal editorial note — exclude from the published tutorial

Reader, situation and purpose are the fixed developer adoption task. P1–P7 provide the entire product evidence set; the date and numeric package facts come from P2/P4, not invented writing benchmarks. The tutorial adapts gr-blog-post's direct answer, traceable key facts, problem-to-case-to-failure structure and FAQs through troubleshooting. It does not fabricate Iris first-person experiences, research datasets, search queries, canonical URLs or multilingual editions. This article is a completed draft, not a published blog. Example output is authored here, not an observed host-client response; discovery and model behavior remain to be verified by the reader. No screenshot or tutorial recording is supplied.

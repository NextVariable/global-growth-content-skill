# Your first task: write a verifiable homepage hero

This tutorial is for an independent developer or small product team with an existing target reader and product facts. You will use Global Positioning & Growth Content to draft a single English homepage hero, then check it against the brief. The example product is this Skill itself. You do not need a second product, a new market study or a complete content campaign.

You need a Skill-capable agent client with its own model access. Obtain the complete `skills/global-growth-content` installation unit from the [public repository and README](https://github.com/NextVariable/global-growth-content-skill#readme). Follow your client's configured Skill-directory convention and confirm the client can discover the package. Installing these Markdown files does not require npm, pip or a paid API for the Skill itself. Your client's model access remains your responsibility. If a package with the same name already exists, preserve and inspect it before making changes. [P2, P5]

## 1. Keep the existing decision in the brief

Create a project document named `product-brief.md` outside the installed Skill directory. Paste the following brief. This is the task input, not a new market conclusion.

```text
Product: Global Positioning & Growth Content
Skill identifier: global-growth-content
Type: Markdown method Skill used inside a Skill-capable agent client.

Existing target-reader decision:
Independent developers and small product teams that already have a target
customer and product facts and need English product content.
This is the adoption task's audience assumption, not validated demand.
Do not choose a different market or claim paying customers.

Page goal:
Help a first-time reader understand what the Skill is and try one
homepage-hero task. The next step is the public repository README.

Workflow:
The user supplies the target reader, product workflow, authorized facts,
supporting evidence and content goal. The agent uses reusable scope and
evidence boundaries plus task-specific guidance to draft content.
The user checks factual claims against the supplied material.

Supported capabilities:
Positioning, pages, developer README, search content, social/UGC briefs
and multilingual rewriting. For this task, produce only an English hero.
The installation unit is skills/global-growth-content and is independent
of other stage packages. It has ten files, including SKILL.md, six
references, one handoff template, agents/openai.yaml and MIT LICENSE.
The client provides the agent model; the Skill does not include credits.

Scope:
No actual publishing, outreach, ad buying, sales or experiment execution.
Generated content is not evidence of market or conversion results.

Proof and limits:
P1: Markdown method, supported content work and required product input.
P2: Independent ten-file package, task-specific references, no required
business scripts or online service.
P3: Content scope ends before distribution, sales and experiments.
P4: A complete package was copied to a temporary isolated Skill directory
on 2026-10-10; entry and internal links had no errors. Automatic discovery
in all clients was not tested. No screenshots or video were supplied.
P5: Use the actual Skill directory configured by the chosen client;
there is no universal installation path. No npm/pip package is required
for using the Markdown Skill.
P6: A real invocation example uses $global-growth-content to rewrite a
homepage hero from authorized facts and an existing target-reader decision.
P7: MIT license and public repository. No customer counts, testimonials,
prices, quality comparisons, time savings or conversion data are available.
The local method version and remote version differed in the shared snapshot;
do not say the latest local methods are already published.

CTA:
Read the README and get the Skill.
https://github.com/NextVariable/global-growth-content-skill#readme
```

Your existing goal enters through “Page goal”; your existing audience decision enters through “Existing target-reader decision.” Neither requires a separate first-stage Skill. A plain-text handoff is enough. Do not put persistent customer documents into the installed method package. [P2, P3, P6]

Observable result: `product-brief.md` contains a fixed reader, a workflow, evidence limits and a usable CTA. Missing customer-performance data is explicitly visible instead of being filled in.

## 2. Confirm the Skill is available

Use your client's documented way to see available Skills. Look for `global-growth-content`. If your client requires refreshing its available-Skill view, follow that client's instructions. Do not assume that writing the invocation proves discovery.

The shared installation record verified copying and internal links only. It did not verify automatic discovery by your client. If you cannot confirm availability, stop here and check the configured directory and package completeness. Do not present an ordinary model response as a verified Skill run. [P4, P5]

Observable result: the client exposes the installed Skill or otherwise confirms it is available according to its own interface.

## 3. Give the agent the brief and one output task

Attach or paste `product-brief.md` using your client's supported file-input mechanism, then send:

```text
Use $global-growth-content.

Use the attached product-brief.md as the authorized product input and
existing target-reader decision. The product is this Skill itself.

Write one complete English homepage hero: eyebrow, headline, subheading,
supporting copy, primary CTA label and URL, and visible use conditions.
Help a first-time reader understand the product's category, workflow and
next step. Do not choose another market or expand into a campaign.

Use capability claims only where the brief supports them. Do not promise
better quality, time savings, adoption numbers or conversion results.
Put source IDs P1-P7 and any unresolved evidence questions in a separate
review note. Keep necessary client/model and publishing conditions in
the public copy. Do not publish anything.
```

Observable result: the agent produces complete hero copy and a separate review note. It should use the supplied audience and repository CTA. It should not ask you to buy the product or invent a performance statistic. Model output can vary, so check the content rather than expecting identical wording. [P1, P6, P7]

## 4. Check the first screen against the facts

Read it as someone encountering the product for the first time. Can you identify a Markdown Skill, understand that your product brief is the input, see what the agent drafts and find the actual README next step? Then read every factual claim against the brief.

A permissible illustrative hero is:

> **A Markdown Skill for product positioning and content**
>
> **Make your product workflow clear from the first screen.**
>
> Turn your existing target-reader decision and product facts into positioning and English product content inside your Skill-capable agent client, using reusable task guidance and evidence boundaries.
>
> Start with one homepage hero. Bring the brief, review the claims and decide what to use.
>
> **Read the README and get the Skill**
>
> Requires a Skill-capable client with its own agent model. The Skill does not include model credits or automatic publishing.

Link the CTA to the URL in the brief. This example is drafted tutorial copy, not a recorded output from a verified client run.

If the result promises “50% faster” or “higher conversion,” request removal because the brief contains no supporting measurement. If it says “SaaS” or “website builder,” ask for correction to “Markdown method Skill.” If it selects another audience, restate the fixed decision and request only the hero. If the CTA offers a free trial or checkout, replace it with the real README link.

Observable result: each factual statement has a source in the brief, necessary use conditions remain visible and unsupported effect claims have been removed. A good-looking draft alone is not that check.

## 5. Save the draft with its review note

Save approved copy as `homepage-hero.md` in your project, alongside the brief and source notes. Keep any unverified audience or effect assumptions in `hero-review.md`. Your first task is complete when you have a full hero, a working repository next step and a record of the claims you checked. No publishing, customer outcome or conversion improvement has been verified by this exercise. [P3, P7]

If you later need another asset, give the Skill that asset's reader, purpose and constraints. You do not have to generate a complete package for this first task.

## Internal production note

Sources: P1-P7 supplied in the common product evidence. The tutorial commands are limited to the documented `$global-growth-content` invocation; file attachment and discovery are client-specific. No client was operated for this draft, and the illustrative hero is not an observed Skill execution. The brief uses only authorized facts about this Skill. The next real validation is client discovery followed by one run and a claim review.

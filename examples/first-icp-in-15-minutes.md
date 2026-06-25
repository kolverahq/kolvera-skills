# Your First ICP in 15 Minutes

A step-by-step walkthrough for first-time Kolvera users. By the end, you will have a target market defined, companies discovered, and your first prospects identified.

## Before you start

→ Kolvera account active (any plan)
→ Kolvera MCP server connected to Claude ([kolvera.io/guide/claude](https://kolvera.io/guide/claude))
→ Skills from this repo installed in your Claude skills directory

## Minute 0-2: Set up your business context

Paste this into Claude:

```
Build my business context from [your-website-url] and set it as primary.
```

This tells Kolvera who you are, what you sell, and how you sound. Every ICP and campaign inherits from this.

## Minute 2-5: Create your ICP

```
Generate an ICP titled "[Your Market Name]" targeting [industry or buyer type], using my primary business context. Then show me the full profile.
```

Example:
```
Generate an ICP titled "AU HR Tech — Decision Makers" targeting HR technology companies in Australia with 20-500 employees, using my primary business context. Then show me the full profile.
```

Claude will create the ICP with target titles, industries, pain points, outreach hooks, and more. Review the output and ask Claude to tighten anything that looks too broad.

## Minute 5-10: Run Deep Research

```
Run Deep Research against my ICP. Wait for it to finish, then show me the results summary and company count.
```

This typically finds 15-40 companies on the first run (3 credits). If you want more:

```
Run one more expand and show me the trend.
```

Each expand costs 2 credits and finds additional companies.

## Minute 10-13: Find decision-makers

```
Find contacts at the top 10 companies in my ICP. Start with companies that have 50+ employees.
```

This runs async (8-12 minutes for a full batch). Claude will poll automatically and report results.

## Minute 13-15: Review what you have

```
Show me a summary: how many companies in the ICP, how many contacts found, how many have valid emails, and which companies still need contacts.
```

## What's next

→ **Run job board scrapes** to find companies actively hiring: "Scrape SEEK and LinkedIn for my ICP"
→ **Build hot lists** to segment prospects: "Build hot lists by vertical for my ICP"
→ **Launch a campaign** to start outreach: "Build a campaign for my top hot list"

Each of these has a dedicated skill in this repo. Say the trigger phrase and Claude runs the full workflow.

"""
Seed data for Insight articles.
Each entry maps directly to the Insight model fields.
Blocks follow Editor.js JSON format: { time, version, blocks: [...] }
"""

INSIGHTS_DATA = [
    {
        "title": "Why Most Dubai Fit-Out Projects Go Over Budget — And How to Prevent It",
        "slug": "why-dubai-fitout-projects-go-over-budget",
        "excerpt": (
            "The gap between initial quote and final invoice is one of the most common frustrations "
            "in the Dubai fit-out industry. We break down exactly where costs escalate, and the "
            "structural decisions that keep our projects on budget."
        ),
        "category": "interior",
        "cover_image_url": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?q=80&w=1800&auto=format",
        "read_time": 7,
        "is_featured": True,
        "status": "published",
        "blocks": {
            "time": 1710000000000,
            "version": "2.28.0",
            "blocks": [
                {
                    "id": "p1",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "In 12 months of delivering fit-out projects across Dubai, we have seen a consistent "
                            "pattern: clients who came to us after a previous project went wrong. The common thread "
                            "in almost every case was not poor design, bad materials, or even incompetent workmanship. "
                            "It was a breakdown in the financial structure of the project from the very beginning."
                        )
                    },
                },
                {
                    "id": "p2",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "This article is for property owners, investors, and businesses who want to understand "
                            "the mechanics of budget overrun — before they start a project, not after."
                        )
                    },
                },
                {
                    "id": "h1",
                    "type": "header",
                    "data": {"text": "The Quote Problem: What Most Clients Don't Realise", "level": 2},
                },
                {
                    "id": "p3",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "A fit-out quote is not a fixed price. In the UAE market, many quotes are structured to "
                            "win the contract, not to reflect the actual cost of delivery. The initial number is low "
                            "enough to be attractive; the final invoice is a different story entirely."
                        )
                    },
                },
                {
                    "id": "p4",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "This is not always malicious. Fit-out pricing is genuinely complex — material costs "
                            "fluctuate, authority approval requirements change, and design ambiguities get resolved "
                            "(expensively) during construction. But the client bears the risk of all of this when "
                            "the contract structure does not clearly define scope, inclusions, and variation procedures."
                        )
                    },
                },
                {
                    "id": "q1",
                    "type": "quote",
                    "data": {
                        "text": (
                            "A quote that wins the job and a quote that reflects the real cost of delivering it "
                            "are often two very different documents."
                        ),
                        "caption": "LuxSpace Project Management Team",
                        "alignment": "left",
                    },
                },
                {
                    "id": "h2",
                    "type": "header",
                    "data": {"text": "The 5 Most Common Budget Overruns", "level": 2},
                },
                {
                    "id": "l1",
                    "type": "list",
                    "data": {
                        "style": "ordered",
                        "items": [
                            (
                                "<b>Undefined scope at contract stage.</b> If the contract doesn't specify exactly "
                                "what is included — down to finishes, fixtures, and hardware — anything unspecified "
                                "becomes a variation charge later."
                            ),
                            (
                                "<b>Authority approval costs excluded from the quote.</b> Dubai Municipality, DDA, "
                                "Trakhees, and DEWA fees are often excluded from initial quotes as 'client-direct' "
                                "costs. These can run AED 20,000–80,000+ on a mid-size project."
                            ),
                            (
                                "<b>Material upgrades mid-project.</b> When specifications are vague, clients make "
                                "upgrade decisions during construction. Each decision adds cost and often extends the timeline."
                            ),
                            (
                                "<b>Structural discoveries after walls open.</b> Old MEP routing, unexpected waterproofing "
                                "issues, or undocumented structural elements — none of these are visible before work starts."
                            ),
                            (
                                "<b>Late design changes.</b> Changing a layout or finish after material orders are placed "
                                "typically results in restocking fees, new procurement lead times, and wasted labour."
                            ),
                        ],
                    },
                },
                {
                    "id": "h3",
                    "type": "header",
                    "data": {"text": "How a Structured Delivery Model Prevents It", "level": 2},
                },
                {
                    "id": "p5",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "At LuxSpace, we operate a structured delivery model that addresses these failure points "
                            "directly. It is not complicated — it is disciplined."
                        )
                    },
                },
                {
                    "id": "h4",
                    "type": "header",
                    "data": {"text": "Full Design Resolution Before Contract", "level": 3},
                },
                {
                    "id": "p6",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "We do not issue a final contract price until the design is fully resolved. This means "
                            "every material is specified, every layout decision is made, and every authority submission "
                            "is planned. The quote you receive is the price you pay."
                        )
                    },
                },
                {
                    "id": "h5",
                    "type": "header",
                    "data": {"text": "Authority Approval Costs Always Included", "level": 3},
                },
                {
                    "id": "p7",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "All permit fees, NOC requirements, and submission costs are calculated and included in "
                            "the project budget before we start. No surprises from DM, DDA, or DEWA during construction."
                        )
                    },
                },
                {
                    "id": "h6",
                    "type": "header",
                    "data": {"text": "What to Ask Before You Sign a Contract", "level": 2},
                },
                {
                    "id": "l2",
                    "type": "list",
                    "data": {
                        "style": "unordered",
                        "items": [
                            "Are authority approval fees included in this quote, or will they be billed separately?",
                            "Is this a fixed-price contract or a cost-plus arrangement?",
                            "What is the variation procedure — and is it in writing?",
                            "Has the design been fully resolved, or will decisions be made during construction?",
                            "What contingency has been built in for structural unknowns?",
                            "Can you show me a schedule of materials with specified grades and brands?",
                        ],
                    },
                },
                {
                    "id": "p8",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "A contractor who cannot answer these questions clearly is a contractor whose final "
                            "invoice will differ significantly from their quote. If you are planning a fit-out project "
                            "in Dubai and want a proposal that is structured, transparent, and fixed — speak to our "
                            "team. We'll give you a clear scope, timeline, and budget within 48 hours."
                        )
                    },
                },
            ],
        },
    },
    {
        "title": "Designing Outdoor Spaces for Dubai's Climate: What Actually Works",
        "slug": "designing-outdoor-spaces-dubai-climate",
        "excerpt": (
            "Most landscaping fails in Dubai within 3 years. The issue isn't budget — "
            "it's material and plant selection for extreme heat and humidity."
        ),
        "category": "landscape",
        "cover_image_url": "https://images.unsplash.com/photo-1559767949-0faa5c7e9992?q=80&w=1800&auto=format",
        "read_time": 6,
        "is_featured": False,
        "status": "published",
        "blocks": {
            "time": 1710000000000,
            "version": "2.28.0",
            "blocks": [
                {
                    "id": "p1",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "The UAE climate presents a unique challenge for landscape designers: temperatures that "
                            "regularly exceed 45°C, humidity levels that can reach 90% overnight, and UV radiation "
                            "that degrades most organic materials in under two years. The majority of landscaping "
                            "projects that fail don't fail because of budget — they fail because the wrong materials "
                            "and plants were specified."
                        )
                    },
                },
                {
                    "id": "h1",
                    "type": "header",
                    "data": {"text": "The Most Common Landscaping Failures in Dubai", "level": 2},
                },
                {
                    "id": "l1",
                    "type": "list",
                    "data": {
                        "style": "unordered",
                        "items": [
                            "Timber decking that warps and splits within 18 months of installation",
                            "Irrigation systems designed for temperate climates that cannot cope with UAE evaporation rates",
                            "Plant species that thrive in Europe or Asia but cannot survive UAE summers",
                            "Shade structures made from canvas or lightweight materials that deteriorate rapidly in UV exposure",
                            "Topsoil selection that drains too slowly or retains too much salt",
                        ],
                    },
                },
                {
                    "id": "h2",
                    "type": "header",
                    "data": {"text": "Materials That Actually Last", "level": 2},
                },
                {
                    "id": "p2",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "For hardscape in the UAE, the specification choices are narrower than most clients expect. "
                            "Porcelain tile (minimum 20mm thickness), composite decking (not natural timber), and "
                            "powder-coated or marine-grade stainless steel for metalwork are the only materials we "
                            "can reliably specify for outdoor use. Natural stone is excellent for paving where drainage "
                            "is properly managed."
                        )
                    },
                },
                {
                    "id": "h3",
                    "type": "header",
                    "data": {"text": "Plant Selection for UAE Conditions", "level": 2},
                },
                {
                    "id": "p3",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "Native and adapted species are the only reliable choice for UAE gardens. Ghaf trees, "
                            "date palms, bougainvillea, and lantana are proven performers. Succulents and cacti work "
                            "well in areas with minimal irrigation access. The temptation to specify lush tropical "
                            "planting — which looks spectacular in a 3D render — almost always results in a dead "
                            "garden within two seasons."
                        )
                    },
                },
                {
                    "id": "q1",
                    "type": "quote",
                    "data": {
                        "text": (
                            "We always ask the client: do you want it to look great in photographs next month, "
                            "or do you want it to look great for the next ten years? The answer determines the "
                            "entire specification."
                        ),
                        "caption": "LuxSpace Landscaping Team",
                        "alignment": "left",
                    },
                },
                {
                    "id": "h4",
                    "type": "header",
                    "data": {"text": "Irrigation: The Detail Most Designers Get Wrong", "level": 2},
                },
                {
                    "id": "p4",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "Dubai's evaporation rates are among the highest in the world. A drip irrigation system "
                            "designed for Mediterranean conditions will fail in the UAE — plants will die mid-summer "
                            "even when watering runs are doubled. Systems need to be designed specifically for UAE "
                            "conditions: deep watering schedules, anti-clog emitters, and pressure-compensating heads "
                            "on all zones exposed to direct sun."
                        )
                    },
                },
            ],
        },
    },
    {
        "title": "Authority Approvals in Dubai: A Complete Guide for Property Owners",
        "slug": "authority-approvals-dubai-complete-guide",
        "excerpt": (
            "NOC letters, DM permits, Trakhees vs DDA — the approval process in Dubai is complex. "
            "This is what you actually need to know before you start any construction or fit-out work."
        ),
        "category": "guides",
        "cover_image_url": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?q=80&w=1800&auto=format",
        "read_time": 8,
        "is_featured": False,
        "status": "published",
        "blocks": {
            "time": 1710000000000,
            "version": "2.28.0",
            "blocks": [
                {
                    "id": "p1",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "Before any construction, fit-out, or significant renovation work can begin in Dubai, "
                            "you will need permissions from one or more authorities. The specific approvals required "
                            "depend on where your property is located, what type of work you're doing, and who owns "
                            "the land. Missing a step costs time — sometimes weeks — and can result in stop-work orders."
                        )
                    },
                },
                {
                    "id": "h1",
                    "type": "header",
                    "data": {"text": "Understanding Dubai's Regulatory Structure", "level": 2},
                },
                {
                    "id": "l1",
                    "type": "list",
                    "data": {
                        "style": "unordered",
                        "items": [
                            "<b>Dubai Municipality (DM)</b> — responsible for most of mainland Dubai, including most residential and commercial properties",
                            "<b>Trakhees</b> — regulatory authority for Dubai World, DP World, and Jebel Ali Port areas",
                            "<b>Dubai Development Authority (DDA)</b> — responsible for freehold zones including the creative district",
                            "<b>DEWA</b> — required for any electrical or plumbing works regardless of area",
                            "<b>Civil Defence</b> — required for fire safety compliance on all commercial fit-outs",
                        ],
                    },
                },
                {
                    "id": "h2",
                    "type": "header",
                    "data": {"text": "The Typical Approval Timeline", "level": 2},
                },
                {
                    "id": "p2",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "For a straightforward residential fit-out in a DM-regulated area, expect a minimum of "
                            "3–4 weeks to obtain the necessary NOC letters and permit. For commercial projects, DEWA "
                            "approvals, or anything in a free zone, allow 6–10 weeks minimum. These timelines assume "
                            "all paperwork is submitted correctly the first time — which rarely happens without "
                            "experienced consultants."
                        )
                    },
                },
                {
                    "id": "q1",
                    "type": "quote",
                    "data": {
                        "text": (
                            "Every delayed approval adds cost. When we include approval management in our projects, "
                            "we build the timeline in from the start — not as an afterthought."
                        ),
                        "caption": "LuxSpace Approvals Team",
                        "alignment": "left",
                    },
                },
                {
                    "id": "h3",
                    "type": "header",
                    "data": {"text": "What Documents You'll Need", "level": 2},
                },
                {
                    "id": "l2",
                    "type": "list",
                    "data": {
                        "style": "unordered",
                        "items": [
                            "Title deed or tenancy contract (Ejari for residential)",
                            "Approved architectural drawings (typically A1 format, stamped by a registered consultant)",
                            "Trade licence of the fit-out contractor",
                            "Undertaking letter from the building developer (most buildings require this)",
                            "DEWA no-objection if electrical modifications are planned",
                            "Civil Defence submission for commercial projects with fire suppression changes",
                        ],
                    },
                },
                {
                    "id": "h4",
                    "type": "header",
                    "data": {"text": "How LuxSpace Handles Approvals", "level": 2},
                },
                {
                    "id": "p3",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "Our approvals team manages the entire process from submission to permit issuance. "
                            "We work with registered consultants for drawing stamping, handle all DM / Trakhees / "
                            "DDA submissions, coordinate DEWA approvals for MEP works, and track progress against "
                            "your project timeline. You receive a copy of every approval document as it's issued."
                        )
                    },
                },
            ],
        },
    },
    {
        "title": "Custom Joinery vs. Off-the-Shelf: What's Worth the Premium?",
        "slug": "custom-joinery-vs-off-the-shelf",
        "excerpt": (
            "For high-end properties, the difference in longevity and finish quality is significant. "
            "We break down when bespoke joinery justifies the cost — and when it doesn't."
        ),
        "category": "joinery",
        "cover_image_url": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?q=80&w=1800&auto=format",
        "read_time": 4,
        "is_featured": False,
        "status": "published",
        "blocks": {
            "time": 1710000000000,
            "version": "2.28.0",
            "blocks": [
                {
                    "id": "p1",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "Joinery is one of the most visible elements of any interior. It's also one of the most "
                            "misunderstood in terms of pricing. Clients frequently ask us why a set of custom wardrobes "
                            "costs three times more than the same configuration from a European flat-pack brand. The "
                            "answer has less to do with materials and more to do with how the piece is made and what "
                            "happens to it over ten years."
                        )
                    },
                },
                {
                    "id": "h1",
                    "type": "header",
                    "data": {"text": "Where Off-the-Shelf Joinery Falls Short", "level": 2},
                },
                {
                    "id": "l1",
                    "type": "list",
                    "data": {
                        "style": "unordered",
                        "items": [
                            "Fixed dimensions that rarely match non-standard room proportions or ceiling heights",
                            "Visible filler pieces and workarounds where units don't meet walls cleanly",
                            "Hardware downgraded to reduce manufacturing cost (hinges, drawer runners, soft-close mechanisms)",
                            "Limited finish options — you get what's in the catalogue",
                            "No adaptation for in-wall electrical, HVAC, or structural obstructions",
                        ],
                    },
                },
                {
                    "id": "h2",
                    "type": "header",
                    "data": {"text": "When Custom Joinery Makes Sense", "level": 2},
                },
                {
                    "id": "p2",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "The business case for bespoke joinery is strongest in three situations: when the room "
                            "has non-standard dimensions (very common in Dubai properties where developers prioritise "
                            "square footage over proportional rooms), when the finish requirement is higher than what "
                            "off-the-shelf products offer, and when the joinery needs to integrate with the architecture "
                            "— flush with walls, framing doorways, or accommodating concealed lighting."
                        )
                    },
                },
                {
                    "id": "q1",
                    "type": "quote",
                    "data": {
                        "text": (
                            "The premium for custom joinery is real. But in a property valued above AED 3M, "
                            "the visual and tactile quality difference between bespoke and catalogue joinery is "
                            "immediately apparent to every buyer or tenant."
                        ),
                        "caption": "LuxSpace Joinery Workshop",
                        "alignment": "left",
                    },
                },
                {
                    "id": "h3",
                    "type": "header",
                    "data": {"text": "Material Choices and Their Lifespans", "level": 2},
                },
                {
                    "id": "p3",
                    "type": "paragraph",
                    "data": {
                        "text": (
                            "Our workshop uses E0-rated MDF core for all cabinet carcasses (formaldehyde-free, "
                            "essential in Dubai's sealed interiors), solid hardwood for frames and exposed edges, "
                            "and Austrian Blum hardware throughout. We offer lacquered, veneered, and solid wood "
                            "door fronts depending on budget and finish requirements. All joinery is climate-"
                            "acclimated before installation to prevent movement after fit."
                        )
                    },
                },
            ],
        },
    },
]

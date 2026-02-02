/**
 * RISEby Enterprise Solutions Database (English Version)
 * Professional consulting services for enterprise transformation
 */

// Category Definitions
window.TASK_CATEGORIES = {
  "ai": {
    title: "AI & Generative AI",
    subtitle: "Artificial Intelligence Solutions",
    description: "From experimentation to enterprise value. In an era where GenAI has become critical infrastructure, we help organizations build robust governance frameworks and implement autonomous AI agents at scale.",
    themeColor: "violet",
    insight: {
      trend: {
        title: "Market Perspective: The Rise of Autonomous AI Agents",
        text: "Following the GenAI adoption wave of 2023-24, AI has evolved from a tool that responds to human commands into an autonomous colleague capable of completing complex tasks end-to-end. Organizations are now entering a phase where AI participates in decision-making processes."
      },
      landscape: [
        { label: "Current Challenge", value: "PoC fatigue with limited ROI. Risk aversion preventing enterprise-wide deployment." },
        { label: "Target State", value: "AI agents autonomously executing routine operations while humans focus on oversight and creative work." }
      ],
      approaches: [
        { title: "Advanced RAG Architecture", desc: "Implementing proprietary data retrieval systems to minimize hallucination and ensure accuracy." },
        { title: "AI Governance Framework", desc: "Building compliant yet enabling guidelines that address EU AI Act and global regulatory requirements." },
        { title: "Multi-Agent Orchestration", desc: "Designing systems where multiple AI agents collaborate to complete complex workflows autonomously." }
      ],
      newIssue: {
        title: "Emerging Challenge: The AI Management Gap",
        desc: "Organizations lack middle managers capable of effectively overseeing AI-augmented teams, leading to suboptimal utilization or uncontrolled deployment."
      }
    }
  },
  "strategy": {
    title: "Corporate Strategy & M&A",
    subtitle: "Strategic Transformation",
    description: "Strategic clarity in an age of uncertainty. From portfolio optimization and PBR enhancement to M&A integration and corporate turnaround—we drive decisive executive action.",
    themeColor: "indigo",
    insight: {
      trend: {
        title: "Market Perspective: Dynamic Portfolio Management",
        text: "Two years after TSE's corporate governance reforms, markets now see through superficial shareholder returns. Organizations that demonstrate bold portfolio restructuring—through strategic divestiture and transformative M&A—are capturing premium valuations."
      },
      landscape: [
        { label: "Current Challenge", value: "Conglomerate discount from unfocused diversification. Delayed exit decisions eroding value." },
        { label: "Target State", value: "ROIC-driven resource allocation with agility to shift capital to growth platforms." }
      ],
      approaches: [
        { title: "Strategic Carve-Out", desc: "Separating non-core businesses through partnerships or divestiture to unlock trapped value." },
        { title: "Roll-Up M&A Strategy", desc: "Pursuing sequential acquisitions to achieve scale economies and drive industry consolidation." },
        { title: "Ambidextrous Organization", desc: "Balancing exploitation of existing businesses with exploration of new growth opportunities." }
      ],
      newIssue: {
        title: "Emerging Challenge: Integration Fatigue",
        desc: "Aggressive deal-making without adequate integration resources leads to cultural collision and key talent attrition."
      }
    }
  },
  "dx": {
    title: "Digital Transformation & IT",
    subtitle: "Technology Modernization",
    description: "Beyond the legacy cliff. From technical debt elimination and cloud-native transformation to zero-trust security—building the digital foundation for competitive advantage.",
    themeColor: "cyan",
    insight: {
      trend: {
        title: "Market Perspective: The Final Phase of Legacy Modernization",
        text: "The long-anticipated 'legacy cliff' has arrived. With SAP ECC end-of-support approaching, enterprises face a decisive moment: modernize or risk obsolescence. Cloud-native architecture is now a prerequisite for competitive relevance."
      },
      landscape: [
        { label: "Current Challenge", value: "Black-boxed core systems. Vendor dependency driving unsustainable cost structures." },
        { label: "Target State", value: "Loosely-coupled, microservices-based architecture enabling business agility." }
      ],
      approaches: [
        { title: "Progressive Modernization", desc: "Leveraging existing assets while incrementally adopting cloud technologies." },
        { title: "Engineering Insourcing", desc: "Building internal agile development capabilities to reduce vendor dependency." },
        { title: "Zero Trust Security", desc: "Implementing identity-centric security architecture with 'never trust, always verify' principles." }
      ],
      newIssue: {
        title: "Emerging Challenge: Cloud Cost Overruns",
        desc: "Naive lift-and-shift migrations result in uncontrolled consumption-based costs exceeding on-premise expenditure."
      }
    }
  },
  "data": {
    title: "Data & Analytics",
    subtitle: "Data-Driven Enterprise",
    description: "From intuition to intelligence. Building the data foundation and analytical culture that transforms decision-making across the organization.",
    themeColor: "blue",
    insight: {
      trend: {
        title: "Market Perspective: Data Mesh and Democratization",
        text: "Centralized data management is giving way to distributed ownership. Organizations are embracing data mesh principles while investing in high-quality data fabrics that enable AI at scale."
      },
      landscape: [
        { label: "Current Challenge", value: "Siloed data across business units. Poor data quality limiting AI applicability." },
        { label: "Target State", value: "Self-service data access enabling data-driven decisions at all levels." }
      ],
      approaches: [
        { title: "Enterprise Data Management", desc: "Implementing MDM and data cataloging to ensure data quality and discoverability." },
        { title: "Analytics Capability Building", desc: "Enabling business users beyond specialists to leverage BI tools effectively." },
        { title: "Data Monetization", desc: "Creating new revenue streams through external data products or enhanced service offerings." }
      ],
      newIssue: {
        title: "Emerging Challenge: Governance Erosion",
        desc: "Data democratization without proper guardrails leads to conflicting KPIs and privacy compliance risks."
      }
    }
  },
  "hr": {
    title: "Human Capital & Organization",
    subtitle: "Workforce Transformation",
    description: "Activating human capital. From skills-based talent models and succession planning to engagement enhancement—building the organization of the future.",
    themeColor: "orange",
    insight: {
      trend: {
        title: "Market Perspective: Hybrid Talent Models",
        text: "Pure job-based employment has shown limitations. Organizations are now adopting hybrid approaches that preserve collaborative culture while rewarding specialized expertise. Human capital disclosure has evolved from compliance to competitive differentiation."
      },
      landscape: [
        { label: "Current Challenge", value: "Seniority-based systems driving top talent attrition. Difficulty attracting digital specialists." },
        { label: "Target State", value: "Performance and role-based rewards driving engagement across all demographics." }
      ],
      approaches: [
        { title: "Role Architecture", desc: "Defining clear accountabilities while maintaining organizational flexibility." },
        { title: "Strategic Reskilling", desc: "Learning through real transformation projects rather than classroom training." },
        { title: "Succession Pipeline", desc: "Data-driven identification and accelerated development of future leaders." }
      ],
      newIssue: {
        title: "Emerging Challenge: Purpose Fatigue",
        desc: "Espoused corporate purpose without aligned practices leads to cynicism and disengagement."
      }
    }
  },
  "scm": {
    title: "Operations & Supply Chain",
    subtitle: "Operational Excellence",
    description: "Resilience meets efficiency. Building robust supply networks, addressing logistics constraints, and digitizing manufacturing operations.",
    themeColor: "emerald",
    insight: {
      trend: {
        title: "Market Perspective: Autonomous Supply Networks",
        text: "Post-logistics crisis, supply chain has transformed from cost center to strategic asset. Organizations are investing in AI-powered autonomous supply chains that self-adjust to demand fluctuations and risk signals."
      },
      landscape: [
        { label: "Current Challenge", value: "Limited visibility causing inventory imbalances. Driver shortages threatening delivery performance." },
        { label: "Target State", value: "End-to-end digitally connected supply network with built-in resilience." }
      ],
      approaches: [
        { title: "Integrated S&OP", desc: "Synchronizing demand and supply planning to optimize inventory and profitability." },
        { title: "Collaborative Logistics", desc: "Shared transportation and warehousing networks to improve utilization." },
        { title: "Smart Manufacturing", desc: "Digitizing craftsman expertise to maintain quality amid labor constraints." }
      ],
      newIssue: {
        title: "Emerging Challenge: Economic Security Imperatives",
        desc: "Geopolitical risk demands supply diversification and friend-shoring despite cost implications."
      }
    }
  },
  "sustainability": {
    title: "Sustainability & Risk",
    subtitle: "Sustainable Enterprise",
    description: "ESG as competitive advantage. From decarbonization and circular economy to economic security—transforming sustainability into business value.",
    themeColor: "teal",
    insight: {
      trend: {
        title: "Market Perspective: From Disclosure to Value Creation",
        text: "Sustainability has evolved from compliance reporting to strategic value creation (SX). With carbon pricing on the horizon, organizations are not only measuring Scope 3 emissions but building circular business models as new profit centers."
      },
      landscape: [
        { label: "Current Challenge", value: "Disclosure burden increasing. Green premium difficult to pass through." },
        { label: "Target State", value: "Sustainability initiatives directly driving brand value and market expansion." }
      ],
      approaches: [
        { title: "Internal Carbon Pricing", desc: "Embedding carbon cost into investment decisions to accelerate decarbonization." },
        { title: "Circular Business Models", desc: "Product take-back and resource recovery systems reducing raw material risk." },
        { title: "Human Rights Due Diligence", desc: "Supply chain monitoring to prevent reputation and regulatory risk." }
      ],
      newIssue: {
        title: "Emerging Challenge: Greenwashing Scrutiny",
        desc: "Regulatory enforcement against unsubstantiated environmental claims intensifies globally."
      }
    }
  }
};

window.TASK_DATABASE = {
  // =================================================================
  // 1. AI & Generative AI
  // =================================================================
  "ai_strategy": {
    categoryId: "ai",
    category: "AI & Generative AI",
    title: "AI Strategy & Roadmap",
    subtitle: "From tactical experiments to strategic transformation",
    themeColor: "violet",
    hero: {
      badge: "For C-Suite & Strategy Leaders",
      description: "Is AI adoption becoming an end in itself? We connect business imperatives with technical feasibility to build enterprise AI roadmaps that maximize return on investment.",
      stats: [
        { label: "Strategy Gap", value: "Siloed Initiatives" },
        { label: "Investment", value: "Unclear ROI" },
        { label: "Technology", value: "Rapid Evolution" }
      ]
    },
    painPoints: [
      { title: "Fragmented AI Initiatives", desc: "Business units deploying tools independently, creating data silos and duplicated efforts.", icon: "Map" },
      { title: "Use Case Scarcity", desc: "Executive mandates to 'use AI' without clear business problems to solve.", icon: "Search" },
      { title: "Expectation Mismatch", desc: "Leadership expecting transformative results from early-stage pilots, leading to premature abandonment.", icon: "BarChart" }
    ],
    structuralIssues: [
      { title: "Organizational Silos", desc: "Departmental budget ownership eliminates incentives for data sharing, confining AI impact to local optimizations rather than enterprise transformation.", icon: "Map" },
      { title: "Risk-Averse Culture", desc: "Performance systems rewarding error avoidance over innovation discourage the experimentation essential for AI adoption.", icon: "Search" },
      { title: "Executive-Operational Disconnect", desc: "Leadership views AI as a silver bullet while frontlines face data quality realities. Without common language, productive investment discussions fail.", icon: "BarChart" }
    ],
    solutions: [
      { phase: "Phase 1", title: "AI Maturity Assessment", desc: "Evaluating data infrastructure, talent capabilities, and governance readiness to establish baseline." },
      { phase: "Phase 2", title: "Use Case Prioritization", desc: "Scoring opportunities on technical feasibility and business impact to focus resources." },
      { phase: "Phase 3", title: "Strategic Roadmap", desc: "Designing short-term quick wins alongside long-term competitive differentiation." }
    ],
    caseStudies: [
      {
        industry: "Financial Services",
        title: "Enterprise AI Roadmap",
        problem: "Duplicated investments across business units.",
        result: "Shared platform and prioritization improved investment efficiency by 30%."
      },
      {
        industry: "Manufacturing",
        title: "AI Opportunity Assessment",
        problem: "Frontline resistance to AI adoption.",
        result: "Started with quality inspection—visible wins drove broader adoption."
      },
      {
        industry: "Trading Company",
        title: "AI Investment Governance",
        problem: "Pilots continuing without exit criteria.",
        result: "Stage-gate process enabled resource concentration on high-potential initiatives."
      }
    ]
  },

  "gen_ai_implementation": {
    categoryId: "ai",
    category: "AI & Generative AI",
    title: "Generative AI Implementation",
    subtitle: "Enterprise-grade LLM deployment",
    themeColor: "violet",
    hero: {
      badge: "For IT & Operations Leaders",
      description: "Moving beyond ChatGPT pilots. We build secure RAG environments that leverage proprietary data while mitigating hallucination and data security risks.",
      stats: [
        { label: "Efficiency", value: "Up to 50% Gains" },
        { label: "Accuracy", value: "Hallucination Risk" },
        { label: "Differentiation", value: "Proprietary Data" }
      ]
    },
    painPoints: [
      { title: "Limited Business Relevance", desc: "Generic LLMs cannot answer company-specific questions, limiting practical utility.", icon: "MessageSquare" },
      { title: "Hallucination Exposure", desc: "Confident but incorrect outputs create unacceptable risk for client-facing or decision-critical applications.", icon: "AlertTriangle" },
      { title: "Capability Concentration", desc: "Benefits captured only by power users, failing to lift organizational productivity.", icon: "User" }
    ],
    structuralIssues: [
      { title: "Tacit Knowledge Gap", desc: "Institutional knowledge exists only in experts' minds—unavailable for AI learning. Analog culture, not technology, is the true barrier.", icon: "MessageSquare" },
      { title: "Zero-Defect Expectations", desc: "Processes designed for 100% accuracy cannot accommodate probabilistic AI outputs. Workflow redesign with human-in-the-loop is essential.", icon: "AlertTriangle" },
      { title: "Learning Time Deficit", desc: "Constant operational demands prevent skill development. Organizations must explicitly allocate time for AI capability building.", icon: "User" }
    ],
    solutions: [
      { phase: "Phase 1", title: "RAG Architecture", desc: "Building secure retrieval systems that ground responses in verified enterprise content." },
      { phase: "Phase 2", title: "Prompt Engineering", desc: "Developing task-specific prompt templates that standardize effective usage." },
      { phase: "Phase 3", title: "Workflow Integration", desc: "Embedding AI into business processes through API integration, beyond chat interfaces." }
    ],
    caseStudies: [
      {
        industry: "Contact Center",
        title: "Agent Assist & Summarization",
        problem: "Long hold times and post-call processing delays.",
        result: "Automated knowledge retrieval and call summarization reduced handling time 40%."
      },
      {
        industry: "Software Development",
        title: "Code Generation & Documentation",
        problem: "Legacy code comprehension consuming excessive time.",
        result: "AI-powered code explanation and documentation doubled maintenance efficiency."
      },
      {
        industry: "Legal Department",
        title: "Contract Review Automation",
        problem: "Standard contract reviews consuming senior attorney time.",
        result: "Automated risk clause extraction reduced initial review time 70%."
      }
    ]
  },

  "ai_governance": {
    categoryId: "ai",
    category: "AI & Generative AI",
    title: "AI Governance & Risk",
    subtitle: "From prohibition to controlled enablement",
    themeColor: "violet",
    hero: {
      badge: "For Legal, Risk & CISO",
      description: "Copyright exposure, data leakage, algorithmic bias. We build governance frameworks that manage AI-specific risks while enabling innovation, aligned with EU AI Act and global regulations.",
      stats: [
        { label: "Shadow AI", value: "Unauthorized Use" },
        { label: "Legal Risk", value: "IP & Privacy" },
        { label: "Compliance", value: "EU AI Act" }
      ]
    },
    painPoints: [
      { title: "Policy Vacuum", desc: "Absent guidelines lead employees to input sensitive data into consumer AI tools.", icon: "ShieldAlert" },
      { title: "IP & Copyright Exposure", desc: "No process to verify AI outputs against existing intellectual property rights.", icon: "FileText" },
      { title: "Explainability Gap", desc: "Black-box AI decisions undermine regulatory compliance and stakeholder accountability.", icon: "HelpCircle" }
    ],
    structuralIssues: [
      { title: "Productivity vs. Security Tension", desc: "Conflicting mandates to 'increase efficiency' and 'avoid risk' drive shadow AI adoption. Prohibition without secure alternatives fails.", icon: "ShieldAlert" },
      { title: "Cross-Functional Expertise Gap", desc: "Legal lacks technical depth; IT lacks regulatory knowledge. AI governance requires integrated capabilities that current structures don't support.", icon: "FileText" },
      { title: "Accountability Ambiguity", desc: "Unclear ownership when AI fails—developer, user, or manager—creates organizational paralysis.", icon: "HelpCircle" }
    ],
    solutions: [
      { phase: "Phase 1", title: "AI Usage Policy", desc: "Defining data classification frameworks and acceptable use guidelines." },
      { phase: "Phase 2", title: "Secure AI Environment", desc: "Deploying private instances with data isolation and comprehensive logging." },
      { phase: "Phase 3", title: "AI Ethics Review Board", desc: "Establishing pre-deployment review processes to prevent high-risk applications." }
    ],
    caseStudies: [
      {
        industry: "Financial Services",
        title: "AI Governance Framework",
        problem: "Enterprise-wide AI prohibition due to security concerns.",
        result: "Secure environment with audit trail enabled controlled adoption."
      },
      {
        industry: "Media",
        title: "IP Risk Management",
        problem: "Unclear rights for generated content.",
        result: "Legal review workflow reduced commercial use risk."
      },
      {
        industry: "Global Manufacturing",
        title: "Multi-Jurisdiction Compliance",
        problem: "EU AI Act readiness lagging at European subsidiaries.",
        result: "Global AI ethics policy strengthened compliance posture."
      }
    ]
  },

  // =================================================================
  // 2. Corporate Strategy & M&A
  // =================================================================
  "portfolio_transformation": {
    categoryId: "strategy",
    category: "Corporate Strategy & M&A",
    title: "Portfolio Transformation",
    subtitle: "Breaking free from conglomerate discount",
    themeColor: "indigo",
    hero: {
      badge: "For CEOs & CFOs",
      description: "When capital allocation is frozen by organizational politics, shareholder value erodes. We drive decisive portfolio restructuring to escape sub-1x PBR and build sustainable enterprise value.",
      stats: [
        { label: "Market Discount", value: "Sub-1x PBR" },
        { label: "Resource Lock", value: "Static Allocation" },
        { label: "Value Erosion", value: "Delayed Exits" }
      ]
    },
    painPoints: [
      { title: "Capital Allocation Paralysis", desc: "Organizational politics prevent shifting resources from legacy to growth businesses.", icon: "Anchor" },
      { title: "Carve-Out Complexity", desc: "System dependencies and workforce transitions create insurmountable execution barriers.", icon: "Scissors" },
      { title: "Investor Communication Gap", desc: "Unable to articulate compelling growth narrative to counter conglomerate discount.", icon: "TrendingDown" }
    ],
    structuralIssues: [
      { title: "Business Unit Entrenchment", desc: "Divisional leaders protecting headcount and revenue base override enterprise optimization.", icon: "Anchor" },
      { title: "Legacy Business Attachment", desc: "Emotional ties to founding businesses or predecessor initiatives prevent rational exit decisions.", icon: "Scissors" },
      { title: "Short-Term Planning Horizon", desc: "Rolling three-year plans based on extrapolation preclude bold portfolio moves requiring decade-long vision.", icon: "TrendingDown" }
    ],
    solutions: [
      { phase: "Phase 1", title: "ROIC-Based Evaluation", desc: "Implementing capital efficiency metrics with objective investment and exit criteria." },
      { phase: "Phase 2", title: "Dynamic Portfolio Management", desc: "Establishing systematic processes for timing entry and exit decisions." },
      { phase: "Phase 3", title: "Carve-Out Execution", desc: "Managing complex separation including IP, systems, and workforce transitions." }
    ],
    caseStudies: [
      {
        industry: "Diversified Conglomerate",
        title: "Strategic Focus & PBR Recovery",
        problem: "Unfocused diversification depressing valuation.",
        result: "Divested three non-core businesses; PBR improved to 1.2x."
      },
      {
        industry: "Electronics Manufacturer",
        title: "Carve-Out Advisory",
        problem: "Legacy hardware division generating sustained losses.",
        result: "Private equity carve-out improved remaining business margins."
      },
      {
        industry: "Chemical Company",
        title: "ROIC Management Implementation",
        problem: "Invisible capital efficiency across divisions.",
        result: "ROIC-based allocation improved capital returns 15%."
      }
    ]
  },

  "new_business": {
    categoryId: "strategy",
    category: "Corporate Strategy & M&A",
    title: "New Business Development",
    subtitle: "Crossing the valley of death",
    themeColor: "indigo",
    hero: {
      badge: "For Innovation & R&D Leaders",
      description: "Technical validation succeeds but commercial scaling fails. We help organizations break through PoC purgatory to achieve viable new business launch.",
      stats: [
        { label: "PoC Fatigue", value: "Endless Pilots" },
        { label: "Commercialization", value: "<10% Success" },
        { label: "Metrics Misalignment", value: "Near-Term P&L" }
      ]
    },
    painPoints: [
      { title: "Valley of Death", desc: "Technical pilots succeed but fail to secure investment for commercial scaling.", icon: "Activity" },
      { title: "Ambidexterity Failure", desc: "Applying mature business metrics to early ventures kills promising initiatives.", icon: "Scale" },
      { title: "Stranded Assets", desc: "Rich IP and data portfolios lack business model innovation capability.", icon: "Database" }
    ],
    structuralIssues: [
      { title: "Innovator's Dilemma", desc: "Existing business profitability makes early-stage ventures appear unattractive; cannibalization fears compound resistance.", icon: "Activity" },
      { title: "Career Risk Avoidance", desc: "Perception that innovation failure derails careers drives top talent away from new ventures.", icon: "Scale" },
      { title: "Inappropriate KPIs", desc: "Applying annual profitability targets to exploration-phase initiatives systematically kills future growth.", icon: "Database" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Kill Line Definition", desc: "Pre-establishing exit criteria to prevent prolonged investment in failing initiatives." },
      { phase: "Phase 2", title: "Business Model Validation", desc: "Testing customer adoption and unit economics alongside technical feasibility." },
      { phase: "Phase 3", title: "Protected Incubation", desc: "Creating organizational space shielded from core business governance and metrics." }
    ],
    caseStudies: [
      {
        industry: "Manufacturing",
        title: "Technology Commercialization",
        problem: "Advanced sensor technology stalled in PoC for three years.",
        result: "Pivoted to construction market; launched subscription model generating ¥300M year one."
      },
      {
        industry: "Trading Company",
        title: "Portfolio Rationalization",
        problem: "Resource dilution across low-potential projects.",
        result: "Stage-gate process exited bottom 20%; concentrated on high-potential ventures."
      },
      {
        industry: "Financial Services",
        title: "AI Service Monetization",
        problem: "AI seen only as cost reduction; no revenue contribution.",
        result: "Repositioned with cross-sell KPIs; transformed to revenue-generating business."
      }
    ]
  },

  "pmi_success": {
    categoryId: "strategy",
    category: "Corporate Strategy & M&A",
    title: "M&A Integration (PMI)",
    subtitle: "Capturing deal value through execution",
    themeColor: "indigo",
    hero: {
      badge: "For M&A & Corporate Development",
      description: "Deal closed but synergies unrealized. We prevent value destruction from cultural collision, systems integration delays, and governance failures.",
      stats: [
        { label: "Talent Risk", value: "Key Person Attrition" },
        { label: "Synergy Gap", value: "Integration Delay" },
        { label: "Control", value: "Governance Vacuum" }
      ]
    },
    painPoints: [
      { title: "Cultural Collision", desc: "Incompatible management styles and compensation structures create organizational conflict.", icon: "Users" },
      { title: "Systems Integration Failure", desc: "IT complexity underestimated; manual workarounds persist indefinitely.", icon: "Server" },
      { title: "Subsidiary Black Box", desc: "Over-delegation to local management prevents early detection of performance issues or misconduct.", icon: "Globe" }
    ],
    structuralIssues: [
      { title: "Deal-Centric Mindset", desc: "Executive attention concentrates on deal closure; integration resources and commitment critically under-invested.", icon: "Users" },
      { title: "IT Due Diligence Neglect", desc: "Pre-deal analysis focuses on financial and legal issues; system integration complexity and cost systematically underestimated.", icon: "Server" },
      { title: "Retention Design Failure", desc: "Inadequate incentive structures for acquired leadership and key talent drive motivation collapse.", icon: "Globe" }
    ],
    solutions: [
      { phase: "Phase 1", title: "100-Day Plan", desc: "Detailed Day 1 through Day 100 execution plan with early wins to build momentum." },
      { phase: "Phase 2", title: "Cultural Integration Program", desc: "Structured dialogue and shared purpose development to bridge organizational identities." },
      { phase: "Phase 3", title: "Global Governance Framework", desc: "Common reporting standards, management systems, and IT platforms for visibility." }
    ],
    caseStudies: [
      {
        industry: "Services",
        title: "Cross-Border PMI",
        problem: "Local management deviated from strategy post-acquisition.",
        result: "KPI standardization and IMO establishment restored discipline; profitable within two years."
      },
      {
        industry: "Manufacturing",
        title: "Domestic Competitor Acquisition",
        problem: "Duplicate functions persisted; cost synergies unrealized.",
        result: "Third-party facilitated integration committee resolved politically sensitive restructuring."
      },
      {
        industry: "Technology",
        title: "Cultural Integration",
        problem: "Mass engineer departure post-acquisition.",
        result: "Junior-led culture initiative and revised performance system improved retention."
      }
    ]
  },

  "turnaround": {
    categoryId: "strategy",
    category: "Corporate Strategy & M&A",
    title: "Corporate Turnaround",
    subtitle: "From crisis to value recovery",
    themeColor: "indigo",
    hero: {
      badge: "For Distressed Situations",
      description: "Cash crisis, persistent losses, organizational fatigue. We drive comprehensive restructuring that goes beyond financial engineering to restore operational profitability.",
      stats: [
        { label: "Balance Sheet", value: "Insolvency Risk" },
        { label: "Cash Burn", value: "Delayed Triage" },
        { label: "Organization", value: "Talent Exodus" }
      ]
    },
    painPoints: [
      { title: "Exit Decision Delay", desc: "Concern for employees and partners delays loss-making business exits, deepening the crisis.", icon: "AlertTriangle" },
      { title: "Plan-Execution Gap", desc: "Restructuring plans satisfy lenders but lack operational implementation capability.", icon: "FileText" },
      { title: "Cash Runway Pressure", desc: "Short-term liquidity demands consume all attention, preventing strategic initiatives.", icon: "TrendingDown" }
    ],
    structuralIssues: [
      { title: "Sunk Cost Fallacy", desc: "Historical investment emotional attachment clouds rational exit decisions.", icon: "AlertTriangle" },
      { title: "Optimism Bias", desc: "Unfounded belief in market recovery delays fundamental restructuring.", icon: "FileText" },
      { title: "Learned Helplessness", desc: "Repeated performance failures create organizational paralysis; small wins are needed to rebuild momentum.", icon: "TrendingDown" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Triage & Cash Preservation", desc: "Stopping non-essential expenditure, liquidating inventory, renegotiating with creditors." },
      { phase: "Phase 2", title: "Business Rationalization", desc: "Objective business evaluation followed by decisive exit, sale, or downsizing." },
      { phase: "Phase 3", title: "Operational Improvement", desc: "Cost reduction, pricing optimization, and revenue enhancement to restore profitability." }
    ],
    caseStudies: [
      {
        industry: "Retail Chain",
        title: "Store Network Restructuring",
        problem: "Over-expansion created persistent losses; approaching technical insolvency.",
        result: "30% store closures with value repositioning achieved operating profit in two years."
      },
      {
        industry: "Manufacturing",
        title: "Sponsor-Supported Restructuring",
        problem: "Over-investment created liquidity crisis.",
        result: "Debt forgiveness and sponsor equity injection enabled production consolidation."
      },
      {
        industry: "Services",
        title: "Chief Restructuring Officer Deployment",
        problem: "Internal constraints prevented decisive restructuring.",
        result: "External CRO executed unprofitable division closure and cost reduction."
      }
    ]
  },

  // =================================================================
  // 3. Digital Transformation & IT
  // =================================================================
  "legacy_modernization": {
    categoryId: "dx",
    category: "Digital Transformation & IT",
    title: "Legacy Modernization",
    subtitle: "Eliminating technical debt",
    themeColor: "cyan",
    hero: {
      badge: "For CIOs & IT Leadership",
      description: "Black-boxed core systems blocking digital initiatives. We help organizations escape the legacy trap—reducing maintenance burden and building foundations for agile innovation.",
      stats: [
        { label: "Technical Debt", value: "80% Run Cost" },
        { label: "Skills Crisis", value: "COBOL Shortage" },
        { label: "Rigidity", value: "Change Resistant" }
      ]
    },
    painPoints: [
      { title: "System Black Box", desc: "Decades of modifications have created undocumented complexity that no one fully understands.", icon: "Box" },
      { title: "Vendor Lock-In", desc: "Single-vendor dependency enables inflated maintenance pricing.", icon: "Lock" },
      { title: "SAP 2027 Deadline", desc: "ECC end-of-support approaching with no clear S/4HANA migration or alternative strategy.", icon: "Database" }
    ],
    structuralIssues: [
      { title: "IT as Order-Taker", desc: "Years of uncritical accommodation of business requests created system complexity; enterprise architecture authority is absent.", icon: "Box" },
      { title: "Change Aversion Culture", desc: "'If it ain't broke, don't fix it' mentality perpetuates aging system risk avoidance.", icon: "Lock" },
      { title: "Short-Term P&L Pressure", desc: "Modernization increases near-term costs; quarterly earnings focus drives repeated postponement.", icon: "Database" }
    ],
    solutions: [
      { phase: "Phase 1", title: "IT Asset Assessment", desc: "Evaluating current systems for modernization priority versus managed decline." },
      { phase: "Phase 2", title: "Fit to Standard", desc: "Adapting business processes to package standards; minimizing custom development." },
      { phase: "Phase 3", title: "Progressive Migration", desc: "Avoiding big-bang risk through phased microservices-based transformation." }
    ],
    caseStudies: [
      {
        industry: "Retail Distribution",
        title: "Mainframe Exit",
        problem: "30-year-old systems blocking new service development.",
        result: "Cloud migration dramatically reduced development lead time."
      },
      {
        industry: "Manufacturing",
        title: "SAP S/4HANA Implementation",
        problem: "Fragmented systems across global operations.",
        result: "Single-instance consolidation enabled accelerated financial close."
      },
      {
        industry: "Insurance",
        title: "COBOL Modernization",
        problem: "Aging specialist workforce creating maintenance risk.",
        result: "Automated conversion to Java reduced maintenance cost 40%."
      }
    ]
  },

  "cloud_native": {
    categoryId: "dx",
    category: "Digital Transformation & IT",
    title: "Cloud Transformation",
    subtitle: "From lift-and-shift to cloud-native",
    themeColor: "cyan",
    hero: {
      badge: "For CTOs & Infrastructure Teams",
      description: "Simply moving servers to cloud? We help organizations fully leverage cloud economics and agility through proper architecture transformation and cost optimization.",
      stats: [
        { label: "Cost Overrun", value: "Consumption Spike" },
        { label: "Skills Gap", value: "Cloud Expertise" },
        { label: "Stalled Migration", value: "Lift-Only" }
      ]
    },
    painPoints: [
      { title: "Cloud Cost Explosion", desc: "Unmanaged consumption-based pricing exceeds on-premise costs.", icon: "DollarSign" },
      { title: "Multi-Cloud Complexity", desc: "Uncoordinated AWS, Azure, GCP adoption creating operational chaos.", icon: "Layers" },
      { title: "Lift-and-Shift Stall", desc: "Server migration completed without architecture changes; agility benefits unrealized.", icon: "Server" }
    ],
    structuralIssues: [
      { title: "On-Premise Mindset", desc: "Treating cloud as 'rental data center' without architecture redesign forfeits elasticity and cost benefits.", icon: "DollarSign" },
      { title: "Budget Structure Mismatch", desc: "Fixed CapEx budget processes cannot accommodate variable OpEx consumption patterns.", icon: "Layers" },
      { title: "Skills Denial", desc: "Expecting on-premise engineers to absorb cloud-native skills without investment creates burnout.", icon: "Server" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Cloud Center of Excellence", desc: "Establishing governance structure and knowledge hub for enterprise cloud adoption." },
      { phase: "Phase 2", title: "Architecture Redesign", desc: "Migrating to serverless and containerized cloud-native patterns." },
      { phase: "Phase 3", title: "FinOps Implementation", desc: "Establishing cost visibility and optimization operating rhythm." }
    ],
    caseStudies: [
      {
        industry: "Financial Services",
        title: "Core Banking Cloud Migration",
        problem: "On-premise systems blocking FinTech API integration.",
        result: "Public cloud migration enabled 10x increase in API connections."
      },
      {
        industry: "Digital Services",
        title: "Cloud Cost Optimization",
        problem: "Reserved instance opportunities unused; costs spiraling.",
        result: "FinOps program eliminated waste; reduced costs 30%."
      },
      {
        industry: "Manufacturing",
        title: "Cloud Governance Platform",
        problem: "Uncontrolled departmental cloud contracts creating risk.",
        result: "Unified platform deployment strengthened governance."
      }
    ]
  },

  "security_zerotrust": {
    categoryId: "dx",
    category: "Digital Transformation & IT",
    title: "Cybersecurity & Zero Trust",
    subtitle: "Beyond perimeter defense",
    themeColor: "cyan",
    hero: {
      badge: "For CISOs & Risk Management",
      description: "Perimeter security is obsolete. We help organizations defend against supply chain attacks and ransomware through zero-trust architecture and cyber resilience.",
      stats: [
        { label: "Supply Chain", value: "Third-Party Entry" },
        { label: "Zero Trust", value: "Perimeter Failure" },
        { label: "Talent", value: "Expert Shortage" }
      ]
    },
    painPoints: [
      { title: "Supply Chain Vulnerability", desc: "Robust headquarters security bypassed through compromised subsidiaries or vendors.", icon: "Globe" },
      { title: "Zero Trust Delay", desc: "Cloud adoption advanced while legacy VPN perimeter security persists.", icon: "Shield" },
      { title: "Incident Response Gap", desc: "No established CSIRT procedures; attack damage expands through delayed response.", icon: "AlertOctagon" }
    ],
    structuralIssues: [
      { title: "Trust-Based Culture", desc: "Inherent trust in 'internal' users resists strict identity management and access controls.", icon: "Globe" },
      { title: "Security as Cost Center", desc: "Viewing security as non-revenue expense leads to chronic underinvestment until breach occurs.", icon: "Shield" },
      { title: "Usability-Security Tradeoff", desc: "User resistance to security friction creates exception proliferation, undermining overall protection.", icon: "AlertOctagon" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Risk Assessment", desc: "Mapping enterprise-wide and supply chain vulnerabilities to identify exposure." },
      { phase: "Phase 2", title: "Zero Trust Deployment", desc: "Implementing identity management and EDR for 'never trust, always verify' security." },
      { phase: "Phase 3", title: "CSIRT & Exercises", desc: "Building incident response capability through organization design and realistic drills." }
    ],
    caseStudies: [
      {
        industry: "Manufacturing",
        title: "Global Security Governance",
        problem: "Overseas subsidiary ransomware attack halted headquarters operations.",
        result: "Unified standards and SOC deployment enabled global visibility."
      },
      {
        industry: "Trading Company",
        title: "Zero Trust Environment",
        problem: "Remote work expansion created VPN bottleneck.",
        result: "Cloud proxy and IDaaS deployment enabled secure, seamless access."
      },
      {
        industry: "Infrastructure",
        title: "Critical Infrastructure Protection",
        problem: "Operational technology (OT) attack exposure.",
        result: "IT/OT integrated security management ensured availability."
      }
    ]
  },

  "it_org_transformation": {
    categoryId: "dx",
    category: "Digital Transformation & IT",
    title: "IT Organization Transformation",
    subtitle: "From outsourcing to capability building",
    themeColor: "cyan",
    hero: {
      badge: "For CIOs & HR Leaders",
      description: "Breaking vendor dependency. We help organizations build internal IT capabilities that match business velocity through insourcing and agile transformation.",
      stats: [
        { label: "Outsourcing", value: "Capability Erosion" },
        { label: "Talent", value: "Acquisition Failure" },
        { label: "Agile", value: "Cultural Barrier" }
      ]
    },
    painPoints: [
      { title: "IT Capability Hollowing", desc: "Even requirements definition delegated to vendors; no internal technical judgment.", icon: "UserMinus" },
      { title: "Agile Incompatibility", desc: "Budget cycles and approval processes designed for waterfall block iterative delivery.", icon: "RefreshCw" },
      { title: "Talent Competition Loss", desc: "Rigid compensation structures prevent competitive offers for engineering talent.", icon: "UserPlus" }
    ],
    structuralIssues: [
      { title: "Outsourcing Comfort Zone", desc: "Risk transfer to vendors is comfortable; taking direct responsibility for insourced delivery requires mindset shift.", icon: "UserMinus" },
      { title: "Plan-Driven Culture", desc: "'Decide everything upfront' waterfall culture conflicts with agile's adaptive approach.", icon: "RefreshCw" },
      { title: "Technical Career Ceiling", desc: "Management-only advancement paths drive technical specialist attrition.", icon: "UserPlus" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Insourcing Roadmap", desc: "Defining core versus non-core capabilities; progressively building internal teams." },
      { phase: "Phase 2", title: "Agile Organization Design", desc: "Creating cross-functional squads combining IT and business expertise." },
      { phase: "Phase 3", title: "Technical Career Framework", desc: "Establishing competitive compensation and specialist career paths." }
    ],
    caseStudies: [
      {
        industry: "Financial Services",
        title: "Internal Development Team",
        problem: "Slow service releases losing to competitors.",
        result: "Insourced team reduced release cycles from 3 months to 2 weeks."
      },
      {
        industry: "Retail",
        title: "IT Role Redefinition",
        problem: "IT organization reduced to help desk function.",
        result: "BPO for routine operations enabled strategic focus shift."
      },
      {
        industry: "Telecommunications",
        title: "Enterprise Agile Deployment",
        problem: "Entrenched waterfall culture.",
        result: "Agile coaching scaled to 100+ teams."
      }
    ]
  },

  // =================================================================
  // 4. Data & Analytics
  // =================================================================
  "data_driven_mgmt": {
    categoryId: "data",
    category: "Data & Analytics",
    title: "Data-Driven Management",
    subtitle: "From intuition to insight",
    themeColor: "blue",
    hero: {
      badge: "For CDOs & Strategy Leaders",
      description: "Data exists but decisions don't follow. We break down silos and build the culture and infrastructure for analytics-driven decision making at all levels.",
      stats: [
        { label: "Data Silos", value: "Fragmentation" },
        { label: "Literacy", value: "Skills Gap" },
        { label: "Quality", value: "Data Issues" }
      ]
    },
    painPoints: [
      { title: "Data Fragmentation", desc: "Separate systems across divisions prevent integrated customer analytics.", icon: "Database" },
      { title: "BI Tool Shelfware", desc: "Expensive platforms deployed but users revert to spreadsheets.", icon: "BarChart2" },
      { title: "Leadership Analytics Gap", desc: "Executives ignore dashboards, making experience-based decisions.", icon: "EyeOff" }
    ],
    structuralIssues: [
      { title: "Data as Power Base", desc: "Departments hoard data as competitive advantage; sharing has no incentive.", icon: "Database" },
      { title: "Intuition-Based Advancement", desc: "Leaders promoted on charisma and past wins dismiss data-driven proposals.", icon: "BarChart2" },
      { title: "Means-Ends Confusion", desc: "Tool selection debates dominate without clarity on which decisions to improve.", icon: "EyeOff" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Data Integration Platform", desc: "Building data warehouse or lake for unified enterprise data access." },
      { phase: "Phase 2", title: "KPI Design & Visualization", desc: "Defining business-critical metrics and dashboard deployment." },
      { phase: "Phase 3", title: "Analytics Culture Building", desc: "Creating habits of data-informed discussion from leadership to frontline." }
    ],
    caseStudies: [
      {
        industry: "Retail",
        title: "Customer ID Integration",
        problem: "Physical and digital customer data separated.",
        result: "Unified ID enabled omnichannel analytics; LTV improved 20%."
      },
      {
        industry: "Manufacturing",
        title: "Executive Dashboard",
        problem: "Global performance aggregation required two weeks.",
        result: "Real-time visibility enabled daily management."
      },
      {
        industry: "Services",
        title: "Data Quality Improvement",
        problem: "Master data inconsistency caused operational errors.",
        result: "MDM implementation reduced errors 90%."
      }
    ]
  },

  "data_platform": {
    categoryId: "data",
    category: "Data & Analytics",
    title: "Data Platform & Governance",
    subtitle: "Building analytics-ready foundations",
    themeColor: "blue",
    hero: {
      badge: "For Data Engineering & IT",
      description: "AI requires quality data. We establish data quality standards and governance frameworks from master data management to data catalog implementation.",
      stats: [
        { label: "Data Quality", value: "Gaps & Duplicates" },
        { label: "Governance", value: "No Ownership" },
        { label: "Discovery", value: "Unknown Location" }
      ]
    },
    painPoints: [
      { title: "Data Quality Deficit", desc: "Inconsistent entry rules create gaps and duplicates unusable for analytics.", icon: "FileWarning" },
      { title: "Master Data Chaos", desc: "Inconsistent customer and product codes prevent cross-functional analysis.", icon: "List" },
      { title: "Governance Vacuum", desc: "No clear data ownership creates security and compliance exposure.", icon: "Shield" }
    ],
    structuralIssues: [
      { title: "Garbage In, Garbage Out", desc: "Data entry seen as burden with no quality incentive. Without structural change, even advanced AI produces garbage output.", icon: "FileWarning" },
      { title: "Tragedy of the Commons", desc: "Shared data with no owner means no one maintains quality or resolves issues.", icon: "List" },
      { title: "Business-IT Disconnect", desc: "IT focuses on storage; business on usage. Misalignment creates unusable data platforms.", icon: "Shield" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Data Assessment", desc: "Inventorying data assets—location, quality, usage—to identify gaps." },
      { phase: "Phase 2", title: "Master Data Management", desc: "Defining and operationalizing enterprise-standard master data." },
      { phase: "Phase 3", title: "Data Catalog Deployment", desc: "Enabling self-service data discovery to accelerate analytics adoption." }
    ],
    caseStudies: [
      {
        industry: "Logistics",
        title: "Dispatch Optimization Foundation",
        problem: "Operations data scattered in paper and spreadsheets.",
        result: "Data lake enabled AI dispatch optimization; improved load efficiency."
      },
      {
        industry: "Financial Services",
        title: "Data Governance Framework",
        problem: "Personal data management status unclear.",
        result: "Data catalog deployment strengthened controls and accelerated analytics."
      },
      {
        industry: "Retail",
        title: "Product Master Consolidation",
        problem: "M&A created duplicate product codes.",
        result: "MDM enabled unified inventory management; reduced stockouts."
      }
    ]
  },

  // =================================================================
  // 5. Human Capital & Organization
  // =================================================================
  "human_capital": {
    categoryId: "hr",
    category: "Human Capital & Organization",
    title: "Human Capital Management",
    subtitle: "From cost center to strategic asset",
    themeColor: "orange",
    hero: {
      badge: "For CHROs & HR Strategy",
      description: "Meeting ISO 30414 and disclosure requirements. We connect human capital strategy to business strategy, building the narrative that demonstrates workforce value to investors.",
      stats: [
        { label: "Disclosure", value: "Regulatory Mandate" },
        { label: "ROI", value: "Impact Unclear" },
        { label: "Strategy Link", value: "HR Isolation" }
      ]
    },
    painPoints: [
      { title: "Measurement Challenge", desc: "Uncertain how to collect human capital data and define meaningful metrics.", icon: "Eye" },
      { title: "Narrative Gap", desc: "Data disclosed without compelling link to enterprise value creation.", icon: "BookOpen" },
      { title: "HR Capability Gap", desc: "Administrative HR function asked to become strategic business partner.", icon: "UserCheck" }
    ],
    structuralIssues: [
      { title: "HR as Administrative Function", desc: "HR positioned as payroll and compliance—lacking authority and skills for strategic workforce planning.", icon: "UserCheck" },
      { title: "Labor as Cost Mindset", desc: "P&L treatment of workforce as expense prevents investment thinking and ROI measurement.", icon: "Eye" },
      { title: "Fragmented HR Data", desc: "Scattered talent management systems prevent integrated workforce analytics.", icon: "BookOpen" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Metrics & Dashboard", desc: "Defining strategy-linked human capital KPIs with executive visibility." },
      { phase: "Phase 2", title: "Value Story Development", desc: "Articulating how workforce strategy drives growth for integrated reporting." },
      { phase: "Phase 3", title: "HR Business Partner Development", desc: "Building HRBP capability to serve as strategic advisors to business units." }
    ],
    caseStudies: [
      {
        industry: "Services",
        title: "ISO 30414 Compliant Disclosure",
        problem: "Investor pressure for human capital transparency.",
        result: "International standard-aligned disclosure improved ESG ratings."
      },
      {
        industry: "Manufacturing",
        title: "HR Investment ROI Visibility",
        problem: "Training budget targeted for cuts due to unclear impact.",
        result: "Demonstrated education-productivity correlation; secured increased investment."
      },
      {
        industry: "Technology",
        title: "HRBP Model Implementation",
        problem: "HR unable to address business unit talent challenges.",
        result: "HRBP deployment resolved hiring and deployment mismatches."
      }
    ]
  },

  "job_based_hr": {
    categoryId: "hr",
    category: "Human Capital & Organization",
    title: "Skills-Based Talent Architecture",
    subtitle: "Beyond seniority-based systems",
    themeColor: "orange",
    hero: {
      badge: "For HR Directors",
      description: "Attracting specialized talent in a competitive market. We design hybrid talent models that balance role clarity with organizational flexibility.",
      stats: [
        { label: "Talent War", value: "Digital Skills" },
        { label: "Role Clarity", value: "Ambiguous JDs" },
        { label: "Demographics", value: "Senior Cost" }
      ]
    },
    painPoints: [
      { title: "Job Architecture Resistance", desc: "Frontline pushback on job descriptions—'who picks up dropped balls?'", icon: "FileText" },
      { title: "Digital Talent Acquisition Failure", desc: "Rigid compensation structures prevent competitive offers for engineers.", icon: "UserPlus" },
      { title: "Senior Workforce Challenge", desc: "Over-compensated senior employees relative to current role value.", icon: "UserMinus" }
    ],
    structuralIssues: [
      { title: "Membership Culture Inertia", desc: "'Assign work to people' tradition conflicts with 'assign people to roles' logic.", icon: "FileText" },
      { title: "Internal Equity Trap", desc: "Universal pay scales prevent market-competitive specialist compensation.", icon: "UserPlus" },
      { title: "Manager JD Capability Gap", desc: "Managers lack training to articulate concrete job descriptions; defaults to vague expectations.", icon: "UserMinus" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Hybrid Role Architecture", desc: "Defining clear accountabilities while preserving collaborative flexibility." },
      { phase: "Phase 2", title: "Market-Referenced Compensation", desc: "Introducing role-based pay informed by external market data." },
      { phase: "Phase 3", title: "Manager Capability Building", desc: "Training leaders to evaluate work and outcomes rather than tenure." }
    ],
    caseStudies: [
      {
        industry: "Electronics Manufacturer",
        title: "Enterprise Job Architecture",
        problem: "Top young talent departing for competitors.",
        result: "20s management track and specialist path restored talent attraction."
      },
      {
        industry: "Chemical",
        title: "Senior Workforce Re-engagement",
        problem: "Post-demotion motivation collapse.",
        result: "Role-based compensation enabled second career challenges."
      },
      {
        industry: "IT Services",
        title: "Technical Expert Track",
        problem: "No non-management career path for engineers.",
        result: "CTO-level compensation track improved engineer retention."
      }
    ]
  },

  "succession_planning": {
    categoryId: "hr",
    category: "Human Capital & Organization",
    title: "Succession Planning",
    subtitle: "Building leadership pipeline",
    themeColor: "orange",
    hero: {
      badge: "For Boards & Nomination Committees",
      description: "CEO transition as process, not event. We help organizations move from reactive selection to systematic leadership pipeline development.",
      stats: [
        { label: "Pipeline Gap", value: "No Candidates" },
        { label: "Objectivity", value: "Subjective Selection" },
        { label: "Tenure Risk", value: "Limited Runway" }
      ]
    },
    painPoints: [
      { title: "Pipeline Vacuum", desc: "Scrambling for candidates when transition approaches—no prepared succession.", icon: "UserX" },
      { title: "Selection Subjectivity", desc: "High-potential identification based on manager preference rather than data.", icon: "EyeOff" },
      { title: "Development Gap", desc: "Classroom-heavy programs without P&L accountability stretch assignments.", icon: "Briefcase" }
    ],
    structuralIssues: [
      { title: "Seniority Progression", desc: "Time-based advancement means leaders arrive at CEO role with limited remaining tenure and change energy.", icon: "UserX" },
      { title: "Development Opportunity Scarcity", desc: "Risk-averse culture prevents candidates from taking challenging stretch assignments that build executive capability.", icon: "Briefcase" },
      { title: "Similarity Bias", desc: "Current leaders unconsciously select successors who resemble themselves, excluding transformational candidates.", icon: "EyeOff" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Leadership Competency Model", desc: "Defining future-state leadership requirements aligned with strategy." },
      { phase: "Phase 2", title: "Objective Assessment", desc: "Third-party multi-rater evaluation to identify high-potential talent." },
      { phase: "Phase 3", title: "Stretch Assignments", desc: "Intentional placement in challenging roles—subsidiary CEO, new venture leader." }
    ],
    caseStudies: [
      {
        industry: "Materials",
        title: "Leadership Development Program",
        problem: "No internal CEO candidates; dependent on external search.",
        result: "Selective program and assessment built 50-person candidate pool."
      },
      {
        industry: "Trading Company",
        title: "Nomination Committee Effectiveness",
        problem: "Opaque selection process.",
        result: "Data-driven succession planning strengthened governance."
      },
      {
        industry: "Retail",
        title: "Diversity in Leadership Pipeline",
        problem: "Targets set without development infrastructure.",
        result: "Early identification and mentoring enabled internal promotion."
      }
    ]
  },

  "engagement_reskilling": {
    categoryId: "hr",
    category: "Human Capital & Organization",
    title: "Engagement & Reskilling",
    subtitle: "Building workforce of the future",
    themeColor: "orange",
    hero: {
      badge: "For HR & Organization Development",
      description: "Countering quiet quitting and preparing for digital transformation. We revitalize organizations through purpose alignment and practical skills development.",
      stats: [
        { label: "Quiet Quitting", value: "Declining Effort" },
        { label: "Early Turnover", value: "Young Talent Loss" },
        { label: "Digital Gap", value: "Lagging Skills" }
      ]
    },
    painPoints: [
      { title: "Quiet Quitting", desc: "Younger employees doing minimum required; emotional disconnection.", icon: "UserMinus" },
      { title: "Reskilling Ineffectiveness", desc: "Training programs provided but motivation absent; no behavior change.", icon: "Book" },
      { title: "Purpose Disconnection", desc: "Corporate vision fails to connect to daily work meaning.", icon: "Target" }
    ],
    structuralIssues: [
      { title: "Purpose-Practice Gap", desc: "Inspiring mission statements paired with unchanged evaluation and management creates cynicism.", icon: "Target" },
      { title: "Career Autonomy Deficit", desc: "Company-directed assignments and training undermine intrinsic motivation to learn.", icon: "Book" },
      { title: "One-Way Communication", desc: "Leadership messages flow down but employee voice mechanisms are absent.", icon: "UserMinus" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Engagement Diagnostics", desc: "Quantifying organizational health to identify genuine bottlenecks." },
      { phase: "Phase 2", title: "Purpose Activation", desc: "Connecting corporate mission to individual work through facilitated dialogue." },
      { phase: "Phase 3", title: "Applied Reskilling", desc: "Learning through real transformation project participation, not classroom instruction." }
    ],
    caseStudies: [
      {
        industry: "IT Services",
        title: "Turnover Reduction",
        problem: "Young employee turnover exceeding 20%.",
        result: "Enhanced 1:1s and revised evaluation reduced turnover to single digits."
      },
      {
        industry: "Retail",
        title: "Post-M&A Cultural Integration",
        problem: "Workforce fragmentation after acquisition.",
        result: "New purpose development and activation programs rebuilt cohesion."
      },
      {
        industry: "Manufacturing",
        title: "Digital Reskilling",
        problem: "Veteran employees resistant to digital tools.",
        result: "Problem-based learning approach increased autonomous improvement initiatives."
      }
    ]
  },

  // =================================================================
  // 6. Operations & Supply Chain
  // =================================================================
  "scm_resilience": {
    categoryId: "scm",
    category: "Operations & Supply Chain",
    title: "Supply Chain Resilience",
    subtitle: "Building disruption-proof networks",
    themeColor: "emerald",
    hero: {
      badge: "For Supply Chain & Procurement",
      description: "Geopolitical risk, natural disasters, supply disruption. We help organizations build supply networks that balance efficiency with resilience.",
      stats: [
        { label: "Visibility Gap", value: "Tier 2/3 Unknown" },
        { label: "Inventory", value: "Excess & Shortage" },
        { label: "Geopolitics", value: "Concentration Risk" }
      ]
    },
    painPoints: [
      { title: "Multi-Tier Opacity", desc: "Tier 2 and 3 supplier conditions invisible; crisis impact assessment delayed.", icon: "Layers" },
      { title: "Inventory Optimization Failure", desc: "Forecast errors create simultaneous overstock and stockout conditions.", icon: "Package" },
      { title: "Geographic Concentration", desc: "Single-country sourcing dependency without contingency plans.", icon: "Globe" }
    ],
    structuralIssues: [
      { title: "Efficiency Maximization Trap", desc: "Just-in-time inventory minimization created fragile networks with no disruption buffer.", icon: "Package" },
      { title: "Information Silos", desc: "Disconnected procurement, production, and sales KPIs prevent real-time demand signal flow.", icon: "Layers" },
      { title: "Procurement Cost Focus", desc: "Buying function evaluated on unit cost alone; resilience investment not recognized.", icon: "Globe" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Supply Network Mapping", desc: "Visualizing multi-tier supply base to identify risk concentration." },
      { phase: "Phase 2", title: "AI Demand Forecasting", desc: "Implementing predictive models that improve inventory turns while reducing stockouts." },
      { phase: "Phase 3", title: "Supply Diversification", desc: "Building 'China plus one' and alternative sourcing strategies." }
    ],
    caseStudies: [
      {
        industry: "Automotive Parts",
        title: "Supply Network Digital Twin",
        problem: "Semiconductor shortage impact assessment delayed.",
        result: "Tier 3 visibility enabled 3x faster alternative sourcing decisions."
      },
      {
        industry: "Consumer Goods",
        title: "AI Inventory Optimization",
        problem: "Overstock driving disposal losses.",
        result: "Predictive AI reduced inventory 20% while improving availability."
      },
      {
        industry: "Electronics",
        title: "Sourcing Risk Diversification",
        problem: "Single supplier dependency caused production halt.",
        result: "Multi-sourcing strategy strengthened business continuity."
      }
    ]
  },

  "logistics_reform": {
    categoryId: "scm",
    category: "Operations & Supply Chain",
    title: "Logistics Transformation",
    subtitle: "Addressing capacity constraints",
    themeColor: "emerald",
    hero: {
      badge: "For Logistics & Supply Chain",
      description: "Driver shortages and regulatory constraints threatening delivery capability. We drive fundamental logistics network redesign before capacity runs out.",
      stats: [
        { label: "Driver Crisis", value: "Capacity Decline" },
        { label: "Cost Pressure", value: "Rate Increases" },
        { label: "Utilization", value: "Low Load Factor" }
      ]
    },
    painPoints: [
      { title: "Capacity Shortage", desc: "Long-haul transportation increasingly difficult; delivery SLAs at risk.", icon: "Truck" },
      { title: "Cost Escalation", desc: "Rate increases cannot be passed through; margins eroding.", icon: "DollarSign" },
      { title: "Low Utilization", desc: "Frequent small shipments result in trucks moving air.", icon: "Box" }
    ],
    structuralIssues: [
      { title: "Customer Service Absolutism", desc: "Sales accepts unreasonable delivery demands, creating logistics inefficiency and cost.", icon: "Truck" },
      { title: "Logistics as Afterthought", desc: "Transportation treated as cost, not strategic; collaborative initiatives blocked.", icon: "Box" },
      { title: "Subcontracting Opacity", desc: "Multi-layer outsourcing obscures actual driver conditions and capacity risk.", icon: "DollarSign" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Network Redesign", desc: "Optimizing facility locations and relay points to reduce long-haul requirements." },
      { phase: "Phase 2", title: "Collaborative Distribution", desc: "Shared transportation with other shippers and modal shift to rail/sea." },
      { phase: "Phase 3", title: "Logistics Digitization", desc: "Dock scheduling and route optimization to eliminate driver wait time." }
    ],
    caseStudies: [
      {
        industry: "Food Manufacturing",
        title: "Competitor Collaboration",
        problem: "Low truck utilization driving up costs.",
        result: "Shared distribution with competitors improved loads and reduced carbon."
      },
      {
        industry: "Wholesale",
        title: "Network Optimization",
        problem: "Driver shortage threatening next-day delivery.",
        result: "AI-optimized facilities maintained service at stable cost."
      },
      {
        industry: "Retail",
        title: "Dock Scheduling System",
        problem: "Long driver wait times causing carrier refusals.",
        result: "90% wait time reduction secured carrier capacity."
      }
    ]
  },

  "smart_factory": {
    categoryId: "scm",
    category: "Operations & Supply Chain",
    title: "Smart Manufacturing",
    subtitle: "Digitizing operational excellence",
    themeColor: "emerald",
    hero: {
      badge: "For Plant Managers & Operations",
      description: "Expert workforce retiring, labor scarce. We implement IoT and AI to automate, capture institutional knowledge, and maintain manufacturing excellence.",
      stats: [
        { label: "Labor", value: "Hiring Difficulty" },
        { label: "Knowledge", value: "Expertise Loss" },
        { label: "Equipment", value: "Aging Assets" }
      ]
    },
    painPoints: [
      { title: "Knowledge Attrition", desc: "Veteran tacit knowledge disappearing; quality variation increasing.", icon: "UserCheck" },
      { title: "Unplanned Downtime", desc: "Aging equipment failures disrupt production schedules.", icon: "AlertOctagon" },
      { title: "Analog Operations", desc: "Paper logs and manual inspection prevent data-driven improvement.", icon: "FileText" }
    ],
    structuralIssues: [
      { title: "Craftsman Culture", desc: "'Watch and learn' apprenticeship tradition resists knowledge formalization.", icon: "UserCheck" },
      { title: "Local Optimization", desc: "Shop floor kaizen excels but factory-wide digital integration lacking.", icon: "FileText" },
      { title: "Investment Justification Difficulty", desc: "Risk prevention value hard to quantify; aging asset replacement deferred.", icon: "AlertOctagon" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Manufacturing Data Visibility", desc: "IoT sensor deployment for real-time equipment and process monitoring." },
      { phase: "Phase 2", title: "Predictive Maintenance", desc: "AI analysis of vibration and acoustic data for failure prediction." },
      { phase: "Phase 3", title: "Digital Knowledge Capture", desc: "Video and AI analysis of expert operations for training content development." }
    ],
    caseStudies: [
      {
        industry: "Automotive Parts",
        title: "Predictive Maintenance",
        problem: "Frequent unplanned line stoppages.",
        result: "Zero surprise downtime; 20% maintenance cost reduction."
      },
      {
        industry: "Chemical",
        title: "Expert Knowledge Digitization",
        problem: "Quality variation after veteran retirement.",
        result: "Operations modeling enabled junior operators to match quality levels."
      },
      {
        industry: "Food Processing",
        title: "Paperless Factory",
        problem: "Manual log compilation consuming resources.",
        result: "Tablet deployment halved input effort; improved traceability."
      }
    ]
  },

  // =================================================================
  // 7. Sustainability & Risk
  // =================================================================
  "decarbonization_gx": {
    categoryId: "sustainability",
    category: "Sustainability & Risk",
    title: "Decarbonization & Green Transformation",
    subtitle: "From measurement to reduction",
    themeColor: "teal",
    hero: {
      badge: "For Sustainability Teams",
      description: "Exhausted by disclosure requirements? We help organizations move beyond Scope 3 measurement to implement effective reduction strategies across the value chain.",
      stats: [
        { label: "Data Gap", value: "No Primary Data" },
        { label: "Cost Burden", value: "Green Premium" },
        { label: "Regulation", value: "Disclosure Load" }
      ]
    },
    painPoints: [
      { title: "Scope 3 Data Challenge", desc: "Supplier primary data unavailable; estimates lack credibility.", icon: "BarChart2" },
      { title: "Supply Chain Engagement", desc: "Cannot require suppliers to absorb reduction costs.", icon: "MessageCircle" },
      { title: "Business Case Gap", desc: "Environmental investments cannot be recovered through pricing.", icon: "DollarSign" }
    ],
    structuralIssues: [
      { title: "Cost Burden Transfer", desc: "Buyer power imposes reduction requirements without cost sharing; suppliers cannot invest.", icon: "MessageCircle" },
      { title: "Data System Fragmentation", desc: "Disconnected procurement, production, and logistics systems prevent product-level emissions tracking.", icon: "BarChart2" },
      { title: "Short-Term Earnings Conflict", desc: "Long-term necessity conflicts with quarterly profit pressure.", icon: "DollarSign" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Data Collection Platform", desc: "Cloud-based supplier data collection to automate emissions accounting." },
      { phase: "Phase 2", title: "Supplier Collaboration", desc: "Joint reduction programs—efficiency support, renewable energy cooperatives." },
      { phase: "Phase 3", title: "Internal Carbon Pricing", desc: "Embedding carbon cost into investment decisions to accelerate decarbonization." }
    ],
    caseStudies: [
      {
        industry: "Food & Beverage",
        title: "Agricultural Supply Chain Collaboration",
        problem: "80% of emissions from raw materials.",
        result: "Farming practice support reduced emissions 20%; strengthened brand."
      },
      {
        industry: "Electronics",
        title: "Renewable Energy Cooperative",
        problem: "SME suppliers unable to access green power.",
        result: "Group purchasing lowered adoption barriers across supply chain."
      },
      {
        industry: "Chemical",
        title: "Internal Carbon Price",
        problem: "Efficiency investments failed ROI hurdles.",
        result: "Carbon value inclusion accelerated decarbonization project approval."
      }
    ]
  },

  "circular_economy": {
    categoryId: "sustainability",
    category: "Sustainability & Risk",
    title: "Circular Economy",
    subtitle: "From waste to value",
    themeColor: "teal",
    hero: {
      badge: "For Strategy & Sustainability",
      description: "Moving beyond make-use-dispose. We help organizations build circular business models that transform resource recovery into growth engines.",
      stats: [
        { label: "Resource Risk", value: "Material Scarcity" },
        { label: "Waste Cost", value: "Environmental Load" },
        { label: "New Markets", value: "Circular Demand" }
      ]
    },
    painPoints: [
      { title: "Reverse Logistics Gap", desc: "No product take-back infrastructure; recycled materials unavailable.", icon: "RefreshCw" },
      { title: "Economics Challenge", desc: "Recycled materials cost more than virgin; product cost increases.", icon: "DollarSign" },
      { title: "Business Model Inertia", desc: "Transition from product sales to service models faces organizational resistance.", icon: "Repeat" }
    ],
    structuralIssues: [
      { title: "Linear System Lock-In", desc: "Existing supply chains optimized for linear throughput; circular transition threatens current business.", icon: "Repeat" },
      { title: "Ecosystem Complexity", desc: "Circularity requires competitor and cross-industry collaboration beyond single-company capability.", icon: "RefreshCw" },
      { title: "Consumer Price Sensitivity", desc: "Immature market for environmental premiums; unclear who absorbs higher costs.", icon: "DollarSign" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Circularity Assessment", desc: "Identifying resource loss points and value recovery opportunities across lifecycle." },
      { phase: "Phase 2", title: "Ecosystem Development", desc: "Building partnerships with collectors, recyclers, and technology providers." },
      { phase: "Phase 3", title: "Service Model Transition", desc: "Shifting from product ownership to access models that retain material control." }
    ],
    caseStudies: [
      {
        industry: "Apparel",
        title: "Garment Take-Back & Regeneration",
        problem: "Disposal criticism threatening brand reputation.",
        result: "Store collection and fiber regeneration technology enabled closed-loop products."
      },
      {
        industry: "Office Equipment",
        title: "Product-as-a-Service Model",
        problem: "New product price competition intensifying.",
        result: "Service model transition with parts reuse improved margins."
      },
      {
        industry: "Consumer Goods",
        title: "Packaging Circularity",
        problem: "Plastic waste regulation pressure.",
        result: "Achieved 50% recycled content packaging."
      }
    ]
  },

  "risk_management": {
    categoryId: "sustainability",
    category: "Sustainability & Risk",
    title: "Enterprise Risk & Economic Security",
    subtitle: "Navigating uncertainty",
    themeColor: "teal",
    hero: {
      badge: "For Risk & Strategy Leaders",
      description: "Geopolitical risk, economic security, reputation threats. We build integrated risk management frameworks that address compound risks threatening enterprise survival.",
      stats: [
        { label: "Geopolitics", value: "US-China Tension" },
        { label: "Technology", value: "IP Protection" },
        { label: "Reputation", value: "Social Media Risk" }
      ]
    },
    painPoints: [
      { title: "Economic Security Compliance", desc: "Export control and technology protection frameworks inadequate.", icon: "Shield" },
      { title: "Geopolitical Scenario Planning", desc: "No contingency plans for Taiwan or other regional crisis scenarios.", icon: "Globe" },
      { title: "Fragmented Risk Management", desc: "Departmental risk silos prevent enterprise-wide impact assessment.", icon: "Layout" }
    ],
    structuralIssues: [
      { title: "Normalcy Bias", desc: "'It won't happen to us' thinking delays investment in crisis preparedness.", icon: "Globe" },
      { title: "Functional Silos", desc: "Legal, IT, communications managing risks independently; compound impacts invisible.", icon: "Layout" },
      { title: "Crisis Response Glorification", desc: "Fire-fighting praised while prevention work goes unrecognized.", icon: "Shield" }
    ],
    solutions: [
      { phase: "Phase 1", title: "Enterprise Risk Assessment", desc: "Developing key risk indicators and quantifying enterprise-wide exposure." },
      { phase: "Phase 2", title: "Scenario Planning & BCP", desc: "Geopolitical crisis planning and business continuity exercises." },
      { phase: "Phase 3", title: "Economic Security Framework", desc: "Building technology protection and supply chain human rights due diligence processes." }
    ],
    caseStudies: [
      {
        industry: "High-Tech",
        title: "Economic Security Program",
        problem: "Advanced technology export risk exposure.",
        result: "Technology classification and access controls prevented leakage."
      },
      {
        industry: "Trading Company",
        title: "Geopolitical Scenario Planning",
        problem: "No exit criteria for regional operations.",
        result: "Country risk-based exit thresholds established."
      },
      {
        industry: "Retail",
        title: "Human Rights Due Diligence",
        problem: "Supply chain labor practices unknown.",
        result: "Audit program enabled sustainable sourcing certification."
      }
    ]
  }
};

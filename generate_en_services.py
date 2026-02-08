#!/usr/bin/env python3
"""
Generate English service pages for RISEby website
"""

import os

# Service IDs and their English titles/descriptions
SERVICES = {
    # AI & Generative AI
    "ai_strategy": ("AI Strategy & Roadmap", "From tactical experiments to strategic transformation. We connect business imperatives with technical feasibility to build enterprise AI roadmaps that maximize return on investment."),
    "gen_ai_implementation": ("Generative AI Implementation", "Enterprise-grade LLM deployment. We build secure RAG environments that leverage proprietary data while mitigating hallucination and data security risks."),
    "ai_governance": ("AI Governance & Risk", "From prohibition to controlled enablement. We build governance frameworks that manage AI-specific risks while enabling innovation."),
    
    # Corporate Strategy & M&A  
    "portfolio_transformation": ("Portfolio Transformation", "Breaking free from conglomerate discount. We drive decisive portfolio restructuring to build sustainable enterprise value."),
    "new_business": ("New Business Development", "Crossing the valley of death. We help organizations break through PoC purgatory to achieve viable new business launch."),
    "pmi_success": ("M&A Integration (PMI)", "Capturing deal value through execution. We prevent value destruction from cultural collision and integration delays."),
    "turnaround": ("Corporate Turnaround", "From crisis to value recovery. We drive comprehensive restructuring that restores operational profitability."),
    
    # Digital Transformation & IT
    "legacy_modernization": ("Legacy Modernization", "Eliminating technical debt. We help organizations escape the legacy trap and build foundations for agile innovation."),
    "cloud_native": ("Cloud Transformation", "From lift-and-shift to cloud-native. We help organizations fully leverage cloud economics and agility."),
    "security_zerotrust": ("Cybersecurity & Zero Trust", "Beyond perimeter defense. We help organizations defend against modern threats through zero-trust architecture."),
    "it_org_transformation": ("IT Organization Transformation", "From outsourcing to capability building. We help organizations build internal IT capabilities that match business velocity."),
    
    # Data & Analytics
    "data_driven_mgmt": ("Data-Driven Management", "From intuition to insight. We build the culture and infrastructure for analytics-driven decision making."),
    "data_platform": ("Data Platform & Governance", "Building analytics-ready foundations. We establish data quality standards and governance frameworks."),
    
    # Human Capital & Organization
    "human_capital": ("Human Capital Management", "From cost center to strategic asset. We connect human capital strategy to business strategy."),
    "job_based_hr": ("Skills-Based Talent Architecture", "Beyond seniority-based systems. We design hybrid talent models that balance role clarity with flexibility."),
    "succession_planning": ("Succession Planning", "Building leadership pipeline. We help organizations move from reactive selection to systematic development."),
    "engagement_reskilling": ("Engagement & Reskilling", "Building workforce of the future. We revitalize organizations through purpose alignment and skills development."),
    
    # Operations & Supply Chain
    "scm_resilience": ("Supply Chain Resilience", "Building disruption-proof networks. We help organizations build supply networks that balance efficiency with resilience."),
    "logistics_reform": ("Logistics Transformation", "Addressing capacity constraints. We drive fundamental logistics network redesign."),
    "smart_factory": ("Smart Manufacturing", "Digitizing operational excellence. We implement IoT and AI to automate and capture institutional knowledge."),
    
    # Sustainability & Risk
    "decarbonization_gx": ("Decarbonization & Green Transformation", "From measurement to reduction. We help organizations implement effective reduction strategies across the value chain."),
    "circular_economy": ("Circular Economy", "From waste to value. We help organizations build circular business models as growth engines."),
    "risk_management": ("Enterprise Risk & Economic Security", "Navigating uncertainty. We build integrated risk management frameworks for compound risks."),
}

# Category pages
CATEGORIES = {
    "ai": ("AI & Generative AI", "From experimentation to enterprise value."),
    "strategy": ("Corporate Strategy & M&A", "Strategic clarity in an age of uncertainty."),
    "dx": ("Digital Transformation & IT", "Beyond the legacy cliff."),
    "data": ("Data & Analytics", "From intuition to intelligence."),
    "hr": ("Human Capital & Organization", "Activating human capital."),
    "scm": ("Operations & Supply Chain", "Resilience meets efficiency."),
    "sustainability": ("Sustainability & Risk", "ESG as competitive advantage."),
}

DETAIL_TEMPLATE = '''<!DOCTYPE html>
<html lang="en" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8">

  <title>{title} | RISEby</title>
  <meta name="description" content="{description}">
  
  <!-- OGP -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="RISEby inc.">
  <meta property="og:locale" content="en_US">
  <meta property="og:url" content="https://riseby.net/en/services/{service_id}.html">
  <meta property="og:title" content="{title} | RISEby">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://riseby.net/assets/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  
  <!-- Canonical & Alternate -->
  <link rel="canonical" href="https://riseby.net/en/services/{service_id}.html">
  <link rel="alternate" hreflang="ja" href="https://riseby.net/services/{service_id}.html">
  <link rel="alternate" hreflang="en" href="https://riseby.net/en/services/{service_id}.html">

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{title}",
  "description": "{description}",
  "provider": {{
    "@type": "Organization",
    "name": "RISEby inc.",
    "url": "https://riseby.net/en/"
  }},
  "serviceType": "Business Consulting",
  "areaServed": {{
    "@type": "Country",
    "name": "Japan"
  }}
}}
  </script>


  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="../../assets/images/favicon.svg">
  <link rel="apple-touch-icon" sizes="180x180" href="../../assets/images/apple-touch-icon.png">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Libraries -->
  <script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Load Database -->
  <script src="../assets/tasks.js"></script>

  <!-- Tailwind Config -->
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{ blue: '#003E68', red: '#ED1C24', dark: '#0B0F19' }}
          }},
          fontFamily: {{
            sans: ['"Inter"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
            display: ['"Montserrat"', 'sans-serif']
          }},
          animation: {{
            'fade-in-up': 'fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards',
          }},
          keyframes: {{
            fadeInUp: {{
              '0%': {{ opacity: '0', transform: 'translateY(20px)' }},
              '100%': {{ opacity: '1', transform: 'translateY(0)' }},
            }},
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{ font-family: "Inter", sans-serif; -webkit-font-smoothing: antialiased; }}
    .font-display {{ font-family: "Montserrat", sans-serif; }}
    html {{ scroll-behavior: smooth; }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800">

<script>window.PAGE_CONTEXT = {{ type: "detail", id: "{service_id}" }};</script>
<div id="root"></div>

  <!-- Dummy Divs for Tailwind JIT -->
  <div style="display: none;">
    <div class="bg-violet-50 bg-violet-100 bg-violet-500 bg-violet-600 bg-violet-800 bg-violet-900 text-violet-50 text-violet-100 text-violet-200 text-violet-500 text-violet-600 text-violet-800 text-violet-900 border-violet-100 border-violet-200 border-violet-500 from-violet-600 via-purple-600 to-indigo-800 shadow-violet-200"></div>
    <div class="bg-indigo-50 bg-indigo-100 bg-indigo-500 bg-indigo-600 bg-indigo-800 bg-indigo-900 text-indigo-50 text-indigo-100 text-indigo-200 text-indigo-500 text-indigo-600 text-indigo-800 text-indigo-900 border-indigo-100 border-indigo-200 border-indigo-500 from-indigo-600 via-blue-600 to-slate-800 shadow-indigo-200"></div>
    <div class="bg-cyan-50 bg-cyan-100 bg-cyan-500 bg-cyan-600 bg-cyan-800 bg-cyan-900 text-cyan-50 text-cyan-100 text-cyan-200 text-cyan-500 text-cyan-600 text-cyan-800 text-cyan-900 border-cyan-100 border-cyan-200 border-cyan-500 from-cyan-600 via-sky-500 to-blue-700 shadow-cyan-200"></div>
    <div class="bg-blue-50 bg-blue-100 bg-blue-500 bg-blue-600 bg-blue-800 bg-blue-900 text-blue-50 text-blue-100 text-blue-200 text-blue-500 text-blue-600 text-blue-800 text-blue-900 border-blue-100 border-blue-200 border-blue-500 from-blue-600 via-indigo-500 to-slate-800 shadow-blue-200"></div>
    <div class="bg-orange-50 bg-orange-100 bg-orange-500 bg-orange-600 bg-orange-800 bg-orange-900 text-orange-50 text-orange-100 text-orange-200 text-orange-500 text-orange-600 text-orange-800 text-orange-900 border-orange-100 border-orange-200 border-orange-500 from-orange-600 via-amber-500 to-red-700 shadow-orange-200"></div>
    <div class="bg-emerald-50 bg-emerald-100 bg-emerald-500 bg-emerald-600 bg-emerald-800 bg-emerald-900 text-emerald-50 text-emerald-100 text-emerald-200 text-emerald-500 text-emerald-600 text-emerald-800 text-emerald-900 border-emerald-100 border-emerald-200 border-emerald-500 from-emerald-600 via-green-500 to-teal-700 shadow-emerald-200"></div>
    <div class="bg-teal-50 bg-teal-100 bg-teal-500 bg-teal-600 bg-teal-800 bg-teal-900 text-teal-50 text-teal-100 text-teal-200 text-teal-500 text-teal-600 text-teal-800 text-teal-900 border-teal-100 border-teal-200 border-teal-500 from-teal-600 via-cyan-500 to-emerald-700 shadow-teal-200"></div>
    <div class="bg-slate-50 bg-slate-100 bg-slate-500 bg-slate-600 bg-slate-800 bg-slate-900 text-slate-50 text-slate-100 text-slate-200 text-slate-500 text-slate-600 text-slate-800 text-slate-900 border-slate-100 border-slate-200 border-slate-500 from-slate-800 from-slate-700 to-slate-900 shadow-slate-200"></div>
    <div class="bg-brand-blue bg-brand-dark"></div>
  </div>
  
  <script type="text/babel">

    const {{ useState, useEffect, useMemo }} = React;

    const Icon = ({{ name, size = 24, className = "" }}) => {{
      if (typeof lucide !== 'undefined' && lucide.icons && lucide.icons[name]) {{
        const iconData = lucide.icons[name];
        return React.createElement('svg', {{
          xmlns: "http://www.w3.org/2000/svg",
          width: size,
          height: size,
          viewBox: "0 0 24 24",
          fill: "none",
          stroke: "currentColor",
          strokeWidth: 2,
          strokeLinecap: "round",
          strokeLinejoin: "round",
          className: className
        }}, iconData.map(([tag, attrs], index) => React.createElement(tag, {{ ...attrs, key: index }})));
      }}
      return <span className="inline-block w-4 h-4 bg-gray-300 rounded-full"></span>;
    }};

    const Image = ({{ src, alt, className, ...props }}) => {{
      const [error, setError] = useState(false);
      if (error) return <div className={{`bg-slate-100 flex items-center justify-center text-slate-400 text-xs font-bold ${{className}}`}}>{{alt}}</div>;
      return <img src={{src}} alt={{alt}} className={{className}} onError={{() => setError(true)}} loading="lazy" {{...props}} />;
    }};

    const Header = ({{ scrolled }}) => {{
      return (
        <header className="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md shadow-sm py-3">
          <div className="container mx-auto px-4 flex items-center justify-between max-w-7xl">
            <a href="../index.html" className="flex items-center gap-3 hover:opacity-80 transition-opacity">
              <Image src="../../assets/images/logo.svg" alt="RISEby" className="h-8 md:h-9" />
            </a>
            <nav className="hidden md:flex items-center gap-8">
              <a href="../index.html#services" className="font-semibold tracking-wide transition-colors hover:opacity-70 text-slate-800">Services</a>
              <a href="../about.html" className="font-semibold tracking-wide transition-colors hover:opacity-70 text-slate-800">About</a>
              <a href="../../services/{service_id}.html" className="font-semibold tracking-wide transition-colors hover:opacity-70 text-slate-800 flex items-center gap-1.5">
                <span className="text-lg">🇯🇵</span> JP
              </a>
              <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white px-6 py-2.5 rounded-full font-bold transition-all duration-300 hover:scale-105 hover:shadow-lg hover:bg-slate-800">
                Contact Us
              </a>
            </nav>
          </div>
        </header>
      );
    }};

    const Footer = () => {{
      const currentYear = new Date().getFullYear();
      return (
        <footer className="bg-[#0B0F19] text-white pt-16 pb-8">
          <div className="container mx-auto px-4 max-w-7xl">
            <div className="flex flex-col md:flex-row justify-between gap-12 mb-12">
              <div className="md:w-1/3">
                <a href="../index.html" className="block mb-6">
                  <Image src="../../assets/images/logo.svg" alt="RISEby" className="h-8 brightness-0 invert opacity-90" />
                </a>
                <p className="text-slate-400 text-sm leading-relaxed mb-6">
                  A consulting firm delivering comprehensive solutions to complex enterprise challenges across AI, strategy, technology, and human capital.
                </p>
                <a href="mailto:contact@riseby.net" className="text-slate-400 hover:text-white transition-colors text-sm">
                  contact@riseby.net
                </a>
              </div>
              <div className="grid grid-cols-2 gap-8">
                <div>
                  <h3 className="font-bold text-sm mb-4 text-white tracking-wider font-display">Company</h3>
                  <ul className="space-y-2 text-sm text-slate-400">
                    <li><a href="../about.html" className="hover:text-white transition-colors">About Us</a></li>
                    <li><a href="../index.html#services" className="hover:text-white transition-colors">Services</a></li>
                  </ul>
                </div>
                <div>
                  <h3 className="font-bold text-sm mb-4 text-white tracking-wider font-display">Contact</h3>
                  <ul className="space-y-2 text-sm text-slate-400">
                    <li><a href="mailto:contact@riseby.net" className="hover:text-white transition-colors">Get in Touch</a></li>
                    <li><a href="../privacy.html" className="hover:text-white transition-colors">Privacy Policy</a></li>
                    <li><a href="../../" className="hover:text-white transition-colors">🇯🇵 日本語</a></li>
                  </ul>
                </div>
              </div>
            </div>
            <div className="border-t border-slate-800 pt-8 text-center text-xs text-slate-500">
              © {{currentYear}} RISEby inc. All rights reserved.
            </div>
          </div>
        </footer>
      );
    }};

    const DetailContent = ({{ taskId }}) => {{
      const task = window.TASK_DATABASE ? window.TASK_DATABASE[taskId] : null;
      if (!task) return <div className="pt-32 text-center">Service Not Found</div>;
      const category = window.TASK_CATEGORIES[task.categoryId];

      return (
        <div className="pt-24 pb-16 animate-fade-in-up">
           <div className="container mx-auto px-4 max-w-5xl mb-16">
              <div className="text-center mb-10">
                 <a href={{`./${{category.id || task.categoryId}}.html`}} className={{`inline-block mb-6 text-xs font-bold tracking-widest uppercase text-${{task.themeColor}}-600 bg-${{task.themeColor}}-50 px-3 py-1 rounded-full hover:bg-${{task.themeColor}}-100 transition-colors`}}>{{category.title}}</a>
                 <h1 className="text-3xl md:text-5xl font-bold text-slate-900 mb-6 leading-tight">{{task.title}}</h1>
                 <p className="text-xl text-slate-500 font-medium mb-8">{{task.subtitle}}</p>
                 <p className="text-slate-600 max-w-3xl mx-auto leading-loose">{{task.hero?.description}}</p>
              </div>
              <div className="grid grid-cols-3 gap-4 md:gap-8 max-w-4xl mx-auto">
                 {{task.hero?.stats?.map((stat, idx) => (
                    <div key={{idx}} className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 text-center">
                       <div className={{`text-2xl md:text-3xl font-bold text-${{task.themeColor}}-600 mb-1 font-display`}}>{{stat.value}}</div>
                       <div className="text-xs text-slate-400 font-bold uppercase">{{stat.label}}</div>
                    </div>
                 ))}}
              </div>
           </div>
           
           <div className="bg-slate-50 py-20 border-y border-slate-200">
              <div className="container mx-auto px-4 max-w-5xl">
                 <h2 className="text-2xl font-bold text-center mb-12">Common Challenges We Address</h2>
                 <div className="grid md:grid-cols-3 gap-8">
                    {{task.painPoints?.map((pain, idx) => (
                       <div key={{idx}} className="bg-white p-8 rounded-2xl shadow-sm border border-slate-100">
                          <div className={{`w-12 h-12 rounded-full bg-${{task.themeColor}}-100 text-${{task.themeColor}}-600 flex items-center justify-center mb-6`}}>
                             <Icon name={{pain.icon}} size={{24}} />
                          </div>
                          <h3 className="font-bold text-slate-900 mb-3">{{pain.title}}</h3>
                          <p className="text-sm text-slate-600 leading-relaxed">{{pain.desc}}</p>
                       </div>
                    ))}}
                 </div>
              </div>
           </div>
           
           <div className="py-20 container mx-auto px-4 max-w-5xl">
                <div className="flex flex-col md:flex-row gap-12 items-center">
                    <div className="md:w-1/2">
                        <h2 className="text-2xl font-bold mb-6">Why Solutions Stall:<br/><span className={{`text-${{task.themeColor}}-600`}}>Structural Barriers</span></h2>
                        <div className="space-y-6">
                            {{task.structuralIssues?.map((issue, idx) => (
                                <div key={{idx}} className="flex gap-4">
                                    <div className={{`flex-shrink-0 w-8 h-8 rounded-full bg-${{task.themeColor}}-50 text-${{task.themeColor}}-600 flex items-center justify-center font-bold`}}>{{idx + 1}}</div>
                                    <div>
                                        <h4 className="font-bold text-slate-900 mb-1">{{issue.title}}</h4>
                                        <p className="text-sm text-slate-600 leading-relaxed">{{issue.desc}}</p>
                                    </div>
                                </div>
                            ))}}
                        </div>
                    </div>
                    <div className="md:w-1/2">
                        <div className={{`bg-${{task.themeColor}}-900 text-white p-10 rounded-3xl shadow-2xl relative overflow-hidden`}}>
                             <div className="absolute top-0 right-0 w-64 h-64 bg-white opacity-5 rounded-full -mr-20 -mt-20"></div>
                             <h3 className="text-xl font-bold mb-8 relative z-10">The RISEby Approach</h3>
                             <div className="space-y-6 relative z-10">
                                {{task.solutions?.map((sol, idx) => (
                                    <div key={{idx}} className="border-l-2 border-white/30 pl-6 relative">
                                        <div className="absolute -left-[5px] top-0 w-2 h-2 rounded-full bg-white"></div>
                                        <div className="text-xs font-bold text-white/60 mb-1">{{sol.phase}}</div>
                                        <div className="font-bold text-lg mb-1">{{sol.title}}</div>
                                        <div className="text-sm text-white/80">{{sol.desc}}</div>
                                    </div>
                                ))}}
                             </div>
                        </div>
                    </div>
                </div>
           </div>

           <div className="bg-slate-900 text-white py-20 text-center">
                <div className="container mx-auto px-4 max-w-3xl">
                    <h2 className="text-3xl font-bold mb-6">Ready to Address This Challenge?</h2>
                    <p className="text-slate-400 mb-10">
                        Our experienced team specializing in {{task.title}}<br/>
                        is ready to partner with you.
                    </p>
                    <a href="mailto:contact@riseby.net" className={{`inline-flex items-center gap-2 bg-${{task.themeColor}}-500 text-white px-10 py-4 rounded-full font-bold hover:bg-white hover:text-${{task.themeColor}}-600 transition-all duration-300 shadow-lg`}}><Icon name="Mail" size={{20}} /> Schedule a Consultation</a>
                </div>
           </div>
        </div>
      );
    }};

    const App = () => {{
      const ctx = window.PAGE_CONTEXT || {{ type: 'detail', id: '{service_id}' }};
      return (
        <div className="min-h-screen font-sans text-slate-800 antialiased selection:bg-brand-blue selection:text-white">
          <Header />
          <DetailContent taskId={{ctx.id}} />
          <Footer />
        </div>
      );
    }};

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<App />);

</script>

<!-- Noscript fallback for SEO -->
<noscript>
  <div style="padding: 40px; max-width: 800px; margin: 0 auto;">
    <h1>{title} - RISEby inc.</h1>
    <p>{description}</p>
    <p><a href="../index.html">Back to Home</a> | <a href="mailto:contact@riseby.net">Contact Us</a></p>
  </div>
</noscript>
</body>
</html>
'''

CATEGORY_TEMPLATE = '''<!DOCTYPE html>
<html lang="en" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8">

  <title>{title} | RISEby</title>
  <meta name="description" content="{description}">
  
  <!-- OGP -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="RISEby inc.">
  <meta property="og:locale" content="en_US">
  <meta property="og:url" content="https://riseby.net/en/services/{category_id}.html">
  <meta property="og:title" content="{title} | RISEby">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://riseby.net/assets/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  
  <!-- Canonical & Alternate -->
  <link rel="canonical" href="https://riseby.net/en/services/{category_id}.html">
  <link rel="alternate" hreflang="ja" href="https://riseby.net/services/{category_id}.html">
  <link rel="alternate" hreflang="en" href="https://riseby.net/en/services/{category_id}.html">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="../../assets/images/favicon.svg">
  <link rel="apple-touch-icon" sizes="180x180" href="../../assets/images/apple-touch-icon.png">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Libraries -->
  <script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Load Database -->
  <script src="../assets/tasks.js"></script>

  <!-- Tailwind Config -->
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{ blue: '#003E68', red: '#ED1C24', dark: '#0B0F19' }}
          }},
          fontFamily: {{
            sans: ['"Inter"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
            display: ['"Montserrat"', 'sans-serif']
          }},
          animation: {{
            'fade-in-up': 'fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards',
          }},
          keyframes: {{
            fadeInUp: {{
              '0%': {{ opacity: '0', transform: 'translateY(20px)' }},
              '100%': {{ opacity: '1', transform: 'translateY(0)' }},
            }},
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{ font-family: "Inter", sans-serif; -webkit-font-smoothing: antialiased; }}
    .font-display {{ font-family: "Montserrat", sans-serif; }}
    html {{ scroll-behavior: smooth; }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800">

<script>window.PAGE_CONTEXT = {{ type: "category", id: "{category_id}" }};</script>
<div id="root"></div>

  <!-- Dummy Divs for Tailwind JIT -->
  <div style="display: none;">
    <div class="bg-violet-50 bg-violet-100 bg-violet-500 bg-violet-600 bg-violet-800 bg-violet-900 text-violet-50 text-violet-100 text-violet-200 text-violet-500 text-violet-600 text-violet-800 text-violet-900 border-violet-100 border-violet-200 border-violet-500"></div>
    <div class="bg-indigo-50 bg-indigo-100 bg-indigo-500 bg-indigo-600 bg-indigo-800 bg-indigo-900 text-indigo-50 text-indigo-100 text-indigo-200 text-indigo-500 text-indigo-600 text-indigo-800 text-indigo-900 border-indigo-100 border-indigo-200 border-indigo-500"></div>
    <div class="bg-cyan-50 bg-cyan-100 bg-cyan-500 bg-cyan-600 bg-cyan-800 bg-cyan-900 text-cyan-50 text-cyan-100 text-cyan-200 text-cyan-500 text-cyan-600 text-cyan-800 text-cyan-900 border-cyan-100 border-cyan-200 border-cyan-500"></div>
    <div class="bg-blue-50 bg-blue-100 bg-blue-500 bg-blue-600 bg-blue-800 bg-blue-900 text-blue-50 text-blue-100 text-blue-200 text-blue-500 text-blue-600 text-blue-800 text-blue-900 border-blue-100 border-blue-200 border-blue-500"></div>
    <div class="bg-orange-50 bg-orange-100 bg-orange-500 bg-orange-600 bg-orange-800 bg-orange-900 text-orange-50 text-orange-100 text-orange-200 text-orange-500 text-orange-600 text-orange-800 text-orange-900 border-orange-100 border-orange-200 border-orange-500"></div>
    <div class="bg-emerald-50 bg-emerald-100 bg-emerald-500 bg-emerald-600 bg-emerald-800 bg-emerald-900 text-emerald-50 text-emerald-100 text-emerald-200 text-emerald-500 text-emerald-600 text-emerald-800 text-emerald-900 border-emerald-100 border-emerald-200 border-emerald-500"></div>
    <div class="bg-teal-50 bg-teal-100 bg-teal-500 bg-teal-600 bg-teal-800 bg-teal-900 text-teal-50 text-teal-100 text-teal-200 text-teal-500 text-teal-600 text-teal-800 text-teal-900 border-teal-100 border-teal-200 border-teal-500"></div>
    <div class="bg-slate-50 bg-slate-100 bg-slate-500 bg-slate-600 bg-slate-800 bg-slate-900 text-slate-50 text-slate-100 text-slate-200 text-slate-500 text-slate-600 text-slate-800 text-slate-900 border-slate-100 border-slate-200 border-slate-500"></div>
    <div class="bg-brand-blue bg-brand-dark"></div>
  </div>
  
  <script type="text/babel">

    const {{ useState, useEffect, useMemo }} = React;

    const Icon = ({{ name, size = 24, className = "" }}) => {{
      if (typeof lucide !== 'undefined' && lucide.icons && lucide.icons[name]) {{
        const iconData = lucide.icons[name];
        return React.createElement('svg', {{
          xmlns: "http://www.w3.org/2000/svg",
          width: size,
          height: size,
          viewBox: "0 0 24 24",
          fill: "none",
          stroke: "currentColor",
          strokeWidth: 2,
          strokeLinecap: "round",
          strokeLinejoin: "round",
          className: className
        }}, iconData.map(([tag, attrs], index) => React.createElement(tag, {{ ...attrs, key: index }})));
      }}
      return <span className="inline-block w-4 h-4 bg-gray-300 rounded-full"></span>;
    }};

    const Image = ({{ src, alt, className, ...props }}) => {{
      const [error, setError] = useState(false);
      if (error) return <div className={{`bg-slate-100 flex items-center justify-center text-slate-400 text-xs font-bold ${{className}}`}}>{{alt}}</div>;
      return <img src={{src}} alt={{alt}} className={{className}} onError={{() => setError(true)}} loading="lazy" {{...props}} />;
    }};

    const Header = () => {{
      return (
        <header className="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md shadow-sm py-3">
          <div className="container mx-auto px-4 flex items-center justify-between max-w-7xl">
            <a href="../index.html" className="flex items-center gap-3 hover:opacity-80 transition-opacity">
              <Image src="../../assets/images/logo.svg" alt="RISEby" className="h-8 md:h-9" />
            </a>
            <nav className="hidden md:flex items-center gap-8">
              <a href="../index.html#services" className="font-semibold tracking-wide transition-colors text-brand-blue">Services</a>
              <a href="../about.html" className="font-semibold tracking-wide transition-colors hover:opacity-70 text-slate-800">About</a>
              <a href="../../services/{category_id}.html" className="font-semibold tracking-wide transition-colors hover:opacity-70 text-slate-800 flex items-center gap-1.5">
                <span className="text-lg">🇯🇵</span> JP
              </a>
              <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white px-6 py-2.5 rounded-full font-bold transition-all duration-300 hover:scale-105 hover:shadow-lg hover:bg-slate-800">
                Contact Us
              </a>
            </nav>
          </div>
        </header>
      );
    }};

    const Footer = () => {{
      const currentYear = new Date().getFullYear();
      return (
        <footer className="bg-[#0B0F19] text-white pt-16 pb-8">
          <div className="container mx-auto px-4 max-w-7xl">
            <div className="flex flex-col md:flex-row justify-between gap-12 mb-12">
              <div className="md:w-1/3">
                <a href="../index.html" className="block mb-6">
                  <Image src="../../assets/images/logo.svg" alt="RISEby" className="h-8 brightness-0 invert opacity-90" />
                </a>
                <p className="text-slate-400 text-sm leading-relaxed mb-6">
                  A consulting firm delivering comprehensive solutions to complex enterprise challenges across AI, strategy, technology, and human capital.
                </p>
                <a href="mailto:contact@riseby.net" className="text-slate-400 hover:text-white transition-colors text-sm">
                  contact@riseby.net
                </a>
              </div>
              <div className="grid grid-cols-2 gap-8">
                <div>
                  <h3 className="font-bold text-sm mb-4 text-white tracking-wider font-display">Company</h3>
                  <ul className="space-y-2 text-sm text-slate-400">
                    <li><a href="../about.html" className="hover:text-white transition-colors">About Us</a></li>
                    <li><a href="../index.html#services" className="hover:text-white transition-colors">Services</a></li>
                  </ul>
                </div>
                <div>
                  <h3 className="font-bold text-sm mb-4 text-white tracking-wider font-display">Contact</h3>
                  <ul className="space-y-2 text-sm text-slate-400">
                    <li><a href="mailto:contact@riseby.net" className="hover:text-white transition-colors">Get in Touch</a></li>
                    <li><a href="../privacy.html" className="hover:text-white transition-colors">Privacy Policy</a></li>
                    <li><a href="../../" className="hover:text-white transition-colors">🇯🇵 日本語</a></li>
                  </ul>
                </div>
              </div>
            </div>
            <div className="border-t border-slate-800 pt-8 text-center text-xs text-slate-500">
              © {{currentYear}} RISEby inc. All rights reserved.
            </div>
          </div>
        </footer>
      );
    }};

    const CategoryContent = ({{ categoryId }}) => {{
      const category = window.TASK_CATEGORIES ? window.TASK_CATEGORIES[categoryId] : null;
      if (!category) return <div className="pt-32 text-center">Loading...</div>;
      const tasks = Object.entries(window.TASK_DATABASE || {{}}).filter(([_, t]) => t.categoryId === categoryId).map(([id, t]) => ({{ id, ...t }}));

      return (
        <div className="pt-24 pb-16 animate-fade-in-up">
          <div className={{`bg-${{category.themeColor}}-50 py-20 border-b border-${{category.themeColor}}-100`}}>
            <div className="container mx-auto px-4 text-center">
              <h1 className="text-4xl md:text-5xl font-bold text-slate-900 mb-6">{{category.title}}</h1>
              <p className="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">{{category.description}}</p>
            </div>
          </div>
          <div className="container mx-auto px-4 max-w-6xl -mt-10 mb-12">
             <div className="bg-white p-8 md:p-12 rounded-2xl shadow-xl border border-slate-100 mb-16 relative overflow-hidden">
                <div className="md:flex gap-10 items-start">
                    <div className="md:w-1/3 mb-8 md:mb-0">
                        <div className={{`w-16 h-16 rounded-2xl bg-${{category.themeColor}}-100 flex items-center justify-center text-${{category.themeColor}}-600 mb-6`}}><Icon name="TrendingUp" size={{32}} /></div>
                        <h3 className="text-xl font-bold text-slate-900 mb-2">Market Insight</h3>
                        <p className="text-slate-600 text-sm leading-relaxed">{{category.insight?.trend?.text}}</p>
                    </div>
                    <div className="md:w-2/3 grid sm:grid-cols-2 gap-6">
                        {{category.insight?.approaches?.map((app, idx) => (
                            <div key={{idx}} className="bg-slate-50 p-5 rounded-xl border border-slate-100">
                                <h4 className={{`font-bold text-${{category.themeColor}}-700 mb-2 text-sm flex items-center gap-2`}}><Icon name="CheckCircle" size={{16}} /> {{app.title}}</h4>
                                <p className="text-slate-600 text-xs leading-relaxed">{{app.desc}}</p>
                            </div>
                        ))}}
                    </div>
                </div>
             </div>
             <h2 className="text-2xl font-bold text-slate-900 mb-8 border-l-4 border-slate-900 pl-4">Our Services</h2>
             <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                {{tasks.map(task => (
                    <a key={{task.id}} href={{`./${{task.id}}.html`}} className="group block bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                        <div className={{`w-12 h-12 rounded-xl bg-${{category.themeColor}}-50 text-${{category.themeColor}}-600 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform`}}><Icon name="ArrowRight" size={{24}} /></div>
                        <h3 className="text-lg font-bold text-slate-900 mb-3 group-hover:text-brand-blue transition-colors">{{task.title}}</h3>
                        <p className="text-slate-500 text-sm line-clamp-2 mb-4">{{task.hero?.description}}</p>
                        <span className={{`text-xs font-bold text-${{category.themeColor}}-600 flex items-center gap-1`}}>Learn More <Icon name="ChevronRight" size={{12}} /></span>
                    </a>
                ))}}
             </div>
          </div>
        </div>
      );
    }};

    const App = () => {{
      const ctx = window.PAGE_CONTEXT || {{ type: 'category', id: '{category_id}' }};
      return (
        <div className="min-h-screen font-sans text-slate-800 antialiased selection:bg-brand-blue selection:text-white">
          <Header />
          <CategoryContent categoryId={{ctx.id}} />
          <Footer />
        </div>
      );
    }};

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<App />);

</script>

<!-- Noscript fallback for SEO -->
<noscript>
  <div style="padding: 40px; max-width: 800px; margin: 0 auto;">
    <h1>{title} - RISEby inc.</h1>
    <p>{description}</p>
    <p><a href="../index.html">Back to Home</a> | <a href="mailto:contact@riseby.net">Contact Us</a></p>
  </div>
</noscript>
</body>
</html>
'''

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    services_dir = os.path.join(script_dir, "en", "services")
    
    # Create services directory if it doesn't exist
    os.makedirs(services_dir, exist_ok=True)
    
    # Generate service detail pages
    for service_id, (title, description) in SERVICES.items():
        content = DETAIL_TEMPLATE.format(
            service_id=service_id,
            title=title,
            description=description
        )
        filepath = os.path.join(services_dir, f"{service_id}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filepath}")
    
    # Generate category pages
    for category_id, (title, description) in CATEGORIES.items():
        content = CATEGORY_TEMPLATE.format(
            category_id=category_id,
            title=title,
            description=description
        )
        filepath = os.path.join(services_dir, f"{category_id}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filepath}")
    
    # Also create index.html for services
    index_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0;url=../index.html#services">
  <title>Services | RISEby</title>
</head>
<body>
  <p>Redirecting to <a href="../index.html#services">Services</a>...</p>
</body>
</html>
'''
    with open(os.path.join(services_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"Generated: {os.path.join(services_dir, 'index.html')}")
    
    print(f"\\nDone! Generated {len(SERVICES)} service pages and {len(CATEGORIES)} category pages.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ブログ一覧ページ生成スクリプト
クールなデザインのブログトップページを生成
"""

import os
import re
from datetime import datetime

BLOG_DIR = "blog"
BASE_URL = "https://riseby.net"

def extract_blog_metadata(filepath):
    """ブログ記事からメタデータを抽出"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # タイトル抽出
    title_match = re.search(r'<title>([^|]+)\|', content)
    title = title_match.group(1).strip() if title_match else os.path.basename(filepath).replace('.html', '')
    
    # 説明抽出
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    description = desc_match.group(1) if desc_match else ""
    
    # 日付抽出（JSON-LDから）
    date_match = re.search(r'"datePublished":\s*"([^"]+)"', content)
    date = date_match.group(1) if date_match else "2025-12-01"
    
    # カテゴリ抽出（ディレクトリ名から）
    category = os.path.basename(os.path.dirname(filepath)).upper()
    
    return {
        'title': title,
        'description': description[:150] + '...' if len(description) > 150 else description,
        'date': date,
        'category': category,
        'url': filepath.replace('\\', '/')
    }


def generate_blog_index():
    """ブログ一覧ページを生成"""
    articles = []
    
    # すべてのブログ記事を収集
    for root, dirs, files in os.walk(BLOG_DIR):
        for file in files:
            if file.endswith('.html') and file != 'index.html':
                filepath = os.path.join(root, file)
                metadata = extract_blog_metadata(filepath)
                articles.append(metadata)
    
    # 日付でソート（新しい順）
    articles.sort(key=lambda x: x['date'], reverse=True)
    
    # 記事カードをJavaScript配列として生成
    articles_js = []
    for article in articles:
        escaped_desc = article['description'].replace('"', "'")
        escaped_title = article['title'].replace('"', "'")
        url_path = article['url'].replace('blog/', '')
        articles_js.append(
            '{' + f'''
            title: "{escaped_title}",
            description: "{escaped_desc}",
            date: "{article['date']}",
            category: "{article['category']}",
            url: "./{url_path}"
        ''' + '}'
        )
    
    articles_array = ',\n        '.join(articles_js)
    
    html = f'''<!DOCTYPE html>
<html lang="ja" prefix="og: http://ogp.me/ns#">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Insights | RISEby Blog</title>
    <meta name="description" content="AI・生成AI、DX、経営戦略に関する最新のインサイトをお届けします。経営者・ビジネスリーダー向けの実践的なナレッジを発信。">
    
    <!-- OGP -->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="RISEby inc.">
    <meta property="og:locale" content="ja_JP">
    <meta property="og:url" content="{BASE_URL}/blog/">
    <meta property="og:title" content="Insights | RISEby Blog">
    <meta property="og:description" content="AI・生成AI、DX、経営戦略に関する最新のインサイトをお届けします。">
    <meta property="og:image" content="{BASE_URL}/assets/images/og-image.jpg">
    <meta name="twitter:card" content="summary_large_image">
    
    <!-- Canonical -->
    <link rel="canonical" href="{BASE_URL}/blog/">
    
    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="../assets/images/favicon.svg">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
    
    <!-- Libraries -->
    <script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{ blue: '#003E68', red: '#ED1C24', dark: '#0B0F19' }}
                    }},
                    fontFamily: {{
                        sans: ['"Noto Sans JP"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
                        display: ['"Montserrat"', 'sans-serif']
                    }},
                    animation: {{
                        'fade-in-up': 'fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards',
                    }},
                    keyframes: {{
                        fadeInUp: {{
                            '0%': {{ opacity: '0', transform: 'translateY(20px)' }},
                            '100%': {{ opacity: '1', transform: 'translateY(0)' }},
                        }}
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        body {{ font-family: "Noto Sans JP", sans-serif; -webkit-font-smoothing: antialiased; }}
        .font-display {{ font-family: "Montserrat", sans-serif; }}
        html {{ scroll-behavior: smooth; }}
        .line-clamp-2 {{ display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
        .line-clamp-3 {{ display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800">
    <div id="root"></div>
    
    <script type="text/babel">
        const {{ useState, useEffect, useMemo }} = React;
        
        const ARTICLES = [
        {articles_array}
        ];
        
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
        
        const Header = () => {{
            const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
            const [scrolled, setScrolled] = useState(false);
            
            useEffect(() => {{
                const handleScroll = () => setScrolled(window.scrollY > 20);
                window.addEventListener('scroll', handleScroll);
                return () => window.removeEventListener('scroll', handleScroll);
            }}, []);
            
            return (
                <header className={{`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${{scrolled ? 'bg-white/95 backdrop-blur-md shadow-sm py-3' : 'bg-white py-4 shadow-sm'}}`}}>
                    <div className="container mx-auto px-4 flex items-center justify-between max-w-7xl">
                        <a href="../index.html" className="flex items-center gap-3 hover:opacity-80 transition-opacity">
                            <img src="../assets/images/logo.svg" alt="RISEby" className="h-8 md:h-9" />
                        </a>
                        <nav className="hidden md:flex items-center gap-8">
                            <a href="../index.html#services" className="font-bold tracking-wide transition-colors hover:opacity-70 text-slate-800">サービス</a>
                            <a href="./" className="font-bold tracking-wide transition-colors text-brand-blue">ブログ</a>
                            <a href="../about.html" className="font-bold tracking-wide transition-colors hover:opacity-70 text-slate-800">会社概要</a>
                            <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white px-6 py-2.5 rounded-full font-bold transition-all duration-300 hover:scale-105 hover:shadow-lg hover:bg-slate-800">
                                お問い合わせ
                            </a>
                        </nav>
                        <button onClick={{() => setMobileMenuOpen(!mobileMenuOpen)}} className="md:hidden p-2 text-slate-800">
                            <Icon name={{mobileMenuOpen ? "X" : "Menu"}} size={{24}} />
                        </button>
                    </div>
                    {{mobileMenuOpen && (
                        <div className="md:hidden absolute top-full left-0 right-0 bg-white border-t border-slate-100 shadow-xl p-4 flex flex-col gap-4">
                            <a href="../index.html#services" className="text-slate-800 font-bold py-3 border-b border-slate-50">サービス</a>
                            <a href="./" className="text-brand-blue font-bold py-3 border-b border-slate-50">ブログ</a>
                            <a href="../about.html" className="text-slate-800 font-bold py-3 border-b border-slate-50">会社概要</a>
                            <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white text-center py-3.5 rounded-lg font-bold shadow-md mt-2">お問い合わせ</a>
                        </div>
                    )}}
                </header>
            );
        }};
        
        const Footer = () => {{
            const currentYear = new Date().getFullYear();
            return (
                <footer className="bg-[#0B0F19] text-white pt-20 pb-10 border-t border-slate-800">
                    <div className="container mx-auto px-4 max-w-7xl">
                        <div className="flex flex-col md:flex-row justify-between gap-12 mb-16">
                            <div className="md:w-1/3">
                                <a href="../index.html" className="block mb-6">
                                    <img src="../assets/images/logo.svg" alt="RISEby" className="h-8 brightness-0 invert opacity-90" />
                                </a>
                                <p className="text-slate-400 text-sm leading-relaxed mb-6">
                                    企業の複合的な経営課題を、AI・戦略・テクノロジー・人の観点から包括的に解決するコンサルティングファーム。
                                </p>
                                <a href="mailto:contact@riseby.net" className="text-slate-400 hover:text-white transition-colors text-sm flex items-center gap-2">
                                    <Icon name="Mail" size={{16}} />
                                    contact@riseby.net
                                </a>
                            </div>
                            <div className="grid grid-cols-2 gap-8">
                                <div>
                                    <h3 className="font-bold text-sm mb-4 text-white tracking-wider font-display">Company</h3>
                                    <ul className="space-y-2 text-sm text-slate-400">
                                        <li><a href="../about.html" className="hover:text-white transition-colors">会社概要</a></li>
                                        <li><a href="../index.html#services" className="hover:text-white transition-colors">サービス</a></li>
                                        <li><a href="./" className="hover:text-white transition-colors">ブログ</a></li>
                                    </ul>
                                </div>
                                <div>
                                    <h3 className="font-bold text-sm mb-4 text-white tracking-wider font-display">Contact</h3>
                                    <ul className="space-y-2 text-sm text-slate-400">
                                        <li><a href="mailto:contact@riseby.net" className="hover:text-white transition-colors">お問い合わせ</a></li>
                                        <li><a href="../privacy.html" className="hover:text-white transition-colors">プライバシーポリシー</a></li>
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
        
        const ArticleCard = ({{ article, featured = false }}) => {{
            const formatDate = (dateStr) => {{
                const date = new Date(dateStr);
                return date.toLocaleDateString('ja-JP', {{ year: 'numeric', month: 'long', day: 'numeric' }});
            }};
            
            if (featured) {{
                return (
                    <a href={{article.url}} className="group block bg-gradient-to-br from-brand-blue to-slate-800 rounded-3xl overflow-hidden shadow-2xl hover:shadow-3xl transition-all duration-500 hover:-translate-y-2">
                        <div className="p-10 md:p-14">
                            <div className="flex items-center gap-4 mb-6">
                                <span className="bg-white/20 text-white text-xs px-3 py-1 rounded-full font-bold uppercase tracking-wider font-display">{{article.category}}</span>
                                <span className="text-white/60 text-sm">{{formatDate(article.date)}}</span>
                            </div>
                            <h2 className="text-2xl md:text-4xl font-bold text-white mb-6 leading-tight group-hover:text-blue-200 transition-colors">
                                {{article.title}}
                            </h2>
                            <p className="text-white/70 text-lg leading-relaxed mb-8 line-clamp-3">
                                {{article.description}}
                            </p>
                            <div className="flex items-center gap-2 text-white font-bold group-hover:gap-4 transition-all">
                                <span>記事を読む</span>
                                <Icon name="ArrowRight" size={{20}} className="group-hover:translate-x-2 transition-transform" />
                            </div>
                        </div>
                    </a>
                );
            }}
            
            return (
                <a href={{article.url}} className="group block bg-white rounded-2xl overflow-hidden shadow-sm border border-slate-100 hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                    <div className="p-6 md:p-8">
                        <div className="flex items-center gap-3 mb-4">
                            <span className="bg-violet-100 text-violet-700 text-xs px-2.5 py-1 rounded-full font-bold uppercase tracking-wider font-display">{{article.category}}</span>
                            <span className="text-slate-400 text-xs">{{formatDate(article.date)}}</span>
                        </div>
                        <h3 className="text-lg font-bold text-slate-900 mb-3 leading-snug group-hover:text-brand-blue transition-colors line-clamp-2">
                            {{article.title}}
                        </h3>
                        <p className="text-slate-500 text-sm leading-relaxed line-clamp-2 mb-4">
                            {{article.description}}
                        </p>
                        <div className="flex items-center gap-1 text-brand-blue text-sm font-bold group-hover:gap-2 transition-all">
                            <span>続きを読む</span>
                            <Icon name="ChevronRight" size={{16}} />
                        </div>
                    </div>
                </a>
            );
        }};
        
        const BlogIndex = () => {{
            const [searchQuery, setSearchQuery] = useState('');
            const [visibleCount, setVisibleCount] = useState(12);
            
            const filteredArticles = useMemo(() => {{
                if (!searchQuery) return ARTICLES;
                const query = searchQuery.toLowerCase();
                return ARTICLES.filter(article => 
                    article.title.toLowerCase().includes(query) ||
                    article.description.toLowerCase().includes(query)
                );
            }}, [searchQuery]);
            
            const featuredArticle = ARTICLES[0];
            const regularArticles = filteredArticles.slice(searchQuery ? 0 : 1, visibleCount);
            
            return (
                <div className="min-h-screen flex flex-col">
                    <Header />
                    
                    <main className="flex-grow pt-24">
                        {{/* Hero Section */}}
                        <section className="py-16 md:py-24 bg-gradient-to-b from-slate-100 to-slate-50">
                            <div className="container mx-auto px-4 max-w-7xl">
                                <div className="text-center mb-12">
                                    <div className="inline-block px-4 py-1.5 bg-slate-900 text-white rounded-full text-xs font-bold uppercase tracking-wider mb-6 font-display">
                                        Insights
                                    </div>
                                    <h1 className="text-4xl md:text-6xl font-bold text-slate-900 mb-6">
                                        ナレッジ & インサイト
                                    </h1>
                                    <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                                        AI・DX・経営戦略の最新トレンドと実践的なナレッジを、経営者・ビジネスリーダー向けにお届けします。
                                    </p>
                                </div>
                                
                                {{/* Search */}}
                                <div className="max-w-xl mx-auto mb-16">
                                    <div className="relative">
                                        <Icon name="Search" size={{20}} className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400" />
                                        <input
                                            type="text"
                                            placeholder="記事を検索..."
                                            value={{searchQuery}}
                                            onChange={{(e) => setSearchQuery(e.target.value)}}
                                            className="w-full pl-12 pr-4 py-4 rounded-2xl border border-slate-200 bg-white shadow-sm focus:outline-none focus:ring-2 focus:ring-brand-blue focus:border-transparent transition-all text-lg"
                                        />
                                    </div>
                                </div>
                                
                                {{/* Featured Article */}}
                                {{!searchQuery && (
                                    <div className="mb-16">
                                        <ArticleCard article={{featuredArticle}} featured />
                                    </div>
                                )}}
                            </div>
                        </section>
                        
                        {{/* Article Grid */}}
                        <section className="py-16 bg-slate-50">
                            <div className="container mx-auto px-4 max-w-7xl">
                                <div className="flex items-center justify-between mb-10">
                                    <h2 className="text-2xl font-bold text-slate-900">
                                        {{searchQuery ? `検索結果: ${{filteredArticles.length}}件` : '最新の記事'}}
                                    </h2>
                                    <div className="text-sm text-slate-500">
                                        全{{ARTICLES.length}}記事
                                    </div>
                                </div>
                                
                                <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
                                    {{regularArticles.map((article, idx) => (
                                        <ArticleCard key={{idx}} article={{article}} />
                                    ))}}
                                </div>
                                
                                {{filteredArticles.length > visibleCount && (
                                    <div className="text-center mt-12">
                                        <button
                                            onClick={{() => setVisibleCount(prev => prev + 12)}}
                                            className="inline-flex items-center gap-2 bg-white border-2 border-slate-200 text-slate-700 px-8 py-4 rounded-full font-bold hover:border-brand-blue hover:text-brand-blue transition-all"
                                        >
                                            <span>もっと見る</span>
                                            <Icon name="ChevronDown" size={{20}} />
                                        </button>
                                    </div>
                                )}}
                                
                                {{filteredArticles.length === 0 && (
                                    <div className="text-center py-20">
                                        <Icon name="FileQuestion" size={{48}} className="mx-auto text-slate-300 mb-4" />
                                        <p className="text-slate-500 text-lg">該当する記事が見つかりませんでした</p>
                                    </div>
                                )}}
                            </div>
                        </section>
                        
                        {{/* CTA Section */}}
                        <section className="py-20 bg-white border-t border-slate-200">
                            <div className="container mx-auto px-4 max-w-3xl text-center">
                                <h2 className="text-3xl font-bold text-slate-900 mb-6">
                                    AI活用について相談する
                                </h2>
                                <p className="text-lg text-slate-600 mb-10">
                                    記事を読んで興味を持たれた方は、お気軽にご相談ください。<br/>
                                    経験豊富なコンサルタントが、貴社の課題解決をサポートします。
                                </p>
                                <a href="mailto:contact@riseby.net" className="inline-flex items-center gap-2 bg-brand-blue text-white px-10 py-4 rounded-full font-bold text-lg shadow-xl hover:shadow-2xl hover:bg-slate-800 transition-all hover:-translate-y-1">
                                    <Icon name="Mail" size={{20}} />
                                    無料相談を申し込む
                                </a>
                            </div>
                        </section>
                    </main>
                    
                    <Footer />
                </div>
            );
        }};
        
        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<BlogIndex />);
    </script>
</body>
</html>
'''
    
    # blog/index.html に出力
    output_path = os.path.join(BLOG_DIR, 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated: {output_path}")
    print(f"Total articles: {len(articles)}")


if __name__ == "__main__":
    generate_blog_index()

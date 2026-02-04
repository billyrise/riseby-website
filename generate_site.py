#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RISEby サイトジェネレーター (SEO Complete Version)
- 各ページに固有のCanonical URL、OGP、構造化データを設定
- sitemap.xmlを自動生成
- robots.txtを最適化
"""

import os
import re
import shutil
import json
from datetime import datetime

# ==========================================
# 設定
# ==========================================
BASE_URL = "https://riseby.net"
INDEX_HTML_PATH = 'index.html'
OUTPUT_DIR = 'services'
BLOG_DIR = 'blog'

TASKS_JS_PATH = None
POSSIBLE_PATHS = [
    os.path.join('assets', 'js', 'tasks.js'),
    os.path.join('assets', 'tasks.js'),
    'tasks.js'
]
for path in POSSIBLE_PATHS:
    if os.path.exists(path):
        TASKS_JS_PATH = path
        break

# ==========================================
# tasks.js パーサー（改良版）
# ==========================================
def parse_tasks_js(content):
    """tasks.jsからカテゴリとタスクを抽出"""
    categories = {}
    tasks = {}
    
    # カテゴリの抽出（改良版正規表現）
    cat_section = re.search(r'window\.TASK_CATEGORIES\s*=\s*\{([\s\S]*?)\};', content)
    if cat_section:
        cat_text = cat_section.group(1)
        # 各カテゴリを抽出
        cat_pattern = r'"(\w+)":\s*\{[^}]*?title:\s*"([^"]+)"[^}]*?description:\s*"([^"]+)"[^}]*?themeColor:\s*"([^"]+)"'
        for m in re.finditer(cat_pattern, cat_text, re.DOTALL):
            cat_id = m.group(1)
            categories[cat_id] = {
                'id': cat_id,
                'title': m.group(2),
                'description': m.group(3),
                'themeColor': m.group(4)
            }
    
    # タスクの抽出（改良版）
    task_section = re.search(r'window\.TASK_DATABASE\s*=\s*\{([\s\S]*)\};', content)
    if task_section:
        task_text = task_section.group(1)
        # 各タスクブロックを抽出
        task_pattern = r'"(\w+)":\s*\{\s*categoryId:\s*"(\w+)"[^}]*?category:\s*"([^"]+)"[^}]*?title:\s*"([^"]+)"[^}]*?subtitle:\s*"([^"]+)"[^}]*?themeColor:\s*"(\w+)"'
        for m in re.finditer(task_pattern, task_text):
            task_id = m.group(1)
            tasks[task_id] = {
                'id': task_id,
                'categoryId': m.group(2),
                'category': m.group(3),
                'title': m.group(4),
                'subtitle': m.group(5),
                'themeColor': m.group(6)
            }
        
        # hero.descriptionを別途抽出
        for task_id in tasks.keys():
            hero_pattern = rf'"{task_id}":\s*\{{[\s\S]*?hero:\s*\{{[^}}]*?description:\s*"([^"]+)"'
            hero_match = re.search(hero_pattern, task_text)
            if hero_match:
                tasks[task_id]['heroDescription'] = hero_match.group(1)
    
    return categories, tasks


# ==========================================
# Reactコンポーネント定義
# ==========================================
COMPONENTS_COMMON = r'''
    const { useState, useEffect, useMemo } = React;

    const Icon = ({ name, size = 24, className = "" }) => {
      if (typeof lucide !== 'undefined' && lucide.icons && lucide.icons[name]) {
        const iconData = lucide.icons[name];
        return React.createElement('svg', {
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
        }, iconData.map(([tag, attrs], index) => React.createElement(tag, { ...attrs, key: index })));
      }
      return <span className="inline-block w-4 h-4 bg-gray-300 rounded-full"></span>;
    };

    const Image = ({ src, alt, className, ...props }) => {
      const [error, setError] = useState(false);
      if (error) return <div className={`bg-slate-100 flex items-center justify-center text-slate-400 text-xs font-bold ${className}`}>{alt}</div>;
      return <img src={src} alt={alt} className={className} onError={() => setError(true)} loading="lazy" {...props} />;
    };
'''

COMPONENT_HEADER = r'''
    const Header = ({ scrolled, mobileMenuOpen, setMobileMenuOpen }) => {
      const textColor = scrolled ? 'text-slate-800' : 'text-white';
      const logoClass = scrolled ? '' : 'brightness-0 invert';
      const ctaClass = scrolled 
        ? 'bg-brand-blue text-white hover:bg-slate-800' 
        : 'bg-white text-brand-blue hover:bg-slate-100 ring-4 ring-white/30';

      return (
        <header className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ease-in-out ${scrolled ? 'bg-white/95 backdrop-blur-md shadow-sm py-3' : 'bg-transparent py-5'}`}>
          <div className="container mx-auto px-4 flex items-center justify-between max-w-7xl">
            <a href="__LINK_PREFIX__index.html" className="flex items-center gap-3 hover:opacity-80 transition-opacity">
              <Image src="__ASSET_PREFIX__assets/images/logo.svg" alt="RISEby" className={`h-8 md:h-9 transition-all duration-500 ${logoClass}`} />
            </a>
            
            <nav className="hidden md:flex items-center gap-8">
              <a href="__LINK_PREFIX__index.html#services" className={`font-bold tracking-wide transition-colors hover:opacity-70 ${textColor}`}>サービス</a>
              <a href="__LINK_PREFIX__blog/" className={`font-bold tracking-wide transition-colors hover:opacity-70 ${textColor}`}>ブログ</a>
              <a href="__LINK_PREFIX__about.html" className={`font-bold tracking-wide transition-colors hover:opacity-70 ${textColor}`}>会社概要</a>
              <a href="mailto:contact@riseby.net" className={`px-6 py-2.5 rounded-full font-bold transition-all duration-300 hover:scale-105 hover:shadow-lg ${ctaClass}`}>
                お問い合わせ
              </a>
            </nav>
            
            <button onClick={() => setMobileMenuOpen(!mobileMenuOpen)} className={`md:hidden p-2 ${textColor}`}>
              <Icon name={mobileMenuOpen ? "X" : "Menu"} size={24} />
            </button>
          </div>
          
          {mobileMenuOpen && (
            <div className="md:hidden absolute top-full left-0 right-0 bg-white border-t border-slate-100 shadow-xl p-4 flex flex-col gap-4 animate-fade-in-up">
              <a href="__LINK_PREFIX__index.html#services" className="text-slate-800 font-bold py-3 border-b border-slate-50">サービス</a>
              <a href="__LINK_PREFIX__blog/" className="text-slate-800 font-bold py-3 border-b border-slate-50">ブログ</a>
              <a href="__LINK_PREFIX__about.html" className="text-slate-800 font-bold py-3 border-b border-slate-50">会社概要</a>
              <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white text-center py-3.5 rounded-lg font-bold shadow-md mt-2">お問い合わせ</a>
            </div>
          )}
        </header>
      );
    };
'''

COMPONENT_FOOTER = r'''
    const Footer = () => {
      const currentYear = new Date().getFullYear();
      
      const footerLinks = useMemo(() => {
        if (!window.TASK_CATEGORIES || !window.TASK_DATABASE) return [];
        return Object.keys(window.TASK_CATEGORIES).map(catId => {
          const category = window.TASK_CATEGORIES[catId];
          const tasks = Object.entries(window.TASK_DATABASE)
            .filter(([id, task]) => task.categoryId === catId)
            .map(([id, task]) => ({ id, ...task })); 
          return {
            title: category.title,
            links: tasks.map(t => ({ label: t.title, url: `__SERVICE_LINK_PREFIX__${t.id}.html` }))
          };
        });
      }, []);

      return (
        <footer className="bg-[#0B0F19] text-white pt-24 pb-12 border-t border-slate-800 font-sans">
          <div className="container mx-auto px-4 max-w-7xl">
            <div className="flex flex-col lg:flex-row gap-16 mb-24">
              <div className="lg:w-1/3">
                <a href="__LINK_PREFIX__index.html" className="block mb-8">
                  <Image src="__ASSET_PREFIX__assets/images/logo.svg" alt="RISEby" className="h-9 brightness-0 invert opacity-90 hover:opacity-100 transition-opacity" />
                </a>
                <p className="text-slate-400 text-sm leading-relaxed mb-8">
                  ライズバイ株式会社 - 企業の複合的な経営課題を、AI・戦略・テクノロジー・人の観点から包括的に解決するコンサルティングファーム。
                </p>
                <div className="mb-10 text-sm text-slate-400 space-y-3">
                  <p>〒150-6115 東京都渋谷区渋谷2-24-12</p>
                  <p>渋谷スクランブルスクエア 15階</p>
                  <a href="mailto:contact@riseby.net" className="hover:text-white transition-colors flex items-center gap-2 mt-6 group">
                    <span className="bg-slate-800 p-2 rounded-full group-hover:bg-slate-700 transition-colors"><Icon name="Mail" size={16} /></span>
                    contact@riseby.net
                  </a>
                </div>
                <p className="text-slate-600 text-xs">
                  © {currentYear} RISEby inc. All rights reserved.
                </p>
              </div>
              <div className="lg:w-2/3 grid grid-cols-2 md:grid-cols-3 gap-8 gap-y-14">
                {footerLinks.map((group, idx) => (
                  <div key={idx}>
                    <h3 className="font-bold text-sm mb-5 text-white tracking-wider font-display">{group.title}</h3>
                    <ul className="space-y-3">
                      {group.links.map((link, lIdx) => (
                        <li key={lIdx}>
                          <a href={link.url} className="text-slate-400 hover:text-white text-xs transition-colors block py-0.5">
                            {link.label}
                          </a>
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            </div>
            {/* AIMOaaS Link */}
            <div className="border-t border-slate-800 pt-10 mb-8">
              <div className="flex flex-col md:flex-row items-center justify-center gap-6">
                <a href="https://aimoaas.com/" target="_blank" rel="noopener noreferrer" className="group flex items-center gap-3 bg-gradient-to-r from-violet-600 to-indigo-600 text-white px-6 py-3 rounded-full font-bold hover:shadow-xl hover:shadow-violet-500/20 transition-all hover:-translate-y-0.5">
                  <Icon name="Shield" size={18} />
                  <span>AIMOaaS™ - AIガバナンス運用代行</span>
                  <Icon name="ExternalLink" size={14} className="opacity-70 group-hover:opacity-100" />
                </a>
              </div>
            </div>
            <div className="flex flex-wrap gap-8 justify-center text-xs text-slate-500">
              <a href="__LINK_PREFIX__about.html" className="hover:text-white transition-colors">会社概要</a>
              <a href="__LINK_PREFIX__privacy.html" className="hover:text-white transition-colors">プライバシーポリシー</a>
              <a href="https://aimoaas.com/" target="_blank" rel="noopener noreferrer" className="hover:text-white transition-colors flex items-center gap-1">AIMOaaS <Icon name="ExternalLink" size={10} /></a>
            </div>
          </div>
        </footer>
      );
    };
'''

COMPONENT_HOME = r'''
    const LogoTicker = () => {
      const [logos, setLogos] = useState([]);
      useEffect(() => {
        const arr = Array.from({length: 40}, (_, i) => i + 1);
        for (let i = arr.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        setLogos(arr);
      }, []);
      
      const Row = ({ items, direction }) => (
        <div className="flex overflow-hidden relative w-full logo-ticker-mask my-6">
          <div className={`flex gap-10 whitespace-nowrap animate-${direction} w-max`}>
            {[...items, ...items, ...items].map((num, idx) => (
              <div key={idx} className="w-36 h-20 bg-white rounded-xl shadow-sm border border-slate-100 flex items-center justify-center p-4 no-context flex-shrink-0 group hover:shadow-md transition-all duration-300 hover:-translate-y-1">
                <img src={`__ASSET_PREFIX__assets/logos/${num}.png`} className="max-w-full max-h-full opacity-60 grayscale group-hover:grayscale-0 group-hover:opacity-100 transition-all duration-300" alt="Client Logo" draggable="false"/>
              </div>
            ))}
          </div>
        </div>
      );
      return (
        <div className="py-16 bg-slate-50 border-y border-slate-200 overflow-hidden">
          <div className="container mx-auto px-4 mb-10 text-center"><p className="text-sm font-bold text-slate-400 uppercase tracking-[0.2em] font-display">Trusted By Leading Companies</p></div>
          <Row items={logos.slice(0, 20)} direction="scroll-left" />
          <Row items={logos.slice(20, 40)} direction="scroll-right" />
        </div>
      );
    };

    const HomeContent = () => {
      const categorizedTasks = {};
      if (window.TASK_DATABASE) {
        Object.entries(window.TASK_DATABASE).forEach(([id, task]) => {
          const cat = task.category;
          if (!categorizedTasks[cat]) categorizedTasks[cat] = [];
          categorizedTasks[cat].push({ id, ...task });
        });
      }
      return (
        <div className="animate-fade-in-up">
          {/* Hero Section */}
          <section className="relative min-h-screen flex flex-col items-center justify-between hero-gradient bg-gradient-to-br from-slate-900 via-brand-blue to-slate-900 text-white overflow-hidden pt-32 pb-16">
            <div className="absolute inset-0 grid-pattern opacity-20"></div>
            <div className="container mx-auto px-4 text-center z-10 max-w-5xl flex-grow flex flex-col justify-center">
              <h1 className="mb-12 drop-shadow-2xl">
                <Image src="__ASSET_PREFIX__assets/images/logo.svg" alt="RISEby inc." className="h-28 md:h-40 mx-auto brightness-0 invert filter" />
              </h1>
              <p className="text-3xl md:text-6xl mb-10 font-light tracking-wide leading-tight">
                <span className="bg-gradient-to-r from-blue-100 to-white bg-clip-text text-transparent font-bold">戦略を描き、現場で動く。</span>
              </p>
              <div className="flex justify-center mb-10">
                  <div className="inline-block px-6 py-2 rounded-full glass-card text-blue-100 text-sm font-bold tracking-wider border-white/20 uppercase font-display">For Executives & Leaders</div>
              </div>
              <p className="text-lg md:text-xl text-indigo-100 mb-14 max-w-3xl mx-auto leading-loose">
                Accenture、Deloitte、EY、KPMG、PwC等大手ファーム出身者が、<br className="hidden md:block"/>戦略立案から実装・定着まで<span className="font-bold text-white border-b-2 border-blue-400 pb-1">一気通貫で支援</span>します。
              </p>
              <div className="flex flex-col sm:flex-row gap-6 justify-center mb-20">
                <a href="mailto:contact@riseby.net" className="group bg-white text-brand-blue px-10 py-5 rounded-full font-bold shadow-xl hover:shadow-2xl transition-all hover:-translate-y-1 inline-flex items-center justify-center gap-3 text-lg"><Icon name="MessageSquare" size={20} className="group-hover:scale-110 transition-transform"/> 無料相談する</a>
              </div>
            </div>
             <div className="animate-bounce opacity-50 pb-4 mt-8"><Icon name="ChevronDown" size={32} /></div>
          </section>

          <LogoTicker />

          {/* News Section */}
          <section className="py-16 bg-white border-b border-slate-200">
            <div className="container mx-auto px-4 max-w-5xl">
              <div className="flex items-center gap-4 mb-8">
                <span className="bg-brand-blue text-white text-xs font-bold px-4 py-1.5 rounded-full uppercase tracking-wider font-display">News</span>
                <h2 className="text-2xl font-bold text-slate-900">お知らせ</h2>
              </div>
              <div className="space-y-4">
                <a href="https://aimoaas.com/" target="_blank" rel="noopener noreferrer" className="group flex flex-col md:flex-row md:items-center gap-4 md:gap-8 p-6 bg-gradient-to-r from-violet-50 to-indigo-50 rounded-2xl border border-violet-100 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-300">
                  <div className="flex items-center gap-4">
                    <span className="text-sm font-bold text-slate-500 whitespace-nowrap">2026.02.01</span>
                    <span className="bg-violet-600 text-white text-xs font-bold px-3 py-1 rounded-full">NEW</span>
                  </div>
                  <div className="flex-grow">
                    <p className="text-slate-900 font-bold group-hover:text-violet-600 transition-colors">
                      AIガバナンス運用代行サービス「AIMOaaS™」の提供を開始しました
                    </p>
                    <p className="text-slate-500 text-sm mt-1">シャドーAIの可視化から24/365監視まで、AI管理の全てをアウトソーシング</p>
                  </div>
                  <div className="flex items-center gap-2 text-violet-600 font-bold text-sm group-hover:gap-3 transition-all">
                    <span>詳細を見る</span>
                    <Icon name="ExternalLink" size={16} />
                  </div>
                </a>
              </div>
            </div>
          </section>

          {/* Services Section */}
          <section id="services" className="py-28 bg-slate-50 border-t border-slate-200">
            <div className="container mx-auto px-4 max-w-7xl">
              <div className="text-center mb-24">
                <h2 className="text-4xl font-bold text-slate-900 mb-6">解決できる課題</h2>
                <p className="text-slate-600">最新のビジネストレンドを踏まえた、具体的な解決策を提供します。</p>
              </div>
              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                {Object.entries(categorizedTasks).map(([cat, tasks]) => {
                  const catId = tasks[0].categoryId;
                  const themeColor = tasks[0].themeColor; 
                  return (
                    <div key={cat} className="bg-white p-10 rounded-2xl shadow-sm border border-slate-100 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                      <a href={`__SERVICE_LINK_PREFIX__${catId}.html`} className="block">
                        <h3 className={`text-xl font-bold text-${themeColor}-900 mb-8 border-b border-${themeColor}-100 pb-4 flex justify-between items-center group-hover:text-${themeColor}-600 transition-colors`}>
                          {cat} <Icon name="ArrowRight" size={20} className="opacity-0 group-hover:opacity-100 transition-opacity -translate-x-2 group-hover:translate-x-0" />
                        </h3>
                      </a>
                      <ul className="space-y-5">
                        {tasks.map(t => (
                          <li key={t.id}>
                            <a href={`__SERVICE_LINK_PREFIX__${t.id}.html`} className={`flex items-center justify-between text-slate-600 hover:text-${t.themeColor}-600 transition-colors group/item p-3 -mx-3 hover:bg-${t.themeColor}-50 rounded-xl`}>
                              <span className="font-medium text-sm">{t.title}</span>
                              <Icon name="ChevronRight" size={16} className="text-slate-300 group-hover/item:text-${t.themeColor}-600 transition-colors" />
                            </a>
                          </li>
                        ))}
                      </ul>
                    </div>
                  );
                })}
              </div>
            </div>
          </section>

          {/* Contact Section */}
          <section className="py-24 bg-white border-t border-slate-200">
            <div className="container mx-auto px-4 max-w-4xl text-center">
              <div className="inline-block px-6 py-2 bg-slate-900 text-white rounded-full text-sm font-bold uppercase tracking-wider mb-8 shadow-lg">Contact Us</div>
              <h2 className="text-4xl font-bold mb-8 text-slate-900">まずは無料相談から</h2>
              <p className="text-xl text-slate-600 mb-16 max-w-2xl mx-auto">
                課題が明確でなくても構いません。<br/>経験豊富なコンサルタントが、貴社の状況を整理し、最適なアプローチを提案します。
              </p>
              <div className="flex flex-col sm:flex-row gap-6 justify-center">
                <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white px-12 py-5 rounded-full font-bold text-lg shadow-2xl hover:shadow-brand-blue/30 transition-all hover:-translate-y-1 inline-flex items-center gap-3">
                  <Icon name="Mail" size={24} /> お問い合わせ
                </a>
                <a href="mailto:contact@riseby.net?subject=資料請求" className="group border-2 border-brand-blue text-brand-blue px-12 py-5 rounded-full font-bold text-lg hover:bg-brand-blue hover:text-white transition-all inline-flex items-center gap-3">
                  <Icon name="FileText" size={24} className="group-hover:text-white"/> 資料請求
                </a>
              </div>
            </div>
          </section>
        </div>
      );
    };
'''

COMPONENT_PAGES = r'''
    const CategoryContent = ({ categoryId }) => {
      const category = window.TASK_CATEGORIES ? window.TASK_CATEGORIES[categoryId] : null;
      if (!category) return <div className="pt-32 text-center">Loading...</div>;
      const tasks = Object.entries(window.TASK_DATABASE || {}).filter(([_, t]) => t.categoryId === categoryId).map(([id, t]) => ({ id, ...t }));

      return (
        <div className="pt-24 pb-16 animate-fade-in-up">
          <div className={`bg-${category.themeColor}-50 py-20 border-b border-${category.themeColor}-100`}>
            <div className="container mx-auto px-4 text-center">
              <h1 className="text-4xl md:text-5xl font-bold text-slate-900 mb-6">{category.title}</h1>
              <p className="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">{category.description}</p>
            </div>
          </div>
          <div className="container mx-auto px-4 max-w-6xl -mt-10 mb-12">
             <div className="bg-white p-8 md:p-12 rounded-2xl shadow-xl border border-slate-100 mb-16 relative overflow-hidden">
                <div className="md:flex gap-10 items-start">
                    <div className="md:w-1/3 mb-8 md:mb-0">
                        <div className={`w-16 h-16 rounded-2xl bg-${category.themeColor}-100 flex items-center justify-center text-${category.themeColor}-600 mb-6`}><Icon name="TrendingUp" size={32} /></div>
                        <h3 className="text-xl font-bold text-slate-900 mb-2">Market Insight</h3>
                        <p className="text-slate-600 text-sm leading-relaxed">{category.insight?.trend?.text}</p>
                    </div>
                    <div className="md:w-2/3 grid sm:grid-cols-2 gap-6">
                        {category.insight?.approaches?.map((app, idx) => (
                            <div key={idx} className="bg-slate-50 p-5 rounded-xl border border-slate-100">
                                <h4 className={`font-bold text-${category.themeColor}-700 mb-2 text-sm flex items-center gap-2`}><Icon name="CheckCircle" size={16} /> {app.title}</h4>
                                <p className="text-slate-600 text-xs leading-relaxed">{app.desc}</p>
                            </div>
                        ))}
                    </div>
                </div>
             </div>
             <h2 className="text-2xl font-bold text-slate-900 mb-8 border-l-4 border-slate-900 pl-4">サービス一覧</h2>
             <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                {tasks.map(task => (
                    <a key={task.id} href={`__SERVICE_LINK_PREFIX__${task.id}.html`} className="group block bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                        <div className={`w-12 h-12 rounded-xl bg-${category.themeColor}-50 text-${category.themeColor}-600 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform`}><Icon name="ArrowRight" size={24} /></div>
                        <h3 className="text-lg font-bold text-slate-900 mb-3 group-hover:text-brand-blue transition-colors">{task.title}</h3>
                        <p className="text-slate-500 text-sm line-clamp-2 mb-4">{task.hero?.description}</p>
                        <span className={`text-xs font-bold text-${category.themeColor}-600 flex items-center gap-1`}>詳細を見る <Icon name="ChevronRight" size={12} /></span>
                    </a>
                ))}
             </div>
          </div>
        </div>
      );
    };

    const DetailContent = ({ taskId }) => {
      const task = window.TASK_DATABASE ? window.TASK_DATABASE[taskId] : null;
      if (!task) return <div className="pt-32 text-center">Service Not Found</div>;
      const category = window.TASK_CATEGORIES[task.categoryId];

      return (
        <div className="pt-24 pb-16 animate-fade-in-up">
           <div className="container mx-auto px-4 max-w-5xl mb-16">
              <div className="text-center mb-10">
                 <a href={`__SERVICE_LINK_PREFIX__${category.id}.html`} className={`inline-block mb-6 text-xs font-bold tracking-widest uppercase text-${task.themeColor}-600 bg-${task.themeColor}-50 px-3 py-1 rounded-full hover:bg-${task.themeColor}-100 transition-colors`}>{category.title}</a>
                 <h1 className="text-3xl md:text-5xl font-bold text-slate-900 mb-6 leading-tight">{task.title}</h1>
                 <p className="text-xl text-slate-500 font-medium mb-8">{task.subtitle}</p>
                 <p className="text-slate-600 max-w-3xl mx-auto leading-loose">{task.hero?.description}</p>
              </div>
              <div className="grid grid-cols-3 gap-4 md:gap-8 max-w-4xl mx-auto">
                 {task.hero?.stats?.map((stat, idx) => (
                    <div key={idx} className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 text-center">
                       <div className={`text-2xl md:text-3xl font-bold text-${task.themeColor}-600 mb-1 font-display`}>{stat.value}</div>
                       <div className="text-xs text-slate-400 font-bold uppercase">{stat.label}</div>
                    </div>
                 ))}
              </div>
           </div>
           
           <div className="bg-slate-50 py-20 border-y border-slate-200">
              <div className="container mx-auto px-4 max-w-5xl">
                 <h2 className="text-2xl font-bold text-center mb-12">このような課題はありませんか？</h2>
                 <div className="grid md:grid-cols-3 gap-8">
                    {task.painPoints?.map((pain, idx) => (
                       <div key={idx} className="bg-white p-8 rounded-2xl shadow-sm border border-slate-100">
                          <div className={`w-12 h-12 rounded-full bg-${task.themeColor}-100 text-${task.themeColor}-600 flex items-center justify-center mb-6`}>
                             <Icon name={pain.icon} size={24} />
                          </div>
                          <h3 className="font-bold text-slate-900 mb-3">{pain.title}</h3>
                          <p className="text-sm text-slate-600 leading-relaxed">{pain.desc}</p>
                       </div>
                    ))}
                 </div>
              </div>
           </div>
           
           <div className="py-20 container mx-auto px-4 max-w-5xl">
                <div className="flex flex-col md:flex-row gap-12 items-center">
                    <div className="md:w-1/2">
                        <h2 className="text-2xl font-bold mb-6">なぜ解決できないのか？<br/><span className={`text-${task.themeColor}-600`}>構造的な要因</span></h2>
                        <div className="space-y-6">
                            {task.structuralIssues?.map((issue, idx) => (
                                <div key={idx} className="flex gap-4">
                                    <div className={`flex-shrink-0 w-8 h-8 rounded-full bg-${task.themeColor}-50 text-${task.themeColor}-600 flex items-center justify-center font-bold`}>{idx + 1}</div>
                                    <div>
                                        <h4 className="font-bold text-slate-900 mb-1">{issue.title}</h4>
                                        <p className="text-sm text-slate-600 leading-relaxed">{issue.desc}</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                    <div className="md:w-1/2">
                        <div className={`bg-${task.themeColor}-900 text-white p-10 rounded-3xl shadow-2xl relative overflow-hidden`}>
                             <div className="absolute top-0 right-0 w-64 h-64 bg-white opacity-5 rounded-full -mr-20 -mt-20"></div>
                             <h3 className="text-xl font-bold mb-8 relative z-10">RISEbyのアプローチ</h3>
                             <div className="space-y-6 relative z-10">
                                {task.solutions?.map((sol, idx) => (
                                    <div key={idx} className="border-l-2 border-white/30 pl-6 relative">
                                        <div className="absolute -left-[5px] top-0 w-2 h-2 rounded-full bg-white"></div>
                                        <div className="text-xs font-bold text-white/60 mb-1">{sol.phase}</div>
                                        <div className="font-bold text-lg mb-1">{sol.title}</div>
                                        <div className="text-sm text-white/80">{sol.desc}</div>
                                    </div>
                                ))}
                             </div>
                        </div>
                    </div>
                </div>
           </div>

           <div className="bg-slate-900 text-white py-20 text-center">
                <div className="container mx-auto px-4 max-w-3xl">
                    <h2 className="text-3xl font-bold mb-6">この課題を解決しませんか？</h2>
                    <p className="text-slate-400 mb-10">
                        {task.title}に関するご相談は、<br/>
                        実績豊富な専門チームが承ります。
                    </p>
                    <a href="mailto:contact@riseby.net" className={`inline-flex items-center gap-2 bg-${task.themeColor}-500 text-white px-10 py-4 rounded-full font-bold hover:bg-white hover:text-${task.themeColor}-600 transition-all duration-300 shadow-lg`}><Icon name="Mail" size={20} /> 無料相談を申し込む</a>
                </div>
           </div>
        </div>
      );
    };
'''

COMPONENT_APP = r'''
    const App = () => {
      const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
      const [scrolled, setScrolled] = useState(false);
      useEffect(() => {
        const handleScroll = () => setScrolled(window.scrollY > 20);
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
      }, []);

      const ctx = window.PAGE_CONTEXT || { type: 'home' };
      let content;
      if (ctx.type === 'category') content = <CategoryContent categoryId={ctx.id} />;
      else if (ctx.type === 'detail') content = <DetailContent taskId={ctx.id} />;
      else content = <HomeContent />;

      return (
        <div className="min-h-screen font-sans text-slate-800 antialiased selection:bg-brand-blue selection:text-white">
          <Header scrolled={scrolled} mobileMenuOpen={mobileMenuOpen} setMobileMenuOpen={setMobileMenuOpen} />
          {content}
          <Footer />
        </div>
      );
    };

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<App />);
'''


# ==========================================
# HTML生成関数
# ==========================================
def generate_meta_tags(canonical_url, title, description, og_image=None):
    """SEO用のメタタグを生成"""
    og_image = og_image or f"{BASE_URL}/assets/og-image.jpg"
    return f'''
  <title>{title} | RISEby</title>
  <meta name="description" content="{description}">
  
  <!-- OGP -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="RISEby inc.">
  <meta property="og:locale" content="ja_JP">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title} | RISEby">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  
  <!-- Canonical -->
  <link rel="canonical" href="{canonical_url}">
'''


def generate_structured_data(page_type, data=None):
    """構造化データ（JSON-LD）を生成"""
    base_org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "RISEby inc.",
        "url": BASE_URL,
        "logo": f"{BASE_URL}/assets/images/logo.png",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "渋谷2-24-12 渋谷スクランブルスクエア 15階",
            "addressLocality": "渋谷区",
            "addressRegion": "東京都",
            "postalCode": "150-6115",
            "addressCountry": "JP"
        }
    }
    
    if page_type == 'home':
        schema = {
            "@context": "https://schema.org",
            "@type": "ConsultingService",
            "name": "RISEby inc.",
            "url": BASE_URL,
            "logo": f"{BASE_URL}/assets/images/logo.png",
            "description": "Accenture、Deloitte、EY、KPMG、PwC等大手ファーム出身者による実行特化型コンサルティング。",
            "address": base_org["address"],
            "priceRange": "$$$"
        }
    elif page_type == 'service' and data:
        schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": data.get('title', ''),
            "description": data.get('description', ''),
            "provider": {
                "@type": "Organization",
                "name": "RISEby inc.",
                "url": BASE_URL
            },
            "serviceType": "Business Consulting",
            "areaServed": {
                "@type": "Country",
                "name": "Japan"
            }
        }
    else:
        schema = base_org
    
    return f'''
  <script type="application/ld+json">
  {json.dumps(schema, ensure_ascii=False, indent=2)}
  </script>
'''


def write_html_file(filepath, page_type, page_id, title, description, depth, template, structured_data_type='default', service_data=None):
    """HTMLファイルを生成"""
    asset_prefix = "../" if depth == 1 else "./"
    link_prefix = "../" if depth == 1 else "./"
    service_link_prefix = "./" if depth == 1 else "./services/"
    
    # URL計算
    if depth == 0:
        relative_path = ""
    else:
        relative_path = filepath.replace('\\', '/')
    canonical_url = f"{BASE_URL}/{relative_path}"
    
    # Reactコンポーネントを組み立て
    full_script = (
        COMPONENTS_COMMON + 
        COMPONENT_HEADER + 
        COMPONENT_FOOTER + 
        COMPONENT_HOME + 
        COMPONENT_PAGES + 
        COMPONENT_APP
    )
    full_script = full_script.replace("__ASSET_PREFIX__", asset_prefix)
    full_script = full_script.replace("__LINK_PREFIX__", link_prefix)
    full_script = full_script.replace("__SERVICE_LINK_PREFIX__", service_link_prefix)

    # テンプレートを書き換え
    new_html = template
    
    # スクリプト置換
    new_html = re.sub(
        r'<script type="text/babel">[\s\S]*?</script>', 
        f'<script type="text/babel">\n{full_script}\n</script>', 
        new_html
    )
    
    # tasks.jsパス更新
    js_path = asset_prefix + TASKS_JS_PATH.replace(os.sep, '/')
    new_html = re.sub(
        r'<script\s+src="[^"]*tasks\.js"\s*></script>', 
        f'<script src="{js_path}"></script>', 
        new_html
    )
    
    # メタタグ置換（SEO修正の核心部分）
    meta_tags = generate_meta_tags(canonical_url, title, description)
    
    # 既存のtitle, description, OGP, canonicalを削除して新規挿入
    new_html = re.sub(r'<title>.*?</title>\s*', '', new_html)
    new_html = re.sub(r'<meta name="description"[^>]*>\s*', '', new_html)
    new_html = re.sub(r'<!-- OGP -->[\s\S]*?<meta name="twitter:card"[^>]*>\s*', '', new_html)
    new_html = re.sub(r'<!-- Canonical -->\s*<link rel="canonical"[^>]*>\s*', '', new_html)
    
    # 構造化データ置換
    structured_data = generate_structured_data(structured_data_type, service_data)
    new_html = re.sub(
        r'<!-- Structured Data \(JSON-LD\) -->[\s\S]*?</script>\s*',
        '',
        new_html
    )
    
    # <meta charset="UTF-8">の後にメタタグと構造化データを挿入
    new_html = new_html.replace(
        '<meta charset="UTF-8">',
        f'<meta charset="UTF-8">\n{meta_tags}\n  <!-- Structured Data (JSON-LD) -->{structured_data}'
    )
    
    # PAGE_CONTEXT設定
    context = f'<script>window.PAGE_CONTEXT = {{ type: "{page_type}", id: "{page_id}" }};</script>'
    new_html = re.sub(r'<script>window\.PAGE_CONTEXT = .*?;</script>\s*', '', new_html)
    new_html = new_html.replace('<div id="root"></div>', f'{context}\n<div id="root"></div>')

    # サブディレクトリ用のパス修正
    if depth == 1:
        new_html = new_html.replace('href="./assets', 'href="../assets')
        new_html = new_html.replace('src="./assets', 'src="../assets')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    return canonical_url


def generate_sitemap(urls):
    """sitemap.xmlを生成"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url_info in urls:
        url = url_info['url']
        priority = url_info.get('priority', '0.5')
        changefreq = url_info.get('changefreq', 'monthly')
        
        sitemap += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>
'''
    
    sitemap += '</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    
    print("Generated: sitemap.xml")


def generate_robots_txt():
    """robots.txtを生成"""
    robots = f'''User-agent: *
Allow: /

# Sitemap
Sitemap: {BASE_URL}/sitemap.xml

# 不要なディレクトリへのクロールを制限
Disallow: /assets/js/
Disallow: /assets/logos/
'''
    
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write(robots)
    
    print("Generated: robots.txt")


# ==========================================
# メイン処理
# ==========================================
def generate_html_files():
    if not TASKS_JS_PATH:
        print("Error: tasks.js not found.")
        return

    with open(TASKS_JS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    categories, tasks = parse_tasks_js(content)
    
    print(f"Found {len(categories)} categories and {len(tasks)} tasks")

    with open(INDEX_HTML_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    # servicesディレクトリを再作成
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    all_urls = []
    
    print("\n=== Generating SEO-Optimized Site ===\n")

    # トップページ
    url = write_html_file(
        INDEX_HTML_PATH, 
        'home', 
        'home', 
        'RISEby inc. | 実行特化型コンサルティング',
        'Accenture、Deloitte、EY、KPMG、PwC等大手ファーム出身者による実行特化型コンサルティング。戦略立案から実装・定着まで一気通貫で支援します。',
        0, 
        template,
        'home'
    )
    all_urls.append({'url': url, 'priority': '1.0', 'changefreq': 'weekly'})
    print(f"Generated: index.html")
    print(f"  -> Canonical: {url}")
    
    # カテゴリページ
    for cid, data in categories.items():
        filepath = os.path.join(OUTPUT_DIR, f"{cid}.html")
        url = write_html_file(
            filepath, 
            'category', 
            cid, 
            data['title'],
            data['description'],
            1, 
            template,
            'service',
            {'title': data['title'], 'description': data['description']}
        )
        all_urls.append({'url': url, 'priority': '0.8', 'changefreq': 'weekly'})
        print(f"Generated: {filepath}")
        print(f"  -> Canonical: {url}")
    
    # 個別サービスページ
    for tid, tdata in tasks.items():
        filepath = os.path.join(OUTPUT_DIR, f"{tid}.html")
        title = tdata.get('title', 'Service')
        desc = tdata.get('heroDescription', tdata.get('subtitle', ''))
        
        url = write_html_file(
            filepath, 
            'detail', 
            tid, 
            title,
            desc[:150] if len(desc) > 150 else desc,
            1, 
            template,
            'service',
            {'title': title, 'description': desc}
        )
        all_urls.append({'url': url, 'priority': '0.7', 'changefreq': 'monthly'})
        print(f"Generated: {filepath}")
        print(f"  -> Canonical: {url}")
    
    # ブログページのURLを収集（修正はしない、sitemapに追加のみ）
    if os.path.exists(BLOG_DIR):
        for root, dirs, files in os.walk(BLOG_DIR):
            for file in files:
                if file.endswith('.html'):
                    relative_path = os.path.join(root, file).replace('\\', '/')
                    url = f"{BASE_URL}/{relative_path}"
                    all_urls.append({'url': url, 'priority': '0.6', 'changefreq': 'monthly'})
    
    # sitemap.xml生成
    print("\n")
    generate_sitemap(all_urls)
    
    # robots.txt生成
    generate_robots_txt()
    
    print(f"\n=== Complete! ===")
    print(f"Total pages in sitemap: {len(all_urls)}")


if __name__ == "__main__":
    generate_html_files()

import os
import re

# ---------------------------------------------------------
# 設定: 対象ディレクトリ
# ---------------------------------------------------------
TARGET_DIR = os.path.join("blog", "ai")

# ---------------------------------------------------------
# 新しいHeaderコンポーネント (修正版)
# ・ロゴをテキスト(span)から画像(img)に変更しました。
# ・パスを ../../assets/images/logo.svg に設定しています。
# ・ブログは背景が白いため、常に「色付きロゴ(標準)」を表示します。
# ---------------------------------------------------------
NEW_HEADER = r"""
        const Header = () => {
            const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
            const [scrolled, setScrolled] = useState(false);

            useEffect(() => {
                const handleScroll = () => setScrolled(window.scrollY > 20);
                window.addEventListener('scroll', handleScroll);
                return () => window.removeEventListener('scroll', handleScroll);
            }, []);

            return (
                <header className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ease-in-out ${scrolled ? 'bg-white/95 backdrop-blur-md shadow-sm py-3' : 'bg-white/80 backdrop-blur-sm py-4 shadow-sm'}`}>
                    <div className="container mx-auto px-4 flex items-center justify-between max-w-7xl">
                        <a href="../../index.html" className="flex items-center gap-3 hover:opacity-80 transition-opacity">
                            <img src="../../assets/images/logo.svg" alt="RISEby" className="h-8 md:h-9" />
                        </a>
                        <nav className="hidden md:flex items-center gap-8">
                            <a href="../../index.html#services" className="font-bold tracking-wide transition-colors hover:opacity-70 text-slate-800">サービス</a>
                            <a href="../../blog/" className="font-bold tracking-wide transition-colors text-brand-blue">ブログ</a>
                            <a href="../../about.html" className="font-bold tracking-wide transition-colors hover:opacity-70 text-slate-800">会社概要</a>
                            <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white hover:bg-slate-800 px-6 py-2.5 rounded-full font-bold transition-all duration-300 hover:scale-105 hover:shadow-lg">
                                お問い合わせ
                            </a>
                        </nav>
                        <button onClick={() => setMobileMenuOpen(!mobileMenuOpen)} className="md:hidden p-2 text-slate-800">
                            <Icon name={mobileMenuOpen ? "X" : "Menu"} size={24} />
                        </button>
                    </div>
                    
                    {mobileMenuOpen && (
                        <div className="md:hidden absolute top-full left-0 right-0 bg-white border-t border-slate-100 shadow-xl p-4 flex flex-col gap-4 animate-fade-in-up">
                            <a href="../../index.html#services" className="text-slate-800 font-bold py-3 border-b border-slate-50">サービス</a>
                            <a href="../../blog/" className="text-brand-blue font-bold py-3 border-b border-slate-50">ブログ</a>
                            <a href="../../about.html" className="text-slate-800 font-bold py-3 border-b border-slate-50">会社概要</a>
                            <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white text-center py-3.5 rounded-lg font-bold shadow-md mt-2">お問い合わせ</a>
                        </div>
                    )}
                </header>
            );
        };
"""

# ---------------------------------------------------------
# 新しいFooterコンポーネント (修正版)
# ・フッターのロゴも画像(img)に変更しました。
# ・フッターは背景が黒なので、brightness-0 invert クラスで白く反転させています。
# ---------------------------------------------------------
NEW_FOOTER = r"""
        const Footer = () => (
            <footer className="bg-[#0B0F19] text-white pt-24 pb-12 border-t border-slate-800 font-sans">
                <div className="container mx-auto px-4 max-w-7xl">
                    <div className="flex flex-col lg:flex-row justify-between gap-16 mb-24">
                        <div className="lg:w-1/3">
                            <a href="../../index.html" className="block mb-8">
                                <img src="../../assets/images/logo.svg" alt="RISEby" className="h-9 brightness-0 invert opacity-90 hover:opacity-100 transition-opacity" />
                            </a>
                            <p className="text-slate-400 text-sm leading-relaxed mb-8">
                                企業の複合的な経営課題を、AI・戦略・テクノロジー・人の観点から包括的に解決するコンサルティングファーム。
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
                                &copy; {new Date().getFullYear()} RISEby Inc. All rights reserved.
                            </p>
                        </div>
                        <div className="lg:w-2/3 grid grid-cols-2 md:grid-cols-3 gap-8 gap-y-14">
                             <div>
                                <h3 className="font-bold text-sm mb-5 text-white tracking-wider font-display">Services</h3>
                                <ul className="space-y-3">
                                    <li><a href="../../index.html#services" className="text-slate-400 hover:text-white text-xs transition-colors">サービス一覧</a></li>
                                    <li><a href="../../index.html" className="text-slate-400 hover:text-white text-xs transition-colors">新規事業開発</a></li>
                                    <li><a href="../../index.html" className="text-slate-400 hover:text-white text-xs transition-colors">DXコンサルティング</a></li>
                                </ul>
                            </div>
                            <div>
                                <h3 className="font-bold text-sm mb-5 text-white tracking-wider font-display">Company</h3>
                                <ul className="space-y-3">
                                    <li><a href="../../about.html" className="text-slate-400 hover:text-white text-xs transition-colors">会社概要</a></li>
                                    <li><a href="../../blog/" className="text-slate-400 hover:text-white text-xs transition-colors">ブログ</a></li>
                                    <li><a href="mailto:contact@riseby.net" className="text-slate-400 hover:text-white text-xs transition-colors">お問い合わせ</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div className="border-t border-slate-800 pt-10 flex flex-wrap gap-8 justify-center text-xs text-slate-500">
                        <a href="../../about.html" className="hover:text-white transition-colors">会社概要</a>
                        <a href="../../privacy.html" className="hover:text-white transition-colors">プライバシーポリシー</a>
                    </div>
                </div>
            </footer>
        );
"""

def update_files():
    if not os.path.exists(TARGET_DIR):
        print(f"エラー: ディレクトリ '{TARGET_DIR}' が見つかりません。")
        return

    print(f"対象ディレクトリ: {TARGET_DIR}")
    count = 0
    
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Headerの置換
                    header_pattern = re.compile(r'const\s+Header\s*=\s*\(\)\s*=>\s*\{[\s\S]*?\};', re.MULTILINE)
                    # 前回の置換で { ... return ... } 形式になっているため、そのパターンを優先
                    if not header_pattern.search(content):
                         header_pattern = re.compile(r'const\s+Header\s*=\s*\(\)\s*=>\s*\([\s\S]*?\);', re.MULTILINE)

                    if header_pattern.search(content):
                        new_content = header_pattern.sub(NEW_HEADER.strip(), content)
                    else:
                        new_content = content

                    # Footerの置換
                    footer_pattern = re.compile(r'const\s+Footer\s*=\s*\(\)\s*=>\s*\([\s\S]*?\);', re.MULTILINE)
                    if not footer_pattern.search(new_content):
                        footer_pattern = re.compile(r'const\s+Footer\s*=\s*\(\)\s*=>\s*\{[\s\S]*?\};', re.MULTILINE)

                    if footer_pattern.search(new_content):
                        new_content = footer_pattern.sub(NEW_FOOTER.strip(), new_content)

                    # 書き込み
                    if content != new_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated: {file}")
                        count += 1
                    else:
                        print(f"No changes: {file}")

                except Exception as e:
                    print(f"Error processing {file}: {e}")

    print(f"\n完了: {count} ファイルのロゴを画像パス(../../assets/images/logo.svg)に更新しました。")

if __name__ == "__main__":
    update_files()
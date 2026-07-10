%global tl_name autotype
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	A LuaLaTeX package for automatic language-specific typography
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/autotype
License:	lppl1.3 mit other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autotype.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autotype.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
autotype is a LuaLaTeX package for automatic language-specific
typography. Currently, only the German language is supported (old and
new orthography). The package makes it possible to suppress ligatures at
word boundaries, to activate a hyphenation algorithm that prefers
hyphenation points at word boundaries (weighted hyphenation), to enable
irregular hyphenations like backen - bak-ken, Schiffahrt - Schiff-fahrt
of traditional German orthography, and to insert long s for blackletter
typesetting.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/lualatex
%dir %{_datadir}/texmf-dist/tex/lualatex
%dir %{_datadir}/texmf-dist/doc/lualatex/autotype
%dir %{_datadir}/texmf-dist/tex/lualatex/autotype
%doc %{_datadir}/texmf-dist/doc/lualatex/autotype/README
%doc %{_datadir}/texmf-dist/doc/lualatex/autotype/autotype-de.pdf
%doc %{_datadir}/texmf-dist/doc/lualatex/autotype/autotype-de.tex
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-cls_pdnm_oop.lua
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-cls_pdnm_pattern.lua
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-cls_pdnm_spot.lua
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-cls_pdnm_trie_simple.lua
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1901-primary.lic.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1901-primary.pat.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1901-secondary.lic.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1901-secondary.pat.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1901-special.lic.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1901-special.pat.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1996-primary.lic.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1996-primary.pat.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1996-secondary.lic.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-1996-secondary.pat.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-CH-1901-primary.lic.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-CH-1901-primary.pat.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-CH-1901-secondary.lic.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-hyph-de-CH-1901-secondary.pat.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-liga-de.lic.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-liga-de.pat.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-pdnm_nl_manipulation.lua
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-round-s-de.lic.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype-round-s-de.pat.txt
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype.lua
%{_datadir}/texmf-dist/tex/lualatex/autotype/autotype.sty

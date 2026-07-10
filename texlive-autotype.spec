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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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


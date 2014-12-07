# revision 15878
# category Package
# catalog-ctan /fonts/rsfs
# catalog-date 2008-12-14 19:11:27 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-rsfs
Version:	20081214
Release:	9
Summary:	Ralph Smith's Formal Script font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/rsfs
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts provide uppercase 'formal' script letters for use as
symbols in scientific and mathematical typesetting (in contrast
to the informal script fonts such as that used for the
'calligraphic' symbols in the TeX maths symbol font). The fonts
are provided as MetaFont source, and as derived Adobe Type 1
format. LaTeX support, for using these fonts in mathematics, is
available via one of the packages calrsfs and mathrsfs.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/rsfs/rsfs10.afm
%{_texmfdistdir}/fonts/afm/public/rsfs/rsfs5.afm
%{_texmfdistdir}/fonts/afm/public/rsfs/rsfs7.afm
%{_texmfdistdir}/fonts/map/dvips/rsfs/rsfs.map
%{_texmfdistdir}/fonts/source/public/rsfs/rsfs10.mf
%{_texmfdistdir}/fonts/source/public/rsfs/rsfs5.mf
%{_texmfdistdir}/fonts/source/public/rsfs/rsfs7.mf
%{_texmfdistdir}/fonts/source/public/rsfs/script.mf
%{_texmfdistdir}/fonts/source/public/rsfs/scriptu.mf
%{_texmfdistdir}/fonts/tfm/public/rsfs/rsfs10.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfs/rsfs5.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfs/rsfs7.tfm
%{_texmfdistdir}/fonts/type1/public/rsfs/rsfs10.pfb
%{_texmfdistdir}/fonts/type1/public/rsfs/rsfs10.pfm
%{_texmfdistdir}/fonts/type1/public/rsfs/rsfs5.pfb
%{_texmfdistdir}/fonts/type1/public/rsfs/rsfs5.pfm
%{_texmfdistdir}/fonts/type1/public/rsfs/rsfs7.pfb
%{_texmfdistdir}/fonts/type1/public/rsfs/rsfs7.pfm
%{_texmfdistdir}/tex/plain/rsfs/scrload.tex
%doc %{_texmfdistdir}/doc/fonts/rsfs/README
%doc %{_texmfdistdir}/doc/fonts/rsfs/README.type1

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081214-2
+ Revision: 755729
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081214-1
+ Revision: 719467
- texlive-rsfs
- texlive-rsfs
- texlive-rsfs
- texlive-rsfs


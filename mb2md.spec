%include        /usr/lib/rpm/macros.perl
Summary:	Converting Mbox mailboxes to Maildir format
Summary(pl):	Konwerter skrzynek Mbox do formatu Maildir
Name:		mb2md
Version:	3.10
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://batleth.sapienti-sat.org/projects/mb2md/%{name}-%{version}.pl
# Source0-md5:	14714b1927e4aeff2807a5dde45aebe7
URL:		http://batleth.sapienti-sat.org/projects/mb2md/
BuildRequires:	perl >= 5.6.0
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Perl script that takes one or more Mbox format mailbox files in a
directory and convert them to Maildir format mailboxes. As the Mbox
format has some drawbacks, D. J. Bernstein created the Maildir format
when he wrote Qmail. With the Mbox format all mail of a specific
folder is stored as one large text file. The Maildir format stores
each mail as a seperate file. It is a faster and more efficient way to
store mail. It works particularly well over NFS, which has a long
history of locking-related woes. The Mbox format is used by some of
the POP3/IMAP servers, most mail servers (MTAs) and mail readers
(MUAs). The Maildir format is used by Qmail, Courier-MTA and can be
also used as a alternative mail storage format by Postfix and Exim. A
good POP3/IMAP server for Maildirs is Courier IMAP.

%description -l pl
mb2md to skrypt Perla, który bierze jeden lub wiêcej plików skrzynek w
formacie Mbox z katalogu i konwertuje je do formatu Maildir. Poniewa¿
format Mbox ma pewne wady, D. J. Bernstein przy pisaniu Qmaila
stworzy³ format Maildir. W formacie Mbox wszystkie wiadomo¶ci w danym
folderze s± zapisywane w jednym du¿ym pliku tekstowym. W formacie
Maildir ka¿da wiadomo¶æ jest zapisywana jako oddzielny plik. Maildir
jest szybszym i bardziej wydajnym sposobem zapisywania poczty. Dzia³a
szczególnie dobrze po NFS, maj±cym d³ug± historiê problemów zwi±zanych
z blokowaniem plików. Format Mbox jest u¿ywany przez czê¶æ serwerów
POP3/IMAP, wiêkszo¶æ serwerów pocztowych (MTA) oraz czytników poczty
(MUA). Format Maildir jest u¿ywany przez Qmaila, Courier-MTA i mo¿e
byæ u¿ywany jako alternatywny format tak¿e przez Postfiksa i Exima.
Dobrym serwerem POP3/IMAP dla skrzynek Maildir jest Courier IMAP.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/mb2md.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mb2md.pl

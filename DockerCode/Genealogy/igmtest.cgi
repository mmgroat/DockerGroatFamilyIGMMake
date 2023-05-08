#!/usr/bin/perl -w
print "Content-type: text/html; charset=utf-8\n\n";
print "Hello World!";
print "<HTML>\n<HEAD>\n<TITLE>Michael M. Groat's Genealogical Database $Title</TITLE>\n";
#  print "<meta charset=\"utf-8\">\n"
print "</HEAD>\n<BODY ";
print "<CENTER><H2>Michael M. Groat's Genealogical Database</H2></CENTER>\n";
print "<CENTER><B>Entries:</B> 13347 &nbsp;&nbsp;<B>Updated:</B> November 26, 2007</CENTER>";
print "<CENTER><B>Contact:</B> <A href=\"mailto:mgroat\@cs.unm.edu\">Michael M. Groat</A> &nbsp;&nbsp <B>Home Page:</B> <A href=\"http://www.cs.unm.edu/~mgroat\">Michael M. Groat's CS Homepage</A></CENTER>";
print "<CENTER><H3>$Title</H3></CENTER><HR>\n";
#use Cwd qw( abs_path );
#use File::Basename qw( dirname );
#use lib dirname(abs_path($0));
#sub trim($);
#$starttime=(times)[0];
#$Program='IGMGet (modified by Randy Winch)';
#$Version='2.7';
#require 'igmini';
#require 'igmlib';
#$tmp=$ENV{'PATH_INFO'};
#(($DB)=($tmp=~m#^/n=(.*)#)) || &IGMDie("PATH_INFO \"$tmp\" not in correct format.");
#$DB='GroatFamily';
#$tmp=$ENV{'QUERY_STRING'};
#$tmp='986563';
#(($key)=($tmp=~/(\w+)/)) || &IGMDie("QUERY_STRING \"$tmp\" not in correct format.");
#
#$focus=$key;





#if ($UseDBM) {
#  dbmopen(%idx,"/nfs/notrust/cgi-bin/mgroat/GroatFamily",undef);
#} else {
#  open(INDEX,$LocINDEX) || print "Can't open index $LocGEDInd";
#  while (<INDEX>) {
#    /^(\S+) (.*)/;
#    $idx{$1}=$2;
#  }
#  close(INDEX);
#}
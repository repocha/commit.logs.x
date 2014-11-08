2.4.10
2.4.9
2.4.8
2.4.7
2.4.6
2.4.5
2.4.4
2.4.3
2.4.2
2.4.1
2.4.0
2.3.16
2.3.15
2.3.14
2.3.13
2.3.12
2.3.11
2.3.10
2.3.9
2.3.8
2.3.7
2.3.6
2.3.5
2.3.4
2.3.3
2.3.2
2.3.1
2.3.0
2.2.x and later:
2.0.x and later:
2.2.29
2.2.28
2.2.27
2.2.26
2.2.25
2.2.24
2.2.23
2.2.22
2.2.21
2.2.20
2.2.19
2.2.18
2.2.17
2.2.16
2.2.15
2.2.14
2.2.13
2.2.12
2.2.11
2.2.10
2.2.9
2.2.8
2.2.7 (not released)
2.2.6
2.2.4
2.2.3
2.2.2
2.2.1
2.2.0
2.1.9
2.1.8
2.1.7
2.1.6
2.1.5
2.1.4
2.1.3
2.1.2
2.1.1
2.0.x and later:
2.1.9
2.1.8
2.1.7
2.1.6
2.1.5
2.1.4
2.1.3
2.1.2
2.1.1
2.0.56
2.0.55
2.0.54
2.0.53
2.0.52
2.0.51
2.0.50
2.0.49
2.0.48
2.0.47
2.0.46
2.0.45
2.0.44
2.0.43
2.0.42
2.0.41
2.0.40
2.0.39
2.0.38
2.0.37
2.0.36
2.0.35
2.0.34
2.0.33
2.0.32
2.0.31
2.0.30
2.0.29
2.0.28
2.0.27
2.0.26
2.0.25
2.0.24
2.0.23
2.0.22
2.0.21
2.0.20
2.0.19
2.0.18
2.0.17
2.0.16
2.0.15
2.0.14
2.0.13
2.0.12
2.0.11
2.0a9
2.0a8
2.0a7
2.0a6
2.0a5
2.0a4
2.0a3
2.0a2
2.0a1
mpm
pthreads
1.3.9
1.3.8 [not released]
1.3.7 [not released]
1.3.6
1.3.5 [not released]
1.3.4
1.3.3
1.3.2
1.3.1
1.3.0
1.3b7
1.3b6
1.3b5
1.3b4
1.3b3
1.3b2 (there is no 1.3b1)
1.3a1
1.2.6
1.2.5
1.2.4
1.2.3
1.2.2 [not released]
1.2.1
1.2
1.2b11
1.2b10
1.2b9  [never announced]
1.2b8
1.2b7
1.2b6
1.2b5
1.2b4
1.2b3:
1.2b2:
1.2b1
1.1.1
1.1.0
1.1b4
1.1b3
1.1b2
1.1b1
1.0.3
1.0.2
1.0.1
1.0.0                                        23 nov 1995
0.8.16                                       05 nov 1995
0.8.15                                       14 oct 1995
0.8.14                                       19 sep 1995
0.8.13                                       07 sep 1995
0.8.12                                       31 aug 1995
0.8.11                                       24 aug 1995
0.8.10                                       18 aug 1995
0.8.9                                        12 aug 1995
0.8.8                                        08 aug 1995
0.8.7                                        03 aug 1995
0.8.6                                        02 aug 1995
0.8.5                                        01 aug 1995
0.8.4
0.8.3
0.8.2                                        19 jul 1995
0.8.1
0.8.0 (nee shambhala 0.6.2)                  16 jul 1995
0.7.3                                        20 jun 1995
0.6.4                                        13 may 1995
0.5.1                                        10 apr 1995
0.4                                          02 apr 1995
0.3                                          24 mar 1995
0.2                                          18 mar 1995
5447
203
5446
#parameters: 14
*) security: cve-2014-3523 (cve.mitre.org) fix a memory consumption denial of service in the winnt mpm (used in all windows installations). workaround: *acceptfilter* <*protocol*> {none|connect} [jeff trawick] 2.4.10 

*) security: cve-2014-0118 (cve.mitre.org) mod_deflate: the deflate input filter (inflates request bodies) now limits the length and compression ratio of inflated request bodies to avoid denial of sevice via highly compressed bodies.  see directives deflateinflate*limitrequestbody*, deflateinflateratiolimit, and deflateinflateratioburst. [yann ylavic, eric covener] 2.4.10 

*) security: cve-2014-0231 (cve.mitre.org) mod_cgid: fix a denial of service against cgi *script*s that do not consume stdin that could lead to lingering httpd child processes filling up the scoreboard and eventually hanging the server.  by default, the client i/o *timeout* (*timeout* directive) now applies to communication with *script*s.  the cgid*script**timeout* directive can be used to set a different *timeout* for communication with *script*s. [rainer jung, eric covener, yann ylavic] 2.4.10 

*) mod_ssl: extend the scope of ssl*session*cache*timeout* to *session*s resumed by tls *session* resumption (rfc 5077). [rainer jung] 2.4.10 

*) mod_ssl: set an error note for requests rejected due to *sslstrictsnivhostcheck*.  [jeff trawick] 2.4.10 

*) mod_ssl: fix issue with *redirect*s to error documents when handling sni errors.  [jeff trawick] 2.4.10 

*) mod_proxy: when ping/pong is *config*ured for a worker, don't send or forward "100 continue" (interim) response to the client if it does not expect one. [yann ylavic] 2.4.10 

*) mod_ldap: be more conservative with the last-used time for *ldapconnectionpoolttl*. pr54587 [eric covener] 2.4.10 

*) mod_ldap: ldap connections used for authn were not respecting *ldapconnectionpoolttl*. pr54587 [eric covener] 2.4.10 

*) mod_authnz_ldap: support primitive ldap servers do not accept filters, such as "sdbm-backed ldap" on z/os, by allowing a special filter "none" to be specified in *authldapurl*. [eric covener] 2.4.10 

*) mod_proxy_fcgi: support io*buffersize* parameter.  [jeff trawick] 2.4.10 

*) mod_*alias*: stop setting context_prefix and context_document environment variables as a result of *alias*match. [eric covener] 2.4.10 

*) mod_cache: fix ah00784 errors on windows when the the *cachelock* directive is enabled.  [eric covener] 2.4.10 

*) mod_authn_socache: fix crash at startup in certain *config*urations. pr 56371. (regression in 2.4.7) [jan kaluza] 2.4.10 

*) mod_ssl: restore argument structure for "exec"-type *sslpassphrasedialog* programs to the form used in releases up to 2.4.7, and emulate a backwards-compatible behavior for existing setups. [kaspar brand] 2.4.10 

*) mod_ssl: "*sslengine* off" will now override a *listen*-based default and does disable mod_ssl for the vhost.  [joe orton] 2.4.10 

*) mod_ssl: add workaround for *sslcertificatefile* when using openssl versions before 0.9.8h and not specifying an *sslcertificatechainfile* (regression introduced with 2.4.8). pr 56410. [kaspar brand] 2.4.10 

*) mod_proxy_html: avoid some possible memory access violation in case of specially crafted files, when the *proxyhtmlmeta* directive is turned on. follow up of pr 56287 [christophe jaillet] 2.4.10 

*) mod_auth_form: make sure the optional functions are loaded even when the *authformprovider* isn't specified. [graham leggett] 2.4.10 

*) mod_ssl: avoid processing bogus *sslcertificatekeyfile* values (and logging garbled file names). pr 56306. [kaspar brand] 2.4.10 

*) mod_ssl: fix merging of global and vhost-level settings with the *sslcertificatefile*, *sslcertificatekeyfile*, and *sslopensslconfcmd* directives. pr 56353. [kaspar brand] 2.4.10 

*) mod_headers: allow the "value" parameter of header and *requestheader* to contain an ap_expr expression if prefixed with "expr=". [eric covener] 2.4.10 

*) mod_proxy: do not try to parse the regular expressions passed by *proxypass*match as url as they do not follow their syntax. pr 56074. [ruediger pluem] 2.4.10 

*) mod_req*timeout*: resolve unexpected *timeout*s on *keepalive* requests under the event mpm. pr56216.  [frank meier <frank meier ergon ch>] 2.4.10 

*) mod_lua: reformat and escape *script* error output. [daniel gruno, felipe daragon <filipe syhunt com>] 2.4.10 

*) mod_lua: remove the non-working early/late arguments for *luahookcheckuserid*. [daniel gruno] 2.4.10 

*) mod_lua: add a fixups hook that checks if the original request is intended for *luamaphandler*. this fixes a bug where *fallbackresource* invalidates the *luamaphandler* directive in certain cases by changing the uri before the map handler code executes [daniel gruno, daniel ferradal <dferradal gmail com>]. 2.4.8 

*) core: support named *group*s and backreferences within the locationmatch, directorymatch, filesmatch and proxymatch directives. (requires non-ancient pcre library) [graham leggett] 2.4.8 

*) mod_dir: add *directorycheckhandler* to allow a 2.2-like behavior, skipping execution when a handler is already set. pr53929. [eric covener] 2.4.8 

*) mod_ssl: remove the hardcoded algorithm-type dependency for the *sslcertificatefile* and *sslcertificatekeyfile* directives, to enable future algorithm agility, and deprecate the *sslcertificatechainfile* directive (obsoleted by *sslcertificatefile*). [kaspar brand] 2.4.8 

*) mod_rewrite: add rewrite*options* inheritdown, inheritdownbefore, and ignoreinherit to allow *rewriterule*s to be pushed from parent scopes to child scopes without explicitly *config*uring each child scope. pr56153.  [edward lu <chaosed0 gmail com>] 2.4.8 

*) freebsd: disable ipv4-mapped *listen*ing sockets by default for versions 5+ instead of just for freebsd 5. pr 53824. [jeff trawick] 2.4.8 

*) mod_proxy_fcgi: fix error message when an unexpected *protocol* version number is received from the application.  pr 56110.  [jeff trawick] 2.4.8 

*) mod_lua: update r:setcookie() to accept a table of *options* and add domain, path and httponly to the list of *options* available to set. pr 56128 [edward lu <chaosed0 gmail com>, daniel gruno] 2.4.8 

*) mod_dir: don't search for a *directoryindex* or *directoryslash* on a url that was just rewritten by mod_rewrite. pr53929. [eric covener] 2.4.8 

*) mod_*session*: when we have a *session* we were unable to decode, behave as if there was no *session* at all. [thomas eckert <thomas.r.w.eckert gmail com>] 2.4.8 

*) mod_*session*: fix problems interpreting the *session*include and *session*exclude *config*uration. pr 56038. [erik pearson <erik adaptations.com>] 2.4.8 

*) mod_authn_core: allow <authnprovider*alias*>'es to be seen from auth stanzas under virtual hosts. pr 55622. [eric covener] 2.4.8 

*) mod_proxy_fcgi: use apr_socket_*timeout*_get instead of hard-coded 30 seconds *timeout*. [jan kaluza] 2.4.8 

*) build: only search for modules (*config**.m4) in known subdirectories, see build/*config*-stubs. [stefan fritsch] 2.4.8 

*) mod_ssl: add support for openssl *config*uration commands by introducing the *sslopensslconfcmd* directive. [stephen henson, kaspar brand] 2.4.8 

*) mod_proxy: remove (never documented) *<proxy* ~ wildcard-url> syntax which is equivalent to *<proxy*match wildcard-url>. [christophe jaillet] 2.4.8 

*) mod_authz_user, mod_authz_host, mod_authz_*group*file, mod_authz_dbm, mod_authz_dbd, mod_authnz_ldap: support the expression parser within the require directives. [graham leggett] 2.4.8 

*) security: cve-2013-4352 (cve.mitre.org) mod_cache: fix a null pointer deference which allowed untrusted origin servers to crash mod_cache in a forward proxy *config*uration.  [graham leggett] 2.4.7 

*) fix potential rejection of valid *maxmemfree* and *threadstacksize* directives.  [mike rumph <mike.rumph oracle.com>] 2.4.7 

*) mod_proxy_fcgi: handle reading *protocol* data that is split between packets.  [jeff trawick] 2.4.7 

*) mod_ssl: improve handling of ephemeral dh and ecdh keys by allowing custom parameters to be *config*ured via *sslcertificatefile*, and by adding standardized dh parameters for 1024/2048/3072/4096 bits. unless custom parameters are *config*ured, the standardized parameters are applied based on the certificate's rsa/dsa key size. [kaspar brand] 2.4.7 

*) mod_ssl, *config*ure: require openssl 0.9.8a or later. [kaspar brand] 2.4.7 

*) mod_ssl: drop support for export-grade ciphers with ephemeral rsa keys, and unconditionally disable anull, enull and exp ciphers (not overridable via *sslciphersuite*). [kaspar brand] 2.4.7 

*) event mpm: fix possible crashes (third party modules accessing c->sbh) or occasional missed mod_status updates for some *keepalive* requests under load. [eric covener] 2.4.7 

*) mod_*session*: reset the max-age on *session* save. pr 47476. [alexey varlamov <alexey.v.varlamov gmail com>] 2.4.7 

*) mod_*session*: after parsing the value of the header specified by the *session*header directive, remove the value from the response. pr 55279. [graham leggett] 2.4.7 

*) windows: correct failure to discard stderr in some error log *config*urations.  (error message ah00093)  [jeff trawick] 2.4.7 

*) mod_*session*_crypto: allow using exec: calls to obtain *session* encryption key.  [daniel ruggeri] 2.4.7 

*) mod_ldap: when looking up sub-*group*s, use an implicit objectclass=* instead of an explicit cn=* filter. [david hawes <dhawes vt.edu>] 2.4.7 

*) mod_auth_basic: add *authbasicusedigestalgorithm* directive to allow migration of passwords from digest to basic authentication. [chris darroch] 2.4.7 

*) suppress formatting of startup messages written to the console when *errorlog*format is used.  [jeff trawick] 2.4.7 

*) mod_headers: add 'setifempty' command to header and *requestheader*. [eric covener] 2.4.7 

*) mod_authz_*group*file, mod_authz_user: reduce severity of ah01671 and ah01663 from error to debug, since these modules do not know what mod_authz_core is doing with their authz_denied return value. [eric covener] 2.4.7 

*) mod_ldap: retry on an ldap *timeout* during authn. [eric covener] 2.4.7 

*) mod_ldap: change "*ldapreferrals* off" to actually set the underlying ldap sdk option to off, and introduce "*ldapreferrals* default" to take the sdk default, sans rebind authentication callback. [jan kaluza <kaluze at redhat.com>] 2.4.7 

*) winnt mpm: don't crash during child process initialization if the *listen* *protocol* is unrecognized.  [jeff trawick] 2.4.7 

*) mod_filter: add "change=no" as a proto-flag to filter*protocol* to remove a providers initial flags set at registration time. [eric covener] 2.4.7 

*) ab: fix potential buffer overflows when processing the t and x command-line *options*.  pr 55360. [mike rumph <mike.rumph oracle.com>] 2.4.7 

*) core: add open_htaccess hook which, in conjunction with dirwalk_stat and post_perdir_*config* (introduced in 2.4.5), allows mpm-itk to be used without patches to httpd core. [stefan fritsch] 2.4.7 

*) mod_lua: if the first yield() of a *luaoutputfilter* returns a string, it should be prefixed to the response as documented. [eric covener] note: not present in 2.4.7 changes 2.4.7 

*) mod_lua: remove etag, content-length, and content-md5 when a *luaoutputfilter* is *config*ured without mod_filter. [eric covener] note: not present in 2.4.7 changes 2.4.7 

*) mod_lua: register *luaoutputfilter* *script*s as changing the content and content-length by default, when run my mod_filter.  previously, growing or shrinking a response that started with content-length set would require mod_filter and filter*protocol* change=yes. [eric covener] note: not present in 2.4.7 changes 2.4.7 

*) mod_lua: return a 500 error if a luahook* *script* doesn't return a numeric return code. [eric covener] note: not present in 2.4.7 changes 2.4.6 

*) security: cve-2013-1896 (cve.mitre.org) mod_dav: sending a merge request against a uri handled by mod_dav_svn with the source href (sent as part of the request body as xml) pointing to a uri that is not *config*ured for dav will trigger a segfault. [ben reser <ben reser.org>] 2.4.5 

*) security: cve-2013-2249 (cve.mitre.org) mod_*session*_dbd: make sure that dirty flag is respected when saving *session*s, and ensure the *session* id is changed each time the *session* changes. this changes the format of the update*session* sql statement. existing *config*urations must be changed. [takashi sato, graham leggett] 2.4.5 

*) mod_auth_basic: add a generic mechanism to fake basic authentication using the ap_expr parser. *authbasicfake* allows the administrator to construct their own username and password for basic authentication based on their needs. [graham leggett] 2.4.5 

*) mpm_event: check that *asyncrequestworkerfactor* is not negative. pr 54254. [jackie zhang <jackie qq zhang gmail com>] 2.4.5 

*) core: support the single_*listen*_unserialized_accept optimization on linux kernel versions 3.x and above.  pr 55121.  [bradley heilbrun <apache heilbrun.org>] 2.4.5 

*) mod_cache_socache: make sure the *cachesocache*maxsize directive is merged correctly. [jens låås <jelaas gmail.com>] 2.4.5 

*) core: add post_perdir_*config* hook. [steinar gunderson <sgunderson bigfoot.com>] 2.4.5 

*) core: make the "default" parameter of the "*errordocument*" option case insensitive. pr 54419 [tianyin xu <tixu cs ucsd edu>] 2.4.5 

*) mod_proxy_html: make the "*proxyhtmlfixups*" *options* case insensitive. pr 54420 [tianyin xu <tixu cs ucsd edu>] 2.4.5 

*) mod_cache: make option "*cachedisable*" in mod_cache case insensitive. pr 54462 [tianyin xu <tixu cs ucsd edu>] 2.4.5 

*) mod_dav: sending an if or if-match header with an invalid etag doesn't result in a 412 precondition failed for a copy operation. pr54610 [timothy wood <tjw omni*group*.com>] 2.4.5 

*) mod_dav: make sure that when we prepare an if url for etag comparison, we compare unencoded paths. pr 53910 [timothy wood <tjw omni*group*.com>] 2.4.5 

*) '*auth*group*file*' and '*authuserfile*' do not accept anymore the optional 'standard' keyword . it was unused and not documented. pr54463 [tianyin xu <tixu cs.ucsd.edu> and christophe jaillet] 2.4.5 

*) core: speed up (for common cases) and reduce memory usage of ap_escape_logitem(). this should save 70-100 bytes in the request pool for a default *config*. [christophe jaillet] 2.4.5 

*) mod_dav: ensure uri is correctly uriencoded on return. pr 54611 [timothy wood <tjw omni*group*.com>] 2.4.5 

*) mod_ssl: add support for subjectaltname-based host name checking in proxy mode (*sslproxycheckpeername*). pr 54030. [kaspar brand] 2.4.5 

*) event mpm: provide error handling for *threadstacksize*. pr 54311 [tianyin xu <tixu cs.ucsd.edu>, christophe jaillet] 2.4.5 

*) core: improve error message where client's request-line exceeds *limitrequestline*. pr 54384 [christophe jaillet] 2.4.5 

*) mod_macro: new module that provides macros within *config*uration files. [fabien coelho] 2.4.5 

*) mod_proxy: add *balancerinherit* and *proxypass*inherit to control whether proxy balancers and workers are inherited by vhosts (default is on). [jim jagielski] 2.4.5 

*) added balancer parameter failon*timeout* to allow server admin to *config*ure an io *timeout* as an error in the balancer. [daniel ruggeri] 2.4.5 

*) mod_*setenv*if: fix crash in case *setenv*if and *setenv*ifexpr are used together. pr 54881. [ruediger pluem] 2.4.5 

*) mod_log_*config*: fix crash when logging request end time for a failed request.  pr 54828 [rainer jung] 2.4.5 

*) mod_ssl: catch missing, mismatched or encrypted client cert/key pairs with *sslproxymachinecertificatefile*/path directives. pr 52212, pr 54698. [keith burdis <keith burdis.org>, joe orton, kaspar brand] 2.4.5 

*) mod_cache_disk: *cacheminfilesize* and *cachemaxfilesize* were always using compiled in defaults of 1000000/1 respectively. [eric covener] 2.4.5 

*) mod_lbmethod_heartbeat, mod_heartmonitor: respect *defaultruntimedir*/ default_rel_runtimedir for the heartbeat storage file.  [jeff trawick] 2.4.5 

*) mod_lua: if a *luamaphandler* doesn't return any value, log a warning and treat it as apache2.ok. [eric covener] 2.4.5 

*) mod_lua: add *luainputfilter*/*luaoutputfilter* for creating content filters in lua [daniel gruno] 2.4.5 

*) mod_lua: allow *script*s handled by the lua-*script* handler to return a status code to the client (such as a 302 or a 500) [daniel gruno] 2.4.5 

*) mod_lua: decline handling 'lua-*script*' if the file doesn't exist, rather than throwing an internal server error. [daniel gruno] 2.4.5 

*) mod_lua: add new directive, *luamaphandler*, for dynamically mapping uris to lua *script*s and functions using regular expressions. [daniel gruno] 2.4.5 

*) mod_lua: add new directive *luacodecache* for controlling in-memory caching of lua *script*s. [daniel gruno] 2.4.4 

*) mod_dir: add support for the value 'disabled' in *fallbackresource*. [vincent deffontaines] 2.4.4 

*) mod_proxy_connect: don't *keepalive* the connection to the client if the backend closes the connection. pr 54474. [pavel mateja <pavel netsafe cz>] 2.4.4 

*) mod_proxy_http: honour special value 0 (unlimited) of *limitrequestbody* pr 54435.  [pavel mateja <pavel netsafe.cz>] 2.4.4 

*) htcacheclean: fix list *options* "-a" and "-a". [rainer jung] 2.4.4 

*) *config*ure: fix processing of --disable-feature for various features. [jeff trawick] 2.4.4 

*) mod_dialup/mod_http: prevent a crash in mod_dialup in case of internal *redirect*. pr 52230. 2.4.4 

*) ab: support socket *timeout* (-s *timeout*). [guido serra <zeph fsfe org>] 2.4.4 

*) core: fix directives like *loglevel* that need to know if they are invoked at virtual host context or in directory/files/location/if sections to work properly in if sections that are not in a directory/files/location. [stefan fritsch] 2.4.4 

*) mod_auth_form: make sure that get_notes_auth() sets the user as does get_form_auth() and get_*session*_auth(). makes sure that remote_user does not vanish during mod_include driven subrequests. [graham leggett] 2.4.4 

*) mod_auth_form: support the expr parser in the *authformloginrequiredlocation*, *authformloginsuccesslocation* and *authformlogoutlocation* directives. [graham leggett] 2.4.4 

*) mod_rewrite: stop mergeing *rewritebase* down to subdirectories unless new option 'rewrite*options* mergebase' is *config*ured. pr 53963. [eric covener] 2.4.4 

*) mod_proxy: add ability to *config*ure the sticky *session* separator. pr 53893. [<inu inusasha de>, jim jagielski] 2.4.4 

*) core: fail startup if the argument to *servertokens* is unrecognized. [jackie zhang  <jackie.qq.zhang gmail.com>] 2.4.4 

*) mod_*session*_dbd: fix a segmentation fault in the function dbd_remove. pr 53452. [<rebanerebane gmail com>, reimo rebane] 2.4.4 

*) mod_ssl: change default for *sslcompression* to off, as compression causes security issues in most setups. (the so called "crime" attack). [stefan fritsch] 2.4.4 

*) ab: add tls1.1/tls1.2 *options* to -f switch, and adapt output to more accurately report the negotiated *protocol*. pr 53916. [nicolás pernas maradei <nico e*mutex* com>, kaspar brand] 2.4.4 

*) core: *errordocument* now works for requests without a host header. pr 48357.  [jeff trawick] 2.4.4 

*) mod_proxy_ajp: fix crash in packet dump code when logging with *loglevel* trace7 or trace8.  pr 53730.  [rainer jung] 2.4.4 

*) httpd.conf: removed the *config*uration directives setting a bad_dnt environment introduced in 2.4.3. the actual directives are commented out in the default conf file. 2.4.4 

*) windows: fix output of -m, -l, and similar command-line *options* which display information about the server *config*uration. [jeff trawick] 2.4.3 

*) mod_authnz_ldap: don't try a potentially expensive nested *group*s search before exhausting all *authldap*group*attribute* checks on the current *group*. pr 52464 [eric covener] 2.4.3 

*) mod_lua: add new directive *luaauthzprovider* to allow implementing an authorization provider in lua. [stefan fritsch] 2.4.3 

*) httpd.conf: added *config*uration directives to set a bad_dnt environment variable based on user-agent and to remove the dnt header field from incoming requests when a match occurs. this currently has the effect of removing dnt from requests by msie 10.0 because it deliberately violates the current specification of dnt semantics for http. [roy t. fielding] 2.4.3 

*) windows: fix ssl failures on windows with *acceptfilter* https none. pr 52476.  [jeff trawick] 2.4.3 

*) the following now respect *defaultruntimedir*/default_rel_runtimedir: - mod_auth_digest: shared memory file [jeff trawick] 2.4.3 

*) mod_rewrite: fix crash with dbd *rewritemap*s. pr 53663. [mikhail t. <mi apache aldan algebra com>] 2.4.3 

*) mod_ssl: add new directive *sslcompression* to disable tls-level compression. pr 53219. [björn jacke <bjoern j3e de>, stefan fritsch] 2.4.3 

*) mod_*setenv*if: compile some global regex only once during startup. this should save some memory, especially with .htaccess. [stefan fritsch] 2.4.3 

*) mod_proxy: fix *proxypass*reverse for balancer *config*urations. pr 45434.  [joe orton] 2.4.3 

*) apxs: use ldflags from *config*_vars.mk in addition to cflags and cppflags. [stefan fritsch] 2.4.3 

*) mod_proxy: fix memory leak or possible corruption in *proxyblock* implementation.  [ruediger pluem, joe orton] 2.4.3 

*) mod_proxy: check hostname from request uri against *proxyblock* list, not forward proxy, if *proxyremote** is *config*ured.  [joe orton] 2.4.3 

*) mod_proxy_connect: avoid dns lookup on hostname from request uri if *proxyremote** is *config*ured.  pr 43697.  [joe orton] 2.4.3 

*) add "strict" and "warnings" pragmas to perl *script*s.  [rich bowen] 2.4.3 

*) the following now respect *defaultruntimedir*/default_rel_runtimedir: - core: the scoreboard (*scoreboardfile*), pid file (*pidfile*), and *mutex*es (*mutex*) [jim jagielski] 2.4.3 

*) mpm_event: don't do a blocking write when starting a lingering close from the *listen*er thread. pr 52229. [stefan fritsch] 2.4.3 

*) mod_so: if a filename without slashes is specified for *loadfile* or *loadmodule* and the file cannot be found in the server root directory, try to use the standard dlopen() search path. [stefan fritsch] 2.4.3 

*) core: log value of status header line in *script* responses rather than the fixed header name.  [chris darroch] 2.4.3 

*) mpm_event: fix handling of *maxconnectionsperchild*. [stefan fritsch] 2.4.3 

*) core: always log if *limitrequestfields*ize triggers.  [stefan fritsch] 2.4.3 

*) core: fix spurious "not allowed here" error returned when the *options* directive is used in .htaccess and "*allowoverride* *options*" (with no specific *options* restricted) is *config*ured.  pr 53444. [eric covener] 2.4.3 

*) mod_authz_core: fix parsing of require arguments in <authzprovider*alias*>. pr 53048. [stefan fritsch] 2.4.3 

*) mod_log_*config*: fix %{abc}c truncating cookie values at first "=". pr 53104. [greg ames] 2.4.3 

*) mod_ext_filter: fix error_log spam when input filters are *config*ured. [joe orton] 2.4.3 

*) core: use a tls 1.0 close_notify alert for internal dummy connection if the chosen *listen*er is *config*ured for https. [joe orton] 2.4.3 

*) core: prevent "httpd -k restart" from killing server in presence of *config* error. [joe orton] 2.4.3 

*) mod_slotmem_shm: honor *defaultruntimedir* [jim jagielski] 2.4.2 

*) mod_rewrite: fix *rewritecond* integer checks to be parsed correctly. pr 53023. [axel reinhold <apache freakout.de>, andré malo] 2.4.2 

*) mod_sed: don't define path_max to a potentially *undefine*d value, causing compile problems on gnu hurd. [stefan fritsch] 2.4.2 

*) core: add ap_runtime_dir_relative() and *defaultruntimedir*. [jeff trawick] 2.4.2 

*) core: fix breakage of *listen* directives with mpms that use a per-directory *config*. pr 52904. [stefan fritsch] 2.4.2 

*) core: disallow directives in *allowoverride*list which are only allowed in virtualhost or server context. these are usually not prepared to be called in .htaccess files. [stefan fritsch] 2.4.2 

*) core: in *allowoverride*list, do not allow 'none' together with other directives. pr 52823. [stefan fritsch] 2.4.2 

*) core: fix merging of *allowoverride*list and *contentdigest*. [stefan fritsch] 2.4.2 

*) mod_request: fix validation of the *keptbodysize* argument so it doesn't always throw a *config*uration error. pr 52981 [eric covener] 2.4.2 

*) "*directoryindex* disabled" now undoes *directoryindex* settings in the current *config*uration section, not just previous *config* sections. pr 52845. [eric covener] 2.4.2 

*) core: check during *config* test that directories for the access logs actually exist. pr 29941. [stefan fritsch] 2.4.2 

*) mod_xml2enc, mod_proxy_html: enable per-module *loglevel*s. [stefan fritsch] 2.4.2 

*) mod_filter: fix segfault with **addoutputfilter*bytype*. pr 52755. [stefan fritsch] 2.4.2 

*) mod_*session*: *session*s are encoded as application/x-www-form-urlencoded strings, however we do not handle the encoding of spaces properly. fixed. [graham leggett] 2.4.2 

*) *config*uration: *example* in comment should use a path consistent with the default *config*uration. pr 52715. [rich bowen, jens schleusener, rainer jung] 2.4.2 

*) *config*uration: switch documentation links from trunk to 2.4. [rainer jung] 2.4.2 

*) *config*ure: fix out of tree build using apr and apr-util in srclib. [rainer jung] 2.4.1 

*) security: cve-2012-0053 (cve.mitre.org) fix an issue in error responses that could expose "httponly" cookies when no custom *errordocument* is specified for status code 400. [eric covener] 2.4.1 

*) core: check during *config*test that the directories for error logs exist. pr 29941 [stefan fritsch] 2.4.1 

*) core *config*uration: add *allowoverride* option to treat syntax errors in .htaccess as non-fatal. pr 52439 [nick kew, jim jagielski] 2.4.1 

*) *config*ure: disable modules at *config*ure time if a prerequisite module is not enabled. pr 52487. [stefan fritsch] 2.4.1 

*) security: cve-2012-0021 (cve.mitre.org) mod_log_*config*: fix segfault (crash) when the '%{*cookiename*}c' log format string is in use and a client sends a nameless, valueless cookie, causing a denial of service. the issue existed since version 2.2.17 and 2.3.3. pr 52256.  [rainer canavan <rainer-apache 7val com>] 2.4.0 

*) mod_ssl: when compiled against openssl 1.0.1 or later, allow explicit control of tlsv1.1 and tlsv1.2 through the ssl*protocol* directive. [kaspar brand] 2.4.0 

*) mod_mime: don't arbitrarily bypass *addoutputfilter* during a *proxypass*, but then allow *addoutputfilter* during a *rewriterule* [p]. make mod_mime behave identically in both cases. pr52342. [graham leggett] 2.4.0 

*) security: cve-2011-4317 (cve.mitre.org) resolve additional cases of url rewriting with *proxypass*match or *rewriterule*, where particular request-uris could result in undesired backend network exposure in some *config*urations. [joe orton] 2.3.16 

*) mod_rewrite: add the allownoslash rewriteoption, which makes it possible for *rewriterule*s to be placed in .htaccess files that match the directory with no trailing slash. pr 48304. [matthew byng-maddick <matthew byng-maddick bbc.co.uk>] 2.3.16 

*) mod_*session*_crypto: add a *session*cryptopassphrasefile directive so that the administrator can hide the keys from the *config*uration. [graham leggett] 2.3.16 

*) core: pass ap_*errorlog*_info struct to error log hook. [stefan fritsch] 2.3.16 

*) mod_ssl: use a shorter setting for *sslciphersuite* in the default default *config*uration file, and add some more information about *config*uring a speed-optimized alternative. [kaspar brand] 2.3.16 

*) mod_ssl: drop support for the sslv2 *protocol*. [kaspar brand] 2.3.16 

*) mod_lua: stop losing track of all but the most specific luahook* directives when multiple per-directory *config* sections are used.  adds *luainherit* directive to control how parent sections are merged.  [eric covener] 2.3.16 

*) pre ga removal of components that will not be included: - mod_noloris was superseded by mod_req*timeout* - mod_serf - mpm_simple [rainer jung] 2.3.16 

*) core: set *maxmemfree* 2048 by default. [stefan fritsch] 2.3.16 

*) *config*ure: additional modules loaded by default: mod_headers. modules moved from module set "few" to "most" and no longer loaded by default: mod_*action*s, mod_*allowmethods*, mod_auth_form, mod_buffer, mod_cgi(d), mod_include, mod_negotiation, mod_ratelimit, mod_request, mod_*userdir*. [rainer jung] 2.3.16 

*) *config*ure: only load the really imporant modules (i.e. those enabled by the 'few' selection) by default. don't handle modules enabled with --enable-foo specially. [stefan fritsch] 2.3.16 

*) mod_ssl: add support for *config*uring persistent tls *session* ticket encryption/decryption keys (useful for clustered environments). [paul querna, kaspar brand] 2.3.16 

*) security: cve-2011-3607 (cve.mitre.org) core: fix integer overflow in ap_pregsub. this can be triggered e.g. with mod_*setenv*if via a malicious .htaccess. [stefan fritsch] 2.3.15 

*) security: cve-2011-3368 (cve.mitre.org) reject requests where the request-uri does not match the http specification, preventing unexpected expansion of target urls in some reverse proxy *config*urations.  [joe orton] 2.3.15 

*) *config*ure: load all modules in the generated default *config*uration when using --enable-load-all-modules. [rainer jung] 2.3.15 

*) mod_req*timeout*: change the default to set some reasonable *timeout* values. [stefan fritsch] 2.3.15 

*) *config*ure: by default, only load those modules that are either required or explicitly selected by a *config*ure --enable-foo argument. the *loadmodule* statements for modules enabled by --enable-mods-shared=most and friends will be commented out. [stefan fritsch] 2.3.15 

*) mod_lua: prevent early lua hooks (*luahooktranslatename* and luahookquickhandler) from being *config*ured in *<directory*>, *<files*>, and htaccess where the *config*uration would have been ignored. [eric covener] 2.3.15 

*) mod_lua: resolve "attempt to index local 'r' (a userdata value)" errors in *luamaphandler* *script*s [eric covener] 2.3.15 

*) mod_log_debug: rename optional argument from if= to expr=, to be more in line with other *config* directives. [stefan fritsch] 2.3.15 

*) mod_headers: require an expression to be specified with expr=, to be more in line with other *config* directives. [stefan fritsch] 2.3.15 

*) mod_*substitute*: to prevent overboarding memory usage, limit line length to 1mb. [stefan fritsch] 2.3.15 

*) mod_*session*_crypto: refactor to support the new apr_crypto api. [graham leggett] 2.3.15 

*) http: add missing location header if local url-path is used as *errordocument* for 30x. [stefan fritsch] 2.3.15 

*) mod_buffer: make sure we step down for subrequests, but not for internal *redirect*s triggered by mod_rewrite. [graham leggett] 2.3.15 

*) mod_remote_ip: fix *config*uration of internal proxies. pr 49272. [jim riggs <jim riggs me>] 2.3.15 

*) mpm_winnt: handle *acceptfilter* 'none' mode correctly; resolve specific server ip endpoint and remote client ip upon connection.  [william rowe] 2.3.15 

*) mod_*setenv*if: remove oid match which is obsoleted by *setenv*ifexpr with peerextlist(). [stefan fritsch] 2.3.15 

*) mod_mime_magic: add signatures for png and swf to the *example* *config*. pr: 48352. [jeremy wagner-kaiser <jwagner-kaiser adknowledge com>] 2.3.15 

*) core, unixd: add -d dump_run_cfg option to dump some *config*uration items from the parsed (or default) *config*. this is useful for init *script*s that need to setup temporary directories and permissions. [stefan fritsch] 2.3.15 

*) core, mod_*action*s, mod_asis: downgrade error log messages which accompany a 404 request status from *loglevel* error to info. pr: 35768. [stefan fritsch] 2.3.15 

*) core: enforce *limitrequestfields*ize after multiple headers with the same name have been merged. [stefan fritsch] 2.3.15 

*) mod_ssl: if *maxmemfree* is set, ask openssl >= 1.0.0 to reduce memory usage.  pr 51618. [cristian rodríguez <crrodriguez opensuse org>, stefan fritsch] 2.3.15 

*) mod_ssl: at startup, when checking a server certificate whether it matches the *config*ured *servername*, also take dnsname entries in the subjectaltname extension into account. pr 32652, pr 47051. [kaspar brand] 2.3.15 

*) mod_*substitute*: reduce memory usage and copying of data. pr 50559. [stefan fritsch] 2.3.15 

*) core: correctly obey *servername* / *server*alias** if the host header from the request matches the virtualhost address. pr 51709. [micha lenk <micha lenk.info>] 2.3.15 

*) core: add *maxrangeoverlaps* and *maxrangereversals* directives to control the number of overlapping and reversing ranges (respectively) permitted before returning the entire resource, with a default limit of 20. [jim jagielski] 2.3.15 

*) core: allow *maxranges* none|unlimited|default and set 'accept-ranges: none' in the case ranges are being ignored with *maxranges* none. [eric covener] 2.3.15 

*) core: add *maxranges* directive to control the number of ranges permitted before returning the entire resource, with a default limit of 200. [eric covener] 2.3.15 

*) mod_cache: ensure that *cachedisable* can correctly appear within a locationmatch. [graham leggett] 2.3.15 

*) mod_cache: fix the moving of the cache filter, which erroneously stood down if the original filter was not added by *config*uration. [graham leggett] 2.3.15 

*) mod_authz_*group*file: increase length limit of lines in the *group* file to 16mb. pr 43084. [stefan fritsch] 2.3.15 

*) core: increase length limit of lines in the *config*uration file to 16mb. pr 45888. pr 50824. [stefan fritsch] 2.3.15 

*) mod_ldap: enable ldapconnection*timeout* for ldap toolkits that have ldap_opt_connect_*timeout* instead of ldap_opt_network_*timeout*, such as tivoli directory server 6.3 and later. [eric covener] 2.3.15 

*) mod_ldap: change default number of retries from 10 to 3, and add an *ldapretries* and *ldapretrydelay* directives. [eric covener] 2.3.15 

*) *config*ure: allow to explicitly disable modules even with module selection 'reallyall'. [stefan fritsch] 2.3.15 

*) mod_rewrite: check validity of each internal (int:) *rewritemap* even if the *rewriteengine* is disabled in server context, avoiding a crash while referencing the invalid int: map at runtime. pr 50994. [ben noordhuis <info noordhuis nl>] 2.3.15 

*) mod_ssl, *config*ure: require openssl 0.9.7 or later. [kaspar brand] 2.3.15 

*) mod_ssl, *config*ure, ab: drop support for rsa bsafe ssl-c toolkit. [kaspar brand] 2.3.15 

*) mod_usertrack: run mod_usertrack earlier in the fixups hook to ensure the cookie is set when modules such as mod_rewrite trigger a *redirect*. also use r->err_headers_out for the cookie, for the same reason.  pr29755. [sami j. mäkinen <sjm almamedia fi>, eric covener] 2.3.15 

*) *config*ure: enable ldap modules in 'all' and 'most' selections if ldap is compiled into apr-util. [stefan fritsch] 2.3.15 

*) mod_authn_socache: fix to work in .htaccess if not *config*ured anywhere in httpd.conf, and introduce an *authn*cacheenable** directive. pr 51991 [nick kew] 2.3.15 

*) mod_proxy: enable absolute urls to be rewritten with *proxypass*reverse, e.g. to reverse proxy "location: https://other-internal-server/login" [nick kew] 2.3.14 

*) mod_*allowmethods*: correct merging of "reset" and do not allow an empty parameter list for the *allowmethods* directive. [rainer jung] 2.3.14 

*) *config*ure: update selection of modules for 'all' and 'most'. 'all' will now enable all modules except for *example* and test modules. make the selection for 'most' more useful (including ssl and proxy). both 'all' and 'most' will now disable modules if dependencies are missing instead of aborting. if a specific module is requested with --enable-xxx=yes, missing dependencies will still cause *config*ure to exit with an error. [stefan fritsch] 2.3.14 

*) core: add more logging to ap_scan_*script*_header_err* functions. add ap_scan_*script*_header_err*_ex functions that take a module index for logging. mod_cgi, mod_cgid, mod_proxy_fcgi, mod_proxy_scgi, mod_isapi: use the new functions in order to make logging *config*urable per-module. [stefan fritsch] 2.3.14 

*) mod_dir: add *directoryindex**redirect* to send an external *redirect* to the proper index.  [eric covener] 2.3.14 

*) *suexec*: add environment variables context_document_root, context_prefix, *redirect*_error_notes, *redirect*_*script*_filename, request_scheme to the whitelist in *suexec*. pr 51499. [graham laverty <graham reg ca>, stefan fritsch] 2.3.14 

*) mod_rewrite: fix regexp *rewritecond* with nocase. [stefan fritsch] 2.3.14 

*) *config*ure: support reallyall option also for --enable-mods-static. [rainer jung] 2.3.14 

*) mod_socache_dc: add --with-distcache to *config*ure for choosing the distcache installation directory. [rainer jung] 2.3.14 

*) *config*ure: only link the httpd binary against pcre. no other support binary needs pcre. [rainer jung] 2.3.14 

*) *config*ure: tolerate dependency checking failures for modules if they have been enabled implicitely. [rainer jung] 2.3.14 

*) *config*ure: allow to specify module specific custom linker flags via the mod_xxx_ldadd variables. [rainer jung] 2.3.13 

*) core: add support to *errorlog*format for logging the system unique thread id under linux. [stefan fritsch] 2.3.13 

*) event: new *asyncrequestworkerfactor* directive to influence how many connections will be accepted per process. [stefan fritsch] 2.3.13 

*) prefork, worker, event: rename maxclients to *maxrequestworkers* which describes more accurately what it does. [stefan fritsch] 2.3.13 

*) mod_ssl: avoid unnecessary renegotiations with *sslverifydepth* 0. pr 48215. [kaspar brand] 2.3.13 

*) mpm_event: if *maxmemfree* is set, limit the number of pools that is kept around. [stefan fritsch] 2.3.13 

*) mod_ssl: disable aecdh ciphers in *example* *config*. pr 51363. [rob stradling <rob comodo com>] 2.3.13 

*) mod_*userdir*/mod_*alias*/mod_vhost_*alias*: correctly set document_root, context_document_root, context_prefix. pr 26052. pr 46198. [stefan fritsch] 2.3.13 

*) core: allow to override document_root on a per-request basis. introduce new context_document_root and context_prefix which provide information about non-global uri-to-directory mappings (from e.g. mod_*userdir* or mod_*alias*) to *script*s. pr 49705. [stefan fritsch] 2.3.13 

*) core: add *<else*if> and *<else*> to complement <if> sections. [stefan fritsch] 2.3.13 

*) mod_ext_filter: remove debuglevel option in favor of per-module *loglevel*. [stefan fritsch] 2.3.13 

*) mod_include: make the "#if expr" element use the new "ap_expr" expression parser. the old parser can still be used by setting the new directive *ssilegacyexprparser*. [stefan fritsch] 2.3.13 

*) core: add some features to ap_expr for use by mod_include: a restricted mode that does not allow to bypass request access restrictions; new variables document_uri (*alias* for request_uri), last_modified; -a as an *alias* for -u; an additional data entry in ap_expr_eval_ctx_t for use by the consumer; an extensible ap_expr_exec_ctx() api that allows to use that data entry. [stefan fritsch] 2.3.13 

*) mod_include: merge directory *config*s instead of one ssi* *config* directive causing all other per-directory ssi* *config* directives to be reset. [stefan fritsch] 2.3.13 

*) mod_charset_lite: remove debuglevel option in favour of per-module *loglevel*. [stefan fritsch] 2.3.13 

*) mod_req*timeout*: fix a timed out connection going into the keep-alive state after a *timeout* when discarding a request body. pr 51103. [stefan fritsch] 2.3.13 

*) *config*ure: fix *script* error when *config*uring module set "reallyall". [rainer jung] 2.3.12 

*) *config*ure, core: provide easier support for apr's hook probe capability. [jim jagielski, jeff trawick] 2.3.12 

*) mod_ldap: make *ldapsharedcachesize* 0 create a non-shared-memory cache per process as opposed to disabling caching completely. this allows to use the non-shared-memory cache as a workaround for the shared memory cache not being available during graceful restarts. pr 48958. [stefan fritsch] 2.3.12 

*) core: support module names with colons in *loglevel* *config*uration. [torsten förtsch <torsten foertsch gmx net>] 2.3.12 

*) mod_proxy_ajp: add support for '*proxyerroroverride* on'. pr 50945. [peter pramberger <peter pramberger.at>, jim jagielski] 2.3.12 

*) mod_proxy_fcgi: add support for '*proxyerroroverride* on'. pr 50913. [mark montague <mark catseye.org>, jim jagielski] 2.3.12 

*) core: change the apis of ap_cfg_getline() and ap_cfg_getc() to return an error code. abort with a nice error message if a *config* line is too long. partial fix for pr 50824. [stefan fritsch] 2.3.12 

*) mod_info: dump *config* to stdout during startup if -ddump_*config* is specified. pr 31956. [stefan fritsch] 2.3.12 

*) mod_log_*config*: prevent segfault. pr 50861. [torsten förtsch <torsten.foertsch gmx.net>] 2.3.12 

*) core: *allowencodedslashes* new option nodecode to allow encoded slashes in request url path info but not decode them. change behavior of option "on" to decode the encoded slashes as 2.0 and 2.2 do.  pr 35256, pr 46830.  [dan poirier] 2.3.12 

*) mod_ldap: add *ldapconnectionpoolttl* to give control over lifetime of bound backend ldap connections.  pr47634 [eric covener] 2.3.12 

*) mod_cache: make *cacheenable* and *cachedisable* *config*urable per directory in addition to per server, making them work from within a locationmatch. [graham leggett] 2.3.12 

*) mod_win32: added shebang check for '! so that .vbs *script*s work as cgi. win32's c*script* interpreter can only use a single quote as comment char. [guenter knauf] 2.3.11 

*) core: create new ap_state_query function that allows modules to determine if the current *config*uration run is the initial one at server startup, and if the server is started for testing/*config* dumping only. [stefan fritsch] 2.3.11 

*) mod_proxy: runtime *config*uration of many parameters for existing balancers via the balancer-manager. [jim jagielski] 2.3.11 

*) mod_proxy: runtime addition of new workers (*balancermember*) for existing balancers via the balancer-manager. [jim jagielski] 2.3.11 

*) mod_ssl: fix a possible startup failure if multiple ssl vhosts are *config*ured with the same *servername* and private key file. [masahiro matsuya <mmatsuya redhat.com>, joe orton] 2.3.11 

*) core: add support to set variables with the 'define' directive. the variables that can then be used in the *config* using the ${var} syntax known from envvar interpolation. [stefan fritsch] 2.3.11 

*) mod_proxy_http: make adding of x-forwarded-* headers *config*urable. *proxyaddheaders* defaults to on. [vincent deffontaines] 2.3.11 

*) mod_ssl: add *config* *options* for ocsp: sslocspresponder*timeout*, *sslocspresponsemaxage*, *sslocspresponsetimeskew*. [kaspar brand <httpd-dev.2011 velox.ch>] 2.3.11 

*) core: apply <if> sections to all requests, not only to file base requests. allow to use <if> inside *<directory*>, *<location*>, and *<files*> sections. the merging of <if> sections now happens after the merging of *<location*> sections, even if an <if> section is embedded inside a *<directory*> or *<files*> section.  [stefan fritsch] 2.3.11 

*) mod_authn_socache: change directive name from authncacheprovider to *authncacheprovidefor*.  the term "provider" is overloaded in this module, and we should avoid confusion between the provider of a backend (*authn*cachesocache**) and the authn provider(s) for which this module provides cacheing (*authncacheprovidefor*). [nick kew] 2.3.11 

*) mod_ssl: change the format of the ssl_{client,server}_{i,s}_dn variables to be rfc 2253 compatible, convert non-ascii characters to utf8, and escape other special characters with backslashes. the old format can still be used with the legacydnstringformat argument to ssl*options*. 2.3.11 

*) core, mod_rewrite: make the request_scheme variable available to *script*s and mod_rewrite. [stefan fritsch] 2.3.11 

*) mod_rewrite: allow to use arbitrary boolean expressions (ap_expr) in *rewritecond*. [stefan fritsch] 2.3.11 

*) core: disallow the mixing of relative and absolute *options* pr 33708. [sönke tesch <st kino-fahrplan.de>] 2.3.11 

*) core: when selecting an ip-based virtual host, favor an exact match for the port over a wildcard (or omitted) port instead of favoring the one that came first in the *config*uration file. [eric covener] 2.3.11 

*) core: overlapping virtual host address/port combinations  now implicitly enable name-based virtual hosting for that address.  the *namevirtualhost* directive has no effect, and _default_ is interpreted the same as "*". [eric covener] 2.3.11 

*) core: in the absence of any *options* directives, the default is now "followsymlinks" instead of "all".  [igor galić] 2.3.11 

*) mod_authz_core: add *authzsendforbiddenonfailure* directive to allow sending '403 forbidden' instead of '401 unauthorized' if authorization fails for an authenticated user. pr 40721. [stefan fritsch] 2.3.10 

*) core: honor '*acceptpathinfo* off' during internal *redirect*s, such as per-directory mod_rewrite substitutions.  pr 50349. [eric covener] 2.3.10 

*) mod_rewrite: add 'rewrite*options* inheritbefore' to put the base rules/conditions before the overridden rules/conditions.  pr 39313. [jérôme grandjanny <jerome.grandjanny cea.fr>] 2.3.10 

*) mod_autoindex: add *indexignore*reset to reset the list of *indexignore*d filenames in higher precedence *config*uration sections.  pr 24243. [eric covener] 2.3.10 

*) core: fail startup when the argument to *servername* looks like a glob or a regular expression instead of a hostname (*?[]).  pr 39863 [rahul nair <rahul.g.nair gmail.com>] 2.3.10 

*) mod_*userdir*: add merging of enable, disable, and filename arguments to *userdir* directive, leaving enable/disable of userlists unmerged. pr 44076 [eric covener] 2.3.10 

*) httpd: when no -k option is provided on the httpd command line, the server was starting without checking for an existing *pidfile*.  pr 50350 [eric covener] 2.3.10 

*) security: cve-2010-1623 (cve.mitre.org) fix a denial of service attack against mod_req*timeout*. [stefan fritsch] 2.3.9 

*) mod_*setenv*if: add *setenv*ifexpr directive to set env var depending on expression. [stefan fritsch] 2.3.9 

*) mod_proxy: fix *proxypass*interpolateenv directive. pr 50292. [stefan fritsch] 2.3.9 

*) *suexec*: add *suexec* directive to disable *suexec* without renaming the binary (*suexec* off), or force startup failure if *suexec* is required but not supported (*suexec* on).  change **suexec*user*group** to fail startup instead of just printing a warning if *suexec* is disabled. [jeff trawick] 2.3.9 

*) mod_rewrite: fix the *rewriteengine* directive to work within a location. previously, once *rewriteengine* was switched on globally, it was impossible to switch off. [graham leggett] 2.3.9 

*) core: do the hook sorting earlier so that the hooks are properly sorted for the pre_*config* hook and during parsing the *config*. [stefan fritsch] 2.3.9 

*) core: in the absence of any *allowoverride* directives, the default is now "none" instead of "all".  pr49823 [eric covener] 2.3.9 

*) mod_proxy: don't allow *proxypass* or *proxypass*reverse in *<directory*> or *<files*>. pr47765 [eric covener] 2.3.9 

*) prefork/worker/event mpms: default value (when no directive is present) of *maxconnectionsperchild*/maxrequestsperchild is changed to 0 from 10000 to match default *config*uration and manual. pr47782 [eric covener] 2.3.9 

*) mod_rewrite: add end flag for *rewriterule* to prevent further rounds of rewrite processing when a per-directory substitution occurs. [eric covener] 2.3.9 

*) mod_proxy: optimise *proxypass* within a location so that it is stored per-directory, and chosen during the location walk. make *proxypass* work correctly from within a locationmatch. [graham leggett] 2.3.9 

*) core: fix segfault if per-module *loglevel* is on virtual host scope. pr 50117. [stefan fritsch] 2.3.9 

*) mod_proxy: move the *proxyerroroverride* directive to have per directory scope. [graham leggett] 2.3.9 

*) mod_*allowmethods*: new module to deny certain http methods without interfering with authentication/authorization. [paul querna, igor galić, stefan fritsch] 2.3.9 

*) core: rename maxrequestsperchild to *maxconnectionsperchild*, which describes more accurately what the directive does. the old name still works but logs a warning. [stefan fritsch] 2.3.9 

*) mod_cache: optionally serve stale data when a revalidation returns a 5xx response, controlled by the *cachestaleonerror* directive. [graham leggett] 2.3.9 

*) mod_cache: allow control over the base url of reverse proxied requests using the *cachekeybaseurl* directive, so that the cache key can be calculated from the endpoint url instead of the server url. [graham leggett] 2.3.9 

*) mod_cache: *cachelastmodifiedfactor*, *cachestorenostore*, *cachestoreprivate*, *cachestoreexpired*, *cacheignorenolastmod*, *cachedefaultexpire*, *cacheminexpire* and *cachemaxexpire* can be set per directory/location. [graham leggett] 2.3.9 

*) mod_disk_cache: *cachemaxfilesize*, *cacheminfilesize*, *cachereadsize* and *cachereadtime* can be set per directory/location. [graham leggett] 2.3.9 

*) core: speed up *config* parsing if using a very large number of *config* files. pr 50002 [andrew cloudaccess net] 2.3.9 

*) mod_ssl: add authz providers for use with mod_authz_core and its requireany/requireall containers: 'ssl' (equivalent to *sslrequire*ssl), 'ssl-verify-client' (for use with '*sslverifyclient* optional'), and 'ssl-require' (expressions with same syntax as *sslrequire*). [stefan fritsch] 2.3.9 

*) core: for process invocation (cgi, fcgid, piped loggers and so forth) pass the system library path (ld_library_path or platform-specific variables) along with the system path, by default.  both should be overridden together as desired using *passenv* etc; see mod_env. [william rowe] 2.3.9 

*) mod_cache: introduce *cachestoreexpired*, to allow administrators to capture a stale backend response, perform if-modified-since requests against the backend, and serving from the cache all 304 responses. this restores pre-2.2.4 cache behavior.  [william rowe] 2.3.9 

*) mod_authz_core: allow authz providers to check args while reading the *config* and allow to cache parsed args. move 'all' and 'env' authz providers from mod_authz_host to mod_authz_core. add 'method' authz provider depending on the http method.  [stefan fritsch] 2.3.9 

*) mod_cache: change the signature of the store_body() provider function within the mod_cache provider interface to support an "in" brigade and an "out" brigade instead of just a single input brigade. this gives a cache provider the option to consume only part of the brigade passed to it, rather than the whole brigade as was required before. this fixes an out of memory and a request *timeout* condition that would occur when the original document was a large file. introduce *cachereadsize* and *cachereadtime* directives to mod_disk_cache to control the amount of data to attempt to cache at a time. [graham leggett] 2.3.9 

*) core: add *errorlog*format to allow *config*uring error log format, including additional information that is logged once per connection or request. add error log ids for connections and request to allow correlating error log lines and the corresponding access log entry. [stefan fritsch] 2.3.9 

*) mod_cache: use a proper filter context to hold filter data instead of misusing the per-request *config*uration. fixes a segfault on trunk when the normal handler is used. [graham leggett] 2.3.9 

*) mod_cgid: log a warning if the *script*sock path is truncated because it is too long. pr 49388.  [stefan fritsch] 2.3.9 

*) vhosts: do not allow _default_ in *namevirtualhost*, or mixing * and non-* ports on *namevirtualhost*, or multiple *namevirtualhost* directives for the same address:port, or *namevirtualhost* directives with no matching virtualhosts, or multiple ip-based virtualhost sections for the same address:port.  these were previously accepted with a warning, but the behavior was *undefine*d.  [dan poirier] 2.3.9 

*) proxy: support setting source address.  pr 29404 [multiple contributors iterating through bugzilla, aron ujvari <xanco nikhok.hu>, aleksey midenkov <asm uezku.kemsu.ru>, <dan *listen*ing-station.net; trunk version nick kew] 2.3.9 

*) http *protocol*: return 400 not 503 if we have to abort due to malformed chunked encoding. [nick kew] 2.3.8 

*) *suexec*: support large log files. pr 45856. [stefan fritsch] 2.3.8 

*) security: cve-2010-1452 (cve.mitre.org) mod_dav, mod_cache, mod_*session*: fix handling of requests without a path segment. pr: 49246 [mark drayton, jeff trawick] 2.3.7 

*) *config*ure: add reallyall option for --enable-mods-shared. [stefan fritsch] 2.3.7 

*) cgi vars: allow path to be set by *setenv*, consistent with ld_library_path pr 43906 [nick kew] 2.3.7 

*) http *protocol* filter: fix handling of longer chunk extensions pr 49474 [<tee.bee gmx.de>] 2.3.7 

*) update ssl cipher suite and add *example* for *sslhonorcipherorder*. [lars eilebrecht, rainer jung] 2.3.7 

*) move **addoutputfilter*bytype* from core to mod_filter.  this should fix nasty side-effects that happen when content_type is set more than once in processing a request, and make it fully compatible with dynamic and proxied contents. [nick kew] 2.3.7 

*) mod_log_*config*: implement logging for sub second timestamps and request end time.  [rainer jung] 2.3.6 

*) security: cve-2009-3555 (cve.mitre.org) mod_ssl: comprehensive fix of the tls renegotiation prefix injection attack when compiled against openssl version 0.9.8m or later. introduces the '*sslinsecurerenegotiation*' directive to reopen this vulnerability and offer unsafe legacy renegotiation with clients which do not yet support the new secure renegotiation *protocol*, rfc 5746. [joe orton, and with thanks to the openssl team] 2.3.6 

*) security: cve-2009-3555 (cve.mitre.org) mod_ssl: a partial fix for the tls renegotiation prefix injection attack by rejecting any client-initiated renegotiations. forcibly disable *keepalive* for the connection if there is any buffered data readable. any *config*uration which requires renegotiation for per-directory/location access control is still vulnerable, unless using openssl >= 0.9.8l. [joe orton, ruediger pluem, hartmut keil <hartmut.keil adnovum.ch>] 2.3.6 

*) core: adjust the output filter chain correctly in an internal *redirect* from a subrequest, preserving filters from the main request as necessary.  pr 17629.  [joe orton] 2.3.6 

*) core: add microsecond timestamp fr*action*s, process id and thread id to the error log. [rainer jung] 2.3.6 

*) *config*ure: the "most" module set gets build by default.  [rainer jung] 2.3.6 

*) *config*ure: building dynamic modules (dso) by default.  [rainer jung] 2.3.6 

*) *config*ure: fix broken vpath build when using included apr. [rainer jung] 2.3.6 

*) mod_*session*_crypto: fix *config*ure problem when building with apr 2 and for vpath builds with included apr. [rainer jung] 2.3.6 

*) mod_*session*_crypto: api compatibility with apr 2 crypto and apr util 1.x crypto. [rainer jung] 2.3.6 

*) core: add per-module and per-directory *loglevel* *config*uration. add some more trace logging. mod_rewrite: replace rewritelog/rewrite*loglevel* with trace log levels. mod_ssl: replace *loglevel*debugdump with trace log levels. mod_ssl/mod_proxy*: adjust *loglevel*s to be less verbose at levels info and debug. mod_dumpio:  replace dumpio*loglevel* with trace log levels. [stefan fritsch] 2.3.6 

*) mod_authnz_ldap: ensure nested *group*s are checked when the top-level *group* doesn't have any direct non-*group* members of attributes in *authldap*group*attribute*. [eric covener] 2.3.6 

*) mod_authnz_ldap: search or comparison during authorization phase can use the credentials from the authentication phase (*authldapsearchasuser*,*authldapcompareasuser*). pr 48340 [domenico rotiroti, eric covener] 2.3.6 

*) mod_authnz_ldap: allow the initial dn search during authentication to use the http username/pass instead of an *anonymous* or hard-coded ldap id (*authldapinitialbindasuser*, *authldapinitialbindpattern*). [eric covener] 2.3.6 

*) mod_authnz_ldap: publish requested ldap data with an authorize_ prefix when this module is used for authorization. see *authldapauthorizeprefix*. pr 45584 [eric covener] 2.3.6 

*) ab: fix number of requests sent by ab when *keepalive* is enabled.  pr 48497. [bryn dole <dole blekko.com>] 2.3.6 

*) log an error for failures to read a chunk-size, and return 408 instead of 413 when this is due to a read *timeout*.  this change also fixes some cases of two error documents being sent in the response for the same scenario. [eric covener] pr49167 2.3.6 

*) mod_proxy_connect: support port ranges in *allowconnect*. pr 23673. [stefan fritsch] 2.3.6 

*) introduce *sslfips* directive to support openssl fips_mode; permits all builds of mod_ssl to use '*sslfips* off' for portability, but the proper build of openssl is required for '*sslfips* on'.  pr 46270. [dr stephen henson <steve openssl.org>, william rowe] 2.3.6 

*) mod_req*timeout*: do not wrongly enforce *timeout*s for mod_proxy's backend connections and other *protocol* handlers (like mod_ftp). [stefan fritsch] 2.3.6 

*) mod_ssl: add the '*sslinsecurerenegotiation*' directive, which allows insecure renegotiation with clients which do not yet support the secure renegotiation *protocol*.  [joe orton] 2.3.6 

*) mod_ssl: fix a potential i/o hang if a long list of trusted cas is *config*ured for client cert auth. pr 46952.  [joe orton] 2.3.6 

*) core: only log a 408 if it is no *keepalive* *timeout*. pr 39785 [ruediger pluem,  mark montague <markmont umich.edu>] 2.3.6 

*) mod_ldap: update *ldaptrustedclientcert* to consistently be a per-directory setting only, matching most of the documentation and *example*s. pr 46541 [paul reder, eric covener] 2.3.6 

*) mod_ldap: *ldaptrustedclientcert* now accepts ca_der/ca_base64 argument types previously allowed only in *ldaptrustedglobalcert*. [eric covener] 2.3.6 

*) mod_ldap: eliminate a potential crash with multiple *ldaptrustedclientcert* when some are not password-protected. [eric covener] 2.3.6 

*) fix startup segfault when the *mutex* directive is used but no loaded modules use httpd *mutex*es.  pr 48787.  [jeff trawick] 2.3.6 

*) proxy: get the headers right in a head request with *proxyerroroverride*, by checking for an overridden error before not after going into a catch-all code path. pr 41646.  [nick kew, stuart children] 2.3.6 

*) mod_proxy_http: make sure that when an *errordocument* is served from a reverse proxied url, that the subrequest respects the status of the original request. this brings the behaviour of proxy_handler in line with default_handler. pr 47106. [graham leggett] 2.3.6 

*) apxs: fix -a and -a *options* to ignore whitespace in httpd.conf [philip m. gollucci] 2.3.6 

*) worker: don't report server has reached maxclients until it has. add message when server gets within *minsparethreads* of maxclients. pr 46996.  [dan poirier] 2.3.6 

*) mod_*session*: *session* expiry was being initialised, but not updated on each *session* save, resulting in timed out *session*s when there should not have been. fixed. [graham leggett] 2.3.6 

*) mod_log_*config*: add the r option to log the handler used within the request. [christian folini <christian.folini netnea com>] 2.3.6 

*) add new *undefine* directive to *undefine* a variable. pr 35350. [stefan fritsch] 2.3.6 

*) make ap_pregsub(), used by *alias*match and friends, use the same syntax for regex backreferences as mod_rewrite and mod_include: remove the use of '&' as an *alias* for '$0' and allow to escape any character with a backslash. pr 48351. [stefan fritsch] 2.3.6 

*) mod_authnz_ldap: if authldapcharset*config* is set, also convert the password to utf-8. pr 45318. [johannes müller <joh_m gmx.de>, stefan fritsch] 2.3.6 

*) turn static function get_server_name_for_url() into public ap_get_server_name_for_url() and use it where appropriate. this fixes mod_rewrite generating invalid urls for *redirect*s to ipv6 literal addresses. [stefan fritsch] 2.3.5 

*) mod_ldap: introduce new *config* option ldap*timeout* to set the *timeout* for ldap operations like bind and search. [stefan fritsch] 2.3.5 

*) mod_proxy, mod_proxy_ftp: move *proxyftpdircharset* from mod_proxy to mod_proxy_ftp. [takashi sato] 2.3.5 

*) mod_proxy, mod_proxy_connect: move *allowconnect* from mod_proxy to mod_proxy_connect. [takashi sato] 2.3.5 

*) mod_cache: do an exact match of the keys defined by *cacheignoreurl*session*identifiers* against the querystring instead of a partial match.  pr 48401. [dodou wang <wangdong.08 gmail.com>, ruediger pluem] 2.3.5 

*) core http: disable *keepalive* when the client has sent expect: 100-continue but we respond directly with a non-100 response. *keepalive* here led to data from clients continuing being treated as a new request. pr 47087 [nick kew] 2.3.5 

*) core: (re)-introduce -t commandline option to suppress *documentroot* check at startup. pr 41887 [jan van den berg <janvdberg gmail.com>] 2.3.5 

*) mod_autoindex: support xhtml as equivalent to html in index*options*, scanhtmltitles, *readmename*, *headername* pr 48416 [dmitry bakshaev <dab18 izhnet.ru>, nick kew] 2.3.5 

*) proxy: fix *proxypass*reverse with relative url derived (slightly erroneously) from pr 38864 [nick kew] 2.3.5 

*) replace accept*mutex*, lockfile, rewritelock, ssl*mutex*, sslstapling*mutex*, and watchdog*mutex*path with a single *mutex* directive.  add apis to simplify setup and user customization of apr proc and global *mutex*es. (see util_*mutex*.h.)  build-time setting default_lockfile is no longer respected; set default_rel_runtimedir instead.  [jeff trawick] 2.3.4 

*) http_core: *keepalive* no longer accepts other than on|off. [takashi sato] 2.3.4 

*) mod_authnz_ldap: add *authldapbindauthoritative* to allow authentication to try other providers in the case of an ldap bind failure. pr 46608 [justin erenkrantz, joe schaefer, tony stevenson] 2.3.4 

*) mod_dav_fs: remove inode keyed locking as this conflicts with atomically creating files. on systems with inode numbers, this is a format change of the *davlockdb*. the old *davlockdb* must be deleted on upgrade. [stefan fritsch] 2.3.3 

*) mod_log_*config*: make ${cookie}c correctly match whole cookie names instead of substrings. pr 28037. [dan franklin <dan dan-franklin.com>, stefan fritsch] 2.3.3 

*) mod_ldap: avoid 500 errors with "unable to set ldap_opt_refhoplimit option to 5" when built against openldap by using sdk ldap_opt_refhoplimit defaults unless *ldapreferralhoplimit* is explicitly *config*ured. [eric covener] 2.3.3 

*) mod_charset_lite: honor 'charset*options* noimplicitadd'. [eric covener] 2.3.3 

*) mod_socache_shmcb: allow parens in file name if cache size is given. fixes ssl*session*cache directive mis-parsing parens in pathname. pr 47945. [stefan fritsch] 2.3.3 

*) allow *proxypreservehost* to work in *<proxy*> sections. pr 34901. [stefan fritsch] 2.3.3 

*) *config*ure: fix threaded_mpms so that mod_cgid is enabled again for worker mpm. [takashi sato] 2.3.3 

*) mod_ldap: if *ldapsharedcachesize* is too small, try harder to purge some cache entries and log a warning. also increase the default *ldapsharedcachesize* to 500000. this is a more realistic size suitable for the default values of 1024 for *ldapcacheentries*/*ldapopcacheentries*. pr 46749. [stefan fritsch] 2.3.3 

*) mod_cache: teach *cacheenable* and *cachedisable* to work from within a location section, in line with how *proxypass* works. [graham leggett] 2.3.3 

*) mod_req*timeout*: new module to set *timeout*s and minimum data rates for receiving requests from the client. [stefan fritsch] 2.3.3 

*) mod_cache: fix uri_meets_conditions() so that *cacheenable* will match by scheme, or by a wildcarded hostname. pr 40169 [peter grandi <pg_asf asf.for.sabi.co.uk>, graham leggett] 2.3.3 

*) mod_mime: make *removetype* override the info from types*config*. pr 38330. [stefan fritsch] 2.3.3 

*) mod_cache: introduce the option to run the cache from within the normal request handler, and to allow fine grained control over where in the filter chain content is cached. adds *cachequickhandler* directive.  [graham leggett] 2.3.3 

*) core: treat *timeout* reading request as 408 error, not 400. log 408 errors in access log as was done in apache 1.3.x. pr 39785 [nobutaka mantani <nobutaka nobutaka.org>, stefan fritsch <sf fritsch.de>, dan poirier] 2.3.3 

*) mod_dav: allow other modules to add things to the dav or allow headers of an *options* request. [jari urpalainen <jari.urpalainen nokia.com>, brian france <brian brianfrance.com>] 2.3.3 

*) mod_mime: detect invalid use of *multiviewsmatch* inside location and locationmatch sections.  pr47754. [dan poirier] 2.3.3 

*) mod_request: make sure the *keptbodysize* directive rejects values that aren't valid numbers. [graham leggett] 2.3.3 

*) mod_*session*_crypto: sanity check should the potentially encrypted *session* cookie be too short. [graham leggett] 2.3.3 

*) mod_*session*.c: prevent a segfault when *session* is added but not *config*ured. [graham leggett] 2.3.3 

*) mod_auth_digest: fail server start when nonce count checking is *config*ured without shared memory, or md5-sess algorithm is *config*ured. [dan poirier] 2.3.3 

*) mod_ssl: the error message when *sslcertificatefile* is missing should at least give the name or position of the problematic virtual host definition. [stefan fritsch sf sfritsch.de] 2.3.3 

*) preserve port information over internal *redirect*s pr 35999 [jonas ringh <jonas.ringh cixit.se>] 2.3.3 

*) mod_autoindex: correctly create an empty cell if the de*script*ion for a file is missing. pr 47682 [peter poeml <poeml suse.de>] 2.3.3 

*) security: cve-2009-1890 (cve.mitre.org) fix a potential denial-of-service attack against mod_proxy in a reverse proxy *config*uration, where a remote attacker can force a proxy process to consume cpu time indefinitely.  [nick kew, joe orton] 2.3.3 

*) mod_*suexec*: correctly set *suexec*_enabled when httpd is run by a non-root user and may have insufficient permissions. pr 42175 [jim radford <radford blackbean.org>] 2.3.3 

*) mod_*alias*: ensure *redirect* issues a valid url. pr 44020 [håkon stordahl <hakon stordahl.org>] 2.3.3 

*) mod_dir: add *fallbackresource* directive, to enable admin to specify an *action* to happen when a url maps to no file, without resorting to *errordocument* or mod_rewrite.  pr 47184 [nick kew] 2.3.3 

*) mod_cgid: do not leak the *listen*ing unix socket file de*script*or to the cgi process. pr 47335 [kornél pál <kornelpal gmail.com>] 2.3.3 

*) mod_*alias*: check sanity in *redirect* arguments. pr 44729 [sönke tesch <st kino-fahrplan.de>, jim jagielski] 2.3.3 

*) mod_cache: add *cacheignoreurl*session*identifiers* directive to ignore defined *session* identifiers encoded in the url when caching. [ruediger pluem] 2.3.3 

*) mod_rewrite: fix the error string returned by *rewriterule*. *rewriterule* returned "*rewritecond*: bad flag delimiters" when the 3rd argument of *rewriterule* was not started with "[" or not ended with "]". pr 45082 [vitaly polonetsky <m_vitaly topixoft.com>] 2.3.3 

*) mod_dbd: add *dbdinitsql* directive to enable sql statements to be run when a connection is opened.  pr 46827 [marko kevac <mkevac gmail.com>] 2.3.3 

*) mod_cgid: improve handling of long af_unix socket names (*script*sock). pr 47037.  [jeff trawick] 2.3.3 

*) mod_proxy_ajp: check more strictly that the backend follows the ajp *protocol*. [mladen turk] 2.3.3 

*) mod_ssl: add *sslproxycheckpeerexpire* and *sslproxycheckpeercn* directives to enable stricter checking of remote server certificates. [ruediger pluem] 2.3.3 

*) mod_proxy_ftp: add *proxyftplistonwildcard* directive to allow files with globbing characters to be retrieved instead of converted into a directory listing.  pr 46789 [dan poirier <poirier pobox.com>] 2.3.3 

*) mod_*substitute*: fix a memory leak. pr 44948 [dan poirier <poirier pobox.com>] 2.3.2 

*) mod_disk_cache: the module now turns off sendfile support if '*enablesendfile* off' is defined globally. [lars eilebrecht] 2.3.2 

*) disabled *defaulttype* directive and removed ap_default_type() from core.  we now exclude content-type from responses for which a media type has not been *config*ured via mime.types, *addtype*, *forcetype*, or some other mechanism. pr 13986. [roy t. fielding] 2.3.2 

*) mod_rewrite: add ipv6 variable to *rewritecond* [ryan phillips <ryan-apache trolocsis.com>] 2.3.2 

*) core: enhance *keepalive**timeout* to support a value in milliseconds. pr 46275. [takashi sato] 2.3.2 

*) mod_ssl: fix merging of sslreneg*buffersize* directive. pr 46508 [<tlhackque yahoo.com>] 2.3.2 

*) prefork: fix child process hang during graceful restart/stop in *config*urations with multiple *listen*ing sockets.  pr 42829.  [joe orton, jeff trawick] 2.3.2 

*) mod_*session*_crypto: ensure that *session*cryptodriver can only be set in the global scope. [graham leggett] 2.3.2 

*) mod_ext_filter: we need to detect failure to startup the filter program (a mangled response is not acceptable).  fix to detect failure, and offer *config*uration option either to abort or to remove the filter and continue. pr 41120 [nick kew] 2.3.2 

*) mod_*session*_crypto: rewrite the *session*_crypto module against the apr_crypto api. [graham leggett] 2.3.2 

*) cgi: return 504 (gateway *timeout*) rather than 500 when a *script* times out before returning status line/headers. pr 42190 [nick kew] 2.3.1 

*) mod_cgid: do not add an empty argument when calling the cgi *script*. pr 46380 [ruediger pluem] 2.3.1 

*) mod_ssl: add sslreneg*buffersize* directive to allow changing the size of the buffer used for the request-body where necessary during a per-dir renegotiation.  pr 39243.  [joe orton] 2.3.1 

*) mod_ssl: improve environment variable extr*action* to be more efficient and to correctly handle dns with duplicate tags. pr 45975.  [joe orton] 2.3.1 

*) remove the obsolete serial attribute from the rpm spec file. compile against the external pcre. add missing binaries fcgistarter, and mod_socache* and mod_*session**. [graham leggett] 2.3.0 

*) rename apis to include ap_ prefix: find_child_by_pid -> ap_find_child_by_pid suck_in_apr -> ap_suck_in_apr sys_privileges_handlers -> ap_sys_privileges_handlers unixd_accept -> ap_unixd_accept unixd_*config* -> ap_unixd_*config* unixd_killpg -> ap_unixd_killpg unixd_set_global_*mutex*_perms -> ap_unixd_set_global_*mutex*_perms unixd_set_proc_*mutex*_perms -> ap_unixd_set_proc_*mutex*_perms unixd_set_rlimit -> ap_unixd_set_rlimit [paul querna] 2.3.0 

*) mod_privileges: new module to make httpd on solaris privileges-aware and to enable different virtualhosts to run with different privileges and unix user/*group* ids [nick kew] 2.3.0 

*) authz: fix handling of authz *config*urations, make default authz logic replicate 2.2.x authz logic, and replace <*satisfy**>, reject, and authzmergerules directives with match, <match*>, and authzmerge directives.  [chris darroch] 2.3.0 

*) mod_authn_core: prevent crash when provider *alias* created to provider which is not yet registered.  [chris darroch] 2.3.0 

*) mod_authn_core: add *authtype* of none to support disabling authentication.  [chris darroch] 2.3.0 

*) core: allow *<limit*> and *<limit*except> directives to nest, and constrain their use to conform with that of other access control and authorization directives.  [chris darroch] 2.3.0 

*) unixd: turn existing code into a module, and turn the set user/*group* and chroot into a child_init function. [nick kew] 2.3.0 

*) mod_dir: support "*directoryindex* disabled" suggested by andré warnier <aw ice-sa.com> [eric covener] 2.3.0 

*) mod_*session*_cookie, mod_*session*_dbd: make sure cookies are set both within the output headers and error output headers, so that the *session* is maintained across *redirect*s. [graham leggett] 2.3.0 

*) mod_*session*_cookie: make sure that cookie attributes are correctly included in the blank cookie when cookies are removed. this fixes an inability to log out when using mod_auth_form. [graham leggett] 2.3.0 

*) mod_*session*: prevent a segfault when a cgi *script* sets a cookie with a null value. [david shane holden <dpejesh apache.org>] 2.3.0 

*) core: when testing for slash-terminated *config*uration paths in ap_location_walk(), don't look past the start of an empty string such as that created by a *<location* ""> directive. [chris darroch] 2.3.0 

*) move the *keptbodysize* directive, kept_body filters and the ap_parse_request_body function out of the http module and into a new module called mod_request, reducing the size of the core. [graham leggett] 2.3.0 

*) mod_dbd: handle integer *config*uration directive parameters with a dedicated function. 2.3.0 

*) change the directives within the mod_*session** modules to be valid both inside and outside the location/directory sections, as suggested by wrowe. [graham leggett] 2.3.0 

*) mod_auth_form: add a module capable of allowing end users to log in using an html form, storing the credentials within mod_*session*. [graham leggett] 2.3.0 

*) mod_*session*_crypto: initialise ssl in the post *config* hook. [ruediger pluem, graham leggett] 2.3.0 

*) mod_*session*_dbd: add a *session* implementation capable of storing *session* information in a sql database via the dbd interface. useful for sites where *session* privacy is important. [graham leggett] 2.3.0 

*) mod_*session*_crypto: add a *session* encoding implementation capable of encrypting and decrypting *session*s wherever they may be stored. introduces a level of privacy when *session*s are stored on the browser. [graham leggett] 2.3.0 

*) mod_*session*_cookie: add a *session* implementation capable of storing *session* information within cookies on the browser. useful for high volume sites where server bound *session*s are too resource intensive. [graham leggett] 2.3.0 

*) mod_*session*: add a generic *session* interface to unify the different attempts at saving persistent *session*s across requests. [graham leggett] 2.3.0 

*) core, authn/z: avoid calling access control hooks for internal requests with *config*urations which match those of initial request.  revert to original behaviour (call access control hooks for internal requests with uris different from initial request) if any access control hooks or providers are not registered as permitting this optimization. introduce wrappers for access control hook and provider registration which can accept additional mode and flag data.  [chris darroch] 2.3.0 

*) mod_authz_dbd: when *redirect*ing after successful login/logout per authzdbd*redirect*query, do not report authorization failure, and use first row returned by database query instead of last row. [chris darroch] 2.3.0 

*) mod_dir, mod_negotiation: pass the output filter information to newly created sub requests; as these are later on used as true requests with an internal *redirect*. this allows for mod_cache et.al. to trap the results of the *redirect*. [dirk-willem van gulik, ruediger pluem] 2.3.0 

*) core: add the option to keep aside a request body up to a certain size that would otherwise be discarded, to be consumed by filters such as mod_include. when enabled for a directory, post requests to shtml files can be passed through to embedded *script*s as post requests, rather being downgraded to get requests. [graham leggett] 2.3.0 

*) mod_ldap, mod_authnz_ldap: add support for nested *group*s (i.e. the ability to authorize an authenticated user via a "require ldap-*group* x" directive where the user is not in *group* x, but is in a sub*group* contained in x. pr 42891 [paul j. reder] 2.3.0 

*) mod_ssl: add support for caching ssl *session*s in memcached. [paul querna] 2.3.0 

*) the lockfile directive, which specifies the location of the accept() *mutex* lockfile, is deprecated. instead, the accept*mutex* directive now takes an optional lockfile location parameter, ala ssl*mutex*. [jim jagielski] 2.3.0 

*) mod_rewrite: support *rewritemap* by sql query [nick kew] 2.3.0 

*) ap_get_server_version() has been removed.  third-party modules must now use ap_get_server_banner() or ap_get_server_de*script*ion(). [jeff trawick] 2.3.0 

*) all mpms: introduce a check_*config* phase between pre_*config* and open_logs, to allow modules to review interdependent *config*uration directive values and adjust them while messages can still be logged to the console.  handle relevant mpm directives during this phase and format messages for both the console and the error log, as appropriate.  [chris darroch] 2.3.0 

*) core: do not allow internal *redirect*s like the *directoryindex* of mod_dir to circumvent the symbolic link checks imposed by followsymlinks and symlinksifownermatch. [nick kew, ruediger pluem, william rowe] 2.3.0 

*) new ssl*loglevel*debugdump [ none (default) | io (not bytes) | bytes ] *config*ures the i/o dump of ssl traffic, when *loglevel* is set to debug. the default is none as this is far greater debugging resolution than the typical administrator is prepared to untangle.  [william rowe] 2.3.0 

*) mod_disk_cache: if possible, check if the size of an object to cache is within the *config*ured boundaries before actually saving data. [niklas edmundsson <nikke acc.umu.se>] 2.3.0 

*) authz: add the new module mod_authn_core that will provide common authn directives such as '*authtype*', '*authname*'.  move the directives '*authtype*' and '*authname*' out of the core module and merge mod_authz_*alias* into mod_authn_core. [brad nicholes] 2.3.0 

*) authz: move the directives 'order', 'allow', 'deny' and '*satisfy*' into the new module mod_access_compat which can be loaded to provide support for these directives. [brad nicholes] 2.3.0 

*) authz: move the 'require' directive from the core module as well as add the directives '<*satisfy*all>', '<*satisfy*one>', '<require*alias*>' and 'reject' to mod_authz_core. the new directives introduce 'and/or' logic into the authorization processing. [brad nicholes] 2.3.0 

*) authz: renamed mod_authz_dbm authz providers from '*group*' and 'file-*group*' to 'dbm-*group*' and 'dbm-file-*group*'. [brad nicholes] 2.3.0 

*) mod_cache: add *cacheminexpire* directive to set the minimum time in seconds to cache a document. [brian akins <brian.akins turner.com>, ruediger pluem] 2.3.0 

*) mod_authz_dbd: sql authz with login/*session* support [nick kew] 2.3.0 

*) fix typo in *proxystatus* syntax error message. [christophe jaillet <christophe.jaillet wanadoo.fr>] 2.3.0 

*) teach mod_ssl to use arbitrary oids in an *sslrequire* directive, allowing string-valued client certificate attributes to be used for access control, as in: *sslrequire* "value" in oid("1.3.6.1.4.1.18060.1") [martin kraemer, david reid] [apache 2.3.0-dev includes those bug fixes and changes with the apache 2.2.xx tree as documented, and except as noted, below.] 2.2.x and later: 

*) security: cve-2014-0118 (cve.mitre.org) mod_deflate: the deflate input filter (inflates request bodies) now limits the length and compression ratio of inflated request bodies to avoid denial of service via highly compressed bodies.  see directives deflateinflate*limitrequestbody*, deflateinflateratiolimit, and deflateinflateratioburst. [yann ylavic, eric covener] 2.2.28 

*) security: cve-2014-0231 (cve.mitre.org) mod_cgid: fix a denial of service against cgi *script*s that do not consume stdin that could lead to lingering httpd child processes filling up the scoreboard and eventually hanging the server.  by default, the client i/o *timeout* (*timeout* directive) now applies to communication with *script*s.  the cgid*script**timeout* directive can be used to set a different *timeout* for communication with *script*s. [rainer jung, eric covener, yann ylavic] 2.2.28 

*) mod_ssl: extend the scope of ssl*session*cache*timeout* to *session*s resumed by tls *session* resumption (rfc 5077). [rainer jung] 2.2.28 

*) mod_cache, mod_disk_cache: with *cachelock* enabled, responses with a vary header might not get the benefit of the thundering herd protection due to an incorrect internal cache key.  pr 50317. [ruediger pluem, jan kaluza, yann ylavic] 2.2.28 

*) mod_rewrite: support *session* cookies with the co= flag when later parameters are used.  the doc for this implied the feature had been backported for quite some time.  pr56014 [eric covener] 2.2.28 

*) mod_proxy: remove (never documented) *<proxy* ~ wildcard-url> syntax which is equivalent to *<proxy*match wildcard-url>. [christophe jaillet] 2.2.27 

*) mod_ssl: change default for *sslcompression* to off, as compression causes security issues in most setups. (the so called "crime" attack). [stefan fritsch] 2.2.26 

*) security: cve-2013-1896 (cve.mitre.org) mod_dav: sending a merge request against a uri handled by mod_dav_svn with the source href (sent as part of the request body as xml) pointing to a uri that is not *config*ured for dav will trigger a segfault. [ben reser <ben reser.org>] 2.2.25 

*) core: support the single_*listen*_unserialized_accept optimization on linux kernel versions 3.x and above.  pr 55121.  [bradley heilbrun <apache heilbrun.org>] 2.2.25 

*) mod_*setenv*if: log error on substitution overflow. [stefan fritsch] 2.2.25 

*) mod_ssl: catch missing, mismatched or encrypted client cert/key pairs with *sslproxymachinecertificatefile*/path directives. pr 52212, pr 54698. [keith burdis <keith burdis.org>, joe orton, kaspar brand] 2.2.25 

*) mod_proxy_balancer: added balancer parameter failon*timeout* to allow server admin to *config*ure an io *timeout* as an error in the balancer. [daniel ruggeri] 2.2.25 

*) mod_dav: ensure uri is correctly uriencoded on return. pr 54611 [timothy wood <tjw omni*group*.com>] 2.2.25 

*) mod_dav: make sure that when we prepare an if url for etag comparison, we compare unencoded paths. pr 53910 [timothy wood <tjw omni*group*.com>] 2.2.25 

*) mod_dav: sending an if or if-match header with an invalid etag doesn't result in a 412 precondition failed for a copy operation. pr54610 [timothy wood <tjw omni*group*.com>] 2.2.25 

*) mod_rewrite: stop merging *rewritebase* down to subdirectories unless new option 'rewrite*options* mergebase' is *config*ured. merging *rewritebase* was unconditionally turned on in 2.2.23. pr 53963. [eric covener] 2.2.24 

*) mod_dir: add support for the value 'disabled' in *fallbackresource*. [vincent deffontaines] 2.2.24 

*) ab: add tls1.1/tls1.2 *options* to -f switch, and adapt output to more accurately report the negotiated *protocol*. pr 53916. [nicolás pernas maradei <nico e*mutex* com>, kaspar brand] 2.2.24 

*) core: use a tls 1.0 close_notify alert for internal dummy connection if the chosen *listen*er is *config*ured for https. [joe orton] 2.2.24 

*) mod_ssl: add new directive *sslcompression* to disable tls-level compression. pr 53219. [björn jacke <bjoern j3e de>, stefan fritsch] 2.2.23 

*) core: fix error handling in ap_scan_*script*_header_err_brigade() if there is no eos bucket in the brigade. pr 48272. [stefan fritsch] 2.2.23 

*) core: prevent "httpd -k restart" from killing server in presence of *config* error. [joe orton] 2.2.23 

*) mod_ssl: when compiled against openssl 1.0.1 or later, allow explicit control of tlsv1.1 and tlsv1.2 through the ssl*protocol* directive, adding tlsv1.1 and tlsv1.2 support by default given 'ssl*protocol* all'. [kaspar brand, william rowe] 2.2.23 

*) mod_log_*config*: fix %{abc}c truncating cookie values at first "=". pr 53104. [greg ames] 2.2.23 

*) mod_proxy_ajp: add support for '*proxyerroroverride* on'. pr 50945. [peter pramberger <peter pramberger.at>, jim jagielski] 2.2.23 

*) added *sslproxymachinecertificatechainfile* directive so the proxy client can select the proper client certificate when using a chain and the remote server only lists the root ca as allowed. 2.2.23 

*) mod_rewrite: fix the *rewriteengine* directive to work within a location. previously, once *rewriteengine* was switched on globally, it was impossible to switch off. [graham leggett] 2.2.23 

*) core: adjust ap_scan_*script*_header_err*() to prevent mod_cgi and mod_cgid from logging bogus data in case of errors. [stefan fritsch] 2.2.23 

*) *config*ure: fix usage with external apr and apu in non-default paths and recent gcc versions >= 4.6. [jean-frederic clere] 2.2.23 

*) security: cve-2011-3368 (cve.mitre.org) reject requests where the request-uri does not match the http specification, preventing unexpected expansion of target urls in some reverse proxy *config*urations.  [joe orton] 2.2.22 

*) security: cve-2011-3607 (cve.mitre.org) fix integer overflow in ap_pregsub() which, when the mod_*setenv*if module is enabled, could allow local users to gain privileges via a .htaccess file. [stefan fritsch, greg ames] 2.2.22 

*) security: cve-2011-4317 (cve.mitre.org) resolve additional cases of url rewriting with *proxypass*match or *rewriterule*, where particular request-uris could result in undesired backend network exposure in some *config*urations. [joe orton] 2.2.22 

*) security: cve-2012-0021 (cve.mitre.org) mod_log_*config*: fix segfault (crash) when the '%{*cookiename*}c' log format string is in use and a client sends a nameless, valueless cookie, causing a denial of service. the issue existed since version 2.2.17. pr 52256. [rainer canavan <rainer-apache 7val com>] 2.2.22 

*) security: cve-2012-0053 (cve.mitre.org) fix an issue in error responses that could expose "httponly" cookies when no custom *errordocument* is specified for status code 400. [eric covener] 2.2.22 

*) *config*: update the default mod_ssl *config*uration: disable sslv2, only allow >= 128bit ciphers, add commented *example* for speed optimized cipher list, limit msie workaround to msie <= 5. [kaspar brand] 2.2.22 

*) mod_log_*config*: prevent segfault. pr 50861. [torsten f�rtsch <torsten.foertsch gmx.net>] 2.2.22 

*) *example* *config*uration: fix entry for *maxranges* (use "unlimited" instead of "0").  [rainer jung] 2.2.22 

*) mod_*substitute*: fix buffer overrun.  [ruediger pluem, rainer jung] 2.2.21 

*) mod_*alias*: adjust log severity of "incomplete *redirect*ion target" message. pr 44020. 2.2.21 

*) mod_rewrite: check validity of each internal (int:) *rewritemap* even if the *rewriteengine* is disabled in server context, avoiding a crash while referencing the invalid int: map at runtime. pr 50994. [ben noordhuis <info noordhuis nl>] 2.2.21 

*) core: allow *maxranges* none|unlimited|default and set 'accept-ranges: none' in the case ranges are being ignored with *maxranges* none. [eric covener] 2.2.21 

*) mod_filter: fix *filterprovider* conditions of type "resp=" (response headers) for cgi. [joe orton, rainer jung] 2.2.20 

*) mod_req*timeout*: fix a timed out connection going into the keep-alive state after a *timeout* when discarding a request body. pr 51103. [stefan fritsch] 2.2.20 

*) core: do the hook sorting earlier so that the hooks are properly sorted for the pre_*config* hook and during parsing the *config*. [stefan fritsch] 2.2.19 

*) log an error for failures to read a chunk-size, and return 408 instead 413 when this is due to a read *timeout*.  this change also fixes some cases of two error documents being sent in the response for the same scenario. [eric covener] pr49167 2.2.18 

*) core: only log a 408 if it is no *keepalive* *timeout*. pr 39785 [ruediger pluem,  mark montague <markmont umich.edu>] 2.2.18 

*) core: treat *timeout* reading request as 408 error, not 400. log 408 errors in access log as was done in apache 1.3.x. pr 39785 [nobutaka mantani <nobutaka nobutaka.org>, stefan fritsch, dan poirier] 2.2.18 

*) core http: disable *keepalive* when the client has sent expect: 100-continue but we respond directly with a non-100 response.  *keepalive* here led to data from clients continuing being treated as a new request. pr 47087.  [nick kew] 2.2.18 

*) mod_win32: added shebang check for '! so that .vbs *script*s work as cgi. win32's c*script* interpreter can only use a single quote as comment char. [guenter knauf] 2.2.18 

*) *config*ure: fix htpasswd/htdbm libcrypt link errors with some newer linkers. [stefan fritsch] 2.2.18 

*) core: *allowencodedslashes* new option nodecode to allow encoded slashes in request url path info but not decode them. pr 35256, pr 46830.  [dan poirier] 2.2.18 

*) *suexec*: add *suexec* directive to disable *suexec* without renaming the binary (*suexec* off), or force startup failure if *suexec* is required but not supported (*suexec* on).  [jeff trawick] 2.2.18 

*) mod_autoindex: merge index*options* from server to directory context when the directory has no mod_autoindex directives. pr 47766. [eric covener] 2.2.18 

*) mod_*userdir*: add merging of enable, disable, and filename arguments to *userdir* directive, leaving enable/disable of userlists unmerged. pr 44076 [eric covener] 2.2.18 

*) core: honor '*acceptpathinfo* off' during internal *redirect*s, such as per-directory mod_rewrite substitutions.  pr 50349. [eric covener] 2.2.18 

*) mod_req*timeout*: do not wrongly enforce *timeout*s for mod_proxy's backend connections and other *protocol* handlers (like mod_ftp). enforce the *timeout* for ap_mode_getline. if there is a *timeout*, shorten the lingering close time from 30 to 2 seconds. [stefan fritsch] 2.2.17 

*) mod_authnz_ldap: if authldapcharset*config* is set, also convert the password to utf-8. pr 45318. [johannes müller <joh_m gmx.de>, stefan fritsch] 2.2.17 

*) mod_log_*config*: make ${cookie}c correctly match whole cookie names instead of substrings. pr 28037. [dan franklin <dan dan-franklin.com>, stefan fritsch] 2.2.17 

*) mod_dir, mod_negotiation: pass the output filter information to newly created sub requests; as these are later on used as true requests with an internal *redirect*. this allows for mod_cache et.al. to trap the results of the *redirect*. pr 17629, 43939 [dirk-willem van gulik, jim jagielski, joe orton, ruediger pluem] 2.2.17 

*) rotatelogs: fix possible buffer overflow if admin *config*ures a mongo log file path. [jeff trawick] 2.2.17 

*) core: (re)-introduce -t commandline option to suppress *documentroot* check at startup. pr 41887 [jan van den berg <janvdberg gmail.com>] 2.2.16 

*) security: cve-2010-2068 (cve.mitre.org) mod_proxy_ajp, mod_proxy_http, mod_req*timeout*: fix *timeout* detection for platforms windows, netware and os2.  pr: 49417. [rainer jung] 2.2.16 

*) apxs: fix -a and -a *options* to ignore whitespace in httpd.conf [philip m. gollucci] 2.2.16 

*) mod_dir: add *fallbackresource* directive, to enable admin to specify an *action* to happen when a url maps to no file, without resorting to *errordocument* or mod_rewrite.  pr 47184 [nick kew] 2.2.16 

*) security: cve-2009-3555 (cve.mitre.org) mod_ssl: comprehensive fix of the tls renegotiation prefix injection attack when compiled against openssl version 0.9.8m or later. introduces the '*sslinsecurerenegotiation*' directive to reopen this vulnerability and offer unsafe legacy renegotiation with clients which do not yet support the new secure renegotiation *protocol*, rfc 5746. [joe orton, and with thanks to the openssl team] 2.2.15 

*) security: cve-2009-3555 (cve.mitre.org) mod_ssl: a partial fix for the tls renegotiation prefix injection attack for openssl versions prior to 0.9.8l; reject any client-initiated renegotiations. forcibly disable *keepalive* for the connection if there is any buffered data readable. any *config*uration which requires renegotiation for per-directory/location access control is still vulnerable, unless using openssl 0.9.8l or later. [joe orton, ruediger pluem, hartmut keil <hartmut.keil adnovum.ch>] 2.2.15 

*) mod_req*timeout*: new module to set *timeout*s and minimum data rates for receiving requests from the client. [stefan fritsch] 2.2.15 

*) mod_proxy_http: make sure that when an *errordocument* is served from a reverse proxied url, that the subrequest respects the status of the original request. this brings the behaviour of proxy_handler in line with default_handler. pr 47106. [graham leggett] 2.2.15 

*) mod_log_*config*: add the r option to log the handler used within the request. [christian folini <christian.folini netnea com>] 2.2.15 

*) mod_ssl: fix a potential i/o hang if a long list of trusted cas is *config*ured for client cert auth. pr 46952.  [joe orton] 2.2.15 

*) mod_authnz_ldap: add *authldapbindauthoritative* to allow authentication to try other providers in the case of an ldap bind failure. pr 46608.  [justin erenkrantz, joe schaefer, tony stevenson] 2.2.15 

*) worker: don't report server has reached maxclients until it has. add message when server gets within *minsparethreads* of maxclients. pr 46996.  [dan poirier] 2.2.15 

*) core: preserve port information over internal *redirect*s pr 35999.  [jonas ringh <jonas.ringh cixit.se>] 2.2.15 

*) mod_filter: fix *filterprovider* matching where "dispatch" string doesn't exist. pr 48054.  [<tietew gmail.com>] 2.2.15 

*) mod_mime: make *removetype* override the info from types*config*. pr 38330.  [stefan fritsch] 2.2.15 

*) mod_charset_lite: honor 'charset*options* noimplicitadd'. [eric covener] 2.2.15 

*) mod_ldap: if *ldapsharedcachesize* is too small, try harder to purge some cache entries and log a warning. also increase the default *ldapsharedcachesize* to 500000. this is a more realistic size suitable for the default values of 1024 for *ldapcacheentries*/*ldapopcacheentries*. pr 46749.  [stefan fritsch] 2.2.15 

*) mod_mime: detect invalid use of *multiviewsmatch* inside location and locationmatch sections.  pr 47754.  [dan poirier] 2.2.15 

*) mod_ldap: don't try to resolve file-based user ids to a dn when *authldapurl* has been defined at a very high level.  pr 45946.  [eric covener] 2.2.14 

*) mod_ldap: bring the *ldapcacheentries* and *ldapopcacheentries* usage() in synch with the manual and the implementation (0 and -1 both disable the cache). [eric covener] 2.2.14 

*) mod_ssl: the error message when *sslcertificatefile* is missing should at least give the name or position of the problematic virtual host definition. [stefan fritsch sf sfritsch.de] 2.2.14 

*) mod_cache: add *cacheignoreurl*session*identifiers* directive to ignore defined *session* identifiers encoded in the url when caching. [ruediger pluem] 2.2.14 

*) mod_autoindex: correctly create an empty cell if the de*script*ion for a file is missing. pr 47682 [peter poeml <poeml suse.de>] 2.2.13 

*) mod_cgid: do not add an empty argument when calling the cgi *script*. pr 46380 [ruediger pluem] 2.2.13 

*) security: cve-2009-1195 (cve.mitre.org) prevent the "includes" option from being enabled in an .htaccess file if the *allowoverride* restrictions do not permit it. [jonathan peatfield <j.s.peatfield damtp.cam.ac.uk>, joe orton, ruediger pluem, jeff trawick] 2.2.12 

*) security: cve-2009-1890 (cve.mitre.org) fix a potential denial-of-service attack against mod_proxy in a reverse proxy *config*uration, where a remote attacker can force a proxy process to consume cpu time indefinitely.  [nick kew, joe orton] 2.2.12 

*) security: cve-2009-0023, cve-2009-1955, cve-2009-1956 (cve.mitre.org) the bundled copy of the apr-util library has been updated, fixing three different security issues which may affect particular *config*urations and third-party modules. 2.2.12 

*) mod_*alias*: check sanity in *redirect* arguments. pr 44729 [sönke tesch <st kino-fahrplan.de>, jim jagielski] 2.2.12 

*) mod_*alias*: ensure *redirect* emits http-compliant urls. pr 44020 2.2.12 

*) mod_rewrite: fix the error string returned by *rewriterule*. *rewriterule* returned "*rewritecond*: bad flag delimiters" when the 3rd argument of *rewriterule* was not started with "[" or not ended with "]". pr 45082 [vitaly polonetsky <m_vitaly topixoft.com>] 2.2.12 

*) mod_proxy: complete *proxypass*reverse to handle balancer url's.  given; *balancermember* balancer://*alias* http://*example*.com/foo *proxypass*reverse /bash balancer://*alias*/bar backend url http://*example*.com/foo/bar/that is now translated /bash/that [william rowe] 2.2.12 

*) mod_proxy_ajp: check more strictly that the backend follows the ajp *protocol*. [mladen turk] 2.2.12 

*) mod_ssl: add *sslproxycheckpeerexpire* and *sslproxycheckpeercn* directives to enable stricter checking of remote server certificates. [ruediger pluem] 2.2.12 

*) mod_*substitute*: fix a memory leak. pr 44948 [dan poirier <poirier pobox.com>] 2.2.12 

*) mod_disk_cache/mod_mem_cache: fix handling of *cacheignoreheaders* directive to correctly remove headers before storing them. [lars eilebrecht] 2.2.12 

*) mod_disk_cache: the module now turns off sendfile support if '*enablesendfile* off' is defined globally. pr 41218. [lars eilebrecht, issac goldstand] 2.2.12 

*) prefork: fix child process hang during graceful restart/stop in *config*urations with multiple *listen*ing sockets.  pr 42829.  [joe orton, jeff trawick] 2.2.12 

*) mod_ssl: add sslreneg*buffersize* directive to allow changing the size of the buffer used for the request-body where necessary during a per-dir renegotiation.  pr 39243.  [joe orton] 2.2.12 

*) cgi: return 504 (gateway *timeout*) rather than 500 when a *script* times out before returning status line/headers. pr 42190 [nick kew] 2.2.12 

*) mod_ext_filter: fix error handling when the filter prog fails to start, and introduce an onfail *config*uration option to abort the request or to remove the broken filter and continue. pr 41120 [nick kew] 2.2.12 

*) set *listen* *protocol* to "https" if port is set to 443 and no proto is specified (as documented but not implemented). pr 46066 [dan poirier <poirier pobox.com>] 2.2.12 

*) *config*ure: don't reject libtool 2.x pr 44817 [arfrever frehtes taifersar arahesis <arfrever.fta gmail.com>] 2.2.11 

*) mod_autoindex: add *config*uration option to insert string in html head (*indexheadinsert*). [nick kew] 2.2.11 

*) add new *logformat* parameter, %k, which logs the number of *keepalive* requests on this connection for this request. pr 45762 [dan poirier <poirier pobox.com>, jim jagielski] 2.2.11 

*) build: correctly set ssl_libs during openssl detection if pkg*config* is not available. pr 46018 [ruediger pluem] 2.2.11 

*) mod_info: was displaying the wrong value for the *keepalive**timeout* value. [jim jagielski] 2.2.11 

*) core: add ap_*timeout*_parameter_parse to public api. [ruediger pluem] 2.2.11 

*) mod_proxy: add the possibility to set the worker parameters connection*timeout* and ping in milliseconds. [ruediger pluem] 2.2.11 

*) mod_proxy_http: don't trigger a retry by the client if a failure to read the response line was the result of a *timeout*. [adam woodworth <mirkperl gmail.com>] 2.2.10 

*) mod_ssl: implement dynamic *mutex* callbacks for the benefit of openssl.  [sander temme] 2.2.10 

*) mod_authn_*alias*: detect during startup when *authdigestprovider* is *config*ured to use an incompatible provider via authnprovider*alias*. pr 45196 [eric covener] 2.2.10 

*) mod_proxy: add 'scolonpathdelim' parameter to allow for ';' to also be used as a *session* path separator/delim  pr 45158. [jim jagielski] 2.2.10 

*) mod_proxy: add connection*timeout* parameter for proxy workers in order to be able to set the *timeout* for connecting to the backend separately. pr 45445. [ruediger pluem, rahul <rahul sun.com>] 2.2.10 

*) core: fix address-in-use startup failure on some platforms caused by creating an ipv4 *listen*er which overlaps with an existing ipv6 *listen*er.  [jeff trawick] 2.2.9 

*) core: add the filename of the *config*uration file to the warning message about the useless use of *allowoverride*. pr 39992. [darryl miles <darryl darrylmiles.org>] 2.2.9 

*) *suexec*: when *group* is given as a numeric gid, validate it by looking up the actual *group* name such that the name can be used in log entries. pr 7862 [<y-koga apache.or.jp>, leif w <warp-9.9 usa.net>] 2.2.9 

*) ab: include *<limit*s.h> earlier if available since we may need int_max (defined there on windows) for the definition of max_requests. pr 45024 [ruediger pluem] 2.2.9 

*) core: do not allow *options* all if not all *options* are allowed to be overwritten. pr 44262 [michał grzędzicki <lazy iq.pl>] 2.2.9 

*) http_filters: don't return 100-continue on *redirect*s. pr 43711 [ruediger pluem] 2.2.9 

*) core: reinstate location walk to fix *config* for subrequests pr 41960 [jose kahan <jose w3.org>] 2.2.9 

*) rotatelogs: log the current file size and error code/de*script*ion when failing to write to the log file.  [jeff trawick] 2.2.9 

*) mod_cgid: explicitly set permissions of the socket (*script*sock) shared by mod_cgid and request processing threads, for os'es such as hpux and aix that do not use umask for af_unix socket permissions. [eric covener, jeff trawick] 2.2.9 

*) mod_log_*config*: add format *options* for %p so that the actual local or remote port can be logged.  pr 43415.  [adam hasselbalch hansen <ahh@one.com>, ruediger pluem, jeff trawick] 2.2.9 

*) added 'disablereuse' option for *proxypass* which, essentially, disables connection pooling for the backend servers. [jim jagielski] 2.2.9 

*) mod_speling: remove regression from 1.3/2.0 behavior and drop dependency between mod_speling and *acceptpathinfo*. pr 43562 [jose kahan <jose w3.org>] 2.2.9 

*) mod_*substitute*: the default is now flattening the buckets after each substitution. the newly added 'q' flag allows for the quicker, more efficient bucket-splitting if the user so desires. [jim jagielski] 2.2.9 

*) *proxypass*reverse is now balancer aware. [jim jagielski] 2.2.9 

*) mod_charset_lite: add translateallmimetypes sub-option to charset*options*, allowing the administrator to skip the mimetype checking that precedes translation. pr 44458 [eric covener] 2.2.9 

*) winnt_mpm: resolve modperl issues by *redirect*ing console mode stdout to /device/nul as the server is starting up, mirroring unix mpm's. pr: 43534  [tom donovan <tom.donovan acm.org>, william rowe] 2.2.8 

*) security: cve-2007-6421 (cve.mitre.org) mod_proxy_balancer: correctly escape the worker route and the worker *redirect* string in the html output of the balancer manager. reported by securityreason. [ruediger pluem] 2.2.7 (not released) 

*) security: cve-2007-6388 (cve.mitre.org) mod_status: ensure refresh parameter is numeric to prevent a possible xss attack caused by *redirect*ing to other urls. reported by securityreason.  [mark cox, joe orton] 2.2.7 (not released) 

*) security: cve-2007-5000 (cve.mitre.org) mod_imagemap: fix a cross-site *script*ing issue.  reported by jpcert. [joe orton] 2.2.7 (not released) 

*) security: cve-2008-0005 (cve.mitre.org) introduce the *proxyftpdircharset* directive, allowing the administrator to identify a default, or specific servers or paths which list their contents in other-than iso-8859-1 charset (e.g. utf-8). [ruediger pluem] 2.2.7 (not released) 

*) mod_ssl: fix handling of the buffered request body during a per-location renegotiation, when an internal *redirect* occurs.  pr 43738. [joe orton] 2.2.7 (not released) 

*) mod_ldap: try to establish a new backend ldap connection when the microsoft ldap client library returns ldap_unavailable, e.g. after the ldap server has closed the connection due to a *timeout*. pr 39095 [eric covener] 2.2.7 (not released) 

*) add explicit charset to the output of various modules to work around possible cross-site *script*ing flaws affecting web browsers that do not derive the response character set as required by  rfc2616.  one of these reported by securityreason [joe orton] 2.2.7 (not released) 

*) http_*protocol*: escape request method in 405 error reporting. this has no security impact since the browser cannot be tricked into sending arbitrary method strings.  [jeff trawick] 2.2.7 (not released) 

*) mod_rewrite: add the novary flag to *rewritecond*. [ruediger pluem] 2.2.7 (not released) 

*) http_*protocol*: escape request method in 413 error reporting. determined to be not generally exploitable, but a flaw in any case. pr 44014 [victor stinner <victor.stinner inl.fr>] 2.2.7 (not released) 

*) mod_filter: don't segfault on (unsupported) chained *filterprovider* usage. pr 43956 [nick kew, ruediger pluem] 2.2.7 (not released) 

*) mod_proxy_http: correctly forward unexpected interim (http 1xx) responses from the backend according to rfc2616.  but make it *config*urable in case something breaks on it. pr 16518 [nick kew] 2.2.7 (not released) 

*) mod_*substitute*: added a new output filter, which performs inline response content pattern matching (including regex) and substitution.  [jim jagielski, ruediger pluem] 2.2.7 (not released) 

*) mod_proxy: canonicalisation improvements. add "nocanon" keyword to *proxypass*, to suppress uri-canonicalisation in a reverse proxy. also, don't escape/unescape forward-proxied urls. pr 41798, 42592 [nick kew, ruediger pluem, roy fielding, jim jagielski] 2.2.7 (not released) 

*) mod_status: add *seerequesttail* directive, which determines if *extendedstatus* displays the 1st 63 characters of the request or the last 63. useful for those requests with large string lengths and which only vary with the last several characters. [jim jagielski] 2.2.7 (not released) 

*) core: fix possible crash at startup in case of nonexistent *documentroot*. pr 39722 [adrian buckley <adrian.buckley ntlworld.com>] 2.2.7 (not released) 

*) http *protocol*: add "*defaulttype* none" option. pr 13986 and pr 16139 [nick kew] 2.2.7 (not released) 

*) http_core: *options* * no longer maps to local storage or uri space. note that unlike previous versions, *options* * no longer returns an allow: header. pr 43519 [jim jagielski] 2.2.7 (not released) 

*) mod_proxy: don't by default violate rfc2616 by setting max-forwards when the client didn't send it to us. leave that as a *config*uration option. pr 16137 [nick kew] 2.2.7 (not released) 

*) mod_proxy: check *proxyblock* for all blocked addresses pr 36987 [timo viipuri <timo.viipuri f-secure.com>] 2.2.7 (not released) 

*) security: cve-2007-3304 (cve.mitre.org) prefork, worker, event mpms: ensure that the parent process cannot be forced to kill processes outside its process *group*. [joe orton, jim jagielski] 2.2.6 

*) security: cve-2006-5752 (cve.mitre.org) mod_status: fix a possible xss attack against a site with a public server-status page and *extendedstatus* enabled, for browsers which perform charset "detection".  reported by stefan esser.  [joe orton] 2.2.6 

*) mod_proxy: enable ignore errors option on *proxypass* status. pr 43167 [francisco gimeno <kikov kikov.org> 2.2.6 

*) mod_authnz_ldap: don't return http_unauthorized during authorization when ldap authentication is *config*ured but we haven't seen any 'require ldap-*' directives, allowing authorization to be passed to lower level modules (e.g. require valid-user) pr 43281 [eric covener] 2.2.6 

*) proxy/ajp_header.c: backport of an ajp *protocol* fix for ebcdic on ebcdic machines, the status_line string was incorrectly converted twice. [jean-frederic clere, martin kraemer] 2.2.6 

*) mod_autoindex: add in type and charset *options* to index*options* directive. this allows the admin to explicitly set the content-type and charset of the generated page and is therefore a viable workaround for buggy browsers affected by cve-2007-4465 (cve.mitre.org). [jim jagielski] 2.2.6 

*) mod_ssl: version reporting update; displays 'compiled against' apache and build-time ssl library versions at *loglevel* [info], while reporting the run-time ssl library version in the server info tags.  helps to identify a mod_ssl built against one flavor of openssl but running against another (also adds ssl-c version number reporting.)  [william rowe] 2.2.6 

*) mod_expires: don't crash on bad *config*uration data pr 43213 [julien perez <julien.perez epsylonia.net>] 2.2.6 

*) mod_dbd: introduce *config*uration *group*s to allow inheritance by virtual hosts of database *config*urations from the main server.  determine the minimal set of distinct *config*urations and share connection pools whenever possible.  allow virtual hosts to override inherited sql statements.  pr 41302.  [chris darroch] 2.2.6 

*) mod_dbd: handle error conditions in dbd_construct() properly. simplify ap_dbd_open() and use correct arguments to apr_dbd_error() when non-threaded.  register correct cleanup data in non-threaded ap_dbd_acquire() and ap_dbd_cacquire().  clean up *config*uration data and merge function.  use ap_log_error() wherever possible. [chris darroch, nick kew] 2.2.6 

*) mod_dbd: stash dbd connections in request_*config* of initial request only, or else sub-requests and internal *redirect*ions may cause entire dbd pool to be stashed in a single http request.  [chris darroch] 2.2.6 

*) mod_ldap: avoid possible crashes, hangs, and busy loops due to improper merging of the cache lock in vhost *config* pr 43164 [eric covener] 2.2.6 

*) mod_deflate: fix *protocol* handling in deflate input filter pr 23287 [nick kew] 2.2.6 

*) mime.types: add registered java*script*/ecma*script* mime types (rfc4329) pr 40299 [dave hodder <dmh dmh.org.uk>] 2.2.6 

*) mod_filter: fix merging of ! and = in *filterchain* pr 42186 [issac goldstand <margol beamartyr.net>] 2.2.6 

*) mod_cgi, mod_cgid: fix use of cgi *script*s as *errordocument*s. pr 39710.  [paul querna, ruediger pluem] 2.2.6 

*) mod_proxy: allow to use different values for *session*id in url encoded id and cookies. pr 41897. [jean-frederic clere] 2.2.6 

*) mod_proxy: fix the 503 returned when *session* route does not match any of the balancer members. [mladen turk] 2.2.6 

*) mod_proxy: added *proxypass*match directive, which is similar to *proxypass* but takes a regex local path prefix. [jim jagielski] 2.2.6 

*) mod_proxy: print the correct error message for erroneous *config*ured *proxypass* directives. pr 40439.  [takashi sato <serai lans-tv.com>] 2.2.6 

*) mod_so: provide more helpful *loadmodule* feedback when an error occurs. [william rowe] 2.2.6 

*) mod_*alias*: accept path components (url part) in *redirect*s. pr 35314. [nick kew] 2.2.6 

*) mod_cache: add *cacheignorequerystring* directive. pr 41484. [fredrik widlund <fredrik.widlund qbrick.com>] 2.2.6 

*) http proxy *proxyerroroverride*: leave 1xx and 3xx responses alone.  only processing of error responses (4xx, 5xx) will be altered. pr 39245. [jeff trawick, bart van der schans <schans hippo.nl>] 2.2.6 

*) core: correct a regression since 2.0.x in the handling of *allowoverride* *options*. pr 41829.  [torsten förtsch <torsten.foertsch gmx.net>] 2.2.6 

*) mod_proxy: fix some proxy setting inheritance problems (eg: proxy*timeout*). pr 11540.  [stuart children <stuart terminus.co.uk>] 2.2.6 

*) unix mpms: catch sigfpe so that exception hooks and *coredumpdirectory* can work after that terminating signal. [eric covener] 2.2.6 

*) core: fix nonblock status of *listen*ing sockets on restart/graceful pr 37680.  [darius davis <darius-abz free-range.com.au>] 2.2.4 

*) allow mod_dumpio to log at other than debug levels via the new dumpio*loglevel* directive. [jim jagielski] 2.2.4 

*) mod_dbd: share per-request database handles across subrequests and internal *redirect*s [chris darroch] 2.2.4 

*) mod_dbd: key connection pools to virtual hosts correctly even when *servername* is unset/unavailable [graham leggett] 2.2.4 

*) mod_authnz_ldap: add an *authldapremoteuserattribute* directive. if set, remote_user will be set to this attribute, rather than the username supplied by the user. useful for *example* when you want users to log in using an email address, but need to supply a userid instead to the backend.  [graham leggett] 2.2.4 

*) core: fix address-in-use startup failure caused by corruption of the list of *listen* sockets in some *config*urations with multiple generic *listen* directives.  [jeff trawick] 2.2.4 

*) mod_proxy: add explicit flushing feature. when servlet container sends ajp body message with size 0, this means that servlet container has asked for an explicit flush. create flush bucket in that case. this feature has been added to the recent tomcat versions without breaking the ajp *protocol*.  [mladen turk] 2.2.4 

*) mod_proxy_balancer: set the new environment variable balancer_route_changed if a worker with a route different from the one supplied by the client had been chosen or if the client supplied no routing information for a balancer with sticky *session*s. [ruediger pluem] 2.2.4 

*) mod_proxy_balancer: add information about the route, the sticky *session* and the worker used during a request as environment variables. pr 39806. [brian <brectanu gmail.com>] 2.2.4 

*) mod_proxy_balancer: extract sticky*session* routing information contained as parameter in the url correctly. pr 40400. [ruediger pluem, tomokazu harada <harada sysrdc.ns-sol.co.jp>] 2.2.4 

*) mod_proxy_ajp: added cping/cpong support for the ajp *protocol*. a new worker directive ping=*timeout* will cause cping packet to be send expecting cpong packet within defined *timeout*. in case the backend is too busy this will fail instead sending the full header.  [mladen turk] 2.2.4 

*) mod_disk_cache: make sure that only positive integers are accepted for the *cachemaxfilesize* and *cacheminfilesize* parameters in the *config* file. pr39380.  [niklas edmundsson <nikke acc.umu.se>] 2.2.4 

*) mod_cache: from rfc3986 (section 6.2.3.) if a uri contains an authority component and an empty path, the empty path is to be equivalent to "/". it explicitly cites the following four uris as equivalents: http://*example*.com http://*example*.com/ http://*example*.com:/ http://*example*.com:80/ [davi arnaut <davi haxent.com.br>] 2.2.4 

*) the full server version information is now included in the error log at startup as well as server status reports, irrespective of the setting of the *servertokens* directive.  ap_get_server_version() is now deprecated, and is replaced by ap_get_server_banner() and ap_get_server_de*script*ion().  [jeff trawick] 2.2.4 

*) mod_proxy_balancer: retry worker chosen by route / *redirect* worker if it is in error state before sending "service temporarily unavailable". pr 38962.  [christian boitel <cboitel lfdj.com>] 2.2.3 

*) security: cve-2006-3747 (cve.mitre.org) mod_rewrite: fix an off-by-one security problem in the ldap scheme handling.  for some *rewriterule*s this could lead to a pointer being written out of bounds.  reported by mark dowd of mcafee. [mark cox] 2.2.3 

*) mod_authn_*alias*: add a check to make sure that the base provider and the *alias* names are different and also that the *alias* has not been registered before. pr 40051. [brad nicholes] 2.2.3 

*) mod_dbd: fix dependence on virtualhost *config*uration in defining prepared statements (possible segfault at startup in user modules such as mod_authn_dbd).  [nick kew] 2.2.3 

*) add optional 'scheme://' prefix to *servername* directive, allowing correct determination of the canonical server url for use behind a proxy or offload device handling ssl; fixing *redirect* generation in those cases. pr 33398. [sander temme] 2.2.3 

*) *config*ure: add "--with-included-apr" flag to force use of the bundled version of apr at build time.  [joe orton] 2.2.3 

*) respect gracefulshutdown*timeout* in the worker and event mpms. [chris darroch, garrett rooney] 2.2.3 

*) mod_deflate: work correctly in an internal *redirect* [brian j. france <list firehawksystems com>] 2.2.2 

*) core: prevent reading uninitialized memory while reading a line of *protocol* input.  pr 39282. [davi arnaut <davi haxent com br>] 2.2.2 

*) mod_dbd: create own pool and *mutex* to avoid problem use of process pool in request processing. [chris darroch <chrisd pearsoncmg com>] 2.2.2 

*) security: cve-2005-3357 (cve.mitre.org) mod_ssl: fix a possible crash during access control checks if a non-ssl request is processed for an ssl vhost (such as the "http request received on ssl port" error message when an 400 *errordocument* is *config*ured, or if using "*sslengine* optional"). pr 37791.  [rüdiger plüm, joe orton] 2.2.1 

*) security: cve-2005-3352 (cve.mitre.org) mod_imagemap: escape untrusted referer header before outputting in html to avoid potential cross-site *script*ing.  change also made to ap_escape_html so we escape quotes.  reported by jpcert. [mark cox] 2.2.1 

*) mod_proxy_ajp: flushing of the output after each ajp chunk is now *config*urable at runtime via the 'flushpackets' and 'flushwait' worker params. minor mmn bump. [jim jagielski] 2.2.1 

*) mod_proxy: fix *keepalive*s not being allowed and set to backend servers. pr 38602. [ruediger pluem, jim jagielski] 2.2.1 

*) mod_proxy_ajp: support common headers of the ajp *protocol* in responses. pr 38340. [aleksey pesternikov <apesternikov yahoo.com>] 2.2.1 

*) mod_proxy_balancer: do not overwrite the status of initialized workers and respect the *config*ured status of uninitilized workers when creating a new child process. [ruediger pluem] 2.2.1 

*) avoid server-driven negotiation when a *script* has emitted an explicit status: header.  pr 38070.  [nick kew] 2.2.1 

*) fix recursive *errordocument* handling.  pr 36090. [chris darroch <chrisd pearsoncmg.com>] 2.2.1 

*) remove support for 'on' and 'off' for *authbasicprovider* and *authdigestprovider*.  [joshua slive, justin erenkrantz] 2.2.0 

*) add in new *usecanonicalphysicalport* directive, which controls whether or not apache will ever use the actual physical port when constructing the canonical port number. [jim jagielski] 2.2.0 

*) require use of apr >= 1.2.0 and apr-util >= 1.2.0 when *config*ured to use external copies of the libraries.  [joe orton] 2.2.0 

*) mod_proxy: do not lowercase the entire worker name of a *balancermember* since this breaks case sensitive uri's.  pr 36906.  [ruediger pluem] 2.1.9 

*) core: **addoutputfilter*bytype* is ignored for proxied requests. pr 31226. [joe orton, ruediger pluem] 2.1.9 

*) mod_log_*config*: %{hextid}p will log the thread id in hex with apr versions 1.2.0 or higher.  [jeff trawick] 2.1.9 

*) eliminated the net_time filter, restructuring the *timeout* logic. this provides a working mod_echo on all platforms, and ensures any custom *protocol* module is at least given an initial *timeout* value based on the *<virtualhost* > context's *timeout* directive. [william rowe] 2.1.9 

*) mod_proxy_balancer: fix handling of sticky *session*s with tomcat. pr 36507.  [ruediger pluem] 2.1.9 

*) fix regression since 2.0.x in *allowoverride* *options* handling. pr 35330.  [kabe <kabe sra-tohoku.co.jp>] 2.1.8 

*) prefork, worker and event mpms: support a graceful-stop procedure: server will wait until existing requests are finished or until "gracefulshutdown*timeout*" number of seconds before exiting. [colm maccarthaigh, ken coar, bill stoddard] 2.1.8 

*) prefork, worker and event mpms: prevent children from holding open *listen*ing ports upon graceful restart or stop. pr 28167. [colm maccarthaigh, brian pinkerton <bp thinkpink.com>] 2.1.8 

*) security: cve-2005-2700 (cve.mitre.org) mod_ssl: fix a security issue where "*sslverifyclient*" was not enforced in per-location context if "*sslverifyclient* optional" was *config*ured in the vhost *config*uration.  [joe orton] 2.1.8 

*) mod_ssl: catch parse errors from mis*config*ured or malformed crls.  pr 36438.  [joe orton] 2.1.8 

*) mod_proxy/mod_proxy_balancer: lbmethods now implemented as providers. prevent problems when no vhost containers were *config*ured with proxy balancers. [jim jagielski] 2.1.8 

*) new provider function to list all available provider names in a specific *group* and version (ap_list_provider_names). [jim jagielski] 2.1.8 

*) mod_cache: enhance *cacheenable*/*cachedisable* to control caching on a per-*protocol*, per-host and per-path basis. intended for proxy *config*urations. [colm maccarthaigh] 2.1.8 

*) mod_cgid: append .pid to the *script* socket filename and remove the *script* socket on exit. [colm maccarthaigh, jim jagielski] 2.1.8 

*) mod_cgid: run the get_*suexec*_identity hook within the request-handler instead of within cgid. pr 36410. [colm maccarthaigh] 2.1.8 

*) add additional ssl*session*cache option, 'nonenotnull', which is similar to 'none' (disabling any external shared cache) but forces openssl to provide a non-null *session* id.  [jim jagielski] 2.1.7 

*) add httxt2dbm to support/ for creating *rewritemap* dbm files. [paul querna] 2.1.7 

*) fixed complaints about unpackaged files within the rpm build after changes to the *config* files. [graham leggett] 2.1.7 

*) mod_cgid: fix buffer overflow processing *script*sock directive. [steve kemp <steve steve.org.uk>] 2.1.5 

*) mod_ssl: setting the *protocol* to 'https' can replace the use of the '*sslengine* on' command. [paul querna] 2.1.5 

*) core: refactor the mapping of accept filters to sockets. add the *acceptfilter* and *protocol* directives to aid in mapping filter types. extend the *listen* directive to optionally take a *protocol* name. [paul querna] 2.1.5 

*) core: allow multiple modules to register interest in a single *config*uration command. [paul querna] 2.1.5 

*) authn_provider_*alias*: adds the *config*uration block tag <authnprovider*alias* baseprovider *alias*> authentication directives contained within this block can be referenced as a new authprovider using the *authbasicprovider* or *authdigestprovider* directive.  these directives will be merged in to the per_dir *config*uration just before the base provider is called. [brad nicholes] 2.1.5 

*) ap_getword_conf: fix backslashes at the end of *config*uration directives. pr 34834. [timo viipuri <viipuri dlc.fi>] 2.1.5 

*) ab: ssl support rewritten, improved, and enabled if ssl is enabled during the build; -f and -z arguments added to specify ssl *protocol* *options*.  [masaoki kobayashi <masaoki techfirm.co.jp>] 2.1.5 

*) mod_ldap: add the directive *ldapverifyservercert* to specify whether to force verification of the server certificate when establishing an ssl connection to the ldap server. [brad nicholes] 2.1.5 

*) add ap_init_take_argv for *config*uration commands. (minor mmn bump) [paul querna] 2.1.5 

*) change the default (when not present in the *config* file) setting for *usecanonicalname* to off. [joshua slive] 2.1.5 

*) mod_*userdir*: the module no longer does any remapping unless the *userdir* directive is present in the *config* file. [joshua slive] 2.1.5 

*) massively simplify the distributed httpd.conf by removing many features and many directives that are at their default setting.  add a selection of *example* *config* excerpts for adding extra features in the conf/extra/ directory.  install the distributed *config* and the extra *config* *example*s in the conf/original/ directory during make install. [joshua slive, justin erenkrantz] 2.1.5 

*) netware: reposition mod_asis, mod_*action*s, mod_cgi, mod_imagemap, mod_*userdir* and mod_autoindex as shared modules rather than built-in modules within the netware build. [brad nicholes] 2.1.5 

*) add *receive*buffersize** directive to control the tcp receive buffer. [eric covener <covener gmail.com>] 2.1.4 

*) add support for use of an external pcre library; pass the --with-pcre flag to *config*ure.  pr 27550.  [joe orton, andres salomon <dilinger voxel.net>] 2.1.3 

*) mod_authnz_ldap: added an optional second parameter to *authldapurl* to allow it to override the connection type set in mod_ldap. this parameter can be set to none, ssl or tls | starttls. [brad nicholes] 2.1.3 

*) mod_proxy: fix *proxyremote*match directive.  pr 33170. [rici lake <rici ricilake.net>] 2.1.3 

*) mod_cache: add *cachestoreprivate* and *cachestorenostore* directive. [justin erenkrantz] 2.1.3 

*) add --enable-pie flag to *config*ure, to build httpd as a position independent executable where supported (gcc/binutils). [joe orton] 2.1.3 

*) mod_disk_cache: cache r->err_headers_out headers.  this allows cgi *script*s to be properly cached.  [justin erenkrantz, sander striker] 2.1.3 

*) mod_ldap: updated to use the new apr-util v1.1 apr_ldap_*_option() api for the setting of server and client ssl certificates. replaced ldaptrustedca directive with *ldaptrustedglobalcert* and *ldaptrustedclientcert* directives to correctly support global certs (ca certs / netware client certs) and per connection client certs as supported by netware, openldap and netscape/mozilla. [graham leggett] 2.1.3 

*) mod_ssl: add *sslcadnrequestfile* and *sslcadnrequestpath* directives which can be used to *config*ure a specific list of ca names to send in a client certificate request.  pr 32848. [tim taylor <tim.taylor dfas.mil>] 2.1.3 

*) add a build *script* to create a solaris package. [graham leggett] 2.1.3 

*) significantly simplify the load balancer scheduling algorithm for the proxy *balancermember* weighting. loadfactors (lbfactors) are now normalized with respect to each other. [jim jagielski] 2.1.3 

*) mod_cgid: catch *config*uration problem where two web server instances share same *serverroot* but admin forgot to use *script*sock. [jeff trawick] 2.1.2 

*) mod_cgi: ensure that all stderr is logged for a *script* which returns a location header to generate a non-local *redirect*.  pr 20111. [joe orton] 2.1.2 

*) mod_ssl: add support for command-line option "-t -ddump_certs" which will dump the filenames of all *config*ured ssl certificates to stdout. [joe orton] 2.1.1 

*) mod_rewrite: removed the max*redirect*s option in favor of the core *limitinternalrecursion* directive.  [andré malo] 2.1.1 

*) mod_info: rewrote *config* tree walk using a recursive function. added ?*config* option. added printout of *config* filename and line numbers. [rici lake <rici ricilake.net>, paul querna] 2.1.1 

*) restructured mod_auth_ldap to fit the new authentication model. the module is now called authnz_ldap and has been moved out of the modules/experimental area and into modules/aaa with the other auth modules.  both the authn_ldap provider and the authz_ldap handler are contained within the authnz_ldap module.  the authz_ldap handler introduces 3 new "requires" values for handling authorization.  these handlers are ldap-user, ldap-*group* and ldap-dn. [brad nicholes] 2.1.1 

*) add test_*config* hook, run only if httpd is invoked using -t. [joe orton] 2.1.1 

*) mod_nw_ssl: added the directive *nwsslupgradeable* to mod_nw_ssl to allow a non-secure connection to be upgraded to secure connections [brad nicholes] 2.1.1 

*) core: add *options*= syntax to *allowoverride* to specify which *options* may be overridden in .htaccess files. pr 29310. [tom alsberg <alsbergt cs.huji.ac.il>, paul querna] 2.1.1 

*) mod_so, core: add new command line *options* to print all loaded modules. '-t -d dump_modules' and '-m' will show all static and shared modules as loaded from the *config*uration file. [paul querna] 2.1.1 

*) mod_autoindex: add showforbidden to index*options* to list files that are not shown because the subrequest returned 401 or 403. pr 10575.  [paul querna] 2.1.1 

*) mod_headers: implement "early" processing option in post_read_request to enable header and *requestheader* directives to be used to set up testcases for pre-fixups request phases [nick kew] 2.1.1 

*) mod_proxy: multiple bugfixes, principally support cookies in *proxypass*reverse, and don't canonicalise url passed to backend. documentation correspondingly updated. [nick kew <nick webthing.com>] 2.1.1 

*) *<ifmodule*> now recognizes the module identifier in addition to the file name. pr 29003.  [edward rudd <eddie omegaware.com>, andré malo] 2.1.1 

*) mod_ssl: add "*sslhonorcipherorder*" directive to enable the openssl 0.9.7 flag which uses the server's cipher order rather than the client's.  pr 28665. [jim schneider <jschneid netilla.com>] 2.1.1 

*) mod_ssl: drop support for the compatenvvars argument to ssl*options*, which was never actually implemented in 2.0. [joe orton] 2.1.1 

*) removed old and unmaintained ap_add_named_module api and changed the following apis to return an error instead of hard exiting: ap_add_module, ap_add_loaded_module, ap_setup_prelinked_modules, and ap_process_resource_*config*.  [andré malo] 2.1.1 

*) mod_headers: allow env clauses also for 'echo' and 'unset' *action*s. [andré malo] 2.1.1 

*) added new module mod_version, which provides version dependent *config*uration containers.  [andré malo] 2.1.1 

*) mod_log_*config* now logs all set-cookie headers if the %{set-cookie}o format is used.  pr 27787.  [andré malo] 2.1.1 

*) mod_cgid: don't allow *script*sock to be specified inside virtualhost; don't place *script* socket inside default server root instead of actual server root.  pr 27886.  [jeff trawick] 2.1.1 

*) mod_proxy: fix handling of non-200 success status codes when "*proxyerroroverride* on" is *config*ured.  pr 20183. [marcus janson <marcus.janson tre.se>, joe orton] 2.1.1 

*) threaded mpms for unix and win32: add support for *threadstacksize* directive (previously netware-only) to override default thread stack size for threads which handle client connections.  required for some third-party modules on platforms with small default thread stack size.  [jeff trawick] 2.1.1 

*) mod_rewrite: eols sent by external *rewritemap*s are now consumed as whole. that way, on systems with more than one eol character *rewritemap* programs no longer need to switch stdout to binary mode. pr 25635.  [andré malo] 2.1.1 

*) mod_rewrite: introduce the *rewritecond* -x check, which returns true if the pattern is a file with execution permissions. [andré malo] 2.1.1 

*) mod_rewrite: allow proxying and *rewriterule*s in directory context for subrequests.  pr 14648, 15114.  [andré malo] 2.1.1 

*) mod_ssl: add support for distributed *session* cache using 'distcache'. [geoff thorpe <geoff geoffthorpe.net>] 2.1.1 

*) mod_proxy with *proxyerroroverride* on in a reverse-proxy *config*uration attaches a body to the 302 response and a wrong content-length header. pr: 22951 [ermanno scaglione scaglione ..at.. starnetone.de] 2.1.1 

*) bring errorheader concept forward from 1.3, so that response header fields can be set for return even on errors or external *redirect*s.  [ken coar] 2.1.1 

*) fix *<limit*> and *<limit*except> parsing to require a closing '>' in the initial container.  pr 25414. [geoffrey young <geoff apache.org>] 2.1.1 

*) mod_ssl/mod_status: re-enable support for output of ssl *session* cache information in server-status page.  [joe orton] 2.1.1 

*) mod_ssl: remove the shmht *session* cache, shmcb should be used instead.  [joe orton] 2.1.1 

*) mod_autoindex: new directive *indexstylesheet* [tyler riddle <triddle_1999 yahoo.com>, paul querna <chip force-elite.com>] 2.1.1 

*) change *listen* directive to bind to all addresses when a hostname is not specified.  [justin erenkrantz] 2.1.1 

*) correct failure with *listen* directives on machines with ipv6 enabled. [colm maccárthaigh <colm stdlib.net>, justin erenkrantz] 2.1.1 

*) mod_rewrite: *rewriterule*s in server context using the force type feature [t=...] no longer disable multiviews.  [andré malo] 2.1.1 

*) mod_rewrite: allow piped rewrite logs to be relative to *serverroot*. [andré malo] 2.1.1 

*) mod_authz_*group*file: strip trailing spaces of *group* names. this hopefully saves some hours of searching for typos. pr 12863. [andré malo] 2.1.1 

*) mod_*action*s: propagate the handler name to the *action* *script* via the *redirect*_handler environment variable.  [andré malo] 2.1.1 

*) mod_*action*s: introduce the "virtual" modifier to the *action* directive, which allows the use of handlers for virtual locations. pr 8431. [andré malo] 2.1.1 

*) mod_speling: recognize *acceptpathinfo* setting for the particular location. default is to reject path information. pr 21059. [andré malo] 2.1.1 

*) change directive name from 'compressionlevel' to '*deflatecompressionlevel*' [ian holsman, andré malo] 2.1.1 

*) mod_rewrite: fix some problems reporting errors with mapping programs (*rewritemap* prg:/something).  [jeff trawick] 2.1.1 

*) allow restart of httpd to occur even with syntax errors in the *config* file.  pr 16813.  [justin erenkrantz] 2.1.1 

*) use apr_layout instead of apache_layout in *config*ure.  pr 15679. [justin erenkrantz] 2.1.1 

*) mod_log_*config* change optional hook to return previous handler [ian holsman] 2.1.1 

*) forward port of mod_*action*s' ability to handle arbitrary methods with the *script* directive.  [andré malo] 2.1.1 

*) let *suexec* send a message to stderr, if it failed or its policy was violated. this message appears in the error log and allows for easier debugging. pr 5381, 7638, 8255, 10773.  [andré malo] 2.1.1 

*) add mod_authz_owner - a forward port of "require file-owner" and "require file-*group*", which was already present in version 1.3.21.  [andré malo] 2.1.1 

*) replace some of the *mutex* locking in the worker mpm with atomic operations for higher concurrency.  [brian pane] 2.1.1 

*) if an httpd.conf has commented out addmodule directives, apxs -i -a will add an un-commented addmodule directive for the new module, which breaks the *config*. pr: 11212 [joe orton] 2.1.1 

*) mod_proxy: do not lowercase the entire worker name of a *balancermember* since this breaks case sensitive uri's.  pr 36906.  [ruediger pluem] 2.1.9 

*) core: **addoutputfilter*bytype* is ignored for proxied requests. pr 31226. [joe orton, ruediger pluem] 2.1.9 

*) mod_log_*config*: %{hextid}p will log the thread id in hex with apr versions 1.2.0 or higher.  [jeff trawick] 2.1.9 

*) eliminated the net_time filter, restructuring the *timeout* logic. this provides a working mod_echo on all platforms, and ensures any custom *protocol* module is at least given an initial *timeout* value based on the *<virtualhost* > context's *timeout* directive. [william rowe] 2.1.9 

*) mod_proxy_balancer: fix handling of sticky *session*s with tomcat. pr 36507.  [ruediger pluem] 2.1.9 

*) fix regression since 2.0.x in *allowoverride* *options* handling. pr 35330.  [kabe <kabe sra-tohoku.co.jp>] 2.1.8 

*) prefork, worker and event mpms: support a graceful-stop procedure: server will wait until existing requests are finished or until "gracefulshutdown*timeout*" number of seconds before exiting. [colm maccarthaigh, ken coar, bill stoddard] 2.1.8 

*) prefork, worker and event mpms: prevent children from holding open *listen*ing ports upon graceful restart or stop. pr 28167. [colm maccarthaigh, brian pinkerton <bp thinkpink.com>] 2.1.8 

*) security: cve-2005-2700 (cve.mitre.org) mod_ssl: fix a security issue where "*sslverifyclient*" was not enforced in per-location context if "*sslverifyclient* optional" was *config*ured in the vhost *config*uration.  [joe orton] 2.1.8 

*) mod_ssl: catch parse errors from mis*config*ured or malformed crls.  pr 36438.  [joe orton] 2.1.8 

*) mod_proxy/mod_proxy_balancer: lbmethods now implemented as providers. prevent problems when no vhost containers were *config*ured with proxy balancers. [jim jagielski] 2.1.8 

*) new provider function to list all available provider names in a specific *group* and version (ap_list_provider_names). [jim jagielski] 2.1.8 

*) mod_cache: enhance *cacheenable*/*cachedisable* to control caching on a per-*protocol*, per-host and per-path basis. intended for proxy *config*urations. [colm maccarthaigh] 2.1.8 

*) mod_cgid: append .pid to the *script* socket filename and remove the *script* socket on exit. [colm maccarthaigh, jim jagielski] 2.1.8 

*) mod_cgid: run the get_*suexec*_identity hook within the request-handler instead of within cgid. pr 36410. [colm maccarthaigh] 2.1.8 

*) add additional ssl*session*cache option, 'nonenotnull', which is similar to 'none' (disabling any external shared cache) but forces openssl to provide a non-null *session* id.  [jim jagielski] 2.1.7 

*) add httxt2dbm to support/ for creating *rewritemap* dbm files. [paul querna] 2.1.7 

*) fixed complaints about unpackaged files within the rpm build after changes to the *config* files. [graham leggett] 2.1.7 

*) mod_cgid: fix buffer overflow processing *script*sock directive. [steve kemp <steve steve.org.uk>] 2.1.5 

*) mod_ssl: setting the *protocol* to 'https' can replace the use of the '*sslengine* on' command. [paul querna] 2.1.5 

*) core: refactor the mapping of accept filters to sockets. add the *acceptfilter* and *protocol* directives to aid in mapping filter types. extend the *listen* directive to optionally take a *protocol* name. [paul querna] 2.1.5 

*) core: allow multiple modules to register interest in a single *config*uration command. [paul querna] 2.1.5 

*) authn_provider_*alias*: adds the *config*uration block tag <authnprovider*alias* baseprovider *alias*> authentication directives contained within this block can be referenced as a new authprovider using the *authbasicprovider* or *authdigestprovider* directive.  these directives will be merged in to the per_dir *config*uration just before the base provider is called. [brad nicholes] 2.1.5 

*) ap_getword_conf: fix backslashes at the end of *config*uration directives. pr 34834. [timo viipuri <viipuri dlc.fi>] 2.1.5 

*) ab: ssl support rewritten, improved, and enabled if ssl is enabled during the build; -f and -z arguments added to specify ssl *protocol* *options*.  [masaoki kobayashi <masaoki techfirm.co.jp>] 2.1.5 

*) mod_ldap: add the directive *ldapverifyservercert* to specify whether to force verification of the server certificate when establishing an ssl connection to the ldap server. [brad nicholes] 2.1.5 

*) add ap_init_take_argv for *config*uration commands. (minor mmn bump) [paul querna] 2.1.5 

*) change the default (when not present in the *config* file) setting for *usecanonicalname* to off. [joshua slive] 2.1.5 

*) mod_*userdir*: the module no longer does any remapping unless the *userdir* directive is present in the *config* file. [joshua slive] 2.1.5 

*) massively simplify the distributed httpd.conf by removing many features and many directives that are at their default setting.  add a selection of *example* *config* excerpts for adding extra features in the conf/extra/ directory.  install the distributed *config* and the extra *config* *example*s in the conf/original/ directory during make install. [joshua slive, justin erenkrantz] 2.1.5 

*) netware: reposition mod_asis, mod_*action*s, mod_cgi, mod_imagemap, mod_*userdir* and mod_autoindex as shared modules rather than built-in modules within the netware build. [brad nicholes] 2.1.5 

*) add *receive*buffersize** directive to control the tcp receive buffer. [eric covener <covener gmail.com>] 2.1.4 

*) add support for use of an external pcre library; pass the --with-pcre flag to *config*ure.  pr 27550.  [joe orton, andres salomon <dilinger voxel.net>] 2.1.3 

*) mod_authnz_ldap: added an optional second parameter to *authldapurl* to allow it to override the connection type set in mod_ldap. this parameter can be set to none, ssl or tls | starttls. [brad nicholes] 2.1.3 

*) mod_proxy: fix *proxyremote*match directive.  pr 33170. [rici lake <rici ricilake.net>] 2.1.3 

*) mod_cache: add *cachestoreprivate* and *cachestorenostore* directive. [justin erenkrantz] 2.1.3 

*) add --enable-pie flag to *config*ure, to build httpd as a position independent executable where supported (gcc/binutils). [joe orton] 2.1.3 

*) mod_disk_cache: cache r->err_headers_out headers.  this allows cgi *script*s to be properly cached.  [justin erenkrantz, sander striker] 2.1.3 

*) mod_ldap: updated to use the new apr-util v1.1 apr_ldap_*_option() api for the setting of server and client ssl certificates. replaced ldaptrustedca directive with *ldaptrustedglobalcert* and *ldaptrustedclientcert* directives to correctly support global certs (ca certs / netware client certs) and per connection client certs as supported by netware, openldap and netscape/mozilla. [graham leggett] 2.1.3 

*) mod_ssl: add *sslcadnrequestfile* and *sslcadnrequestpath* directives which can be used to *config*ure a specific list of ca names to send in a client certificate request.  pr 32848. [tim taylor <tim.taylor dfas.mil>] 2.1.3 

*) add a build *script* to create a solaris package. [graham leggett] 2.1.3 

*) significantly simplify the load balancer scheduling algorithm for the proxy *balancermember* weighting. loadfactors (lbfactors) are now normalized with respect to each other. [jim jagielski] 2.1.3 

*) mod_cgid: catch *config*uration problem where two web server instances share same *serverroot* but admin forgot to use *script*sock. [jeff trawick] 2.1.2 

*) mod_cgi: ensure that all stderr is logged for a *script* which returns a location header to generate a non-local *redirect*.  pr 20111. [joe orton] 2.1.2 

*) mod_ssl: add support for command-line option "-t -ddump_certs" which will dump the filenames of all *config*ured ssl certificates to stdout. [joe orton] 2.1.1 

*) mod_rewrite: removed the max*redirect*s option in favor of the core *limitinternalrecursion* directive.  [andré malo] 2.1.1 

*) mod_info: rewrote *config* tree walk using a recursive function. added ?*config* option. added printout of *config* filename and line numbers. [rici lake <rici ricilake.net>, paul querna] 2.1.1 

*) restructured mod_auth_ldap to fit the new authentication model. the module is now called authnz_ldap and has been moved out of the modules/experimental area and into modules/aaa with the other auth modules.  both the authn_ldap provider and the authz_ldap handler are contained within the authnz_ldap module.  the authz_ldap handler introduces 3 new "requires" values for handling authorization.  these handlers are ldap-user, ldap-*group* and ldap-dn. [brad nicholes] 2.1.1 

*) add test_*config* hook, run only if httpd is invoked using -t. [joe orton] 2.1.1 

*) mod_nw_ssl: added the directive *nwsslupgradeable* to mod_nw_ssl to allow a non-secure connection to be upgraded to secure connections [brad nicholes] 2.1.1 

*) core: add *options*= syntax to *allowoverride* to specify which *options* may be overridden in .htaccess files. pr 29310. [tom alsberg <alsbergt cs.huji.ac.il>, paul querna] 2.1.1 

*) mod_so, core: add new command line *options* to print all loaded modules. '-t -d dump_modules' and '-m' will show all static and shared modules as loaded from the *config*uration file. [paul querna] 2.1.1 

*) mod_autoindex: add showforbidden to index*options* to list files that are not shown because the subrequest returned 401 or 403. pr 10575.  [paul querna] 2.1.1 

*) mod_headers: implement "early" processing option in post_read_request to enable header and *requestheader* directives to be used to set up testcases for pre-fixups request phases [nick kew] 2.1.1 

*) mod_proxy: multiple bugfixes, principally support cookies in *proxypass*reverse, and don't canonicalise url passed to backend. documentation correspondingly updated. [nick kew <nick webthing.com>] 2.1.1 

*) *<ifmodule*> now recognizes the module identifier in addition to the file name. pr 29003.  [edward rudd <eddie omegaware.com>, andré malo] 2.1.1 

*) mod_ssl: add "*sslhonorcipherorder*" directive to enable the openssl 0.9.7 flag which uses the server's cipher order rather than the client's.  pr 28665. [jim schneider <jschneid netilla.com>] 2.1.1 

*) mod_ssl: drop support for the compatenvvars argument to ssl*options*, which was never actually implemented in 2.0. [joe orton] 2.1.1 

*) removed old and unmaintained ap_add_named_module api and changed the following apis to return an error instead of hard exiting: ap_add_module, ap_add_loaded_module, ap_setup_prelinked_modules, and ap_process_resource_*config*.  [andré malo] 2.1.1 

*) mod_headers: allow env clauses also for 'echo' and 'unset' *action*s. [andré malo] 2.1.1 

*) added new module mod_version, which provides version dependent *config*uration containers.  [andré malo] 2.1.1 

*) mod_log_*config* now logs all set-cookie headers if the %{set-cookie}o format is used.  pr 27787.  [andré malo] 2.1.1 

*) mod_cgid: don't allow *script*sock to be specified inside virtualhost; don't place *script* socket inside default server root instead of actual server root.  pr 27886.  [jeff trawick] 2.1.1 

*) mod_proxy: fix handling of non-200 success status codes when "*proxyerroroverride* on" is *config*ured.  pr 20183. [marcus janson <marcus.janson tre.se>, joe orton] 2.1.1 

*) threaded mpms for unix and win32: add support for *threadstacksize* directive (previously netware-only) to override default thread stack size for threads which handle client connections.  required for some third-party modules on platforms with small default thread stack size.  [jeff trawick] 2.1.1 

*) mod_rewrite: eols sent by external *rewritemap*s are now consumed as whole. that way, on systems with more than one eol character *rewritemap* programs no longer need to switch stdout to binary mode. pr 25635.  [andré malo] 2.1.1 

*) mod_rewrite: introduce the *rewritecond* -x check, which returns true if the pattern is a file with execution permissions. [andré malo] 2.1.1 

*) mod_rewrite: allow proxying and *rewriterule*s in directory context for subrequests.  pr 14648, 15114.  [andré malo] 2.1.1 

*) mod_ssl: add support for distributed *session* cache using 'distcache'. [geoff thorpe <geoff geoffthorpe.net>] 2.1.1 

*) mod_proxy with *proxyerroroverride* on in a reverse-proxy *config*uration attaches a body to the 302 response and a wrong content-length header. pr: 22951 [ermanno scaglione scaglione ..at.. starnetone.de] 2.1.1 

*) bring errorheader concept forward from 1.3, so that response header fields can be set for return even on errors or external *redirect*s.  [ken coar] 2.1.1 

*) fix *<limit*> and *<limit*except> parsing to require a closing '>' in the initial container.  pr 25414. [geoffrey young <geoff apache.org>] 2.1.1 

*) mod_ssl/mod_status: re-enable support for output of ssl *session* cache information in server-status page.  [joe orton] 2.1.1 

*) mod_ssl: remove the shmht *session* cache, shmcb should be used instead.  [joe orton] 2.1.1 

*) mod_autoindex: new directive *indexstylesheet* [tyler riddle <triddle_1999 yahoo.com>, paul querna <chip force-elite.com>] 2.1.1 

*) change *listen* directive to bind to all addresses when a hostname is not specified.  [justin erenkrantz] 2.1.1 

*) correct failure with *listen* directives on machines with ipv6 enabled. [colm maccárthaigh <colm stdlib.net>, justin erenkrantz] 2.1.1 

*) mod_rewrite: *rewriterule*s in server context using the force type feature [t=...] no longer disable multiviews.  [andré malo] 2.1.1 

*) mod_rewrite: allow piped rewrite logs to be relative to *serverroot*. [andré malo] 2.1.1 

*) mod_authz_*group*file: strip trailing spaces of *group* names. this hopefully saves some hours of searching for typos. pr 12863. [andré malo] 2.1.1 

*) mod_*action*s: propagate the handler name to the *action* *script* via the *redirect*_handler environment variable.  [andré malo] 2.1.1 

*) mod_*action*s: introduce the "virtual" modifier to the *action* directive, which allows the use of handlers for virtual locations. pr 8431. [andré malo] 2.1.1 

*) mod_speling: recognize *acceptpathinfo* setting for the particular location. default is to reject path information. pr 21059. [andré malo] 2.1.1 

*) change directive name from 'compressionlevel' to '*deflatecompressionlevel*' [ian holsman, andré malo] 2.1.1 

*) mod_rewrite: fix some problems reporting errors with mapping programs (*rewritemap* prg:/something).  [jeff trawick] 2.1.1 

*) allow restart of httpd to occur even with syntax errors in the *config* file.  pr 16813.  [justin erenkrantz] 2.1.1 

*) use apr_layout instead of apache_layout in *config*ure.  pr 15679. [justin erenkrantz] 2.1.1 

*) mod_log_*config* change optional hook to return previous handler [ian holsman] 2.1.1 

*) forward port of mod_*action*s' ability to handle arbitrary methods with the *script* directive.  [andré malo] 2.1.1 

*) let *suexec* send a message to stderr, if it failed or its policy was violated. this message appears in the error log and allows for easier debugging. pr 5381, 7638, 8255, 10773.  [andré malo] 2.1.1 

*) add mod_authz_owner - a forward port of "require file-owner" and "require file-*group*", which was already present in version 1.3.21.  [andré malo] 2.1.1 

*) replace some of the *mutex* locking in the worker mpm with atomic operations for higher concurrency.  [brian pane] 2.1.1 

*) if an httpd.conf has commented out addmodule directives, apxs -i -a will add an un-commented addmodule directive for the new module, which breaks the *config*. pr: 11212 [joe orton] 2.1.1 

*) mod_cgi(d): remove block on *options* method so that *script*s can respond to *options* directly rather than via server default. [roy fielding] pr 15242 2.0.55 

*) added *traceenable* [on|off|extended] per-server directive to alter the behavior of the trace method.  this addresses a flaw in proxy conformance to rfc 2616 - previously the proxy server would accept a trace request body although the rfc prohibited it.  the default remains '*traceenable* on'.  [william rowe] 2.0.55 

*) fix a file de*script*or leak when starting piped loggers.  pr 33748. [joe orton] 2.0.55 

*) security: cve-2005-1268 (cve.mitre.org) mod_ssl: fix off-by-one overflow whilst printing crl information at "*loglevel* debug" which could be triggered if *config*ured to use a "malicious" crl.  pr 35081.  [marc stern <mstern csc.com>] 2.0.55 

*) mod_*userdir*: fix possible memory corruption issue.  pr 34588. [david leonard <dleonard vintela.com>] 2.0.55 

*) mod_rewrite: use buffered i/o to improve performance with large *rewritemap* txt: files.  [greg ames] 2.0.55 

*) mod_cache: add *cacheignoreheaders* directive.  pr 30399. [rüdiger plüm <r.pluem t-online.de>] 2.0.54 

*) mod_ldap: added the directive ldapconnection*timeout* to *config*ure the ldap socket connection *timeout* value. [brad nicholes] 2.0.54 

*) add a build *script* to create a solaris package. [graham leggett] 2.0.54 

*) mod_ssl: if *sslusername* is used, set r->user earlier.  pr 31418. [david reid] 2.0.54 

*) mod_proxy: fix *proxyremote*match directive.  pr 33170. [rici lake <rici ricilake.net>] 2.0.53 

*) conf: remove *adddefaultcharset* from the default *config*uration because setting a site-wide default does more harm than good. pr 23421. [roy fielding] 2.0.53 

*) add charset to *example* cgi *script*s.  [roy fielding] 2.0.53 

*) remove compiled-in upper limit on *limitrequestfields*ize. [bill stoddard] 2.0.53 

*) start keeping track of time-taken-to-process-request again for mod_status if *extendedstatus* is enabled. [jim jagielski] 2.0.53 

*) security: cve-2004-0885 (cve.mitre.org) mod_ssl: fix a bug which allowed an *sslciphersuite* setting to be bypassed during an ssl renegotiation.  pr 31505. [hartmut keil <hartmut.keil adnovum.ch>, joe orton] 2.0.53 

*) mod_ssl: fail at startup rather than segfault at runtime if a client cert is *config*ured with an encrypted private key. pr 24030.  [joe orton] 2.0.53 

*) mod_cache: *cachedisable* will only disable the urls it was meant to disable, not all caching. pr 31128. [edward rudd <eddie omegaware.com>, paul querna] 2.0.53 

*) fix the global *mutex* crash when the global *mutex* is never allocated due to disabled/empty caches. [jess holle <jessh ptc.com>] 2.0.52 

*) fix a segfault in the ldap cache when it is *config*ured switched off. [jess holle <jessh ptc.com>] 2.0.52 

*) security: cve-2004-0811 (cve.mitre.org) fix merging of the *satisfy* directive, which was applied to the surrounding context and could allow access despite *config*ured authentication.  pr 31315.  [rici lake <rici ricilake.net>] 2.0.52 

*) fix the handling of uris containing %2f when *allowencodedslashes* is enabled.  previously, such urls would still be rejected. [jeff trawick, bill stoddard] 2.0.52 

*) mod_log_*config*: fix a bug which prevented request completion time from being logged for i_insist_on_extra_cycles_for_clf_compliance processing.  pr 29696.  [alois treindl <alois astro.ch>] 2.0.51 

*) security: cve-2004-0747 (cve.mitre.org) fix buffer overflow in expansion of environment variables in *config*uration file parsing.  [andré malo] 2.0.51 

*) include directives no longer refuse to process symlinks on directories. instead there's now a maximum nesting level of included directories (128 as distributed). this is *config*urable at compile time using the -dap_max_include_dir_depth switch. pr 28492.  [andré malo] 2.0.51 

*) win32: apache -k start|restart|install|*config* can leave stranded piped logger processes (eg, rotatelogs.exe) due to improper server shutdown on these code paths. [bill stoddard] 2.0.51 

*) prevent cgi *script* output which includes a content-range header from being passed through the byterange filter.  [joe orton] 2.0.51 

*) *satisfy* directives now can be influenced by a surrounding *<limit*> container.  pr 14726.  [andré malo] 2.0.51 

*) mod_rewrite now officially supports *rewriterule*s in *<proxy*> sections. pr 27985.  [andré malo] 2.0.51 

*) mod_ssl: add "*sslusername*" directive to set r->user based on a chosen ssl environment variable.  pr 20957. [martin v. loewis <martin v.loewis.de>] 2.0.51 

*) *suexec*: pass the server_signature envvar through to cgis. [zvi har'el <rl math.technion.ac.il>] 2.0.51 

*) mod_*userdir*: ensure that the *userdir* identity is used for *suexec* *userdir* access in a virtual host which has *suexec* *config*ured. pr 18156.  [joshua slive] 2.0.51 

*) mod_rewrite no longer confuses the *rewritemap* caches if different maps defined in different virtual hosts use the same map name. pr 26462.  [andré malo] 2.0.51 

*) mod_*setenv*if: remove "support" for remote_user variable which never worked at all. pr 25725.  [andré malo] 2.0.51 

*) extend the *setenv*if directive to capture subexpressions of the matched value.  [andré malo] 2.0.51 

*) recursive include directives no longer crash. the server stops including *config*uration files after a certain nesting level (128 as distributed). this is *config*urable at compile time using the -dap_max_include_depth switch. pr 28370.  [andré malo] 2.0.51 

*) mod_dir: the trailing-slash behaviour is now *config*urable using the *directoryslash* directive.  [andré malo] 2.0.51 

*) allow proxying of resources that are invoked via *directoryindex*. pr 14648, 15112, 29961.  [andré malo] 2.0.51 

*) util_ldap: switched the lock types on the shared memory cache from thread reader/writer locks to global *mutex*es in order to provide cross process cache protection. [brad nicholes] 2.0.51 

*) enable the option to support *anonymous* shared memory in mod_ldap. this makes the cache work on linux again. [graham leggett] 2.0.51 

*) enable special *errordocument* value 'default' which restores the canned server response for the scope of the directive. [geoffrey young, andré malo] 2.0.51 

*) accept urls for the *serveradmin* directive. if the supplied argument is not recognized as an url, assume it's a mail address. pr 28174.  [andré malo, paul querna] 2.0.51 

*) mod_cgi: handle output on stderr during *script* execution on unix platforms; preventing deadlock when stderr output fills pipe buffer. also fixes case where stderr from nph- *script*s could be lost. pr 22030, 18348.  [joe orton, jeff trawick] 2.0.50 

*) mod_*alias* now emits a warning if it detects overlapping **alias** directives.  [andré malo] 2.0.50 

*) ap_set_sub_req_*protocol* and ap_finalize_sub_req_*protocol* are now exported on win32 and netware as well (minor mmn bump).  pr 28523. [edward rudd <eddie omegaware.com>, andré malo] 2.0.50 

*) *<virtualhost* myhost> now applies to all ip addresses for myhost instead of just the first one reported by the resolver.  this corrects a regression since 1.3.  [jeff trawick] 2.0.50 

*) util_ldap: allow relative paths for ldaptrustedca to be resolved against *serverroot* pr#26602 [brad nicholes] 2.0.50 

*) allow *requestheader* directives to be conditional. pr 27951. [vincent deffontaines <vincent gryzor.com>, andré malo] 2.0.50 

*) allow *limitrequestbody* to be reset to unlimited. pr 29106 [andré malo] 2.0.50 

*) fix a bunch of cases where the return code of the regex compiler was not checked properly. this affects: mod_*setenv*if, mod_usertrack, mod_proxy, mod_proxy_ftp and core. pr 28218.  [andré malo] 2.0.50 

*) mod_ssl: fix a potential segfault in the 'shmcb' *session* cache for small cache sizes.  pr 27751.  [geoff thorpe <geoff geoffthorpe.net>] 2.0.50 

*) regression from 1.3: at startup, *suexec* now will be checked for availability, the setuid bit and user root. the works only if httpd is compiled with the shipped apr version (0.9.5). pr 28287.  [andré malo] 2.0.50 

*) unix mpms: stop dropping connections when the file de*script*or is at least fd_setsize.  [jeff trawick] 2.0.50 

*) quotes cannot be used around require *group* and require dn directives, update the documentation to reflect this. also add quotes around the dn and *group* within debug messages, to make it more obvious why authentication is failing if quotes are used in error.  pr 19304.  [graham leggett] 2.0.50 

*) mod_ssl: fix memory leak in *session* cache handling.  pr 26562 [madhusudan mathihalli] 2.0.50 

*) fix crash when apache was started with no *listen* directives. [michael corcoran <mcorcoran warpsolutions.com>] 2.0.50 

*) core_output_filter: fix bug that could result in sending garbage over the network when module handlers construct bucket brigades containing multiple file buckets all referencing the same open file de*script*or. [bojan smojver] 2.0.50 

*) fix memory corruption problem with ap_custom_response() function. the core per-dir *config* would later point to request pool data that would be reused for different purposes on different requests. [jeff trawick, based on an old 1.3 patch submitted by will lowe] 2.0.50 

*) win32: tweak worker thread accounting routines to eliminate server hang when number of *listen* directives in httpd.conf is greater than or equal to the setting of *threadsperchild*. [bill stoddard] 2.0.49 

*) security: cve-2004-0174 (cve.mitre.org) fix starvation issue on *listen*ing sockets where a short-lived connection on a rarely-accessed *listen*ing socket will cause a child to hold the accept *mutex* and block out new connections until another connection arrives on that rarely-accessed *listen*ing socket. with apache 2.x there is no performance concern about enabling the logic for platforms which don't need it, so it is enabled everywhere except for win32.  [jeff trawick] 2.0.49 

*) win32: find_read_*listen*ers was not correctly handling multiple *listen*ers on the win32disableacceptex path.  [bill stoddard] 2.0.49 

*) fix bug in mod_usertrack when no *cookiename* is set.  pr 24483. [manni wood <manniwood planet-save.com>] 2.0.49 

*) remove compile-time length limit on request strings. length is now enforced solely with the *limitrequestline* *config* directive. [paul j. reder] 2.0.49 

*) mod_ssl: send the close alert message to the peer before closing the ssl *session*.  pr 27428.  [madhusudan mathihalli, joe orton] 2.0.49 

*) mod_log_*config*: fix corruption of buffered logs with threaded mpms.  pr 25520.  [jeff trawick] 2.0.49 

*) add fatal exception hook for use by diagnostic modules.  the hook is only available if the --enable-exception-hook *config*ure parm is used and the *enableexceptionhook* directive has been set to "on".  [jeff trawick] 2.0.49 

*) mod_*setenv*if: fix the regex optimizer, which under circumstances treated the supplied regex as literal string. pr 24219. [andré malo] 2.0.49 

*) mod_rewrite: catch an edge case, where strange subsequent *rewriterule*s could lead to a 400 (bad request) response.  [andré malo] 2.0.49 

*) add support for imt minor-type wildcards (e.g., text/*) to *expiresbytype*.  pr#7991  [ken coar] 2.0.49 

*) proxy_http fix: mod_proxy hangs when both *keepalive* and *proxyerroroverride* are enabled, and a non-200 response without a body is generated by the backend server. (e.g.: a client makes a request containing the "if-modified-since" and "if-none-match" headers, to which the backend server respond with status 304.) [graham wiseman <gwiseman fscinternet.com>, richard reiner] 2.0.49 

*) mod_ssl: fix potential segfault on lookup of ssl_*session*_id. pr 15057.  [otmar lendl <lendl nic.at>] 2.0.49 

*) mod_ssl: fix streaming output from an nph- cgi *script*. pr 21944 [joe orton] 2.0.49 

*) fix a long delay with cgi requests and *keepalive* connections on aix.  [jeff trawick] 2.0.49 

*) fix *rewritebase* directive to not add double slashes.  [andré malo] 2.0.49 

*) improve '*config*ure --help' output for some modules.  [astrid keßler] 2.0.49 

*) correct *usecanonicalname* off to properly check incoming port number. [jim jagielski] 2.0.49 

*) security: cve-2003-0020 (cve.mitre.org) escape arbitrary data before writing into the *errorlog*. unescaped *errorlog*s are still possible using the compile time switch "-dap_unsafe_error_log_unescaped".  [geoffrey young, andré malo] 2.0.49 

*) win32 mpm: implement *maxmemfree* to enable setting an upper limit on the amount of storage used by the bucket brigades in each server thread. [bill stoddard] 2.0.49 

*) complain via error_log when mod_include's includes filter is enabled, but the relevant *options* flag allowing the filter to run for the specific resource wasn't set, so that the filter won't silently get skipped. next remove itself, so the warning will be logged only once [stas bekman, jeff trawick, bill rowe] 2.0.49 

*) mod_info: html escape *config*uration information so it displays correctly. pr 24232. [thom may] 2.0.49 

*) restore the ability to add a de*script*ion for directories that don't contain an index file.  (broken in 2.0.48) [andré malo] 2.0.49 

*) fix a problem with the display of empty variables ("*setenv* foo") in mod_include.  pr 24734  [markus julen <mj zermatt.net>] 2.0.49 

*) mod_log_*config*: log the minutes component of the timezone correctly. pr 23642.  [hong-gunn chew <hgbug gunnet.org>] 2.0.49 

*) mod_expires: initialize *expiresdefault* to null instead of "" to avoid reporting an internal server error if it is used without having been set in the httpd.conf file. pr: 23748, 24459 [andré malo, liam quinn  <liam htmlhelp.com>] 2.0.49 

*) fix the inability to log errors like exec failure in mod_ext_filter/mod_cgi *script* children.  this was broken after such children stopped inheriting the error log handle. [jeff trawick] 2.0.49 

*) fix mod_info to use the real *config* file name, not the default *config* file name.  [aryeh katz <aryeh secured-services.com>] 2.0.49 

*) security: cve-2003-0789 (cve.mitre.org) mod_cgid: resolve some mishandling of the af_unix socket used to communicate with the cgid daemon and the cgi *script*. [jeff trawick] 2.0.48 

*) security: cve-2003-0542 (cve.mitre.org) fix buffer overflows in mod_*alias* and mod_rewrite which occurred if one *config*ured a regular expression with more than 9 captures. [andré malo] 2.0.48 

*) mod_include: fix segfault which occured if the filename was not set, for *example*, when processing some error conditions. pr 23836.  [brian akins <bakins web.turner.com>, andré malo] 2.0.48 

*) fix the *config* parser to support <foo>..</foo> containers (no arguments in the opening tag) supported by httpd 1.3. without this change mod_perl 2.0's <perl> sections are broken. ["philippe m. chiasson" <gozer cpan.org>] 2.0.48 

*) mod_cgid: fix a hash table corruption problem which could result in the wrong *script* being cleaned up at the end of a request.  [jeff trawick] 2.0.48 

*) update httpd-*.conf to be clearer in describing the connection between *addtype* and *addencoding* for defining the meaning of compressed file extensions. [roy fielding] 2.0.48 

*) ensure that ssl-std.conf is generated at *config*ure time, and switch to using the expanded *config* variables to work the same as httpd-std.conf pr: 19611 [thom may] 2.0.48 

*) mod_autoindex: if a directory contains a file listed in the *directoryindex* directive, the folder icon is no longer replaced by the icon of that file. pr 9587. [david shane holden <dpejesh yahoo.com>] 2.0.48 

*) mod_log_*config*: fix %b log format to write really "-" when 0 bytes were sent (e.g. with 304 or 204 response codes).  [astrid keßler] 2.0.48 

*) avoid an infinite recursion, which occured if the name of an included *config* file or directory contained a wildcard character. pr 22194. [andré malo] 2.0.48 

*) unix: handle permissions settings for flock-based *mutex*es in unixd_set_global|proc_*mutex*_perms().  allow the functions to be called for any type of *mutex*.  pr 20312  [jeff trawick] 2.0.48 

*) fix a misleading message from the some of the threaded mpms when maxclients has to be lowered due to the setting of *serverlimit*. [jeff trawick] 2.0.48 

*) lower the severity of the "*listen*er thread didn't exit" message to debug, as it is of interest only to developers.  pr 9011 [jeff trawick] 2.0.48 

*) mpms: the bucket brigades subsystem now honors the *maxmemfree* setting. [cliff woolley, jean-jacques clar] 2.0.48 

*) install *config*.nice into the build/ directory to make minor version upgrades easier. [joshua slive] 2.0.48 

*) mod_rewrite: ignore *rewriterule*s in .htaccess files if the directory containing the .htaccess file is requested without a trailing slash. pr 20195.  [andré malo] 2.0.48 

*) remember an authenticated user during internal *redirect*s if the *redirect*ion target is not access protected and pass it to *script*s using the *redirect*_remote_user environment variable. pr 10678, 11602.  [andré malo] 2.0.48 

*) don't respect the server header field as set by modules and cgis. as with 1.3, for proxy requests any such field is from the origin server; otherwise it will have our server info as controlled by the *servertokens* directive.  [jeff trawick] 2.0.47 

*) security: cve-2003-0192 (cve.mitre.org) fixed a bug whereby certain sequences of per-directory renegotiations and the *sslciphersuite* directive being used to upgrade from a weak ciphersuite to a strong one could result in the weak ciphersuite being used in place of the strong one. [ben laurie] 2.0.47 

*) security [vu#379828] prevent the server from crashing when entering infinite loops. the new *limitinternalrecursion* directive *config*ures limits of subsequent internal *redirect*s and nested subrequests, after which the request will be aborted.  pr 19753 (and probably others). [william rowe, jeff trawick, andré malo] 2.0.47 

*) core_output_filter: don't split the brigade after a flush bucket if it's the last bucket.  this prevents creating unneccessary empty brigades which may not be destroyed until the end of a *keepalive* connection. [juan rivera <juan.rivera citrix.com>] 2.0.47 

*) mod_cgid: eliminate a double-close of a socket.  this resolves various operational problems in a threaded mpm, since on the second attempt to close the socket, the same de*script*or was often already in use by another thread for another purpose. [jeff trawick] 2.0.47 

*) make mod_expires' *expiresbytype* work properly, including for dynamically-generated documents.  [ken coar, bill stoddard] 2.0.46 

*) *config*ure.in: play nice with libtool-1.5. [wilfredo sanchez] 2.0.46 

*) ssl *session* caching(shmht) : fix a segv problem with shmht *session* caching. pr 17864. [andreas leimbacher <andreasl67 yahoo.de>, madhusudan mathihalli] 2.0.46 

*) fixes for vpath builds; copying special.mk and any future .mk files from the source tree as well as the build tree (now creates a usable *config*uration for apxs), and eliminated redundant -i'nclude paths. [william rowe] 2.0.46 

*) linux 2.4+: if apache is started as root and you code *coredumpdirectory*, coredumps are enabled via the prctl() syscall. [greg ames] 2.0.46 

*) mod_log_*config*: add the ability to log the id of the thread processing the request via new %p formats.  [jeff trawick] 2.0.46 

*) use appropriate language codes for czech (cs) and traditional chinese (zh-tw) in default *config* files. pr 9427.  [andré malo] 2.0.46 

*) hook mod_rewrite's type checker before mod_mime's one. that way the *rewriterule* [t=...] flag should work as expected now. pr 19626. [andré malo] 2.0.46 

*) fix ap_construct_url() so that it surrounds ipv6 literal address strings with [].  this fixes certain types of *redirect*ion. pr 19207.  [jeff trawick] 2.0.46 

*) added *allowencodedslashes* directive to permit control of whether the server will accept encoded slashes ('%2f') in the uri path. default condition is off (the historical behaviour).  this permits environments in which the path-info needs to contain encoded slashes.  pr 543, 2389, 3581, 3589, 5687, 7066, 7865, 14639.  [ken coar] 2.0.46 

*) when using *redirect* in directory context, append requested query string if there's no one supplied by *config*uration. pr 10961. [andré malo] 2.0.46 

*) fixed a segfault when multiple *proxyblock* directives were used. pr: 19023 [sami tikka <sami.tikka f-secure.com>] 2.0.46 

*) security: cve-2003-0083 (cve.mitre.org) forward port: escape special characters (especially control characters) in mod_log_*config* to make a clear distinction between client-supplied strings (with special characters) and server-side strings. this was already introduced in version 1.3.25. [andré malo] 2.0.46 

*) mod_deflate: check also err_headers_out for an already set content-encoding: gzip header. this prevents gzip compressed content from a cgi *script* from being compressed once more. pr 17797. [andré malo] 2.0.45 

*) added an rpm build *script*. [graham leggett, joe orton <jorton redhat.com>] 2.0.45 

*) security:  eliminated leaks of several file de*script*ors to child processes, such as cgi *script*s.  this fix depends on the apr library release 0.9.2 or later (0.9.3 was distributed with the httpd source tarball for apache 2.0.45.)  pr 17206 [christian kratzer <ck cksoft.de>, bjoern a. zeeb <bz zabbadoz.net>] 2.0.45 

*) prevent endless loops of internal *redirect*s in mod_rewrite by aborting after exceeding a limit of internal *redirect*s. the limit defaults to 10 and can be changed using the rewrite*options* directive. pr 17462.  [andré malo] 2.0.45 

*) keep the subrequest filter in place when a subrequest is *redirect*ed.  pr 15423.  [jeff trawick] 2.0.45 

*) mod_deflate: extend the *deflatefilternote* directive to allow accurate logging of the filter's in- and outstream. [andré malo] 2.0.45 

*) allow ssl*mutex* to select/use the full range of apr locking mechanisms available to it. also, fix the bug that ssl*mutex* uses apr_lock_default no matter what.  pr 8122  [jim jagielski, martin kutschker <martin.t.kutschker blackbox.net>] 2.0.45 

*) mod_usertrack: don't set the cookie in subrequests. this works around the problem that cookies were set twice during fast internal *redirect*s. pr 13211.  [andré malo] 2.0.45 

*) use .sv instead of .se as extension for swedish documents in the default *config*uration. pr 12877.  [andré malo] 2.0.45 

*) mod_cgi, mod_cgid, mod_ext_filter: log errors when *script*s cannot be started on unix because of such problems as bad permissions, bad shebang line, etc.  [jeff trawick] 2.0.45 

*) fix segfault which occurred when a section in an included *config*uration file was not closed. pr 17093.  [andré malo] 2.0.45 

*) enhance the behavior of mod_isapi's writeclient() callback to provide better emulation for isapi modules that presume that the first writeclient() call may send status and headers.  an *example* of writeclient() abuse is the foxisapi module, which relies on that assumpion and now works.  [william rowe, milan kosina] 2.0.45 

*) while processing filters on internal *redirect*s, remember seen eos buckets also in the request structure of the *redirect* issuer(s). this prevents filters (such as mod_deflate) from adding garbage to the response. pr 14451.  [andré malo] 2.0.45 

*) *suexec*: be more pedantic when cleaning environment. clean it immediately after startup. pr 2790, 10449. [jeff stewart <jws purdue.edu>, andré malo] 2.0.45 

*) fix apxs to insert *loadmodule* directives only outside of sections. pr 8712, 9012.  [andré malo] 2.0.45 

*) fix *suexec* compile error under sunos4, where strerror() doesn't exist. pr 5913, 9977. [jonathan w miner <jonathan.w.miner lmco.com>] 2.0.45 

*) mod_auth_digest no longer tries to guess *authdigestdomain*, if it's not specified. now it assumes "/" as already documented. pr 16937. [andré malo] 2.0.45 

*) fix mod_cern_meta to not create empty *metafiles* when the metafile searched for does not exist.  pr 12353 [owen rees <owen_rees hp.com>] 2.0.45 

*) fix bug where '*satisfy* any' without an *authtype* lost all mime information (and more). related to pr 9076.  [andré malo] 2.0.45 

*) mod_file_cache: fixed a segfault when multiple *mmapfile* directives were used.  pr 16313.  [cliff woolley] 2.0.45 

*) use saner default *config* values for *suexec*. pr 15713. [thom may <thom planetarytramp.net>] 2.0.45 

*) mod_rewrite: allow "*rewriteengine* off" even if no "*options* followsymlinks" (or symlinksifownermatch) is set. pr 12395.  [andré malo] 2.0.45 

*) added character set support to mod_auth_ldap to allow it to convert extended characters used in the user id to utf-8 before authenticating against the ldap directory. the new directive authldapcharset*config* is used to specify the *config* file that contains the character set conversion table. [brad nicholes] 2.0.45 

*) mod_autoindex: bring forward the index*options* ignorecase option from apache 1.3.  pr 14276 [david shane holden <dpejesh yahoo.com>, william rowe] 2.0.44 

*) reorder the definitions for mod_ldap and mod_auth_ldap within *config*.m4 to make sure the parent mod_ldap is defined first. this ensures that mod_ldap comes before mod_auth_ldap in the httpd.conf file, which is necessary for mod_auth_ldap to load. pr 14256  [graham leggett] 2.0.44 

*) rename cachemaxstreamingbuffer to mcachemaxstreamingbuffer. move implementation of mcachemaxstreamingbuffer from mod_cache to mod_mem_cache. mcachemaxstreamingbuffer now defaults to the lesser of 100,000 bytes or mcachemaxcacheobjectsize. this should eliminate the need for explicitly coding mcachemaxstreamingbuffer in most *config*urations. [bill stoddard] 2.0.44 

*) mod_cache: fix pr 15113, a core dump in cache_in_filter when a *redirect* occurs. the code was passing a format string and integer to apr_pstrcat. changed to apr_psprintf. [paul j. reder] 2.0.44 

*) fix critical bug in new --enable-v4-mapped *config*ure option implementation which broke ipv4 *listen*ing sockets on some systems.  [hiroyuki hanai <hanai imgsrc.co.jp>] 2.0.44 

*) mod_*setenv*if: fix *browsermatch*nocase support for non-regex patterns [andré malo <nd perlig.de>] 2.0.44 

*) build: './*config*ure && make' now works without an in-tree apr and apr-util. [wilfredo sanchez] 2.0.44 

*) mod_log_*config*: allow '%%' escaping in *customlog* format strings to insert a literal, single '%'. [andré malo <nd perlig.de>] 2.0.44 

*) mod_autoindex: addde*script*ion directives for directories now work as in apache 1.3, where no trailing '/' is specified on the directory name.  previously, the trailing '/' *had* to be specified, which was incompatible with apache 1.3.  pr 7990  [jeff trawick] 2.0.44 

*) add --[enable|disable]-v4-mapped *config*ure option to control whether or not apache expects to handle ipv4 connections on ipv6 *listen*ing sockets.  either setting will work on systems with the ipv6_v6only socket option.  --enable-v4-mapped must be used on systems that always allow ipv4 connections on ipv6 *listen*ing sockets.  pr 14037 (bugzilla), pr 7492 (gnats) [jeff trawick] 2.0.44 

*) mod_*setenv*if: add server_addr special keyword to allow envariable setting according to the server ip address which received the request.  [ken coar] 2.0.44 

*) mod_cgid: terminate cgi *script*s when the client connection drops.  pr 8388  [jeff trawick] 2.0.44 

*) rearrange openssl engine initialization to support rand *redirect*ion on crypto accelerator. [frederic donnat <frederic.donnat zencod.com>] 2.0.44 

*) mod_isapi: fix an issue where the hse_req_done_with_*session* notification is received before the httpextensionproc() returns hse_status_pending.  this only affected isapi .dll's *config*ured with the *isapifakeasync* on directive.  pr 11918 [john desetto <jdesetto radiantsystems.com>, william rowe] 2.0.44 

*) improves the user friendliness of the *cacheroot* processing over my last pass. this version avoids the pool allocations but doesn't avoid all of the runtime checks. it no longer terminates during post-*config* processing. an error is logged once per worker, indicating that the *cacheroot* needs to be set. [paul j. reder] 2.0.44 

*) fix a bug where we keep files open until the end of a *keepalive* connection, which can result in: (24)too many open files: file permissions deny server access especially on threaded servers.  [greg ames, jeff trawick] 2.0.44 

*) the value emitted by *serversignature* now mimics the server http header as controlled by *servertokens*.  [francis daly <deva daoine.org>] 2.0.44 

*) terminate cgi *script*s when the client connection drops.  this fix only applies to some normal paths in mod_cgi.  mod_cgid is still busted.  pr 8388  [jeff trawick] 2.0.44 

*) fix a bug where 416 "range not satisfiable" was being returned for content that should have been *redirect*ed. [greg ames] 2.0.44 

*) fix streaming output from an nph- cgi *script*.  cgi:irc now works.  pr 8482  [jeff trawick] 2.0.44 

*) change the *cacheroot* processing to check for a required value at *config* time. this saves a lot of wasted processing if the mod_disk_cache module is loaded but no *cacheroot* was provided. this fix also adds code to log an error and avoid useless pallocs and procesing when the computed cache file name cannot be opened. this also updates the docs accordingly.  [paul j. reder] 2.0.44 

*) introduce the *enablesendfile* directive, allowing users of nfs shares to disable sendfile mechanics when they either fail outright or provide intermitantly corrupted data.  pr [william rowe] 2.0.44 

*) add the *proxybadheader* directive, which gives the admin some control on how mod_proxy should handle bogus http headers from proxied servers. this allows 2.0 to "emulate" 1.3's behavior if desired. [jim jagielski] 2.0.44 

*) fix a problem with streaming *script* output and mod_cgid. [jeff trawick] 2.0.44 

*) security: cve-2002-0840 (cve.mitre.org) html-escape the address produced by ap_server_signature() against this cross-site *script*ing vulnerability exposed by the directive '*usecanonicalname* off'.  also html-escape the server_name environment variable for cgi and ssi requests.  it's safe to escape as only the '<', '>', and '&' characters are affected, which won't appear in a valid hostname.  reported by matthew murphy <mattmurphy kc.rr.com>.  [brian pane] 2.0.43 

*) fix a core dump in mod_cache when it attemtped to store uncopyable buckets. this happened, for instance, when a file to be cached contained ssi tags to execute a cgi *script* (passed as a pipe bucket). [paul j. reder] 2.0.43 

*) fix a *mutex* problem in mod_ssl *session* cache support which could lead to an infinite loop.  pr 12705 [amund elstad <amund.elstad ergo.no>, jeff trawick] 2.0.43 

*) allow the *userdir* directive to accept a list of directories. this matches what apache 1.3 does.  also add documentation for this feature. [jay ball <jay veggiespam.com>] 2.0.43 

*) *suexec* needs to use the same default directory as the rest of server, namely /usr/local/apache2. [sangbeom han <sbhan os.korea.ac.kr>] 2.0.43 

*) the *protocol* version (eg: http/1.1) in the request line parsing is now case insensitive. [jim jagielski] 2.0.41 

*) allow **addoutputfilter*bytype* to add multiple filters per directive. [justin erenkrantz] 2.0.41 

*) add support for using fnmatch patterns in the final path segment of an include statement (eg.. include /foo/bar/*.conf). and remove the noise on stderr during *config* dir processing. [joe orton <jorton redhat.com>] 2.0.41 

*) add *modmimeusepathinfo* directive.  [justin erenkrantz] 2.0.41 

*) fix *fileetag*s none operation.  pr 12207. [justin erenkrantz, andrew ho <andrew tellme.com>] 2.0.41 

*) restored the experimental leader/followers mpm to working condition and converted its thread synchronization from *mutex*es to atomic cas.  [brian pane] 2.0.41 

*) win32: implement *threadlimit* directive in the windows mpm. [bill stoddard] 2.0.41 

*) remove cacheon *config* directive since it is set but never checked. no sense wasting cycles on unused code. besides, the only truly bug free code is deleted code. :)   [paul j. reder] 2.0.41 

*) bufferlogs are now run-time enabled, and the log_*config* now has 2 new callbacks to allow a 3rd party module to actually do the writing of the log file [ian holsman] 2.0.41 

*) correct *isapireadaheadbuffer* to default to 49152, per mod_isapi docs. [andré malo, astrid keßler <kess kess-net.de>] 2.0.41 

*) fix a null pointer dereference in the merge_env_dir_*config*s function of the mod_env module. pr 11791 [paul j. reder] 2.0.41 

*) new option to *servertokens* 'maj[or]'. only show the major version also surfaced this directive in the standard *config* (default full) [ian holsman] 2.0.41 

*) change mod_rewrite to use apr-util's dbm support for dbm rewrite maps.  the dbm type (e.g., ndbm, gdbm) can be specified on the *rewritemap* directive.  pr 10644  [jeff trawick] 2.0.41 

*) fixed mod_rewrite's *rewritemap* prg: support so that request/response pairs will no longer get out of sync with each other.  pr 9534 [cliff woolley] 2.0.41 

*) performance improvement for *keepalive* requests: when setting aside a small file for potential concatenation with the next response on the connection, set aside the file de*script*or rather than copying the file into the heap.  [brian pane] 2.0.41 

*) security: cve-2002-0661 (cve.mitre.org) close a very significant security hole that applies only to the win32, os2 and netware platforms.  unix was not affected, cygwin may be affected.  certain uris will bypass security and allow users to invoke or access any file depending on the system *config*uration.  without upgrading, a single .conf change will close the vulnerability.  add the following directive in the global server httpd.conf context before any other *alias* or *redirect* directives; *redirect*match 400 "\\\.\." reported by auriemma luigi <bugtest sitoverde.com>. [brad nicholes] 2.0.40 

*) security: cve-2002-0654 (cve.mitre.org) close a path-revealing exposure in cgi/cgid when we fail to invoke a *script*.  the modules would report "couldn't create child process /path-to-*script*/*script*.pl" revealing the full path of the *script*.  reported by jim race <jrace qualys.com>. [bill stoddard] 2.0.40 

*) mod-deflate now checks to make sure that 'gzip-only-text/html' is set to 1, so we can exclude things from the general case with *browsermatch*. [ian holsman, andre schild <a.schild aarboard.ch>] 2.0.40 

*) accept multiple leading /'s for requests within the *documentroot*. pr 10946  [william rowe, david shane holden <dpejesh yahoo.com>] 2.0.40 

*) restore the ability to specify host names on *listen* directives. pr 11030.  [jeff trawick, david shane holden <dpejesh yahoo.com>] 2.0.40 

*) when deciding on the default address family for *listen*ing sockets, make sure we can actually bind to an af_inet6 socket before deciding that we should default to af_inet6.  this fixes a startup problem on certain levels of openunix.  pr 10235.  [jeff trawick] 2.0.40 

*) changes to the internationalized error documents: comment them out in the default *config* file to make the default install as simple as possible; correct the english 500 error to be more understandable; add a swedish translation. [thomas sjogren <thomas northernsecurity.net>, erik abele <erik codefaktor.de>, rich bowen, joshua slive] 2.0.40 

*) increase the limit on file de*script*ors per process in apachectl. [brian pane] 2.0.40 

*) add a new directive: *maxmemfree*.  *maxmemfree* makes it possible to *config*ure the maximum amount of memory the allocators will hold on to for reuse.  anything over the *maxmemfree* threshold will be free()d.  this directive is useful when uncommon large peaks occur in memory usage.  it should _not_ be used to mask defective modules' memory use.  [sander striker] 2.0.40 

*) fixed the content-length filter so that http/1.0 requests to cgi *script*s would not result in a truncated response. [ryan bloom, justin erenkrantz, cliff woolley] 2.0.40 

*) fix a long-standing bug in 2.0, cgi *script*s were being called with relative paths instead of absolute paths.  apache 1.3 used absolute paths for everything except for *suexec*, this brings back that standard.  [ryan bloom] 2.0.40 

*) fix infinite loop due to two http_in filters being present for internally *redirect*ed requests.  pr 10146.  [justin erenkrantz] 2.0.40 

*) switch conn_rec->*keepalive* to an enumeration rather than a bitfield. [justin erenkrantz] 2.0.40 

*) support winnt cgi invocation through **script*interpretersource* 'registry' for *script* interpreter paths and names with non-ascii characters in the executable filepath.  [william rowe] 2.0.40 

*) mod_rewrite can now set cookies  (*rewriterule* (.*) - [co=name:$1:.domain]) [brian degenhardt <bmd mp3.com>, ian holsman] 2.0.40 

*) we must set the mime-type for .shtml files to text/html if we want them to be parsed for ssi tags.  add the *config* for that to the default *config* file so that it is easier to enable .shtml parsing. [dave dyer <ddyer real-me.net>] 2.0.38 

*) make the default_handler catch all requests that aren't served by another handler.  this also gets us to return a 404 if a directory is requested, there is no *directoryindex*, and mod_autoindex isn't loaded.  [justin erenkrantz] 2.0.38 

*) allow 'make install destdir=/path'.  this allows packagers to install into a directory different from the one that was *config*ured.  this also mirrors the root= feature from 1.3.  we cannot use prefix=, because both apr and apr-util resolve their installation paths at *config*uration time.  this means that there is no variable prefix to replace.  [andreas hasenack <andreas netbank.com.br>] 2.0.38 

*) aix 4.3.2 and above: define single_*listen*_unserialized_accept. these levels of aix don't have a thundering herd problem with accept().  [jeff trawick] 2.0.38 

*) prefork mpm: ignore *mutex* errors during graceful restart.  for certain types of *mutex*es (particularly sysv semaphores), we should expect to occasionally fail to obtain or release the *mutex* during restart processing.  [jeff trawick] 2.0.38 

*) fix install-bindist.sh so that it finds any perl instead of just early perl 5.x versions.  this is consistent with a build/install from source, and it allows the perl *script*s installed by a bindist to work on systems with perl 5.6.  [jeff trawick] 2.0.38 

*) allow cgi *script*s to return their content-length.  this also fixes a hang on head requests seen on certain platforms (such as freebsd). [justin erenkrantz] 2.0.38 

*) allow post method over ssl when per-directory client cert authentication is used with 'ssl*options* +optrenegotiate' enabled and a client cert was found in the ssl *session* cache. 2.0.37 

*) 'ssl*options* +optrengotiate' will use client cert in from the ssl *session* cache when there is no cert chain in the cache.  prior to the fix this situation would result in a forbidden response and error message "cannot find peer certificate chain" [doug maceachern] 2.0.37 

*) ap_finalize_sub_req_*protocol*() shouldn't send an eos bucket if one was already sent.  pr 9644  [jeff trawick] 2.0.37 

*) fix the display of the default name for the mime types *config* file.  pr 9729  [matthew brecknell <mbrecknell orchestream.com>] 2.0.37 

*) fix the working directory *for winnt/2k/xp services only* to change to the apache directory (one level above the location of apache.exe, in the case that apache.exe resides in bin/.) solves the case of *serverroot* /foo paths where /foo was not on the same drive as /winnt/system32.  [william rowe] 2.0.37 

*) make 2.0's "accept*mutex*" startup message now "completely" match how 1.3 does it. [jim jagielski] 2.0.37 

*) fix apxs to allow "apxs -q installbuilddir" and to allow querying certain other variables from *config*_vars.mk.  pr 9316 [jeff trawick] 2.0.37 

*) remove all special mod_ssl uris.  this also fixes the bug where *redirect*ing (.*) will allow an ssl protected page to be viewed without ssl.  [ryan bloom] 2.0.37 

*) fix the binary build install *script* so that the build logic created by "apxs -g" will work when the user has a binary build.  [jeff trawick] 2.0.37 

*) netware: piping log entries through rotatelogs using the *customlog*s directive is finally supported now that we have the pipes and spawning functionality working. [brad nicholes] 2.0.37 

*) allow *rewritemap* prg:'s to take command-line arguments.  pr 8464. [james tait <jtait wyrddreams.demon.co.uk>] 2.0.37 

*) apachectl passes through any httpd *options*.  note: apachectl should be used in preference to httpd since it ensures that any appropriate environment variables have been set up. [jeff trawick] 2.0.37 

*) fix the combination of mod_cgid, mod_setuexec, and mod_*userdir*. pr 7810  [colm maccarthaigh <colmmacc redbrick.dcu.ie>] 2.0.37 

*) fix *suexec* execution of cgi *script*s from mod_include. pr 7791, 8291  [colm maccarthaigh <colmmacc redbrick.dcu.ie>] 2.0.37 

*) fix segfaults at startup on some platforms when mod_auth_digest, mod_*suexec*, or mod_ssl were used as dso's due to the way they were tracking the current init phase since dso's get completely unloaded and reloaded between phases.  pr 9413. [tsuyoshi sasamoto <nazonazo super.win.ne.jp>, brad nicholes] 2.0.37 

*) fix an unusual set of ./*config*ure arguments that could cause mod_http to be built as a dso, which it currently doesn't support.  pr 9244. [cliff woolley, robin johnson <robbat2 orbis-terrarum.net>] 2.0.37 

*) win32: fix bug in apr_sendfile() that caused incorrect operation of the %x, %b and %b *logformat* *options*. pr 8253, 8996. [bill stoddard] 2.0.37 

*) remove ssllog and ssl*loglevel* directives in favor of having mod_ssl use the standard *errorlog* directives.  [justin erenkrantz] 2.0.37 

*) mod_isapi: all mod_isapi directives, excluding isapi*cachefile*, may now be specified to the <file/directory > container, rather than by vhost.  [william rowe] 2.0.37 

*) added *enablemmap* *config* directive to enable the server administrator to disable memory-mapping of delivered files on a per-directory basis.  [brian pane] 2.0.37 

*) performance enhancements for mod_*setenv*if  [brian pane] 2.0.37 

*) reverse the hook ordering for mod_*userdir* and mod_*alias* so that *alias*/*script**alias* will override *userdir*.  pr 8841 [joshua slive] 2.0.37 

*) fix mod_rewrite hang when apr uses sysv semaphores and rewrite*loglevel* is set to anything other than 0.  pr: 8143 [aaron bannert, cliff woolley] 2.0.37 

*) allow mod_rewrite's set of "int:" internal *rewritemap* functions to be extended by third-party modules via an optional function. [tahiry ramanamampanoharana <nomentsoa hotmail.com>, cliff woolley] 2.0.37 

*) fix generated httpd.conf to respect layout for *loadmodule* lines. pr 8170.  [thom may <thom planetarytramp.net>] 2.0.37 

*) reverted a minor optimization in mod_ssl.c that used the vhost id as the *session* id context rather that a md5 hash of that vhost id, because it caused very long vhost id's to be unusable with mod_ssl. pr 8572.  [cliff woolley] 2.0.36 

*) fix the link to the de*script*ion of the *coredumpdirectory* directive in the server-wide document.  pr 8643.  [jeff trawick] 2.0.36 

*) fixed shmcb *session* caching.  [aaron bannert, cliff woolley] 2.0.36 

*) synced with remaining changes from mod_ssl 2.8.8-1.3.24: - avoid sigbus on sparc machines with shmcb *session* caches - allow whitespace between the pipe and the name of the program in ssllog "| /path/to/program".  [cliff woolley] 2.0.36 

*) changes to the worker mpm's queue management and thread synchronization code to reduce *mutex* contention  [brian pane] 2.0.36 

*) don't install *.in *config*uration files since we already install *-std.conf files.  [aaron bannert] 2.0.36 

*) fix subreqs that are promoted via fast_*redirect* from having invalid frec->r structures.  this would cause subtle errors later on in request processing such as seen in pr 7966.  [justin erenkrantz] 2.0.36 

*) fix *suexec* behavior with user directories.  pr 7810. [colm <colmmacc redbrick.dcu.ie>] 2.0.36 

*) reject a blank *userdir* directive since it is ambiguous.  pr 8472. [justin erenkrantz] 2.0.36 

*) fix win32 'short name' *alias*es in httpd.conf directives. pr 8009  [william rowe] 2.0.36 

*) fix perchild mpm so that it can be *config*ured with the move to the experimental directory.  [scott lamb <slamb slamb.org>] 2.0.36 

*) fix perchild mpm so that it uses ap_gname2id for *group*s instead of ap_uname2id. [scott lamb <slamb slamb.org>] 2.0.36 

*) fix *acceptpathinfo*. pr 8234  [cliff woolley] 2.0.36 

*) security: cve-2002-1592 (cve.mitre.org) [cert vu#165803] added the aplog_toclient flag to ap_log_rerror() to explicitly tell the server that warning messages should be sent to the client in addition to being recorded in the error log. prior to this change, ap_log_rerror() always sent warning messages to the client. in one case, a faulty cgi *script* caused the server to send a warning message to the client that contained the full path to the cgi *script*. this could be considered a minor security exposure. [bill stoddard] 2.0.36 

*) moved the call to apr_mmap_dup outside the error branch so that it would actually get called. this fixes a core dump at init everytime you use the *mmapfile* directive. pr 8314 [paul j. reder] 2.0.36 

*) trigger an error when a *loadmodule* directive attempts to load a module which is built-in.  this is a common error when switching from a dso build to a static build.  [jeff trawick] 2.0.36 

*) allow vpath builds to succeed when *config*ured from an empty directory.  [thom may <thom planetarytramp.net>] 2.0.36 

*) merge in latest gnu *config*.guess and *config*.sub files.  pr 7818. [justin erenkrantz] 2.0.36 

*) properly *substitute* sbindir as httpd's location in apachectl.  pr 7840. [andreas hasenack <andreas netbank.com.br>] 2.0.36 

*) allow win32 shebang *script*s to follow the path (or omit the .exe suffix from the shebang command), and allow **script*interpretersource* registry or registrystrict to override shebang lines, as 1.3 did. pr 8004  [william rowe] 2.0.36 

*) worker mpm: fix a situation where a child exited without releasing the accept *mutex*.  depending on the os and *mutex* mechanism this could result in a hang.  [jeff trawick] 2.0.36 

*) update the instructions for how to get started with mod_*example*. [stas bekman] 2.0.36 

*) fix *pidfile* to default to rel_runtimedir instead of rel_logfiledir.  pr 7841.  [andreas hasenack <andreas netbank.com.br>] 2.0.36 

*) win32: fix problem that caused rapid performance degradation when number of connecting clients exceeded *threadsperchild*. [bill stoddard] 2.0.36 

*) proxy was bombing out every second *keepalive* request, caused by a stray crlf before the second response's status line. proxy now tries to read one more line if it encounters a crlf where it expected a status. pr 10010 [graham leggett] 2.0.36 

*) deprecated the apr_lock.h api. please see the following files for the improved thread and process locking and signaling: apr_proc_*mutex*.h, apr_thread_*mutex*.h, apr_thread_rwlock.h, apr_thread_cond.h, and apr_global_*mutex*.h.  [aaron bannert] 2.0.36 

*) remind the admin about the user and *group* directives when we are unable to set permissions on a semaphore.  pr 7812  [jeff trawick] 2.0.36 

*) fix *proxypass* when frontend is https and backend is http [doug maceachern] 2.0.36 

*) mod_rewrite: updated to use the new apr global *mutex* type. [aaron bannert] 2.0.35 

*) worker, prefork, perchild, beos mpms: add -dforeground switch to cause the apache parent process to run in the foreground (similar to -dno_detach except that it doesn't switch *session* ids). [jeff trawick] 2.0.35 

*) added support for posix semaphore *mutex* locking (accept*mutex* posixsem) for those platforms that support it. if using the default implementation, this is between pthread and sysvsem in priority. this implies it's the new default for darwin. [jim jagielski] 2.0.35 

*) worker mpm: don't create a *listen*er thread until we have a worker thread.  otherwise, in situations where we'll have to wait a while to take over scoreboard slots from a previous generation, we'll be accepting connections we can't process yet.  [jeff trawick] 2.0.35 

*) don't allow initialization to succeed if we can't get a socket corresponding to one of the *listen* statements.  [jeff trawick] 2.0.34 

*) allow all perchild directives to accept either numerical uid/gid or logical user/*group* names.  [scott lamb <slamb slamb.org>] 2.0.34 

*) implement ssl proxy to support *proxypass* / https:// and the sslproxy* directives [doug maceachern] 2.0.34 

*) [apr-related] the ordering of the default accept *mutex* method has been changed to better match what's done in apache 1.3. the ordering is now (highest to lowest): pthread -> sysvsem -> fcntl -> flock. [jim jagielski] 2.0.34 

*) added exp_foo and rel_foo variables to *config*_vars.mk for all apache and autoconf path variables (like --sysconfdir, --sbindir, etc). exp_foo is the "expanded" version, which means that all internal variable references have been interpolated. rel_foo is the same as $exp_foo, only relative to $prefix if they share a common path.  [aaron bannert] 2.0.34 

*) be more vocal about what accept*mutex* values we allow, to make us closer to how 1.3 does it. [jim jagielski] 2.0.34 

*) get nph- cgi *script*s working again.  prs 8902, 8907, 9983 [jeff trawick] 2.0.34 

*) add accessor function to set r->content_type. from now on, ap_rset_content_type() should be used to set r->content_type. this change is required to properly implement the **addoutputfilter*bytype* *config*uration directive. [bill stoddard, sander striker, ryan bloom] 2.0.34 

*) change *config*ure so that solaris 8 and above have single_*listen*_unserialized_accept defined by default. according to sun people solaris 8+ doesn't have a thundering herd problem [ian holsman] 2.0.34 

*) allow uris specifying cgi *script*s to include '/' at the end (e.g., /cgi-bin/printenv/) on aix and solaris (and other oss which ignore '/' at the end of the names of non-directories). pr 10138  [jeff trawick] 2.0.34 

*) implement ssl*session*cache shmht and shmcb based on apr_rmm and apr_shm.  [madhusudan mathihalli <madhusudan_mathihalli hp.com>] 2.0.34 

*) fix apxs -g handling.  move *config*_vars.mk from the top build directory to the build directory.  pr 10163  [jeff trawick] 2.0.34 

*) add a missing manualdir entry in the debian *config*.layout. [thom may <thom planetarytramp.net>] 2.0.34 

*) new directive proxyio*buffersize*. sets the size of the buffer used when reading from a remote http server in proxy. [graham leggett] 2.0.34 

*) modify receive/send loop in proxy_http and proxy_ftp so that should it be necessary, the remote server socket is closed before transmitting the last buffer (set by proxyio*buffersize*) to the client. this prevents the backend server from being forced to hang around while the last few bytes are transmitted to a slow client. fix the case where no error checking was performed on the final brigade in the loop. [graham leggett] 2.0.34 

*) scrap *cachemaxexpire*min and *cachedefaultexpire*min. change *cachemaxexpire* and *cachedefaultexpire* to use seconds rather than hours. [graham leggett, bill stoddard] 2.0.34 

*) new directive ssi*undefine*decho. to change the '(none)' echoed for a *undefine*d variable. [ian holsman] 2.0.34 

*) proxy http and connect: keep trying other addresses from the dns when we can't get a socket in the specified address family.  we may have gotten back an ipv6 address first and yet our system is not *config*ured to allow ipv6 sockets.  [jeff trawick] 2.0.34 

*) add a missing errordir entry in the debian *config*.layout. pr: 10067 [dirk-jan faber <dirk-jan selwerd.nl>, aaron bannert, thom may <thom planetarytramp.net>] 2.0.34 

*) rename the filter ordering priorities.  the recent filtering fixes have showcased problems with their usage.  therefore, we need to rename them to increase the clarity.  (content->resource, http_header->content_set/*protocol*)  [justin erenkrantz] 2.0.33 

*) new directive for mod_proxy: *proxyremote*match. this provides regex pattern matching for the determination of which requests to use the remote proxy for. [jim jagielski] 2.0.33 

*) fix *customlog* bytes-sent with http 0.9.  [justin erenkrantz] 2.0.33 

*) prevent apache from ignoring sighup due to some lingering 1.3 cruft in piped logs and *rewritemap* child processes. [william rowe] 2.0.33 

*) all instances of apr_lock_t have been removed and converted to one of the following new lock apis: apr_thread_*mutex*.h, apr_proc_*mutex*.h, or apr_global_*mutex*.h. no new code should use the apr_lock.h api, as the old api will soon be deprecated. [aaron bannert] 2.0.33 

*) fix for multiple file buckets on win32, where the first file bucket would cause the immediate closure of the socket on any non-*keepalive* requests.  [ryan morgan <rmorgan covalent.net>] 2.0.33 

*) convert mod_auth_digest to use the new apr_global_*mutex*_t type.  [aaron bannert] 2.0.33 

*) worker mpm: improve logging of errors with the interface between the *listen*er thread and worker threads.  [jeff trawick] 2.0.33 

*) introduce **addoutputfilter*bytype* directive.  [justin erenkrantz] 2.0.33 

*) fix incorrect check for *script*_in in mod_cgi.  pr 9669. [david mackenzie <djm pix.net>] 2.0.33 

*) fix segfault and display error when ssl*mutex* file can not be created.  [adam sussman <myddryn vishnu.vidya.com>] 2.0.33 

*) change the verbage on the *scoreboardfile* in our default *config*s. also change the default to be commented out (unspecified) so we get *anonymous* shared memory by default.  [aaron bannert] 2.0.33 

*) implement new *scoreboardfile* directive logic. this affects how we create the scoreboard's shared memory segment. if the directive is present, a name-based segment is created. if the directive is not present, first an *anonymous* segment is created, and if that fails, a name-based segment is created from a file of the name default_scoreboard. this gives third-party applications the ability to access our scoreboard.  [aaron bannert] 2.0.33 

*) fix ap_directory_merge() to correctly merge *config*s when there is no *<directory* /> block.  [justin erenkrantz, william rowe] 2.0.33 

*) performance: reuse per-connection trans*action* pools in the worker mpm, rather than destroying and recreating them.  [brian pane] 2.0.33 

*) mod_negotiation: *force*languagepriority** now uses 'prefer' as the default if the directive is not specified.  this mirrors older behavior without changes to the httpd.conf.  [william rowe] 2.0.32 

*) allow statically linked support binaries with the new --enable-static-support flag, and enable this behavior in the binbuild *script*. also add a new --enable-static-htdbm flag.  [aaron bannert] 2.0.32 

*) be a bit more sane with regard to canonicalnames.  if the user has specified they want to use the canonicalname, but they have not *config*ured a port with the *servername*, then use the same port that the original request used. [ryan bloom and ken coar] 2.0.32 

*) *suexec*: allow https and ssl_* environment variables to be passed through to cgi *script*s. pr 9163 [brian reid <breid *customlog*ic.com>, zvi har'el <rl math.technion.ac.il>] 2.0.32 

*) apxs: ltflags envvar can override default libtool *options*.  try "ltflags=' ' apxs -c mod_foo.c" to see what libtool does under the covers.  [jeff trawick] 2.0.32 

*) the location: response header field, used for external *redirect*, *must* be an absoluteuri.  the *redirect* directive tested for that, but *redirect*match didn't -- it would allow almost anything through.  now it will try to turn an abs_path into an absoluteuri, but it will correctly varf like *redirect* if the final *redirect*ion target isn't an absoluteuri.  [ken coar] 2.0.31 

*) add a *timeout* option to the proxy code 'proxy*timeout*' [ian holsman] 2.0.31 

*) ftp directory listings are now always retrieved in ascii mode. the ftp proxy properly escapes uri's and html in the generated listing, and escapes the path components when talking to the ftp server. it is now possible to browse the root directory by using a url like:   ftp://user@host/%2f/ (ported from apache_1.3.24) also, the last path component may contain wildcard characters '*' and '?', and if they do, a directory listing is created instead of a file retrieval. *example*: ftp://user@host/httpd/server/*.c [martin kraemer] 2.0.31 

*) added single-*listen*er unserialized accept support to the worker mpm [brian pane] 2.0.31 

*) new directive for mod_proxy: '*proxypreservehost*'. this passes the incoming host header through to the proxied server [geoff <g.russell ieee.org>] 2.0.31 

*) new directive option for *proxypass*. it now can block a location from being proxied [jukka pihl <jukka.pihl entirem.com>] 2.0.31 

*) change the pre_*config* hook to return a value. modules can now emit an error message and then cause the server to quit gracefully during startup. this required a bump to the mmn.  [aaron bannert] 2.0.31 

*) fix some unix socket de*script*or leaks in the handler side of mod_cgid (the part that runs in the server process).  whack a silly "close(-1)" in the handler too.  [jeff trawick] 2.0.31 

*) fixed path_info and query_string from mod_negotiation results. resolves the common case of using negotation to resolve the request /*script*/foo for /*script*.cgi/foo.  [william rowe] 2.0.31 

*) do not install unnecessary pcre headers like *config*.h and internal.h. [joe orton <joe manyfish.co.uk>] 2.0.31 

*) fix a problem in the parsing of the *<proxy* foo> directive. [jeff trawick] 2.0.31 

*) clear the output socket de*script*or in unixd_accept() to make sure we don't supply a bogus socket to the caller if the accept fails. this caused problems with the worker mpm, which tried to process the returned socket if it was non-null.  [brian pane] 2.0.31 

*) add *fileetag* directive to allow *config*urable control of what data are used to form etag values for file-based uris.  mmn bumped to 20020111 because of fields added to the end of the core_dir_*config* structure.  [ken coar] 2.0.31 

*) fix a segfault in mod_rewrite's logging code caused by passing the wrong *config* to ap_get_remote_host().  [jeff trawick] 2.0.31 

*) fixed a segfault that happened during graceful shutdown (or when the httpd ran out of file de*script*ors) with the worker mpm [brian pane] 2.0.31 

*) split all win32 modules [excluding the core components mod_core, mod_so, mod_win32 and the winnt mpm] into individual loadable modules, so the administrator may individually disable the former compiled-in modules by simply commenting out their *loadmodule* directives.  [william rowe] 2.0.31 

*) mod_ssl adjustments to help with using toolkits other than openssl: use ssl functions/macros instead of directly dereferencing ssl structures wherever possible. add type-casts for the cases where functions return a generic pointer. add $ssl/include to *config*ure search path. [madhusudan mathihalli <madhusudan_mathihalli hp.com>] 2.0.31 

*) fix *sslpassphrasedialog* exec: and *sslrandomseed* exec: [doug maceachern] 2.0.30 

*) fix a typo in mod_deflate's m4 *config* section. [albert chin <china thewrittenword.com>] 2.0.30 

*) fix the module identifer as shown in the docs for various core modules (e.g., the identifer for mod_log_*config* was previously listed as *config*_log_module).  pr #9338 [james watson <ap2bug sowega.org>] 2.0.30 

*) fix *limitrequestbody* directive by placing it in the http filter.  [justin erenkrantz] 2.0.30 

*) introduced the *force*languagepriority** directive, to prevent returning multiple_choices or none_acceptable in some cases, when using multiviews.  [william rowe] 2.0.30 

*) fix a problem which prevented mod_cgid and *suexec* from working together reliably [greg ames] 2.0.30 

*) remove the call to exit() from within mod_auth_digest's post_*config* phase.  [aaron bannert] 2.0.30 

*) win32: fix bug that could cause cgi *script*s with query_strings to fail. [bill stoddard] 2.0.30 

*) move any load library path environment variables out of apachectl and into a separate environment variable file which can be more easily tailored by the admin.  the environment variable file as built by apache may have additional system- specific settings.  for *example*, on os/390 we tailor the heap settings to allow lots of threads.  [jeff trawick] 2.0.30 

*) the pod no longer assumes the child is *listen*ing on 127.0.0.1 and now pulls the first hostname in the list of *listen*ers to perform the dummy connect on. this fixes a bug when the user had *config*ured the *listen* directive for an ip other than 127.0.0.1. this would result in undead children and error messages such as "connection refused: connect to *listen*er". [aaron bannert] 2.0.30 

*) change make install and apxs -i processing of dso modules to perform special handling on platforms where libtool doesn't install mod_foo.so.  this fixes some wonkiness on hp-ux, tru64, and aix which prevented standard *loadmodule* statements from working. [jeff trawick] 2.0.30 

*) resolved segfault in mod_isapi when *config*uring with isapi*cachefile*. pr 8563, 8919  [william rowe] 2.0.30 

*) add back in the "*suexec* mechanism enabled (wrapper: /path/to/*suexec*)" message that we had back in apache-1.3 and still have scattered throughout our docs.  [aaron bannert] 2.0.30 

*) change post_*config* hook to return a value, allowing you to flag a error post *config* [ian holsman, jeff trawick] 2.0.29 

*) allow *suexec*_bin (the path to the *suexec* binary that is hard-coded into the server) to be specified to the *config*ure *script* by the --with-*suexec*-bin parameter.  [aaron bannert] 2.0.29 

*) bail out at *config*ure time if an invalid mpm was specified. [jean-frederic clere <jfrederic.clere fujitsu-siemens.com>] 2.0.29 

*) prevent segv in ap_note_basic_auth_failure() when no *authname* is *config*ured [john sterling <sterling covalent.net>] 2.0.29 

*) fixed the behavior of the *xbithack* directive. [taketo kabe <kabe sra-tohoku.co.jp>, cliff woolley] pr#8804 2.0.29 

*) fix a file de*script*or leak in mod_include.  when we include a file, we use a sub-request, but we didn't destroy the sub-request immediately, instead we waited until the original request was done.  this patch closes the sub-request as soon as the data is done being generated.  [brian pane <bpane pacbell.net>] 2.0.29 

*) allow modules that add sockets to the ap_*listen*ers list to define the function that should be used to accept on that socket.  each mpm can define their own function to use for the accept function with the mpm_accept_func macro.  this also abstracts out all of the unix accept error handling logic, which has become out of synch across unix mpms. [ryan bloom] 2.0.29 

*) fix a bug which would cause the response headers to be omitted when sending a negotiated *errordocument* because the required filters were attached to the wrong request_rec. [john sterling <sterling covalent.net>] 2.0.29 

*) add '*redirect*-carefully' environment option to disable sending *redirect*s under special circumstances.  this is helpful for microsoft's webfolders when accessing a directory resource via dav methods.  [justin erenkrantz] 2.0.29 

*) really reset the maxclients value in worker and threaded when the *config*ured value is not a multiple of the number of threads per child.  we said we did previously but we forgot to. [jeff trawick] 2.0.29 

*) if shared modules are requested and mod_so is not available, produce a fatal *config*-time error.  [justin erenkrantz] 2.0.29 

*) when no port is given in a "*servername* host" directive, the server_rec->port is now set to zero, not 80. that allows for run-time deduction of the correct server port (depending on ssl/plain, and depending also on the current setting of *usecanonicalname*). this change makes *redirect*ions work, even with https:// connections. as in apache-1.3, the connection's actual port number is never used, only the *servername* setting or the client's host: setting. documentation updated to reflect the change. [martin kraemer] 2.0.28 

*) introduce an apache mod_ssl initial *config*uration template (ssl.conf, generated from ssl-std.conf).  [ralf s. engelschall] 2.0.27 

*) add the support/checkgid helper app, which checks the run-time validity of *group* identifiers usable in the *group* directive. [ken coar] 2.0.27 

*) various --enable-so *options* have been fixed: --enable-so is treated as "static"; explicit --enable-so=shared issues an error; and explicit --enable-so fails with error on systems without apr_has_dso.  [aaron bannert] 2.0.27 

*) fix some bungling of the remote port in rfc1413.c so that *identitycheck* retrieves the proper user id instead of failing and thus always returning "nobody." [dick streefland <dick.streefland xs4all.nl>] 2.0.27 

*) simplified mod_env's directives to behave as most directives are expected, in that un*setenv* will not unset a *setenv* and *passenv* directive following that un*setenv* within the same container. also provides a runtime startup warning if a *passenv* *config*ured environment value is *undefine*d.  [william rowe] 2.0.27 

*) the worker mpm is now completely ported to apr's new lock api. it uses native apr types for thread *mutex*es, cross-process *mutex*es, and condition variables.  [aaron bannert] 2.0.27 

*) exit when we can't *listen* on any of the *config*ured ports.  this is the same behavior as 1.3, and it avoids having the mpms to deal with bogus ap_*listen*_rec structures.  [jeff trawick] 2.0.27 

*) introduce the *multiviewsmatch* directive, to allow the operator to be flexible in recognizing handlers and filters filename extensions as part of the multiviews matching logic, strict with *multiviewsmatch* negotiatedonly to accept only filename extentions that designate negotiated parameters, (content type, charset, etc.) or multiviewsall for the 1.3 behavior of matching any files, even if they have unregistered extensions.  [william rowe] 2.0.26 

*) fixed the *config*ure *script* to add a *loadmodule* directive to the default httpd.conf for any module that was compiled as a dso.  [aaron bannert <aaron clove.org>] 2.0.26 

*) prefork: don't segfault when we are able to *listen* on some but not all of the *config*ured ports.  [jeff trawick] 2.0.26 

*) introduce ap_directory_walk rewrite (with further optimizations required) to adapt to the ap_process_request_internal() changes. optimized so subrequests and *redirect*s now reuse previous section merges, until we mismatch with the original directory_walk, and precomputed r->finfo results will cause directory_walk to skip the most expensive phases of the function.  [william rowe] 2.0.26 

*) remove the port directive.  in it's place, the *listen* directive is now a required directive, which tells apache what port to *listen* on.  the *servername* directive has also been extended to accept an optional port.  if the port is specified to the *servername*, the server will report that port whenever it reports the port that it is *listen*ing on.  this change was made to ease *config*uration errors that stem from having a port directive, and a *listen* directive.  in that situation, the server would only *listen* to the port specified by the *listen* command, which caused a lot of confusion to users.  [ryan bloom] 2.0.26 

*) added mod_mime_magic, mod_unique_id and mod_vhost_*alias* to the win32 build, as loadable modules.  [william rowe] 2.0.26 

*) allow *config*ure help strings to work with autoconf 2.50+ and 2.13. [justin erenkrantz] 2.0.26 

*) some style changes to the code that does *proxyerroroverride*. fixed *config* merge behaviour. [graham leggett] 2.0.26 

*) switch proc_pthread accept*mutex* *config*uration directive to pthread to be consistent with 1.3.  [justin erenkrantz] 2.0.26 

*) cleanup the worker mpm.  we no longer re-use trans*action* pools.  this incurs less overhead than shuffling the pools around so that they can be re-used.  remove one of the queue's condition variables.  we just redefined the api to state that you can't try to add more stuff than you allocated segments for.  [aaron bannert <aaron clove.org>] 2.0.26 

*) remove the win32 *script*-processing exception from mod_cgi, and roll build_command_line/build_argv_list into a unified, overrideable ap_cgi_build_command optional function.  [william rowe] 2.0.26 

*) fix a seg fault in mod_include.  when we are generating an internal *redirect*, we must set r->uri to "", not a bogus string, and not null.  [ryan bloom] 2.0.26 

*) optimized location_walk, so subrequests, *redirect*s and second passes now reuse previous section merges on a *<location* > by *<location* > basis, until we mismatch with the original location_walk. [william rowe] 2.0.26 

*) back out the 1.45 change to util_*script*.c.  this change made us set the environment variable request_uri to the *redirect*ed uri, instead of the originally requested uri. [taketo kabe <kabe sra-tohoku.co.jp>] 2.0.26 

*) normalize the primary request, *redirect*s and sub-requests to run the same ap_process_request_internal for consistency in robustness, behavior and security.  [william rowe] 2.0.26 

*) some initial support for the cygwin platform [prefork only]. this is not to be confused with support for the winnt/win32 platform, which is the recommended *config*uration for native win32 users.  the cygwin platform support is recommended for cygwin platform users. [stipe tolj <tolj wapme-systems.de>] 2.0.26 

*) changed syntax of set{input|output}filter.  the list of filters must be semicolon delimited (if more than one filter is given.) the set{input|output}filter directive now overrides a parent container's directive (e.g. *setinputfilter* in *<directory* /web/foo> will override any *setinputfilter* directive in *<directory* /web>.) this new syntax is more consistent with add{input|output}filter directives defined in mod_mime.  also cures a bug in prior releases where the set{input|output}filter directive would corrupt the global *config*uration if the multiple directives were nested. [william rowe] 2.0.26 

*) cured what's ailed mime for quite some time.  if an addsomething was given in the *config*uration (language, charset, handler or encoding) apache would set the content type as given by *addtype*, but refused to check the mime.types file if *addtype* wasn't given for that specific extension.  setting the *addhandler* for .html without setting the *addtype* text/html html would cause apache to use the default content type.  [william rowe] 2.0.26 

*) move the installed /manual directory out of the /htdocs/ tree, so that it can be kept more independently from the remaining document root. the "*alias* /manual ..." already allowed for easy projection into existing private document trees. [martin kraemer] 2.0.25 

*) fix a performance problem with the worker mpm.  we now create trans*action* pools once, and re-use them for each connection. [aaron bannert <aaron clove.org>] 2.0.25 

*) introduce the *addinputfilter* filter[;filter...] ext [ext...] and corresponding *addoutputfilter* syntax, to insert one or more filters by mod_mime filename extension processing. [william rowe] 2.0.25 

*) fix a growing connection pool in core_output_filter() for *keepalive* requests.  [jeff trawick] 2.0.25 

*) clean up location_walk, so that this step performs a minimum amount of redundant effort (it must be run twice, but it will no longer reparse all *<location* > blocks when the request uri hadn't changed.)  [william rowe] 2.0.25 

*) eliminate proxy: (and all other 'special') processing from the ap_directory_walk() phase.  modules that want to use special walk logic should refer to the mod_proxy map_to_location *example*, with it's proxy_walk and proxysection implementation.  this makes either directory_walk flavor much more legible, since that phase only runs against real *<directory* > blocks. [william rowe] 2.0.25 

*) introduce the map_to_storage hook, which allows modules to bypass the directory_walk and file_walk for non-file requests.  trace shortcut moved to http_*protocol*.c as apr_hook_middle, and the directory_walk/file_walk happen as apr_hook_very_last in core.c. [william rowe] 2.0.25 

*) add the ability for mod_include to add the includes filter if the file is *config*ured for the server-parsed handler. this makes the *config*uration for .shtml files much easier to understand, and allows mod_include to honor apache 1.3 *config* files.   based on doug maceachern's patch to php to do the same thing.  [ryan bloom] 2.0.25 

*) force openssl to ignore process local-caching and to always get/set/delete *session*s using mod_ssl's callbacks [madhusudan mathihalli <madhusudan_mathihalli hp.com>, geoff thorpe <geoff geoffthorpe.net>] 2.0.25 

*) fix segv in mod_mime if no *addtype*s are *config*ured [john sterling <sterling covalent.net>] 2.0.25 

*) changed the late-1.3 log_*config* substitution %c to %x, to log the status of the closed connection, as it conflicts with the far more common, historical ssl logging directive %...{var}c.  [william rowe] 2.0.25 

*) added a default commented-out mod_ldap and mod_auth_ldap *config*uration to httpd-std.conf and httpd-win.conf [graham leggett] 2.0.25 

*) fix an assertion failure in mod_ssl when the *keepalive* *timeout* is reached.  [jeff trawick] 2.0.24 

*) rounded out the mod_mime add/remove pairs by adding *removelanguage* and *removecharset* directives.  [william rowe] 2.0.24 

*) the unix mpms other than perchild now allow child server processes to use the accept *mutex* when starting as root and using sysv sems for the accept *mutex*.  previously, this combination would lead to fatal errors in the child server processes.  perchild can't use sysv sems because of security issues.  [jeff trawick, greg ames] 2.0.24 

*) we have always used the obsolete/deprecated netscape syntax for our tracking cookies; now the *cookiestyle* directive allows the webmaster to choose the netscape, rfc2109, or rfc2965 format.  the new *cookiedomain* directive allows the setting of the cookie's domain= attribute, too.  pr #s 5006, 5023, 5920, 6140 [ken coar] 2.0.24 

*) begin to sanitize the mpm *config*uration directives.  now, all mpms use the same functions for all common mpm directives.  this should make it easier to catch all bugs in these directives once. [cody sherr <csherr covalent.net>] 2.0.24 

*) close a major resource leak.  every time we had issued a graceful restart, we leaked a socket de*script*or. [ryan bloom] 2.0.24 

*) all mod_autoindex query parsing is now quietly quashed with the indexoption ignoreclient.  the indexoption suppresscolumnsorting still drops the column sort <a href>'s for the column headers, but ignoreclient is required to ignore these query *options* entirely. [william rowe] 2.0.23 

*) introduced new mod_autoindex index*options* flags: suppressicon to drop the icon column, suppressrules to drop the <hr> elements, and htmltable to create rudimentary html table listings (implies fancyindexing).  [william rowe] 2.0.23 

*) re-introduced the mod_autoindex index*options* flag trackmodified from apache 1.3.15.  this is needed for two reasons, first, given multiple machines within a server farm, etags and last-modified stamps won't correspond from machine to machine, and second, many unixes don't capture changes to the date or time stamp of existing files, since these don't modify the dirent itself.  [william rowe] 2.0.23 

*) re-introduced the mod_autoindex index*options* flag foldersfirst and directorywidth *options* from apache 1.3.10. [william rowe, ken coar] 2.0.23 

*) eliminated fancyindexing directive, deprecated early in apache 1.3 by the index*options* fancyindexing syntax.  [william rowe] 2.0.23 

*) mod_autoindex now excludes any file names that would result in an error, other than a success or *redirect*.  also optimized the parent directory, always included except in the uri '/'. [william rowe] 2.0.23 

*) eliminate mod_cgi's handling of .exe files without the .exe file extension.  this is already handled by multiviews, if the admin wishes to *addhandler* .exe or define a content type handler and associate .exe files with that content type.  multiviews must be enabled to allow these to be served.  [william rowe] 2.0.23 

*) add a handler to mod_includes.c.  this handler is designed to implement the *xbithack* directive.  this can't be done with a fixup, because we need to check the content-type, which is only available in the handler phase.  [ryan bloom] 2.0.23 

*) add the ability to extend the methods that apache understands and have those methods *<limit*>able in the httpd.conf. it uses the same bit mask/shifted offset as the original http methods such as m_get or m_post, but expands the total bits from an int to an ap_int64_t to handle more bits for new request methods than an int provides.  [cody sherr <csherr covalent.net>] 2.0.23 

*) add a single *listen*er/multiple worker mpm.  this mpm is definately not fully correct, but it allows us to solve many of the problems that exist in the threaded mpm.  this is a modified version of the threaded mpm.  [ryan bloom] 2.0.23 

*) apache/win32 now fills in the service de*script*ion with apache's server version string, including loaded and advertised modules. [william rowe] 2.0.22 

*) improved support for the win32 build, to recover gracefully from missing apr or apr-util directories or the awk interpreter, create the proper cgi-bin *example*s, including a test-cgi.bat, and fix the perl shebang line for printenv.pl, when installing from the build environment.  [william rowe] 2.0.22 

*) use new apr number conversion functions to reduce cpu consumption when setting the content length, and in mod_log_*config*. [brian pane] 2.0.22 

*) fix seg faults in mod_status with *extendedstatus* enabled, after restarts.  a garbage pointer to a vhost's server_rec from the previous generation was being left around under certain conditions. [greg ames] 2.0.22 

*) improve the exports generating awk *script*.  in the past, we had work around problems in the awk *script* by avoiding some #if and #ifdefs.  this has bitten us many times in generating the exports.c file.  this improvement allows corrects the header file parsing. [sander striker <striker apache.org>] 2.0.21 

*) win32: prevent *listen*ing sockets from being inherited by the apache child process, cgi *script*s, rotatelog process etc.  if the apache child process segfaults, any processes that the child started are not reaped. prior to this fix, these processes inherited the *listen*ing sockets which sometimes prevented the restarted apache child process from accepting connections (ie, the server would hang). [bill stoddard] 2.0.21 

*) provide vhost and request strings when *extendedstatus* is on. [greg ames] 2.0.21 

*) fix some issues with the pod and prefork: check the pod *after* processing a connection so that a server processing a time- consuming request bails out as soon as practical; when the parent process wakes up a server process via connect(), use an apr *timeout* on the connect() so that we don't hang for a long time if there aren't server processes around to do accept(). [jeff trawick, greg ames] 2.0.21 

*) apxs no longer generates ap_send_http_header() in the *example* handler 2.0.19 

*) fix brokenness when *threadsperchild* is higher than the built-in limit.  we left ap_threads_per_child at the higher value which led to segfaults when doing certain scoreboard operations. [jeff trawick] 2.0.19 

*) extend mod_*setenv*if to support specifying regular expressions on the *setenv*if (and *setenv*ifnocase) directive attribute field. *example*:  *setenv*if ^ts*  [a-z].* have_ts will cause have_ts to be set if any of the request headers begins with "ts" and has a value that begins with any character in the set [a-z]. [bill stoddard] 2.0.19 

*) win32 platforms now fully support mod_*userdir* *options*.  [will rowe] 2.0.19 

*) extend mod_headers to support conditional driven header add, append and set. use *setenv*if to set an envar and conditionally add/append/set headers based on this envar thusly: *setenv*if tsmyheader value have_tsmyheader header add myheader "%t %d" env=have_tsmyheader if the request contains header "tsmyheader: value" then header myheader: "t=xxxxxxxxxx d=yyyy" will be sent on the response. [bill stoddard] 2.0.19 

*) extend mod_headers to support using format specifiers on header add, append and set header values. two format specifiers are supported: %t - reports, in utc microseconds since the epoch, when the request was received. %d - reports the time, in microseconds, between when the request was received and the response sent. *example*s: header add myheader "this request served in %d microseconds. %t" results in a header being added to the response that looks like this: myheader: this request served in d=5438 microseconds. t=991424704447256 [bill stoddard] 2.0.19 

*) optimise reset_filter() in http_*protocol*.c. [greg stein] 2.0.19 

*) reimplement mod_headers as an output filter. mod_headers can now add custom headers to inbound requests using the *requestheader* directive and to responses using the same old header directive.  [graham leggett] 2.0.18 

*) fix processing of the trace method.  previously we passed bogus parms to form_header_field() and it overlaid some vhost structures, resulting in a segfault in check_host*alias*(). [greg ames, jeff trawick] 2.0.18 

*) do not start piped log processes during the *config* file preflight.  this change also circumvents a problem on windows where the rotatelog processes created during preflight was not getting cleaned up properly. [bill stoddard] 2.0.18 

*) fix httpd's definition of ltflags to be consistent with that of apr and apr-util, allow it to be overridden by the *config*ure command-line (default="--silent") and introduce lt_ldflags to replace what we were formerly abusing as ltflags.  [roy fielding] 2.0.18 

*) simplify the *config*ure process by moving all libtool stuff to apr and moving hints.m4 inline.  [roy fielding] 2.0.18 

*) mod_log_*config*: %c connection status incorrectly logged as "-" (non-*keepalive*) when max*keepalive*requests is set to 0. [bill stoddard] 2.0.18 

*) completely revamp *config*ure so that it preserves the standard make variables cppflags, cflags, cxxflags, ldflags and libs by moving the *config*ure additions to extra_* variables.  also, allow the user to specify notest_* values for all of the above, which eliminates the need for thread_cppflags, thread_cflags, and optim.  fix the setting of includes and extra_includes.  check flags as they are added to avoid pointless duplications.  fix the order in which flags are given on the compile and link lines.  remove obsolete macros apr_doextra, ac_add_library, ac_check_define, apache_passthru, and apache_once. added apr_save_the_environment and apr_restore_the_environment macros. renamed ac_type_rlim_t macro to apache_type_rlim_t.  [roy fielding] 2.0.18 

*) fix seg fault at start-up introduced by ryan's change to enable modules to specify their own logging tags. mod_log_*config* registers an optional function, ap_register_log_handler(). ap_register_log_handler() was being called by http_core before the directive hash table was created. this patch creates the directive hash table before ap_register_log_handler() is registered as an optional function. [jean-frederic clere <jfrederic.clere fujitsu-siemens.com>] 2.0.18 

*) allow modules to specify their own logging tags.  this basically allows a module to tell mod_log_*config* that when %x is encountered a specific function should be called.  currently, x can be any single character.  it may be more useful to make this a string at some point. [ryan bloom] 2.0.17 

*) add more *options* to the ap_mpm_query function.  this also allows mpms to report if their threads are dynamic or static.  finally, this also implements a new api, ap_show_mpm, which returns the mpm that was required into the core. [harrie hazewinkel <harrie covalent.net>] 2.0.17 

*) remove bindaddress from the default *config* file. [<giles nemeton.com.au>] 2.0.17 

*) allow module authors to add a module to their apache build using --with-module, without re-running buildconf.  the syntax is: --with-module=module_type:/path/to/module.c the *config*ure *script* will copy the module.c file to modules/module_type, and it will be added to the relevant makefiles. currently, this only works for static modules.  [ryan bloom] 2.0.17 

*) change the default installation directory to /usr/local/apache2, as now defined by the "apache" layout in *config*.layout. [marc slemko] 2.0.16 

*) fix segfaults for *config*uration file syntax errors such as "*<directory*>" followed by "</directory" and "*<directory*>" followed by "</directoryz>".  [jeff trawick] 2.0.16 

*) cleanup the --enable-layout option of *config*ure.  this makes us use a consistent location for the *config*.layout file, and it makes *config*ure more portable. [jun-ichiro hagino <itojun iijlab.net>] 2.0.16 

*) move ap_set_last_modified to the core.  this is a potentially controversial change, because this is kind of http specific.  however many *protocol*s should be able to take advantage of this kind of information.  i expect that headers will need one more layer of indirection for multi-*protocol* work, but this is a small step in the right direction.  [ryan bloom] 2.0.16 

*) add a *script*sock directive to the default *config* file.  this is only enabled when mod_cgid is used. [taketo kabe <kabe sra-tohoku.co.jp>] 2.0.15 

*) untangled the buildconf *script* and eliminated the need for build's aclocal.m4, generated_lists, build.mk, build2.mk, and a host of other libtool muck that is now under srclib/apr/build.  [roy fielding] 2.0.15 

*) security: fix a major security problem with double-reverse lookup checking.  previously, a client connecting over ipv4 would not be matched properly when the server had an ipv6 *listen*ing socket. pr #7407   [taketo kabe <kiabe sra-tohoku.co.jp>] 2.0.15 

*) change the way the beos mpm handles polling to allow it to stop and restart.  problem was the sockets being polled were being reset by the select call, so once it had accepted a connection it was no longer *listen*ing on the udp socket we use for shutdown instructions. apr needs to be altered, patch on it's way. [david reid] 2.0.15 

*) get rid of an inadvertent close of file de*script*or 2 in mod_mime_magic.  [greg ames, jeff trawick] 2.0.15 

*) add a hook, create_request.  this hook allows modules to modify a request while it is being created.  this hook is called for all request_rec's, main request, sub request, and internal *redirect*. when this hook is called, the r->main, r->prev, r->next pointers have been set, so modules can determine what kind of request this is.  [ryan bloom] 2.0.15 

*) cleanup the build process a bit more.  the apache *config*ure *script* no longer creates its own helper *script*s, it just uses apr's. [jean-frederic clere <jfrederic.clere fujitsu-siemens.com>] 2.0.15 

*) avoid using sscanf to determine the http *protocol* number in the common case because sscanf is a performance hog. from mike abbot's accelerating apache patch number 6. [mike abbot <mja trudge.engr.sgi.com>, bill stoddard] 2.0.15 

*) security: fix a security exposure in mod_access.  previously when ipv6 *listen*ing sockets were used, allow/deny-from-ipv4-address rules were not evaluated properly (pr #7407).  also, add the ability to specify ipv6 address strings with optional prefix length on allow and deny.  [jeff trawick] 2.0.15 

*) reimplement the windows mpm (mpm_winnt.c) to eliminate calling duplicatehandle on an iocompletionport (a practice which ms "discourages"). the new model does not rely on associating the completion port with the *listen*ing sockets, thus the completion port can be completely managed within the child process.  a dedicated thread accepts connections off the network, then calls postqueuedcompletionstatus() to wake up worker threads blocked on the completion port. [bill stoddard] 2.0.15 

*) bring forward the --*suexec*-umask option which allows the builder to preset the umask for *suexec* processes.  [ken coar] 2.0.15 

*) add a -v flag to *suexec*, which causes it to display the compile-time settings with which it was built.  (only usable by root or the ap_httpd_user username.)  [ken coar] 2.0.15 

*) fix content-length computation.  we only compute a content-length if we are not in a 1.1 request and we cannot chunk, and this is a *keepalive* or we already have all the data.  [ryan bloom] 2.0.14 

*) report unbounded containers in the *config* file.  previously, a typo in the </container> directive could result in the rest of the *config* file being silently ignored, with undesired defaults used. [jeff trawick] 2.0.14 

*) move more code from the http module into the core server.  this is core code, basically the default handler, the default input and output filters, and all of the core *config*uration directives. all of this code is required in order for the server to work, with or without http.  the server is closer to working without the http module, although there is still more to do.  [ryan bloom] 2.0.14 

*) fix mod_info, so that *<directory*> and *<location*> directives are not displayed twice when displaying the current *config*uration. [ryan morgan <rmorgan covalent.net>] 2.0.14 

*) add *config* directives to override default_error_msg and default_time_format.  this was sent in as pr 6193. [dan rench <drench xnet.com>] 2.0.14 

*) begin to move *protocol* independant functions out of mod_http.  the goal is to have only functions that are http specific in the http directory. [ryan bloom] 2.0.13 

*) move the error_bucket definition from the http module to the core server.  every *protocol* will need this ability, not just http.  [ryan bloom] 2.0.12 

*) fix a seg fault in mod_*userdir*.c.  we used to use the pw structure without ever filling it out.  this fixes pr 7271. [taketo kabe <kabe sra-tohoku.co.jp> and cliff woolley <cliffwoolley yahoo.com>] 2.0.12 

*) make mod_dir use a fixup for sending a *redirect* to the browser. before this, we were using a handler, which doesn't make much sense, because the handler wasn't generating any data, it would either return a *redirect* error code, or declined.  this fits the current hooks better.  [ryan morgan <rmorgan covalent.net>] 2.0.12 

*) rename the module structures so that the exported symbol matches the file name, and it is easier to automate the installation process (generating *loadmodule* directives from the module filenames). [martin kraemer] 2.0.12 

*) don't disable threads just because we are using the prefork mpm. if somebody wants to compile without threads, they must now add --disable-threads to the *config*ure command line.  [ryan bloom] 2.0.11 

*) cleanup the mod_tls *config*ure process.  this should remove any need to hand-edit any files.  we require openssl 0.9.6 or later, but *config*ure doesn't check that yet.  [ryan bloom] 2.0.11 

*) add new *logformat* directive, %d, to log time it takes to serve a request in microseconds. [bill stoddard] 2.0.11 

*) change *addinputfilter* and *addoutputfilter* to *setinputfilter* and *setoutputfilter*.  this corresponds nicely with the other set directives, which operate on containers while the add* directives tend to work directly on extensions.  [ryan bloom] 2.0.11 

*) fix the *alias*match directive in apache 2.0.  when we brought a patch forward from 1.3 to 2.0, we missed a single line, which broke regex *alias*es.  [ryan bloom] 2.0.11 

*) we have a poor abstr*action* in the *protocol*.  this is a temporary hack to fix the bug, but it will need to be fixed for real.  if we find an error while sending out a custom error response, we back up to the first non-ok request and send the data.  then, when we send the eos from finalize_request_*protocol*, we go to the last request, to ensure that we aren't sending an eos to a request that has already received one.  because the data is sent on a different request than the eos, the error text never gets sent down the filter stack.  this fixes the problem by finding the last request, and sending the data with that request.  [ryan bloom] 2.0.11 

*) get the correct ip address if *servername* isn't set and we can't find a fully-qualified domain name at startup. pr#7170 [danek duvall <dduvall eng.sun.com>] 2.0.11 

*) make mod_cgid work with *suexec*.  [ryan bloom] 2.0.11 

*) adopt apr user/*group* name features for mod_rewrite.  eliminates some 'extra' stat's for user/*group* since they should never occur, and now resolves the *script*_user and *script*_*group*, including on winnt ntfs volumes.  [william rowe] 2.0.11 

*) adopt apr features for simplifing mod_*userdir*, and accept the new win32/os2 exceptions without hiccuping.  [william rowe] 2.0.11 

*) replace *config*ure --with-optim option by using and saving the environment variable optim instead.  this is needed because *config*ure *options* do not support multiple flags separated by spaces. [roy fielding] 2.0.11 

*) modify the apr_stat/lstat/getfileinfo calls within apache to use the most optimal apr_finfo_wanted bits.  this spares win32 from performing very expensive owner, *group* and permission lookups and allows the server to function until these apr_finfo_t fields are implemented under win32.  [william rowe] 2.0.11 

*) support for typedsafe optional functions - that is functions exported by optional modules, which, therefore, may or may not be present, depending on *config*uration. see the experimental modules mod_optional_fn_{ex,im}port for sample code. [ben laurie] 2.0.11 

*) when *suexec* is specified, we need to add it to the list of targets to be built.  if we don't, then any changes to the *config*uration won't affect *suexec*, unless 'make *suexec*' is specifically run.  [ryan bloom] 2.0.11 

*) move init*group*gs, ap_uname2id and ap_gname2id from util.c to mpm_common.c.  these functions are only valid on some platforms, so they should not be in the main-line code. [ryan bloom] 2.0.11 

*) stop checking to see if this is a pipelined request if we know for a fact that it isn't.  basically, if r->connection->*keepalive* == 0. this keeps us from making an extra read call when serving a 1.0 request.  [ryan bloom and greg stein] 2.0.11 

*) fix the handling of variable expansion look-ahead in mod_rewrite, i.e. syntax like %{la-u:remote_user}, and also fix the parsing of more complicated nested *rewritemap* lookups. pr#7087 [tony finch] 2.0.11 

*) some adjustment on the handling and automatic setting (via hints.m4) of various compilation flags (eg: cflags). also, add the capability to specify flags (notest_cflags and notest_ldflags) which are used to compile apache, but not used during the *config*uration process. useful for flags like "-werror". [jim jagielski] 2.0.11 

*) ebcdic: fix some missing ascii conversion on some *protocol* data. [jeff trawick] 2.0.11 

*) use a real pool to dup the error log de*script*or.  [ryan bloom] 2.0.11 

*) get *suexec* working again.  we can't send absolute paths to *suexec* because it refuses to execute those programs.  *suexec* also wasn't always recognizing *config*uration changes made using the autoconf setup.  [ryan bloom] 2.0.11 

*) allow the buildconf process to find the *config*.m4 files in the correct order.  basically, we can now name *config*.m4 files as *config*\d\d.m4, and we will sort them correctly when inserting them into the build process.  [ryan bloom] 2.0.11 

*) get mod_cgid to use apr calls for creating the actual cgi process. this also allows mod_cgid to use ap_os_create_priviledged_process, thus allowing for *suexec* execution from mod_cgid.  currently, we do not support everything that standard *suexec* supports, but at least it works minimally now. [ryan bloom] 2.0.11 

*) allow *suexec* to be *config*ured from the ./*config*ure command line. [ryan bloom] 2.0.11 

*) apache is now ipv6-capable.  on systems where apr supports ipv6, apache gets ipv6 *listen*ing sockets by default.  additionally, the *listen*, *namevirtualhost*, and *<virtualhost*> directives support ipv6 numeric address strings (e.g., "*listen* [fe80::1]:8080"). [jeff trawick] 2.0.11 

*) modify the install directory layout.  modules are now installed in modules/.  shared libraries should be installed in libraries/, but we don't have any of those on unix yet.  all install directories are modifyable at *config*ure time. [ryan bloom] 2.0.11 

*) get the functions in server/linked into the server, regardless of which modules linked into the server.  this uses the same hack for apache that we use for apr and apr-util to ensure all of the necessary functions are linked.  as a part of thise, the charset_ebcdic was renamed to ap_charset_ebcdic for namespace protection, and to make the *script*s a bit easier. [ryan bloom] 2.0.11 

*) rework the rfc1413 handling to make it thread-safe, use a *timeout* on the query, and remove ipv4 dependencies.  [jeff trawick] 2.0.11 

*) get "*namevirtualhost* *" working in 2.0.  [ryan bloom] 2.0.11 

*) get mod_cgid and mod_rewrite to work as dsos by changing the way they keep track of whether or not their  post *config* hook has been called before.  instead of a static variable (which is replaced when the dso is loaded a second time), use userdata in the process pool. [jeff trawick] 2.0a9 

*) win32 now requires perl to complete the final install step for users to build + install on win32.  makefile.win now rewrites @@*serverroot*@ and installs the conf, htdocs and htdocs/manual directories. [william rowe] 2.0a9 

*) cleanup the export list a bit.  this creates a single unified list of functions exported by apr.  the export list is generated at *config*ure time, and that list is then used to generate the exports.c file. because of the way the export list is generated, we only export those functions that are valid on the platform we are building on. [ryan bloom] 2.0a9 

*) enable logging the cookie with mod_log_*config* [sander van zoest <sander covalent.net>] 2.0a9 

*) fix a segfault in mod_info when it reaches the end of the *config*uration. [jeff trawick] 2.0a9 

*) apr: add new apr_getopt_long function to handle long *options*. [b. w. fitzpatrick <fitz red-bean.com>] 2.0a8 

*) make cgi-bin work as a regular directory when using mod_vhost_*alias* with no virtual*script**alias* directives. pr#6829 [tony finch] 2.0a8 

*) mod_info.c has now been ported to apache 2.0.  as a part of this change, the root of the *config*uration tree has been exposed to modules as ap_conftree. [ryan morgan <rmorgan covalent.net>] 2.0a8 

*) get single_*listen*_unserialized_accept working again.  this uses the hints file to determine which platforms define single_*listen*_unserialized_accept. [ryan bloom] 2.0a8 

*) destroy the pthread *mutex* in lock_intra_cleanup() for pr#6824. [shuichi kitaguchi <ki hh.iij4u.or.jp>] 2.0a8 

*) always compute the content length, whether it is sent or not. the reason for this, is that it allows us to correctly report the bytes_sent when logging the request.  this also simplifies content-length filter a bit, and fixes the actual byte-reporing code in mod_log_*config*.c [ryan bloom] 2.0a8 

*) port three log methods from mod_log_*config* 1.3 to 2.0: clf compliant '-' byte count, method and *protocol*. [bill stoddard] 2.0a8 

*) add a new *logformat* directive, %c, that will log connection status at the end of the response as follows: 'x' - connection aborted before the response completed. '+' - connection may be kept-alive by the server. '-' - connection will be closed by the server. [bill stoddard] 2.0a8 

*) most apache functions work on ebcdic machines again, as *protocol* data is now translated (again).  [jeff trawick] 2.0a8 

*) add *suexec* support back.  [manoj kasichainula] 2.0a8 

*) namespace protect some macros declared in ap_*config*.h [ryan bloom] 2.0a8 

*) apr pipes on unix and win32 are now cleaned up automatically when the associated pool goes away.  (apr pipes on os/2 were already had this logic.)  this resolvs a fatal file de*script*or leak with cgis. [jeff trawick] 2.0a8 

*) the final line of the *config* file was not being read if there was no \n at the end of it.  this was caused by apr_fgets returning apr_eof even though we had read valid data.  this is solved by making cfg_getline check the buff that was returned from apr_fgets. if apr_fgets return apr_eof, but there was data in the buf, then we return the buf, otherwise we return null. [ryan bloom] 2.0a8 

*) security: tighten up the syntax checking of host: headers to fix a security bug in some mass virtual hosting *config*urations that can allow a remote attacker to retrieve some files on the system that should be inaccessible. [tony finch] 2.0a8 

*) add support for /, //, //*servername* and //server/sharename parsing of *<directory*> blocks under win32 and os2. [tim costello, william rowe, brian harvard] 2.0a8 

*) fix mod_log_*config* so that it compiles cleanly with buffered_logs [mike abbott <mja sgi.com>] 2.0a7 

*) install apachectl correctly, and *substitute* the proper values so that it works again.  [ryan bloom] 2.0a7 

*) bring forward from 1.3.13 the *config* directory implementation [jim jagielski] 2.0a7 

*) multiple build and *config*uration fixes build process: -add datadir and localstatedir substitutions -fix layout name -fix logfilename misspelling -fix evaluation of installation dir variables and -replace $foobar by $(foobar) to be usefull in the makefile cross compile: -add rules for cross-compiling in rules.mk. okay, rule to check for $cc_for_build is still missing -use check_tool instead of check_prog for ranlib -add missing "ar=@ar@" to severaly makefile.in's -cache result for "struct rlimit" -compile all helper programs with native and cross compiler and use the native version to generate header file [rüdiger kuhlmann <tadu gmx.de>] 2.0a7 

*) add .dll caching directive isapi*cachefile* to mod_isapi. [william rowe] 2.0a7 

*) expand dbmmanage to allow -d -m -s -p *options* for crypt, md5, sha1 and plaintext password encodings.  make feature tests a bit more flexible.  [william rowe] 2.0a7 

*) security: cve-2000-0913 (cve.mitre.org) fix a security problem that affects certain *config*urations of mod_rewrite. if the result of a *rewriterule* is a filename that contains expansion specifiers, especially regexp backreferences $0..$9 and %0..%9, then it may be possible for an attacker to access any file on the web server. [tony finch] 2.0a7 

*) overhaul of dbmmanage to allow a *group*s arg (as in apache 1.2) as well as a comment arg to the add, adduser and update cmds. update allows the user to clear or preserve pw/*group*s/comment. fixed a bug in dbmmanage that prevented the check option from parsing a password followed by :*group*... text.  corrected the seed calcualation for win32 systems, and added -lsdbm support. [william rowe] 2.0a7 

*) *config*ured mod_auth_dbm to compile with sdbmlib under win32. [william rowe] 2.0a7 

*) avoid a segfault when parsing .htaccess files.  an uninitialized tree pointer was passed to ap_build_*config*(). [jeff trawick] 2.0a7 

*) change the way that inet_addr & inet_network are checked for in apr's *config*ure process to allow beos bone to correctly find them. with this change beos bone now builds from source with no problems.  [david reid] 2.0a7 

*) fix a bug parsing *config*uration file containers.  with a sequence like this in the *config* file *<ifmodule* mod_kilroy.c> any stuff </ifmodule> *<ifmodule* mod_lovejoy.c> (blank line) any stuff </ifmodule> the second container would be terminated at the blank line due to sediment in the buffer from reading the prior </ifmodule> and an error message would be generated for the real </ifmodule> for the second container.  also due to this problem, any two characters could be used for "</" in the close of a container. [jeff trawick] 2.0a7 

*) modify mod_include to be a filter.  currently, it has only been tested on actual files, but it should work for cgi *script*s too. [ryan bloom] 2.0a7 

*) *namevirtualhost* can now take "*" as an argument instead of an ip address. this allows you to create a purely name-based virtual hosting server that does not have any ip addresses in the *config*uration file and which ignores the local address of any connections. pr #5595, pr #4455 [tony finch] 2.0a7 

*) fix chunking problem with cgi *script*s.  the general problem was that the cgi modules were adding an eos bucket and then the core added an eos bucket.  the chunking filter finalizes the chunked response when it encounters an eos bucket.  because two eos buckets were sent, we finalized the response twice.  the fix is to make sure we only send one eos, by utilizing a flag in the request_rec. [ryan bloom] 2.0a7 

*) fix merging of *adddefaultcharset* directive. pr #5872 (1.3) [jun kuriyama <kuriyama imgsrc.co.jp>] 2.0a7 

*) add filtered i/o to apache.  this is based on bucket brigades, currently the buckets still use buff under the covers, but that should change quickly.  the only currently written filter is the core filter which just calls ap_bwrite.  [the apache *group*] 2.0a6 

*) abort *config*uration if --with-layout was specified and there's no layout definition file.  [ken coar] 2.0a6 

*) add support for '--with-port=n' option to *config*ure.  [ken coar] 2.0a6 

*) a *config*uration file parsing problem was fixed.  when the *config*uration file started with an ifmodule/ifdefine container, only the last statement in the container would be retained. [jeff trawick] 2.0a5 

*) integrate the mod_dav module for webdav *protocol* handling. this adds the dav and dav_fs modules, the sdbm library, and additional xml handling utilities. [greg stein] 2.0a5 

*) if sizeof(long long) == sizeof(long), then prefer long in apr *config*ure.in.  [dave hill <ddhill zk3.dec.com>] 2.0a5 

*) ab would start up more connections than needed, then quit when the desired number were finished. also fixed a logic error involving ab *keepalive*s.  [victor j. orlikowski] 2.0a5 

*) winnt: implement non-blocking pipes with *timeout*s to communicate with cgis. apache 2.0a4 had non-blocking pipes but without *timeout*s (i.e, if a *timeout* was specified, the pipe reverted to a full blocking pipe). now the behaviour is more in line with unix non-blocking pipes. [bill stoddard] 2.0a5 

*) winnt: implement accept socket reuse. using mod_file_cache to cache open file handles along with accept socket reuse enables apache 2.0 to serve non-*keepalive* requests for static files at 3x the rate of apache 1.3.(e.g, apache 1.3 will serve 400 rps and apache 2.0 will serve almost 1200 rps on my system). [bill stoddard] 2.0a5 

*) merge mod_mmap_static function into mod_file_cache. mod_file_cache supports two *config* directives, *mmapfile* (same behavious as mod_mmap_static) and *cachefile*. use the *cachefile* directive to cache open file handles. this directive only works on systems that have implemented the ap_sendfile api. *cachefile* works today on windows nt, but has not been tested on any flavors of unix. [bill stoddard] 2.0a5 

*) cleanup the *config*uration.  with the last few changes the *config*uration process automatically: inherits information about how to build from apr.  allowing apr to inform apache that it should or should not use -ldl detects which mod_cgi should be used mod_cgi or mod_cgid, based on the threading model apache calls apr's *config*ure process before finishing it's *config*uration processing, allowing for more information flow between the two. [ryan bloom] 2.0a5 

*) fix error messages issued from mpms which explain where to change compiled-in limits (e.g., *threadsperchild*, maxclients, starttreads). [greg ames] 2.0a5 

*) ap_create_pipe() now leaves pipes in blocking state.  (this helps reduce the number of syscalls on unix.)  ap_set_pipe_*timeout*() is now the way that the blocking state of a pipe is manipulated. ap_block_pipe() is gone.  [jeff trawick] 2.0a5 

*) correct the problem where the only local host name that the ip stack can discover are 'undotted' private names.  if no fully qualified domain name can be identified, the default *servername* will be set to the machine's ip address string. a warning is always provided if the *servername* not specified, but assumed.  solves pr6215 [william rowe] 2.0a5 

*) repair problems with *config* file processing which caused segfault at init when virtual hosts were defined and which caused *servername* to be ignored when there was no valid dns setup.  [jeff trawick] 2.0a5 

*) repair c++ compatibility in ap_*config*.h, apr_file_io.h, apr_network_io.h, and apr_thread_proc.h. [tyler j. brooks <tylerjbrooks home.com>, jeff trawick] 2.0a5 

*) change *config*uration command setup to be properly typesafe when in maintainer mode. note that this requires a compiler that can initialise unions. [ben laurie] 2.0a5 

*) turn on buffering for *config* file reads.  part of this was to repair buffered i/o support in unix and implement buffered ap_fgets() for all platforms.  [brian havard, jeff trawick] 2.0a5 

*) win32: fix problem where utc offset was not being set correctly in the access log. problem reported on news *group* by jerry baker. [bill stoddard] 2.0a5 

*) security: cve-2000-1204 (cve.mitre.org) prevent the source code for cgis from being revealed when using mod_vhost_*alias* and the cgi directory is under the document root and a user makes a request like http://www.*example*.com//cgi-bin/cgi as reported in <news:960999105.344321 ernani.logica.co.uk> [tony finch] 2.0a5 

*) when mod_cgid is started as root, the cgi daemon now switches to the *config*ured user/*group* (like other httpd processes) instead of continuing as root.  [jeff trawick] 2.0a5 

*) the prefork mpm now uses an apr lock for the accept() *mutex*. it has not been getting a lock at all recently.  httpd -v now displays apr's selection of the lock mechanism instead of the symbols previously respected by prefork.  [jeff trawick] 2.0a5 

*) fix typo in *config*ure *script* when checking for mod_so.  bash doesn't seem to have a problem but /bin/sh on solaris does. symptom: "./*config*ure: test: unknown operator ==" [jeff trawick] 2.0a5 

*) move pre_*config* hook call to between *config*uration read and *config* tree walk.  this allows all modules to implement pre_*config* hooks and know that they will be called at an appropriate time. [ryan bloom] 2.0a4 

*) mod_cgi, mod_cgid: make *script*log directive work again. [jeff trawick] 2.0a4 

*) add pre-*config* hooks back to all modules. [ryan bloom] 2.0a4 

*) fix a sigsegv in ap_md5digest(), which is used when you have *contentdigest* enabled and we can't/don't mmap the file. [jeff trawick] 2.0a4 

*) we now report the correct line number for syntax errors in *config* files.  [ryan bloom, greg stein, jeff trawick] 2.0a4 

*) fix corruption of ifs variable in --with-module= handling. depending on the user's shell or customization thereof, there would be errors generating ap_*config*_auto.h later in the *config*ure procedure.  [jeff trawick] 2.0a4 

*) mod_cgi: restore logging of stderr from child process when *script*log isn't used (as in 1.3), except that on unix it is now logged via ap_log_rerror() instead of by the child having stderr_fileno refer to the error log.  [greg ames, jeff trawick] 2.0a4 

*) add '-d' argument processing for run time *config*uration defines. [william rowe] 2.0a4 

*) add mod_charset_lite for *config*uring character set translation. [jeff trawick] 2.0a4 

*) fix ap_resolve_env() so that it handles new function added in a prior alpha (see "added the capability to do ${envvar} constructs in the *config* file.") as well as the constructs used by mod_rewrite. [paul reder <rederpj raleigh.ibm.com>] 2.0a4 

*) add the ability to hook into the *config* file reading phase.  basically if a directive is specified exec_on_read, then when that directive is read from the *config* file, the assocaited function is executed.  this should only be used for those directives that must muck with how the server interprets the *config*.  this should not be used for directives that re-order or replace items in the *config* tree.  those changes should be made in the pre-*config* step. [ryan bloom] 2.0a4 

*) add mod_*example* to the build system. [tony finch] 2.0a4 

*) fix a couple of problems in rfc1413 support (controlled by the *identitycheck* directive).  apache did not build the request string properly and more importantly apache would loop forever if the would-be ident server dropped the connection before sending a properly terminated response. [jeff trawick] 2.0a4 

*) *config*ure creates *config*.nice now containing your *config*ure *options*. syntax: ./*config*.nice [--more-*options*] [sascha schumann] 2.0a4 

*) fix mm *config*uration on solaris 8 x86 and os/390.  don't require /sbin in path on freebsd (all submitted to rse previously) [jeff trawick] 2.0a4 

*) the *config*ure option --with-program-name has been added to allow developers to rename the executable at *config*ure time.  this also changes the name of the *config* files to match the executable's name. [ryan bloom] 2.0a3 

*) mod_autoindex: add `index*options* +versionsort', to nicely sort filenames containing version numbers. [martin pool] 2.0a3 

*) ap_set_pipe_*timeout*(), ap_poll(), and apr_so_*timeout* now take microseconds instead of seconds.  some storage leaks and other minor bugs in related code were fixed.  [jeff trawick] 2.0a3 

*) win32: get non-blocking cgi pipe reads working under windows nt. this addresses pr 1623. still need to address timing out runaway cgi *script*s. [bill stoddard] 2.0a3 

*) win32: fix a bug in ap_get_oslevel which causes getversionex() to always fail. need to initialise the dwosversioninfosize member of the osversioninfo struct before calling getversionex, so getversionex always fails. the patch also enhances ap_get_oslevel (and the associated enum) to handle selected service packs for nt4, and adds recognition for windows 2000. this is useful, eg. if we can recognise nt4 sp2 then we can use readfilescatter and writefilegather in readwrite.c. [tim costello <tim.costello btfinancial*group*.com>] 2.0a3 

*) get apr dso code working under windows. includes cross platform fixes to mod_so.c. [<tim.costello btfinancial*group*.com>] 2.0a3 

*) eliminate apr_win.h and apr_win*config*.h (and the ugly #ifdefs they cause). now, apr.h and apr_*config*.h are generated from apr.hw and apr_*config*.hw at build time. at this point, the server will not compile on windows because of the recent dso commits. fixing those next. [bill rowe & bill stoddard] 2.0a3 

*) allow beos to survive restarts, log properly and a few small things it had problems with due to the way it setup users and *group*s. [david reid] 2.0a2 

*) clear hook registrations between reads of the *config* file. when dsos are unloaded and re-loaded the old hook pointers may no longer be valid. this fix eliminates potential segfaults. [allan edwards <ake raleigh.ibm.com>] 2.0a2 

*) fix a problem with sigfunc not being defined or bypassed if sig*action*() wasn't found. [jim jagielski] 2.0a2 

*) put in korean and norwegian index.html pages (2.0 and 1.3) which where donated by lee kuk hyun and lorant czaran. 'fixed' confusing ee/et name and made all extensions language/dialect rather than country reflecting. changed *example* files to explicit reflect the iso charset and added a few common ones to the *example* *config* [dirkx] 2.0a2 

*) extend external module capability.  to use this, you call *config*ure with --with-module=path/to/mod1,path/to/mod2,etc. [ryan bloom] 2.0a2 

*) backported the various "default charset" fixes from 1.3.12, including the *adddefaultcharset* directive. [jim jagielski] 2.0a2 

*) added the capability to do ${envvar} constructs in the *config* file. e.g. '*serveradmin* ${postmaster}'. as commited it does this on a line by line basis; i.e. if the envvar expands to something with spaces you have to protect it by adding quotes around it (unless of course you expect it to contains more than one argument. alternatively you can compile it on a per token basis; which is what people usually expect by setting resolve_env_per_token. but this hampers fancier hacks. [dirk-willem van gulik] 2.0a2 

*) changed the '*errordocument*' syntax in that it no longer supports the asymetric *errordocument* 301 "some message note the opening " quote, without a closing quote. it now has either the following syntaxes *errordocument* xxx /local/uri *errordocument* xxx http://valid/url *errordocument* xxx "some message" the recognition heuristic is: if it has a space it is a message. if it has no spaces and starts with a / or is a valid url then treat it that way. otherwise it is assumed to be a message. this breaks backward compatibility but makes live a hell of a lot easier for gui's and *config* file parsers. [dirk-willem van gulik] 2.0a2 

*) changed '*cachenegotiateddocs*' from its present/not-present syntax into a 'on' or 'off' syntax. as it currently is the only non nesting token which uses no_args and thus is an absolute pain for any *config* interface automation. this breaks backward compatibility. [dirk-willem van gulik] 2.0a2 

*) security: more rigorous checking of host: headers to fix security problems with mass name-based virtual hosting (whether using mod_rewrite or mod_vhost_*alias*). [ben hyde, tony finch] 2.0a1 

*) add back support for *usecanonicalname* in *<directory*> containers. [manoj kasichainula] 2.0a1 

*) cleaned apr build environment integration and bootstrap apr automatically for developers from src/*config*ure. [ralf s. engelschall] 2.0a1 

*) support line-continuation feature in *config*.option file and allow the loading of multiple option sections at once via ``--with-option=<section1>,<section2>,...'' [ralf s. engelschall] 2.0a1 

*) implement the apaci --with-option facility (per default used the *config*.option file). [ralf s. engelschall] mpm 

*) start to implement module-defined hooks that are a) fast and b) typesafe. replace pre_connection module call with a register_hook call and implement pre_connection as a hook. the intent is that these hooks will be extended to allow apache to be multi-*protocol*, and also to allow the calling order to be specified on a per-hook/per-module basis. [ben laurie] mpm 

*) mpm_prefork: throw away all the alarm/*timeout* crud; and clean up the signal handling for the new world order.  [dean gaudet] mpm 

*) crude ap_thread_*mutex* abstr*action* so that we get the pthread stuff out of alloc.c for now.  [dean gaudet] mpm 

*) new buff option added: bo_*timeout*. it describes the *timeout* for buff operations (generally over a network). [dean gaudet, ryan bloom, manoj kasichainula] pthreads 

*) created http_accept abstr*action*. added 4 new functions (not exported): init_accept(), begin_accepting_requests(), get_request(), stop_accepting_requests() [bill stoddard] pthreads 

*) remove bogus error message when a *redirect* doesn't set location. instead, use an empty string to avoid coredump if the error message was supposed to include a location.  [roy fielding] 1.3.9 

*) don't allow *config*ure to include mod_auth_digest unless it is explicitly requested, even if the user asked for all modules. [roy fielding] 1.3.9 

*) fixed generated addmodule adjustments in apaci's `*config*ure' *script* in order to allow (new) modules like mod_vhost_*alias* to be handled correctly (which was touched by the adjustments for mod_*alias*). [ralf s. engelschall] 1.3.9 

*) win32: create the cgi *script* process as detached.  this may solve the problem observed by some win95/98 users where they get cgi *script* output sent to the console.  [bill stoddard] 1.3.9 

*) add de*script*ion of -t command-line option to usage(). [ralf s. engelschall] 1.3.9 

*) flush the output buffer immediately after sending an error or *redirect* response, since the result may be needed by the client to abort a long data transfer or restart a series of pipelined requests. [tom vaughan <tvaughan aventail.com>, roy fielding] 1.3.8 [not released] 

*) rewritelock/*rewritemap* didn't work properly with virtual hosts. [dmitry khrustalev <dima bog.msu.su>] pr#3874 1.3.8 [not released] 

*) win32: more apache -k restart work. restarts are now honored immediately and connections in the *listen* queue are -not- lost. this is made possible by the use of the wsaduplicatesocket() call.  the *listen*ers are opened in the parent, duplicated, then the duplicates are passed to the child. the original *listen* sockets are not closed by the parent across a restart, thus the *listen* queue is preserved. [bill stoddard <stoddard raleigh.ibm.com>] 1.3.7 [not released] 

*) fix '*config*ure' to work correctly with sysv-based versions of 'tr' (consistent with *config*ure's use as well). [jim jagielski] 1.3.7 [not released] 

*) apxs: add "-s var=val" option which allows for override of cfg_* built-in values. add "-e" option which works like -i but doesn't install the dso; useful for editing httpd.conf with apxs. fix editing code so that multiple invocations of apxs -a will not create duplicate *loadmodule*/addmodule entries; apxs can now be used to re- enable/disable a module.  [wilfredo sanchez] 1.3.7 [not released] 

*) win32: *redirect* cgi *script* stderr (*script* debug info) into the error.log when cgi *script*s fail. this makes apache on win32 behave more like unix. [bill stoddard <stoddard raleigh.ibm.com>] 1.3.7 [not released] 

*) add the new mass-vhost module (mod_vhost_*alias*.c) developed and used by demon internet, ltd. [tony finch <fanf demon.net>] 1.3.7 [not released] 

*) *documentroot* checking: under previous versions, when apache first started up, it used to do a stat of each *documentroot* to see if it existed and was a directory. if not, then an error message was printed. this has been disabled. if *documentroot* does not exist, you will get error messages in error_log. if the '-t' command line option is used (to check the *config*uration) the check of *documentroot* is performed. an additional command line option, '-t', has been added if you want to avoid the *documentroot* check even when checking the *config*uration. [jim jagielski] 1.3.7 [not released] 

*) win32: changed behaviour of apache -k restart. previously, the server would drain all connections in the stack's *listen* queue before honoring the restart. on a busy server, this could take hours.  now, a restart is honored almost immediately. all connections in apache's queues are handled but connections in the stack's *listen* queue are discarded. restart triggered by maxrequestperchild is unchanged. [bill stoddard <stoddard raleigh.ibm.com>] 1.3.7 [not released] 

*) determine ap_byte_order for ap_*config*_auto.h and already use this at least for expat. [ralf s. engelschall] 1.3.7 [not released] 

*) allow *setenv*if[nocase] to test environment variables as well as header fields and request attributes.  [ken coar] 1.3.7 [not released] 

*) testcompile updated. we can now run programs and output the results during the *config*ure process. [ jim jagielski] 1.3.7 [not released] 

*) the source is now quad (long long) aware as needed. specifically, the *config*ure process determines the correct size of off_t and *void. when the os/platform/compiler supports quads, ap_snprintf() provides for the 'q' format qualifier (if quads are not available, 'q' is silently "demoted" to long). [jim jagielski] 1.3.7 [not released] 

*) fixed the *config*ure --without-support option so it doesn't result in an infinite loop.  [marc slemko] 1.3.7 [not released] 

*) piped error logs could cause a segfault if an error occured during *config*uration after a restart. [aidan cully <aidan panix.com>] pr#4456 1.3.7 [not released] 

*) if a "location" field was stored in r->err_headers_out rather than r->headers_out, *redirect* processing wouldn't find it and the server would core dump on ap_escape_html(null).  check both tables and raise http_internal_server_error with a log message if location isn't set.  [doug maceachern, ken coar] 1.3.7 [not released] 

*) add 'request_*protocol*' special keyword to mod_*setenv*if so that environment variables can be set according to the *protocol* version (e.g., http/0.9 or http/1.1) of the request.  [ken coar] 1.3.7 [not released] 

*) fix sed regex for generating ap_*config*_auto.h in src/*config*ure. [jan gallo <gallo pvt.sk>] pr#3690, pr#4373 1.3.7 [not released] 

*) always log months in english format for %t in mod_log_*config*. [petr lampa <lampa fee.vutbr.cz>] pr#4366, 679 1.3.7 [not released] 

*) support for server-parsed and multiview-determined *readmename* and *headername* files in mod_autoindex. removed the restriction on "/"s in *readmename* and *headername* directives since the *sub_req* routines will deal with the access issues. (it's now possible to have {site|*group*|project|customer|...} wide readmes and headers.) [raymond s brand <rsbx rsbx.net>, ken coar] pr#1574, 3026, 3529, 3569, 4256 1.3.7 [not released] 

*) fix *config*uration engine re-entrant hangups, which solve a handful of problems seen with mod_perl <perl> *config*uration sections [salvador ortiz garcia <sog msg.com.mx>] 1.3.7 [not released] 

*) mac os and mac os x server now use the appropriate custom layout by default when building with apaci; allow for platform-specific variable defaults in *config*ure. [wilfredo sanchez] 1.3.7 [not released] 

*) do setgid() before init*group*s() in http_main; some platforms zap the *group*list when setgid() is called.  this was fixed in *suexec* earlier, but the main httpd code missed the change. [rob saccoccio <robs infinitetechnology.com>]  pr#2579 1.3.7 [not released] 

*) add iconsdir, htdocsdir, and cgidir to *config*.layout. [wilfredo sanchez] 1.3.7 [not released] 

*) fix minor but annoying bug with the test for *config*uration.tmpl being newer than *config*uration so that it is less likely to fail when using apaci and shadow sources. [wilfredo sanchez] 1.3.7 [not released] 

*) modify mod_autoindex's handling of addde*script*ion so that the behaviour matches the documentation.  [ken coar] pr#1898, 3072. 1.3.7 [not released] 

*) add functionality to the install-bindist.sh *script* created by binbuild.sh to use tar when copying distribution files to the *serverroot*. this allows upgrading an existing installation without nesting the new distribution in the old. install-bindist.sh now detects the local perl5 path to install apxs and dbmmanage with proper path to perl interpreter. add an install-binsupport target which copies the source files for apxs and dbmmanage to bindist to allow these *script*s to be properly installed relative to the destination *serverroot*. [randy terbush, covalent technologies, <randy covalent.net>] 1.3.7 [not released] 

*) fixed a bug in mod_dir that causes a child process will infinitely recurse when it attemps to handle a request for a directory wnd the value of the *directoryindex* directive is a single dot. also likely to happen for anyother values of *directoryindex* that will map back to the same directory. the handler now only considers regular files as being index candidates. no pr#s found. [raymond s brand <rsbx rsbx.net>] 1.3.7 [not released] 

*) ease *config*uration debugging by making testcompile fall back to using "make" if the $make variable is unset [martin kraemer] 1.3.7 [not released] 

*) fixed the *serversignature* directive to work as documented. [raymond s brand <rsbx rsbx.net>] pr#4248 1.3.7 [not released] 

*) add "opt" (sysv-style) layout to *config*.layout. [raymond s brand <rsbx rsbx.net>] 1.3.7 [not released] 

*) add support for os/2 (case insenstive filesystem, .exe suffix, etc) to apaci files and related *script*s. [yitzchak scott-thoennes <sthoenna efn.org>, ralf s. engelschall] pr#4269 1.3.7 [not released] 

*) fix special *rewritecond* "-s" pattern matching. [bob finch <bob nas.com>] 1.3.7 [not released] 

*) fix value quoting in src/*config*ure *script* for ap_*config*_auto.h [paul sutton <paul awe.com>] 1.3.7 [not released] 

*) make sure rewritelock can be used only in the global context, (i.e. outside of any *<virtualhost*> sections) because it's a global facility of the rewrite engine. [ralf s. engelschall] 1.3.7 [not released] 

*) apaci would not correctly build *suexec*. [maria verina <mariav icgeb.trieste.it>] pr#4260 1.3.7 [not released] 

*) "index*options* none" generated extra spaces at the end of each line.  [<inkling firstnethou.com>] pr#3770 1.3.7 [not released] 

*) the "100 continue" response wasn't being sent after internal *redirect*s. [jose kahan <kahan w3.org>] pr#3910, 3806, 3575 1.3.7 [not released] 

*) port: deal with uts compiler error in http_*protocol*.c [dave dykstra <dwd bell-labs.com>] pr#4189 1.3.7 [not released] 

*) fix a memory leak which is exacerbated by certain *config*urations. [dean gaudet] pr#4225 1.3.7 [not released] 

*) ebcdic platforms: david submitted patches for two bugs in the md5 digest port for ebcdic machines: a) the htdigest utility overwrote the old contents of the digest file b) the content-md5 header value (*contentdigest* directive) was wrong when the returned file was not converted from ebcdic, but was a binary (e.g., image file) in the first place. [david mccreedy <mccreedy us.ibm.com>] 1.3.7 [not released] 

*) support/htpasswd now permits the password to be specified on the command line with the '-b' switch.  this is useful when passwords need to be maintained by *script*s -- particularly in the win32 environment.  [ken coar] 1.3.7 [not released] 

*) win32: win32 multiple services patch. added capability to install and run multiple copies of apache as individual services. *example* 1: apache -n apache1 -i -f c:/httpd.conf installs apache as service 'apache1' and associates c:/httpd.conf with that service. net start apache1 starts apache1 service. net stop apache1 stops apache1 service *example* 2: apache -n apache2 -i installs apache as service 'apache2'. httpd.conf is located under the default server root (/apache/conf/httpd.conf). net start apache2 starts apache2 service. *example* 3: apache -n apache3 -i -d c:/program files/apache install apache as service 'apache3' and sets server root to c:/program files/apache. *example* 4: apache -n apache2 -k restart restart apache2 service [keith wannamaker, ken parzygnat, bill stoddard] 1.3.7 [not released] 

*) proxy ftp: instead of using the hardwired string "text/plain" as a fallback type for files served by the ftp proxy, use the ap_default_type() function to determine the *config*ured type. this allows for special *config*urations like *<directory* proxy:ftp://some.host> *defaulttype* gargle/blurb </directory> additionally, add the content-encoding: header to ftp proxy replies when the encoding is defined (by the *addencoding* directive). because it was missing, it was almost impossible to browse compressed files using the ftp proxy (works now perfectly in communicator). the ftp proxy now also returns the date: and server: header lines (if not much else... this code is "somewhat" broken) like normal requests do. [martin kraemer] 1.3.7 [not released] 

*) be more smart in apaci's *config*ure *script* when determining the uid/gid for user/*group* directives and use the determined uid/gid to initialize the permissions on the proxycachedir. [dirk-willem van gulik, ralf s. engelschall] 1.3.7 [not released] 

*) fix sed-substitutions in `make install': path elements like `httpd/conf' (for instance from an apaci *config*ure --sysconfdir=/etc/httpd/conf option) were *substitute*d with $(target).conf, etc. same for other strings with dots where the dot wasn't matched as plain text. [ralf s. engelschall] 1.3.7 [not released] 

*) fix verbose output of apaci *config*ure (option -v) [martin kraemer, ralf s. engelschall] 1.3.6 

*) win32: binary installer now runs the *config*uration dll before the reboot prompt (which is only given if msvcrt.dll system dll is new or updated). this should avoid the *config*uration directory being empty after installation. [paul sutton] pr#3767, 3800, 3827, 3850, 3900, 3953, 3988 1.3.5 [not released] 

*) win32: binary installer now creates start menu *options* to start and stop apache as a console application and to uninstall the apache service on nt. [paul sutton] pr#3741 1.3.5 [not released] 

*) using apaci, the main *config* file (usually httpd.conf) was not being adjusted as $(target).conf. [wilfredo sanchez <wsanchez apple.com>] 1.3.5 [not released] 

*) move the directive `*extendedstatus*' in httpd.conf-dist-win _after_ the dso/dll section because it's a directive from mod_status and isn't available before the dll of mod_status is loaded. [martin poeschl <mpoeschl gmx.net>] pr#3936 1.3.5 [not released] 

*) security: fix a bug in the calculation of the buffer size for the line continuation facility in apache's *config*uration files which could lead to a buffer overflow situation. [thomas devanneaux <thomas.devanneaux enst.fr>] pr#3617 1.3.5 [not released] 

*) let apaci's *config*ure *script* correctly complain for unknown --enable-xxx and --disable-xxx *options*. [ralf s. engelschall] pr#3958 1.3.5 [not released] 

*) add apple's mac os x server layout "rhapsody" to *config*.layout. [wilfredo sanchez] 1.3.5 [not released] 

*) in *config*ure, do not append the target name to the directory path if the path already contains "apache".  [ralf s. engelschall] 1.3.5 [not released] 

*) add %v to mod_log_*config*, this logs the hostname according to the *usecanonicalname* setting (this is the pre-1.3.4 behaviour of %v).  useful for mass vhosting.  [tony finch <dot dotat.at>] 1.3.5 [not released] 

*) add support for \n and \t to mod_log_*config*, can be used to produce more reliable logs with multiline entries.  [tony finch <dot dotat.at>] 1.3.5 [not released] 

*) os/2 ap_os_canonical_filename()'s behaviour is improved: ap_assert() is removed. this allows *<directory* proxy:*> directives to work and prevents invalid requests from killing the process. [brian havard <brianh kheldar.apana.org.au>] 1.3.5 [not released] 

*) src/support/: the apachebench benchmark program was overhauled by david n. welton: you can now have it generate an html table, presumably for integration into other html sources. david updated the ab man page as well and added some missing de*script*ions. thanks! [david n. welton <davidw prosa.it>] 1.3.5 [not released] 

*) win32: the filename validity checker now allows filenames containing characters in the range 0x80 to 0xff (for *example* accented characters). [paul sutton] pr#3890 1.3.5 [not released] 

*) added conditional logging based upon environment variables to mod_log_*config*.  mod_log_referer and mod_log_agent are now deprecated.  [ken coar] 1.3.5 [not released] 

*) added -s option to install.sh so that *options* can be passed to strip on some platforms. [ralf s. engelschall, wilfredo sanchez] 1.3.5 [not released] 

*) tweak modules makefile generated by *config*ure so that it handles the test case of no modules being selected. [<chaz reliant.com>] 1.3.5 [not released] 

*) added a *<limit*except method ...> sectioning directive that allows the user to assign authentication control to any http method that is *not* given in the argument list; i.e., the logical negation of the *<limit*> directive.  this is particularly useful for controlling access on methods unknown to the apache core, but perhaps known by some module or cgi *script*. [roy fielding, tony finch] 1.3.5 [not released] 

*) prevent apachectl from complaining if the *pidfile* exists but does not contain a process id, as might occur if the server is being rapidly restarted. [wilfredo sanchez] 1.3.5 [not released] 

*) proxy: the various calls to ap_proxyerror() can return http/1.1 status code different from 500. this allows the proxy to, e.g., return "403 forbidden" for *proxyblock*'ed url's. [martin kraemer] related to pr#3455 1.3.5 [not released] 

*) win32: add new *config* directive, **script*interpretersource*, to enable searching the win32 registry for *script* interpreters. [bill stoddard] 1.3.5 [not released] 

*) win32: any error messages from -i or -u command line *options* are now displayed on the console output rather than sent to the error log. also the "running apache..." message is not output unless apache is going to serve requests. [paul sutton] 1.3.5 [not released] 

*) let src/*config*ure be aware of cflags *options* starting with plus signs as it's the case for the hp/ux compiler. [doug yatcilla <yatcilda umdnj.edu>] pr#3681 1.3.5 [not released] 

*) a consistent and conservative style for all shell *script*s has been implemented. basically, all shell string tests use the traditional hack of 'if [ "x$var" != "x" ]' or 'if [ "x$var" = "xstring" ]' to protect against bare null variable strings (ie: wrapping both sides with double quotes and prepending 'x'). 'x' was chosen because it's more universal and hopefully easier for old shell prgrammers, as well as being easier to search for in 'vi' (/x\$) :) [jim jagielski] 1.3.5 [not released] 

*) renamed macros status_drops_connection to ap_status_drops_connection and vestigial scan_*script*_header to ap_scan_*script*_header_err, mostly for aesthetic reasons. [roy fielding] 1.3.4 

*) index*options* suppresscolumnsorting only turned off making the column headers anchors; you could still change the display order by manually adding a '?n=a' or similar query string to the url.  now suppresscolumnsorting locks in the sort order so it can't be overridden this way.  [ken coar] 1.3.4 

*) added *indexorderdefault* directive to supply a default sort order for fancyindexed directory listings.  [ken coar] pr#1699 1.3.4 

*) instead of fixing a bug in the generation procedure for *config*.status (a backslash was missing) we remove the bug together with it's complete context because the special cases of the past can now no longer occur because of the recent magic for the --with-layout default. [ralf s. engelschall] pr#3590 1.3.4 

*) two minor enhancements to mod_rewrite: first *rewriterule* now also supports the ``nocase|nc'' flag (as *rewritecond* already does for ages) to match case insensitive (this especially avoids nasty patterns like `[tt][ee][ss][tt]'). second two additional internal map functions `escape' and `unescape' were added which can be used to escape/unescape to/from hex-encodings in urls parts (this is especially useful in combination with map lookups). [magnus bodin, ian kallen, ralf s. engelschall] 1.3.4 

*) fix some inconsistencies related to the scopes of directives. the only user visible change is that the directives `*usecanonicalname*' and `*contentdigest*' now use the (more correct) `*options*' scope instead of (less correct) `auth*config*' scope.  [ralf s. engelschall] 1.3.4 

*) when modules update/modify the file name in the *config*file_t structure, syntax errors will report the updated name, not the original one. [fabien coelho <coelho cri.ensmp.fr>] pr#3573 1.3.4 

*) for %v log *servername* regardless of the *usecanonicalname* setting (similarly for %p).  [dean gaudet] 1.3.4 

*) *config*ure was initializing the variables $osdir, $incdir and $shell rather late (too late for some invocations of testcompile). this improves the make environment available to testcompile and the *.module *script*s. [martin kraemer] 1.3.4 

*) the hashbang emulation code in ap_execve.c would interpret #!/hashbang/*script*s correctly, but failed to fall back to a standard shell for *script*s which did not start with #! now shell_path is started in these cases. [martin kraemer] 1.3.4 

*) cleanup the command line *options*: `-?' was documented to show the usage list but does it with an error because `?' is not a valid command. otoh a lot of users expect `-h' to print such a usage list and instead are annoyed for ages by our huge unreadable list of directives. so we now changed the command line *options* this way: 1. `-l' => `-r' intent: we need `-l' to be free, and `-r' for the dso run-time path is very similar to the popular linker option. 2. `-h' => `-l' intent: while -l gives the small list of modules, -l now gives the large list of directives implemented by these modules.  this is also consistent with -v (short version info) and -v (large version info). 3. `-?' => `-h' intent: it's now the expected option ;-) the manual page was adjusted accordingly. [ralf s. engelschall] pr#2714 1.3.4 

*) fixed problem of fclose() on an unopened file in *suexec* if log_exec wasn't defined.  [rick franchuk <rickf transpect.net>] 1.3.4 

*) removed recently introduced bugs and disfigurements in apaci: o fixed argument line processing: using $args was broken: it was not initialized and using args="$args $apc_option" and even args="$args \"$apc_option\"" fails in the second processing round for any arguments containing whitespaces. the only correct way is to use the construct "$@" (but not possible here) or iterate _both_ times over the implicit argument line (no argument to for-loop) which is what we now use. o make --with-layout=apache the default without creating redundancy (copying the --with-layout block in the argument parsing loop).  we achieve this by using the "$@" construct together with the `set' command to prepend --with-layout=apache to the command line in case --with-layout is not used. o fixed auto-suffix handling now that *config*.layout exists. paths which are auto-suffixed are marked with a trailing plus sign in *config*.layout and every path now can be marked this way (not only the four paths for which we do it currently).  additionally the suffix is no longer a static one. instead it's now `/<target>' where <target> is the argument of the --target option or per default `httpd'. o allow also tabs (and only spaces) where we match whitespaces o various fixes and cleanups related to used shell coding style o made jim happy by replacing `written by' with `initially written by' ;-) o trimmed output of --help to fit into 80 columns [ralf s. engelschall] 1.3.4 

*) added two new core api functions, ap_single_module_*config*ure() and ap_single_module_init(), which are now used by mod_so to *config*ure a module after loading. [ralf s. engelschall] 1.3.4 

*) port: add defines for use_flock_serialized_accept and single_*listen*_unserialized_accept to netbsd/openbsd section of ap_*config*.h to allow serialized accept for multiport *listen*s. [roy fielding, curt sampson] pr#3120 1.3.4 

*) port: fixed a misplaced #endif for netbsd/openbsd section of ap_*config*.h that would skip several defines if default_*group* was overridden. [roy fielding] 1.3.4 

*) port: the i86 version of dgux has support for strncasecmp and strcasecmp, so allow it in ap_*config*.h. [amiel lee yee] pr#3247 1.3.4 

*) fix ordering of definitions in ap_*config*.h so that ap_inline is defined before it might be used. [victor khimenko] 1.3.4 

*) make generation of src/*config*uration.apaci more robust: it failed to differenciate between modules when one module name was a postfix of another (e.g. cgi vs. fastcgi). we now check for mod_xxx, libxxx and even just xxx (think about totally non-standard names like "apache_ssl", too). [ralf s. engelschall] pr#3380 1.3.4 

*) in src/*config*ure remove the server_subversion support (already deprecated since 1.3b7) and make whitespace handling more robust (it failed horrible when whitespaces were present in the arguments of -d *options*). [ralf s. engelschall] pr#3240 1.3.4 

*) allow special *options* -wc,xxx and -wl,xxx on apxs compile/link command. they can occur multiple times and their arguments (`xxx') are passed as is to the compiler/linker command.  [ralf s. engelschall] 1.3.4 

*) added a generic --with-layout=[file:]id option. id here is a layout identifier, currently "apache" and "gnu" are pre-defined in the file *config*.layout.  custom layouts are possible by using file:id as the argument where the layout id is taken from file. the *config*.layout file consists of <layout id>..</layout> sections where inside those sections "path_variable: path_value" pairs can be specified. these lines are converted to path_variable='path_value'. 1.3.4 

*) add a *defaultlanguage* directive so that files missing a language extension (e.g., .fr, .de) can be labelled as being some other default language. *defaultlanguage* can appear in *<directory*> and *<files*> containers as well as .htaccess files.  [paul sutton] pr#1180 1.3.4 

*) fix target *config*uration when *config*uring and installing using apaci *config*ure. target now defines the basename of the *config*uration file, startup *script*, manual page, etc. log_error_core() now reports the server binary name given by argv[0]. target can now also be defined with --target=target parameter passed to apaci *config*ure. [ralf engelschall, randy terbush] 1.3.4 

*) api: ap_exists_*config*_define() function is now "public" [doug maceachern] 1.3.4 

*) fix documentation of `*action*' directive: it can activate a cgi *script* when either a handler or a mime content type is triggered by the request. [andrew pimlott <pimlott math.harvard.edu>] pr#3340 1.3.4 

*) ignore a "*errordocument* 401" directive with a full url and write a notice to the error log. it is not possible to send a 401 response and a *redirect* at the same time.  [lars eilebrecht] 1.3.4 

*) add apaci --*suexec*-docroot and --*suexec*-logfile *options* which can be used to set the document root directory (doc_root) and the *suexec* logfile (log_exec), respectively. additionally the --layout option was changed to show more information about the *suexec* setup. [lars eilebrecht] pr#3316, 3357, 3361 1.3.4 

*) enabled all of the webdav method names for use by third-party modules, limit, and *script* directives.  that includes patch, propfind, proppatch, mkcol, copy, move, lock, and unlock. improved mod_*action*s.c so that it can use any of the methods defined in httpd.h.  added ap_method_number_of(method) for getting the internal method number.  [roy fielding] 1.3.4 

*) win32: log more explicit error messages if spawning an interpreted *script* failed, including the command line used to attempt to execute the interpreter and the win32 error code returned.  [marc slemko] 1.3.4 

*) http_*config*.c would respond with 501 (method not implemented) if a content type handler was specified but could not be found, which should have been a 500 response.  likewise, mod_proxy.c would responsd with a 501 if the uri scheme is unrecognized instead of the correct response of 403 (forbidden).  [roy fielding] 1.3.4 

*) fix in mod_autoindex: for files where the last modified time stamp was unavailable, an empty string was printed which was 2 bytes short. the size and de*script*ion columns were therefore not aligned correctly. [martin kraemer] (no pr#) 1.3.4 

*) add apaci --permute-module=foo:bar option which can be used to on-the-fly/batch permute the order of two modules (mod_foo and mod_bar) in the *config*uration[.apaci] file. two special and important variants are supported for the option argument: first begin:foo which permutes module mod_foo with the begin of the module list, i.e. it `moves' the module to the begin of the list (gives it lowest priority).  and second foo:end which permutes mod_foo with the end of the module list, i.e. it `moves' the module to the end of the list (gives it highest priority). [ralf s. engelschall] 1.3.4 

*) the *config* parser wasn't correctly noticing a missing '>' on container start lines (e.g., it wouldn't spot "*<directory* /" as a syntax error).  [ryan bloom <rbbloom us.ibm.com>] pr#3279 1.3.4 

*) add a '*removehandler*' directive which will selectively remove all handler associations for the specified file extensions. [ryan bloom <rbbloom us.ibm.com>] pr#1799. 1.3.4 

*) properly handle & allow "nul" and ".*/null" in access*config* and resource*config* directives on win32.  also add a note to the effect of 'useless user directive ignored on win32' to the *errorlog* if a user directive is encountered on win32. [ken parzygnat <kparz raleigh.ibm.com>] pr#2078, 2303. 1.3.4 

*) fix inheritance of index*options* namewidth and remove unintended restriction on +namewidth, +iconheight, and +iconwidth.  [ken coar] 1.3.4 

*) fix per-directory *config* merging for cases in which a 500 error is encountered in an .htaccess file somewhere down the tree. [ken coar]  pr#2409 1.3.4 

*) remove extra trailing whitespace from the getline results as part of the *protocol* processing, which is extra nice because it works between continuation lines, is almost no cost in the normal case of no extra whitespace, and saves memory. [roy fielding] 1.3.3 

*) fix a possible race condition between timed-out requests and the ap_bhalfduplex select that might result in an infinite loop on platforms that do not validate the de*script*or. [roy fielding] 1.3.3 

*) win32: add "-k shutdown" and "-k restart" *options* to signal a running apache server [paul sutton] 1.3.3 

*) add the server signature text (from the core *serversignature* directive) to the list of envariables available to *script*s, ssi, and the like. [ken coar] 1.3.3 

*) fix the server_name variable under sub-request situations (where `*usecanonicalname* off' is used) like cgi's called from ssi pages or *rewritecond* variables by adopting r->hostname to sub-requests. [james grinter <jrg blodwen.demon.co.uk>] pr#3111 1.3.3 

*) fix stderr *redirect*ion under syslog-based error logging situation. [youichirou koga <y-koga jp.freebsd.org>] pr#3095 1.3.3 

*) document `*errorlog* syslog:facility' variant of error logging. [youichirou koga <y-koga jp.freebsd.org>] pr#3096 1.3.3 

*) quote paths in default *config*uration files.  [wilfredo sanchez] 1.3.3 

*) fix problem with *script*s and filehandle inheritance on win32. [ken parzygnat <kparz raleigh.ibm.com>]  pr#2884, 2910 1.3.3 

*) add [*redirect*_]variants environment variable to mod_speling so that *errordocument* 300 processors can reformat the list if desired.  [ken coar] pr#2859 1.3.3 

*) add +/- incremental prefixes to index*options* keywords, and enable merging of multiple index*options* directives.  [ken coar] 1.3.3 

*) os/2: the new header tests get things right, need to update ap_*config*.h.  [brian havard] 1.3.3 

*) port: add pyramid dc/osx support to *config*uration mechanism. [earle ake <akee wpdiss1.wpafb.af.mil>] 1.3.3 

*) correct comment in mod_log_*config*.c about its internals. [elf sternberg <elf halcyon.com>] 1.3.3 

*) avoid possible line overflow in *config*ure: use an awkfile to handle the creation of modules.c [jim jagielski] 1.3.2 

*) fix apaci's `*group*' *config*uration adjustment - especially for linux platforms where `no*group*' exists in /etc/*group*. [ralf s. engelschall] 1.3.2 

*) fix the recently introduced c header file checking: we now use the c pre-processor pass only (and no longer the complete compiler pass) to determine whether a c header file exists or not. because only this way we're safe against inter-header dependencies (which caused horrible portability problems). the only drawback is that we now have a cpp *config*uration variable which has to be determined first (we do a similar approach as gnu autoconf does here). when all fails the user still has the possibility to override it manually via apaci or src/*config*uration. as a fallback for the header check itself we can directly check the existance of the file under /usr/include, too. [ralf s. engelschall] pr#2777 1.3.2 

*) fix possible buffer overflow situation in *suexec*.c. [jeff stewart <jws purdue.edu>] pr#2790 1.3.2 

*) fix documentation of *proxypass*/*proxypass*reverse according to the trailing slash problem. [jon drukman <jsd gamespot.com>] pr#2933 1.3.2 

*) allow "include" directives anywhere in the server *config* files (but not .htaccess files).  [ken coar] pr#2727 1.3.2 

*) the proxy was refusing to serve connect requests except to port 443 (https://) and 563 (snews://). the new *allowconnect* directive allows the *config*uration of the ports to which a connect is allowed.  [sameer parekh, martin kraemer] 1.3.2 

*) problems encountered during .htaccess parsing or cgi execution that lead to a "500 server error" condition now provide explanatory text (in the *error_notes envariable) to *errordocument* 500 *script*s. [ken coar] pr#1291 1.3.2 

*) add namewidth keyword to index*options* directive so that the width of the filename column is customisable.  [ken coar, dean gaudet] pr#1949, 2324. 1.3.2 

*) the *<ifmodule* and *<ifdefine* block starting directives now only allow exactly one argument. previously, the optional negation character '!' could be separated by whitespace without a syntax error being reported, albeit defeating the ifmodule functionality (enclosed directives would always be executed). by using the stricter syntax, these hard-to-track errors can be avoided. [martin kraemer] 1.3.2 

*) simplify handling of index*options* in mod_autoindex -- and btw cause the standalone fancyindexing directive to logically or into any existing index*options* settings rather than wiping them out.  [ken coar] 1.3.2 

*) new `*gprofdir*' directive when compiled with -dgprof, where gprof can plop gmon.out profile data for each child [doug maceachern] 1.3.2 

*) use the construct ``"$@"'' instead of ``$*'' in the generated *config*.status *script* to be immune against arguments with whitespaces. [yves arrouye <yves apple.com>] pr#2866 1.3.2 

*) replace the inlined information grabbing stuff for the *config*uration adjustment feature (no --without-confadjust) with calls to a new helper *script* `buildinfo.sh' which is both more flexible and already proofed to be more robust against platform differences. this mainly fixes the recently occured ``sed: command garbled: ...'' problems. [ralf s. engelschall] pr#2776, pr#2848 1.3.2 

*) bump up max_env_flags in mod_rewrite.h from the too conservatice limit of 5 to 10 because there are some users out there who always have 5 to 8 variables in one *rewriterule* and had to patch mod_rewrite.h for every release. so 15 should be now more than enough, even for them. (i never needed more than 4 in my *rewriterule*s ;-) [ralf s. engelschall] 1.3.2 

*) make sure the *config*.status file is not overridden when just ``*config*ure --help'' is used. [ralf s. engelschall] pr#2844 1.3.2 

*) fix *suexec* installation under `make install root=xxx' situation. [ralf s. engelschall] 1.3.2 

*) extend the output of the -v switch to include the paths of all compiled-in *config*uration files, if they were overridden at compile time, for least astonishment of the user. [martin kraemer] 1.3.2 

*) when reading a request in *extendedstatus* mode, the "old" vhost, request and client information is not displayed. [jim jagielski] 1.3.2 

*) status is no longer available. full status information now run-time *config*urable using the *extendedstatus* directive. [jim jagielski] 1.3.2 

*) security: added compile-time and *config*urable limits for various aspects of reading a client request to avoid some simple denial of service attacks, including limits on maximum request-line size (*limitrequestline*), number of header fields (*limitrequestfields*), and size of any one header field (*limitrequestfields*ize).  also added a *config*urable directive *limitrequestbody* for limiting the size of the request message body.  [roy fielding] 1.3.2 

*) fix a problem with the new os/2 *mutex*es.  [brian havard] 1.3.2 

*) enhance mod_speling so that *checkspelling* can be used in *<directory*> containers and .htaccess files.  [ken coar] 1.3.2 

*) api: new ap_custom_response() function for hooking into the *errordocument* mechanism at runtime [doug maceachern] 1.3.2 

*) api: scan_*script*_header_err_core() now "public" and renamed ap_scan_*script*_header_err_core() [doug maceachern] 1.3.2 

*) the irixn32 rule was being ignored. *config*ure now correctly adds -n32 only if irixn32 says to. [jim jagielski, alain st-denis <alain.st-denis ec.gc.ca>] pr#2736 1.3.2 

*) fix *suexec* start message: has to be of `notice' level to really get printed together with the standard startup message because the `notice' level is handled special inside ap_log_error() for startup messages. [ralf s. engelschall] pr#2761 pr#2761 pr#2765 1.3.2 

*) fixed *example*s in mod_rewrite.html document. [youichirou koga <y-koga jp.freebsd.org>, ralf s. engelschall] pr#2756 1.3.2 

*) one more portability fix for apaci shadow tree support: swap order of awk and sed in top-level *config*ure *script* to avoid sed fails on some platforms (for instance sunos 4.1.3 and ncr sysv) because of the non-newline-termined output of awk. [ralf s. engelschall] pr#2729 1.3.2 

*) fix win32 part of ap_spawn_child() by providing a reasonable child_info structure instead of just null. this fixes at least the *rewritemap* programs under win32. [marco de michele <mdemichele tin.it>] pr#2483 1.3.2 

*) add workaround to top-level `*config*ure' *script* for brain dead `echo' commands which interpet escape sequences per default. [ralf s. engelschall] pr#2654 1.3.2 

*) make sure that the path to the perl interpreter is correctly adjusted under `make install' also for the printenv cgi *script*. [ralf s. engelschall] pr#2595 1.3.2 

*) use a more straight forward and thus less problematic sed command in src/helper/mkdir.sh *script*.  [ralf s. engelschall] 1.3.2 

*) make sure the `*config*ure' *script*s doesn't fail when trying to guess the domainname of the machine and there are multiple `domainname' and `search' entries in /etc/resolv.conf. [ralf s. engelschall] pr#2710 1.3.2 

*) fix document "hyperlink" for dso.html in src/*config*uration.tmpl [knut a.syed <knut.syed nhh.no>] pr#2674 1.3.2 

*) fix broken ranlib handling in src/*config*ure (the entry from src/*config*uration.tmpl was ignored) and additionally force ranlib to /bin/true under hp/ux where ranlib exists but is deprecated. [ralf s. engelschall] pr#2627 1.3.1 

*) win32: canonicalize *serverroot* before checking to see if it is a valid directory.  the failure to do this caused certain *serverroot* settings (eg. "*serverroot* /apache") to be improperly rejected.  [marc slemko] 1.3.1 

*) global renaming of c header files to both get rid of conflicts with third party packages and to again reach consistency: 1. conf.h      -> ap_*config*.h 2. conf_auto.h -> ap_*config*_auto.h \ these are now merged 3. ap_*config*.h -> ap_*config*_auto.h / in the *config* process 4. compat.h    -> ap_compat.h 5. apctype.h   -> ap_ctype.h backward compatibility files for conf.h and compat.h were created. 1.3.1 

*) mod_mmap_static will no longer take *action* on requests unless at least one "*mmapfile*" directive is present in the *config*uration. this experimental module has to do some black magic to operate inside the current api and thus creates side-effects for other modules under some circumstances. [ralf s. engelschall] 1.3.1 

*) add conservative ticks around more egrep arguments in top-level *config*ure to avoid problems under brain-dead platforms like digital unix (osf1). [ralf s. engelschall] pr#2596 1.3.1 

*) mod_*setenv*if (*browsermatch** and friends) will now match a missing field with "^$".  [ken coar] 1.3.1 

*) cache a proxied request in the event that the client cancels the transfer, provided that the *config*ured percentage of the file has already been transferred. it works for http transfers only.  the new *config*uration directive is called cacheforcecompletion. [glen parker <glenebob nwlink.com>] pr#2277 1.3.1 

*) *suexec*'s error messages have been clarified a little bit.  [ken coar] 1.3.1 

*) clean up some, but perhaps not all, 8-bit character set problems with *config* file parsing, and url parsing.  we now define ap_isdigit(), ap_isupper(), ... which cast to an (unsigned char). this should work on most modern unixes. [dean gaudet] pr#800, 2282, 2553  (and others) 1.3.1 

*) the *<limit*> parsing routine was incorrectly treating methods as case-insensitive.  [ken coar] 1.3.1 

*) fix the guess-dso-flags-from-perl stuff in src/*config*ure: "perl" was used instead of "$perl" which contains the correctly determined perl interpreter (important for instance on systems where "perl" and "perl5" exists, like bsdi or freebsd, etc). [ralf s. engelschall] pr#2505 1.3.1 

*) move the initial *suexec*-related startup message from plain fprintf()/stderr to a delayed ap_log_error()-based one to avoid problems when apache is started from inetd (instead of standalone). under this situation startup messages on stderr lead to problems (the line is sent to the client in front of the requested document). [ralf s. engelschall] pr#871, pr#1318 1.3.1 

*) win32: if we can't figure out how to execute a file in a *script* directory, bail out of the request with an error message.  [w g stoddard] 1.3.1 

*) *indexignore* should be case-blind on win32 (and any other case-aware but case-insensitive platforms).  new #define for this added to conf.h (case_blind_filesystem).  [ken coar] pr#2455 1.3.1 

*) let apaci's *config*ure *script* determine some *config*uration parameters (*group*, port, *serveradmin*, *servername*) via some intelligent tests to remove some of the classical hurdles for new users when setting up apache. this is done per default because it is useful for the average user. package authors can use the --without-confadjust option to disable these *config*uration adjustments. [ralf s. engelschall] 1.3.1 

*) added an extra_deps *config*uration parameter which can be used to add an extra makefile dependency for the httpd target, for instance to external third-party libraries, etc. [ralf s. engelschall] 1.3.1 

*) add *<ifdefine*>..</ifdefine> sections to the core module (with same spirit as *<ifmodule*>..</ifmodule> sections) which can be used to skip or process contained commands dependend of ``-d parameter'' *options* on the command line. this can be used to achieve logical conditions like *<ifdefine* reverseproxy> instead of physically ones (e.g. *<ifmodule* mod_proxy.c>) and thus especially can be used for conditionally loading dso-based modules via *loadmodule*, etc. [ralf s. engelschall] 1.3.1 

*) portability fix for apaci shadow tree support: swap order of awk and sed in top-level *config*ure *script* to avoid sed fails on some platforms (for instance sunos 4.1.3 and ncr sysv) because of the non-newline-termined output of awk. [bill houle <bhoule sandiegoca.ncr.com>] pr#2435 1.3.1 

*) add a tiny but useful goody to apaci's *config*ure *script*: the generation of a *config*.status *script* (as gnu autoconf does) which remembers the used *config*ure command and hence can be used to restore the *config*uration by just re-running this *script* or for remembering the *config*uration between releases. [ralf s. engelschall] 1.3.1 

*) add httpd -t (test) option for running *config*uration syntax tests only. if something is broken it complains and exits with a return code non-equal to 0. this can be used manually by the user to check the apache *config*uration after editing and is also automatically used by apachectl on (graceful) restart command to make sure apache doesn't die on restarts because of a *config*uration which is now broken since the last (re)start. this way `apachectl restart' can be used inside cronjobs without having to expect apache to be falling down. additionally the httpd -t can be run via `apachectl *config*test'. [ralf s. engelschall] pr#2393 1.3.1 

*) apache would incorrectly downcase the entire content-type passed from cgis.  this affected server-push *script*s and such which use multipart/x-mixed-replace;boundary=thisrandomstring. [dean gaudet] pr#2394 1.3.1 

*) fix missing usage de*script*ion for *metafiles* directive. [david mackenzie <djm va.pubnix.com>] pr#2384 1.3.1 

*) mod_log_*config* wouldn't let vhosts use log formats defined in the main server.  [christof damian <damian mediaconsult.com>] pr#2090 1.3.1 

*) change "*options* none" to "*options* followsymlinks" in the *<directory* /> section of the default access.conf-dist (and -win even though it doesn't matter there).  this has better performance, and more intuitive semantics.  [dean gaudet] 1.3.1 

*) workaround for *config*ure *script* and old `test' commands which do not support the -x flag (for instance under platforms like ultrix). this is solved by another helper *script* findprg.sh which searches for perl and awk like printpath but _via different names_. [ralf s. engelschall] 1.3.1 

*) proxy cache fixes: account for directory sizes, fork off garbage collection to continue in background, use predefined types (off_t, size_t, time_t), log the current cache usage percentage at *loglevel* debug [martin kraemer, based on discussion between dean gaudet & dirk vangulik] 1.3.0 

*) avoid problems with braindead awks by additionally searching for gawk and nawk in apaci's *config*ure *script*. [dave dykstra <dwd bell-labs.com>, ralf s. engelschall] pr#2319 1.3.0 

*) make sure the argument for the --add-module option to apaci's *config*ure *script* is of type [path/to/]mod_xxx.c because all calculations inside *config*ure and src/*config*ure depend on this. [ralf s. engelschall] pr#2307 1.3.0 

*) changes usage of perror/fprintf to stderr to more proper ap_log_error in mod_mime, mod_log_referer, mod_log_agent, and mod_log_*config*. [brian behlendorf] 1.3.0 

*) have nt properly set the directory for cgi *script*s (& other spawned children) [w g stoddard <wgstodda us.ibm.com>] 1.3.0 

*) propagate environment to cgi *script*s correctly in win32. [w g stoddard <wgstodda us.ibm.com>] pr#2294 1.3.0 

*) upgrade the child spawning code in mod_rewrite for the *rewritemap* programs: ap_spawn_child_err() is used and the win32 case now uses createprocess() instead of a low-level execl() (which caused problems in the past under win32). [ralf s. engelschall] 1.3.0 

*) proxy fix: the proxy special failure routine ap_proxyerror() was updated to use the normal apache error processing, thereby allowing proxy errors to be treated by *errordocument*'s as well. for this purpose, a new module-to-core communication variable "error-notes" was introduced; the proxy (and possibly other modules) communicates its error text using this variable. its content is copied to a new cgi-env-var *redirect*_error_notes for use by *errordocument*s. the old proxy special error routine ap_proxy_log_uerror() was replaced by regular ap_log_error() calls, many messages were made more informative. [martin kraemer] pr#494, 1259 1.3.0 

*) transform the *config*ure message "you need root privileges for *suexec*" from a fatal error into a (more friendly) warning because the building ("make") of apache we can allow, of course. root privileges are needed only for the installation step ("make install"). so make sure the user is aware of this fact but let him proceed as long as he can. [ralf s. engelschall] pr#2288 1.3.0 

*) make sure a mime-type can be forced via a *rewriterule* even when no substitution takes place, for instance via the following rule: ``*rewriterule* ^my*script*$ - [t=application/x-httpd-cgi]'' this was often requested by users in the past to force a single *script* without a .cgi extension and outside any cgi-bin dirs to be executed as a cgi program. [ralf s. engelschall] pr#2254 1.3b7 

*) a fix for *protocol* issues surrounding 400, 408, and 414 responses. [ed korthof] 1.3b7 

*) fix support *script* `dbmmanage': it was unable to handle some sort of passwords, especially passwords with "0" chars. [ralf s. engelschall] pr#2242 1.3b7 

*) win32: cgis could cause a hang (because of a deadlock in the standard c library), so cgi handling has been changed to use win32 native handles instead of c file de*script*ors. [ben laurie and bill stoddard <wgstodda us.ibm.com>] pr#1129, 1607 1.3b7 

*) replace the addversionplatform directive with *servertokens* which provides for more control over the format of the server: header line. server_subversion is no longer supported; all module should use the ap_add_version_component() api function instead. [jim jagielski] 1.3b7 

*) the ldflags_shlib_export variable of src/*config*uration[.tmpl] was not retrieved in src/*config*ure and thus was not useable. [ralf s. engelschall] 1.3b7 

*) various makefile consistency cleanups: - make osdir also automatically be relative to src/ like incdir - subdirs is now generated in src/makefile only and not in makefile.*config* because it is a local define for this location. - remove broken_bprintf_flags because is it no longer used inside any makefile but make sure that at least the "-k inline" is kept in cflags for sco 5. - update the "depend" targets in makefile.tmpl files to use $(osdir), too. - updated the dependencies theirself - removed not existing shlib variable from "clean" targets - replaced shlib_objs/shlibs_obj consistently with objs_pic because objs already exists and objs_pic are also just plain objects and have not directly to do with "shared" things. the only difference is that they contain pic. so objs_pic is the more canonical name. - updated the makefile-dependency lines for objs_pic - removed the makefile-dependency line in *config*ure to avoid double definitions - replaced ugly xx-so.o/xx.so-o hack with a clean and consistent usage of xxx.lo as gnu libtool does with its pic objects - reduce local complexity in modules makefile.tmpl by moving the last existing target "depend" to the generation section in *config*ure, too. - removed the historical $(spacer) which was used in the past together with broken_bprintf_flags to avoid zig-zags in the build process. this is no longer needed. - force the build and run of the gen_xxx programs under main/ as the first step before building the objects because it looks cleaner [ralf s. engelschall] 1.3b7 

*) when opening "*config*uration" files (like httpd.conf, htaccess and htpasswd), apache will not allow them to be non-/dev/null device files. this closes a dos hole. at the same time, we use ap_pfopen to open these files to handle *timeout*s. [jim jagielski, martin kraemer] 1.3b7 

*) apache will now log the reason its httpd children exit if they exit due to an unexpected signal.  (it requires a new porting define, sys_siglist, which if defined should point to a list of text de*script*ions of the signals available.  see porting.)  [dean gaudet] 1.3b7 

*) win32: chdir() doesn't make sense in a multithreaded environment like win32.  before, win32 cgi's could have had sporadic failures if a chdir call from one thread was made between another chdir call and a spawn in another thread.  so, for now don't chdir for cgi *script*s in win32.  the current cgi "spec" is unclear as to whether it's necessary.  long-term fix is to either serialize the chdir/spawn combo or use win32 native calls to spawn a process.  this temp fix was necessary to remove this as a showstopper for 1.3's release. [brian behlendorf] 1.3b7 

*) cleanup the *suexec* support in apaci and make it more safe: 1. add big fat hint in install about risks and to read the htdocs/manual/*suexec*.html document before using the *suexec*-related *config*ure *options*. 2. make sure the user has at least provided one --*suexec*-xxxx option (specifies *suexec* parameters) in addition to --enable-*suexec* option. if only --enable-*suexec* is given apaci stops with a hint to install and htdocs/manual/*suexec*.html documents. 3. provide two additional --*suexec*-xxxx *options* to make the *suexec* *config*uration complete (especially for package maintainers who else had to patch the source tree) by providing ways to *config*ure minimal uid/gid and safe path, too. [ralf s. engelschall] 1.3b7 

*) cleanup of the `*config*ure --shadow' process: - make sure the *config*ure *script* creates its temporary files in the shadow tree to avoid conflicts with parallel *config*ure runs - removed unnecessary option "-r" from "rm" call for makefiles - make sure the *config*ure *script*s creates the shadow-wrapper makefile only when no shadow trees already exists - make sure "make distclean" removes the shadow-wrapper makefile but only when no more shadow trees exists - overhauled mkshadow.sh *script*: now its more ifs-safe and approx. twice as fast (in the past it needed 70sec, now it runs just 38sec) - make sure cvs does not complain about the created files makefille.<gnutriple> and directories src.<gnutriple> [ralf s. engelschall] 1.3b7 

*) added the ap_add_version_component() api routine and the addversionplatform core directive.  the first allows modules to declare themselves in the server response header field value, augmenting the server_subversion define in the *config*uration file with run-time settings (more useful in a loadable-module environment). addversionplatform inserts a comment such as "(unix)" or "(win32)" into the server version string.  [ken coar] pr#2056 1.3b7 

*) add a note to httpd.conf-dist that apache will on some systems fail to start when the *group* # is set to a negative or large positive value. [martin kraemer] 1.3b7 

*) make sure the module execution order is correct even when some modules are loaded under runtime (`*loadmodule*') via the dso mechanism: 1. the list of loaded modules is now a dynamically allocated one and not the original statically list from modules.c 2. the loaded modules are now correctly setup by *loadmodule* for later use by the addmodule command. 3. when the dso mechanism for modules is used apaci's `install' target now enables all created `*loadmodule*' lines per default because this is both already expected by the user _and_ needed to avoid confusion with the next point and reduces the makefile.tmpl complexity 4. when the dso mechanism for modules is used, apaci's `install' target now additionally makes sure the module list is reconstructed via a complete `clearmodulelist+addmodule...' entry. 5. the support tool `apxs' now also makes sure an addmodule command is added in addition to the *loadmodule* command. 6. the modules.c generation was extended to now contain two comments to make sure no one is confused by the confusing terminology of loading/linking (we use load=link+load & link=activate instead of the obvious load=activate & link=link :-( ) this way now there is no longer a difference under execution time between statically and dynamically linked modules. [ralf s. engelschall] 1.3b7 

*) add a comment to mod_*example*.c showing the format of a flag command handler.  [ken coar] 1.3b7 

*) makes mod_rewrite, mod_log_*config*, mod_status and the *serversignature* feature compatible with '*usecanonicalname* off' by changing r->server->server_hostname to ap_get_server_name().  and i changed some functions which use r->server->port to use ap_get_server_port() instead, because if there's no port directive in the *config* r->server->port is 0. [lars eilebrecht] 1.3b7 

*) get/set_module_*config* are trivial enough to be better off inline.  worth 1.5% performance boost. [dean gaudet] 1.3b7 

*) [bs2000 security] bs2000 needs an extra authentication to initialize the task environment to the unprivileged user id. otherwise cgi *script*s would have a way to gain super user access. [martin kraemer] 1.3b7 

*) fix to mod_*alias*: translate_*alias*_redir is dealing with a uri, not a filename, so the check for drive letters for win32 and emx is not necessary. [dean gaudet] 1.3b7 

*) port: various porting changes to support aix 3.2, 4.1.5, 4.2 and 4.3. additionally the checks for finding the vendor dso library were moved from mod_so.c to *config*ure because first it needs $plat etc. and second mod_so already uses an abstr*action* layer and does not fiddle with the vendor functions itself. [jens-uwe mager, ralf s. engelschall] 1.3b7 

*) suppress "error(0)" messages for ap_log_error() when the aplog_noerrno is unset (as it is in situations like *timeout*s) where it is unclear whether errno is set or not.  [martin kraemer] 1.3b7 

*) just having apaci's localstatedir is too general and not enough for most of the systems. 1.3b6 again required manual apaci patches by package maintainers from red hat and freebsd because for their filesystem layout a little bit more flexibility in *config*uring the paths is needed. hence we provide three additional *config*ure *options* (--runtimedir, --logfiledir, --proxycachedir) which now can be used for more granular adjustments if --localstatedir is not enough to fit the particular needs. as a nice side-effect this reduces some subdir fiddling in *config*ure+makefile.tmpl. [ralf s. engelschall] 1.3b7 

*) make the install root for "make install" in apaci's makefile overrideable by package authors.  this way we are even more friendly to package maintainers (especially debian and red hat) who build for the real prefix via "*config*ure --prefix=/<real>" but use a different local prefix via "make root=/tmp/apache install" for rolling the package without bristling the target location on their system. [ralf s. engelschall] 1.3b7 

*) workaround sed limitations in apaci's *config*ure *script* by now substituting in chunks of 50 commands (because for instance hpux's vendor sed has a limit of max. 98 commands) [ralf s. engelschall] pr#2136 1.3b7 

*) workaround braindead awk's when generating ap_*config*.h: the split() and substr() functions cannot be nested under vendor awk from solaris 2.6. [ralf s. engelschall] pr#2139 1.3b7 

*) various bugfixes and cleanups for the apaci *config*ure *script*: o fix ifs handling for _nested_ situation o fix perl interpreter search: take first one found instead of last one o fix dso consistency check o print error messages to stderr instead of stdout o add install-quiet for --shadow situation to makefile stub o reduce complexity by avoiding sed-hacks for rule and module list loops [ralf s. engelschall] 1.3b7 

*) fix the path to the *scoreboardfile* in the install-*config* target, too. [ralf s. engelschall] pr#2105 1.3b7 

*) let "*config*ure" clear out the users parameters (provided as shell variables) to avoid side-effects in "src/*config*ure" when the user exported them (which is not needed, but some users do it). [ralf s. engelschall] pr#2101 1.3b7 

*) provide backward compatibility from some old src/*config*uration.tmpl parameter names to the canonical autoconf-style shell variable names. for instance cflags vs. extra_cflags. the extra_xxx variants are accepted now but a hint message is displayed. [ralf s. engelschall] 1.3b7 

*) make sure that "make install" doesn't overwrite the *documentroot* and cgi *script*s from an existing apache installation. [ralf s. engelschall, jim jagielski] pr#2084 1.3b7 

*) make `*config*ure --compat' more "compatible" by first let the libexecdir default to eprefix/libexec instead of eprefix/bin and second by making sure the "avoid-bristling-suffix" /apache is not appended to sysconfdir, datadir, localstatedir and includedir when --compat is used. [ralf s. engelschall, lars eilebrecht] 1.3b7 

*) fix the path to the *mimemagicfile* in the install-*config* target, too. [ralf s. engelschall] pr#2089 1.3b7 

*) if you start apache with the -s command line option it will dump out the parsed vhost settings.  this is useful for folks trying to figure out what is wrong with their vhost *config*uration. (other dumps may be added in the future.) [dean gaudet] 1.3b7 

*) because /usr/local/apache is the default prefix the ``*config*ure --compat'' option no longer has to set prefix, again. this way the --compat option honors a leading --prefix option. [lars eilebrecht] 1.3b7 

*) port: make sure some awk's don't fail in src/*config*ure with "string too long" errors when generating the modules entry for src/makefile [ben hyde, ralf s. engelschall] 1.3b7 

*) make sure src/*config*ure doesn't complain about the old directory /usr/local/etc/httpd/ when apaci is used.  [lars eilebrecht] 1.3b6 

*) ++++ the big symbol renaming ++++ to avoid symbol clashes with third-party code compiled into the server, we globally applied the prefix "ap_" to the following classes of functions: - apache provided general functions (e.g., ap_cpystrn) - public api functions (e.g., palloc, bgets) - private functions which we can't make static (because of cross-object usage) but should be (e.g., new_connection) for backward source compatibility a new header file named compat.h was created which provides defines for the old symbol names and can be used by third-party module authors. [the apache *group*] 1.3b6 

*) add "distclean" target to src/-makefiles to provide "make distclean" also inside the src subtree (i.e. for non-apaci users). following gnu makefile conventions while "clean" removes only stuff created by "all" targets, "distclean" additionally removes the stuff from the *config*uration process. this way "make distclean" (hence the name) provides a fresh source tree as it was for distribution. [ralf s. engelschall] 1.3b6 

*) fixed ordering of argument checks for *rewritebase* directive. [todd eigenschink <eigenstr mixi.net>] pr#2045 1.3b6 

*) add documentation file and src/*config*uration.tmpl entry for the experimental mod_mmap_static module. because although it is and marked as an experimental one it is distributed and thus should be documented and prepared for *config*uration the same way as all others modules. [ralf s. engelschall] 1.3b6 

*) now src/*config*ure uses a fallback strategy for the shared object support on platforms where no explicit information is available: if a perl installation exists we ask it about its shared object support and if it's the dlopen-style one we shamelessly guess the compiler and linker flags for creating shared objects from perls knowledge. of course, the user is warning about what we are doing and informed that he should send us the guessed flags when they work. [ralf s. engelschall] 1.3b6 

*) modify the log directives in httpd.conf-dist files to use *customlog* so that users have *example*s of how *customlog* can be used. [lars eilebrecht] 1.3b6 

*) add the new apache autoconf-style interface (apaci) for the top-level of the apache distribution tree.  until apache 1.3 there was no real out-of-the-box batch-capable build and installation procedure for the complete apache package. this is now provided by a top-level "*config*ure" *script* and a corresponding top-level "makefile.tmpl" file.  the goal is to provide a gnu autoconf-style frontend which is capable to both drive the old src/*config*ure stuff in batch and additionally installs the package with a gnu-conforming directory layout. any *options* from the old *config*uration scheme are available plus a lot of new *options* for flexibly customizing apache. [ralf s. engelschall] 1.3b6 

*) bug: *config*ure was using tcc and cc inconsistently. make sure *config*ure knows which cc we are using. [jim jagielski] 1.3b6 

*) "*options* +includes" wasn't correctly merged if "+includesnoexec" was defined in a parent directory. [lars eilebrecht] 1.3b6 

*) sigxcpu and sigxfsz are now reset to sig_dfl at boot-time.  this is necessary on at least solaris where the /etc/rc?.d *script*s are run with these signals ignored, and "sig_ign" settings are maintained across exec(). [rein tollevik <reint sys.sol.no>] pr#2009 1.3b6 

*) fix the check for symbolic links in ``*rewritecond* ... -l'': stat() was used instead of lstat() and thus this flag didn't work as expected. [rein tollevik <reint sys.sol.no>] pr#2010 1.3b6 

*) the default for *hostnamelookups* was changed to off, but there was a problem and it wasn't taking effect. [dean gaudet] 1.3b6 

*) port: clean up *undefine*d signals on some platforms (sco, beos). [dean gaudet] 1.3b6 

*) after a sighup the *listen*ing sockets in the parent weren't properly marked for closure on fork(). [jürgen keil <jk tools.de>] pr#2000 1.3b6 

*) reanimated the (still undocumented) proxy receive buffer size directive: renamed from *receive*buffersize** to proxy*receive*buffersize** because the old name was really too generic, added documentation for this directive to the mod_proxy.html and corrected the hyperlink to it in the new_features_1.3.html document.  [ralf s. engelschall] pr#1348 1.3b6 

*) fix a bug in the src/helpers/fp2rp *script* and make it a little bit faster [martin kraemer] 1.3b6 

*) make *config*ure die when you give it an unknown command switch. [ben hyde] 1.3b6 

*) add five new and fresh manpages for the support programs: dbmmanage.1, *suexec*.8, htdigest.1, rotatelogs.8 and logresolve.8.  now all up-to-date and per default compiled support programs have manual pages - just to document our stuff a little bit more and to be able to do really unix-like installations ;-) [ralf s. engelschall] 1.3b6 

*) major cleanups to the *config*ure *script* to make it and its generated makefiles again readable and maintainable: add srcdir option, removed includes_depth[0-2] kludge, cleanup of target option, cleanup of generated sections, consequently added makefile headers with inheritance information, added subdir movement messages for easier following where the build process currently stays (more verbose then standard make, less verbose than gnu make), same style to comments in the *config*ure *script*, added apache license header, fixed a few bugs, etc. [ralf s. engelschall] 1.3b6 

*) mod_proxy was not clearing the proxy-connection header from requests; now it does.  this did not violate any spec, however causes poor inter*action*s when you are talking to remote proxies. [marc slemko] pr#1741 1.3b6 

*) performance tweak to mod_log_*config*.  [dmitry khrustalev] 1.3b6 

*) clean up some undocumented behavior of mod_*setenv*if related to "merging" two *setenv*if directives when they match the same header and regex.  document that mod_*setenv*if will perform comparisons in the order they appear in the *config* file.  optimize mod_*setenv*if by doing more work at *config* time rather than at runtime. [dean gaudet] 1.3b6 

*) src/include/ap_*config*.h now wraps it's #define's with #ifndef/#endif's to allow for modules to overrule them and to reduce redefinition warnings [jim jagielski] 1.3b6 

*) added support for building shared objects even for library-style modules (which are built from more than one object file). this now provides the ability to build mod_proxy as a shared object module. additionally modules like mod_*example* are now also supported for shared object building because the generated makefiles now no longer assume there is at least one statically linked module. [ralf s. engelschall] 1.3b6 

*) prior to the existence of mod_*setenv* it was necessary to tweak the tz environment variable in the apache core.  but that tweaking interferes with mod_*setenv*.  so don't tweak if the user has specified an explicit tz variable.  [jay soffian <jay cimedia.com>] pr#1888 1.3b6 

*) various improvements to the *config*uration and build support for compiling modules as shared objects. especially solaris 2.x, sunos 4.1, irix and osf1 support with gcc and vendor compilers was added.  this way shared object support is now provided out-of-the-box for freebsd, linux, solaris, sunos, irix and osf1. in short: on all major platforms! [ralf s. engelschall] 1.3b6 

*) fix one more special locking problem for *rewritemap* programs in mod_rewrite: according to the documentation of flock(), "locks are on files, not file de*script*ors.  that is, file de*script*ors duplicated through dup(2) or fork(2) do not result in multiple instances of a lock, but rather multiple references to a single lock. if a process holding a lock on a file forks and the child explicitly unlocks the file, the parent will lose its lock.". to overcome this we have to make sure the rewritelock file is opened _after_ the childs were spawned which is now the case by opening it in the child_init instead of the module_init api hook. [ralf s. engelschall] pr#1029 1.3b6 

*) change to location and locationmatch semantics.  locationmatch no longer lets a single slash match multiple adjacent slashes in the url.  this change is for consistency with *rewriterule* and *alias*match.  multiple slashes have meaning in urls that they do not have in (some) filesystems.  location on the other hand can be considered a shorthand for a more complicated regex, and it does match multiple slashes with a single slash -- which is also consistent with the *alias* directive. [dean gaudet] related pr#1440 1.3b6 

*) the *config*ure *script* now generates src/include/ap_*config*.h which contains the set of defines used when apache is compiled on a platform. this file can then be included by external modules before including any apache header files in case they are being built separately from apache.  along with this change, a couple of minor changes were made to make apache's #defines coexist peacefully with any autoconf defines an external module might have. [rasmus lerdorf] 1.3b6 

*) fix mod_rewrite for the ugly api case where *<virtualhost*> sections exist but without any rewritexxxxx directives. here mod_rewrite is given no chance by the api to initialize its per-server *config*uration and thus receives the wrong one from the main server. this is now avoided by remembering the server together with the *config* structure while *config*uring and later assuming there is no *config* when we see a difference between the remembered server and the one calling us. [ralf s. engelschall] pr#1790 1.3b6 

*) fixed the dbm *rewritemap* support for mod_rewrite: first the support now is automatically disabled under *config*ure time when the dbm_xxx functions are not available. second, two heavy source code errors in the dbm support code were fixed.  this makes dbm *rewritemap*'s usable again after a long time of brokenness. [ralf s. engelschall] pr#1696 1.3b6 

*) now all *config*uration files support unix-style line-continuation via the trailing backslash ("\") character. this enables us to write down complex or just very long directives in a more readable way.  the backslash character has to be really the last character before the newline and it has not been prefixed by another (escaping) backslash. [ralf s. engelschall] 1.3b6 

*) when using *proxypass* the ?querystring was not passed correctly. [joel truher <truher wired.com>] 1.3b6 

*) api: rewrite of absoluteuri handling, and in particular how absoluteuris match vhosts.  unless a request is a proxy request, a "http://host" url is treated as if a similar "host:" header had been supplied.  this change was made to support future http/1.x *protocol*s which may require clients to send absoluteuris for all requests. in order to achieve this change subtle changes were made to the api.  in a request_rec, r->hostlen has been removed.  r->unparsed_uri now exists so that the unmodified uri can be retrieved easily.  r->proxyreq is not set by the core, modules must set it during the post_read_request or translate_names phase. plus changes to the virtualhost test suite for absoluteuri testing. this fixes several bugs with the proxy proxying requests to vhosts managed by the same httpd. [dean gaudet] 1.3b6 

*) reduce memory usage, and speed up *server*alias** support.  as a side-effect users can list multiple *server*alias** directives and they're all considered. [chia-liang kao <clkao cirx.org>] pr#1531 1.3b6 

*) add the `%a' construct to *logformat* and *customlog* to log the client ip address. [todd eigenschink <eigenstr mixi.net>] pr#1885 1.3b6 

*) make all possible meta-construct expansions ($n, %n, %{name} and ${map:key}) available for all location where a string is created in mod_rewrite rewriting rulesets: 1st arg of *rewritecond*, 2nd arg of *rewriterule* and for the [e=name:string] flag of *rewriterule*. this way the possible expansions are consequently usable at all string creation locations. [ralf s. engelschall] 1.3b6 

*) fix initialization of rewrite*loglevel* (default now is 0 as documented and not 1) and the per-virtual-server merging of directives. now all directives except `*rewriteengine*' and `rewriteoption' are either completely overridden (default) or completely inherited (when `rewrite*options* inherit') is used. [ralf s. engelschall] pr#1325 1.3b6 

*) fix `*rewritemap*' program lookup in situations where such maps are defined but disabled (`*rewriteengine* off') in per-server context. [ralf s. engelschall] pr#1431 1.3b6 

*) fix bug introduced in 1.3b4-dev, *config* with no port setting would cause server to bind to port 0 rather than 80.  [dean gaudet] 1.3b6 

*) fix long-standing problem with *rewritemap* _programs_ under unix derivates (like sunos and freebsd) which don't accept the locking of pipes directly.  a new directive rewritelock is introduced which can be used to setup a separate locking file which then is used for synchronization. [ralf s. engelschall] pr#1029 1.3b6 

*) win32: the server root is obtained from the registry key hklm\software\apache *group*\apache\<version> (version is currently "1.3 beta"), unless overridden by the -d command line flag. the value is stored by running "apache -i -d *serverroot*". [paul sutton] 1.3b6 

*) the mod_*setenv*if *browsermatch* backwards compatibility command did not work properly with spaces in the regex.  [ronald tschalaer] pr#1825 1.3b6 

*) add new *rewritemap* types: first, `rnd' which is equivalent to the `txt' type but with a special post-processing for the looked-up value: it parses it into alternatives according to `|' chars and then only one particular alternative is chosen randomly (this is an essential functionality needed for balancing between backend-servers when using apache as a reverse proxy.  the looked up value here is a list of servers). second, `int' with the built-in maps named `tolower' and `toupper' which can be used to map url parts to a fixed case (this is an essential feature to fix the case of server names when doing mass virtual-hosting with the help of mod_rewrite instead of using *<virtualhost*> sections). [ralf s. engelschall, parts based on code from jay soffian <jay cimedia.com>] pr#1631 1.3b6 

*) add a new directive to mod_proxy similar to *proxypass*: `*proxypass*reverse'. this directive lets apache adjust the url in location-headers on http *redirect* responses sent by the remote server. this way the virtually mapped area is no longer left on *redirect*s and thus by-passed which is especially essential when running apache as a reverse proxy. [ralf s. engelschall] 1.3b6 

*) use sa_resethand or sa_oneshot when installing the coredump handlers. in particular the handlers could trigger themselves into an infinite loop if *rlimitmem* was used with a small amount of memory -- too small for the signal stack frame to be set up.  [dean gaudet] 1.3b6 

*) fix multiple *userdir* problem introduced during 1.3b4-dev. [dean gaudet] pr#1850 1.3b6 

*) linux 2.0 and above implement rlimit_as, rlimit_data has almost no effect.  work around it by using rlimit_as for the *rlimitmem* directive.  [enrik berkhan <enrik inka.de>] pr#1816 1.3b6 

*) previously apache would permit </files> to end *<files*match> (and similary for location and directory), now this is diagnosed as an error.  improve error messages for mismatched sections (*<files*>, *<files*match>, *<directory*>, *<directory*match>, ...). [dean gaudet, martin kraemer] 1.3b6 

*) *<files*> is not permitted within *<location*> (because of the semantic ordering).  [dean gaudet] pr#379 1.3b6 

*) *<files*> with wildcards was broken by the change in wildcard semantics (* does not match /).  to fix this, *<files*> now apply only to the basename of the request filename.  this fixes some other inconsistencies in *<files*> semantics (such as *<files* a*b> not working).  [dean gaudet] pr#1817 1.3b6 

*) security: "*userdir* /abspath" without a * in the path would allow remote users to access "/~.." and bypass access restrictions (but note /~../.. was handled properly). [lauri jesmin <jesmin ut.ee>] pr#1701 1.3b6 

*) preserve the content encoding given by the *addencoding* directive when the client doesn't otherwise specify an encoding. [ronald tschalaer <ronald.tschalaer psi.ch>] 1.3b5 

*) all *browsermatch* directives mentioned in htdocs/manual/known_client_problems.html are in the default *config*uration files.  [lars eilebrecht] 1.3b4 

*) http/1.1 requires x-gzip and gzip encodings be treated equivalent, similarly for x-compress and compress.  apache now ignores a leading x- when comparing encodings.  it also preserves the encoding the client requests (for *example* if it requests x-gzip, then apache will respond with x-gzip in the content-encoding header). [ronald tschalaer <ronald.tschalaer psi.ch>] pr#1772 1.3b4 

*) added mod_so module to support dynamic loading of modules on unix (like mod_dld for win32). this replaces mod_dld.c. use sharedmodule instead of addmodule in *config*uration to build shared modules [sameer parekh, paul sutton] 1.3b4 

*) api: generalize default_port manipulations to make support of different *protocol*s easier. [ben laurie, randy terbush] 1.3b4 

*) there are many cases where users do not want apache to form self-referential urls using the "canonical" *servername* and port. the new *usecanonicalname* directive (default on), if set to off will cause apache to use the client-supplied hostname and port. api: part of this change required a change to the construct_url() prototype; and the addition of get_server_name() and get_server_port(). [michael douglass <mikedoug texas.net>, dean gaudet] pr#315, 459, 485, 1433 1.3b4 

*) yet another rearrangement of the source tree.. now all the common header files are in the src/include directory.  the -imain -iap references in makefiles have been changed to the simpler -iinclude instead.  in addition to simplifying the build a little bit, this also makes it clear when a module is referencing something in a other than kosher manner (e.g., the proxy including mod_mime.h). module-private header files (the proxy, mod_mime, the regex library, and mod_rewrite) have not been moved to src/include; nor have the os-abstr*action* files.  [ken coar] 1.3b4 

*) *options* and *allowoverride* weren't properly merging in the main server setting inside vhosts (only an issue when you have no *<directory*> or other section containing an *options* that affects a request).  *options* +foo or -foo in the main_server wouldn't affect the main_server's lookup defaults.  [dean gaudet] 1.3b4 

*) mod_unique_id was erroneously generating a second unique id when an internal *redirect* occured.  such *redirect*s occur, for *example*, when processing a *directoryindex* match.  [dean gaudet] 1.3b4 

*) more mod_mime_magic cleanup:  fewer syscalls; should handle "files" which don't exist on disk more gracefully; handles vhosts properly. update documentation to reflect the code -- if there's no *mimemagicfile* directive then the module is not enabled. [dean gaudet] 1.3b4 

*) port: some older *nix dialects cannot automatically start *script*s which begin with a #! interpreter line (the shell starts the *script*s appropriately on these platforms). apache now supports starting of "hashbang-*script*s" when the need_hashbang_emul define is set. [martin kraemer, with code from peter wemm <peter zeus.dialix.oz.au> taken from tcsh] 1.3b4 

*) for clarity the following compile time definition was changed: safe_unserialized_accept  ->   single_*listen*_unserialized_accept also, for *example*, have_mmap would mean to use mmap() scoreboards and not be a general notice that the os has mmap(). now the have_mmap/shmget #defines strictly are informational that the os has that method of shared memory; the type to use for the scoreboard is a seperate #define (use_mmap_scoreboard and use_shmget_scoreboard). this allows outside modules to determine if shared memory is available and allows apache to determine the best method to use for the scoreboard. [jim jagielski] 1.3b4 

*) port: a/ux can handle single-*listen* accepts without *mutex* locking, so we add single_*listen*_unserialized_accept. [jim jagielski] 1.3b4 

*) when die() happens we need to eat any request body if one exists. otherwise we can't continue with a *keepalive* *session*.  this shows up as a post problem with msie 4.0, typically against pages which are authenticated.  [roy fielding] pr#1399 1.3b4 

*) fix y2k problem with date printing in *suexec* log. [paul eggert <eggert twinsun.com>] pr#1343 1.3b4 

*) *suexec* errors now include the errno/de*script*ion.  [marc slemko] pr#1543 1.3b4 

*) port: osf/1 now uses use_flock_serialized_accept to solve pr#467. the choice of flock vs. fcntl was made based on timings which showed that even on non-nfs, non-exported filesystems fcntl() was an order of magnitude slower.  it also uses single_*listen*_unserialized_accept so that single socket users will see no difference. [dean gaudet] pr#467 1.3b4 

*) mod_rewrite's rewritelog should behave like mod_log_*config*, it shouldn't force hostname lookups.  [dean gaudet] pr#1684 1.3b4 

*) for maximum portability, the environment passed to cgis should only contain variables whose names match the regex /[a-za-z][a-za-z0-9_]*/.  this is now enforced by stamping underscores over any character outside the regex.  this affects http_* variables, in a way that should be backward compatible for all the standard headers; and affects variables set with *setenv*/*browsermatch* and similar directives. [dean gaudet] 1.3b4 

*) new -c and -c command line arguments usage: -c "directive" : process directive before reading *config* files -c "directive" : process directive after reading *config* files *example*: httpd -c "perlmodule apache::httpd_conf" [doug maceachern, martin kraemer] 1.3b4 

*) win32: fix the execution of cgis that are *script*s and called with path info that does not have an '=' in. (eg. http://server/cgi-bin/printenv?foobar) [marc slemko] pr#1591 1.3b4 

*) the *authname* must now be enclosed in quotes if it is to contain spaces.  [ken coar] pr#1195 1.3b4 

*) non-win32 was missing destroy_*mutex* definition.  [ben hyde] 1.3b4 

*) mod_autoindex had an fread() without checking the result code. it also wouldn't handle "*addicon*bytype (txt,/icons/text.gif text/*" (note the missing closing paren) properly.  [dean gaudet] 1.3b4 

*) "*redirect*match gone /" would cause a sigsegv. [dean gaudet] pr#1319 1.3b4 

*) the pthread_*mutex*_* functions return an error code, and don't set errno.  [igor tatarinov <tatarino prairie.nodak.edu>] 1.3b4 

*) fix problems with *timeout*s in inetd mode and -x mode.  [dean gaudet] 1.3b4 

*) give a more informative error when no *authtype* is set. [lars eilebrecht] 1.3b3 

*) directives owned by http_core can now use the new check_cmd_context() routine to ensure that they're not being used within a container (e.g., *<directory*>) where they're invalid.  [martin kraemer] 1.3b3 

*) mod_autoindex wasn't displaying the *readmename* file at the bottom unless it was also doing fancyindexes, but it displayed the *headername* file at the top under all circumstances.  it now shows the *readmename* file for simple indices, too, as it should. [ken coar] pr#1373 1.3b3 

*) complete rewrite ;-) of mod_rewrite's url rewriting engine: now the rewriting engine (the heart of mod_rewrite) is organized more straight-forward, first time well documented and reduced to the really essential parts. all redundant cases were stripped off and processing now is the same for both per-server and per-directory context with only a minimum difference (the prefix stripping in per-dir context). as a side-effect some subtle restrictions and two recently discovered problems are gone: wrong escaping of query_string on *redirect*s in per-directory context and restrictions on the substitution url on *redirect*s. additionally some minor source cleanups were done. [ralf s. engelschall] 1.3b3 

*) lars eilebrecht wrote a whole new set of apache vhost internals documentation, *example*s, explanations and caveats. they live in a new subdirectory htdocs/manual/vhost/. [lars eilebrecht <sfx unix-ag.org>] 1.3b3 

*) if ap_slack fails to allocate above the low slack line it's a good indication that further problems will occur; it's a better indication than many external libraries give us when we actually run out of de*script*ors.  so report it to the user once per restart. [dean gaudet] pr#1181 1.3b3 

*) add a "suppresscolumnsorting" option to the index*options* list, which will keep the column heading from being links for sorting the display.  [ken coar, suggested by brian tiemann <btman pacific.net>] pr #1261 1.3b3 

*) preserve handler value on *proxypass*'ed requests by not calling find_types on a proxy'd request; fixes problems where some *proxypass*'ed urls weren't actually passed to the proxy. [lars eilebrecht] pr#870 1.3b3 

*) fix problem with use_flock_serialized_accept not working properly. each child needs to open the lockfile instead of using the passed file-de*script*or from the parent. [jim jagielski] pr#1056 1.3b3 

*) default to use_fcntl_serialized_accept on hpux to properly handle multiple *listen* directives.  [marc slemko] pr#872 1.3b3 

*) when a *config*uration parse complained about a bad directive, the logger would use whatever (unrelated) value was in errno. errno is now forced to einval first in this case.  [ken coar] 1.3b3 

*) a sed command in the *config*ure *script* pushed the edge of posixness, breaking on some systems.  [bhaba r.misra <system vt.edu>] pr#1368 1.3b3 

*) solaris >= 2.5 was totally broken due to a mess up using pthread *mutex*es.  [roy fielding, dean gaudet] 1.3b3 

*) ensure that one copy of *config* warnings makes it to the error_log.  [dean gaudet] 1.3b3 

*) invent new structure and associated methods to handle *config* file reading. add "custom" hook to use *config* file cfg_getline() on something which is not a file*  [martin kraemer] 1.3b3 

*) various improvements in detecting *config* file errors (missing closing directives for *<directory*>, *<files*> etc. blocks, prohibiting global server settings in *<virtualhost*> blocks, flagging unhandled multiple arguments to *<directory*>, *<files*> etc.) [martin kraemer] 1.3b3 

*) add support to *suexec* wrapper program for mod_unique_id's unique_id variable to provide this one to *suexec*'d cgis, too. [m.d.parker <mdpc netcom.com>] pr#1284 1.3b3 

*) new support tool: src/support/split-logfile, a sample perl *script* which splits up a combined access log into separate files based on the name of the virtual host (listed first in the log records by "%v"). [ken coar] 1.3b2 (there is no 1.3b1) 

*) *config*ure uses a sh trap and didn't set its exitcode properly. [dean gaudet] pr#1159 1.3b2 (there is no 1.3b1) 

*) yet another vhost revamp.  add the *namevirtualhost* directive which explicitly lists the ip:port pairs that are to be used for name-vhosts. from a given ip:port, regardless what the host: header is, you can only reach the vhosts defined on that ip:port.  the precedence of vhosts was reversed to match other precedences in the *config* -- the earlier vhosts override the later vhosts.  all vhost matching was moved into http_vhost.[ch].  [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) *coredumpdirectory* directive directs where the core file is written when a sigsegv, sigbus, sigabort or sigabrt are received.  [marc slemko, dean gaudet] 1.3b2 (there is no 1.3b1) 

*) when booting, apache will now detach itself from stdin, stdout, and stderr.  stderr will not be detached until after the *config* files have been read so you will be able to see initial error messages.  after that all errors are logged in the error_log. this makes it more convenient to start apache via rsh, ssh, or crontabs.  [dean gaudet] pr#523 1.3b2 (there is no 1.3b1) 

*) *suexec*.c wouldn't build without -dlog_exec. [jason a. dour] 1.3b2 (there is no 1.3b1) 

*) mod_autoindex improperly counted &escapes; as more than one character in the de*script*ion.  it also improperly truncated de*script*ions that were exactly the maximum length. [martin kraemer] 1.3b2 (there is no 1.3b1) 

*) *redirect*match was not properly escaping the result (pr#1155).  also "*redirect*match /advertiser/(.*) $1" is now permitted. [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) mod_include now uses symbolic names to check for request success and return http errors, and correctly handles all types of *redirect*ions (previously it only did temporary *redirect* correctly). [ken coar, roy fielding] 1.3b2 (there is no 1.3b1) 

*) mod_*userdir* was modifying r->finfo in cases where it wasn't setting r->filename.  since those two are meant to be in sync with each other this is a bug.  ["paul b. henson" <henson intranet.csupomona.edu>] 1.3b2 (there is no 1.3b1) 

*) inetd mode (which is buggy) uses *timeout*s without having setup the jmpbuffer. [dean gaudet] pr#1064 1.3b2 (there is no 1.3b1) 

*) if buffered_logs is defined then mod_log_*config* will do atomic buffered writes -- that is, it will buffer up to pipe_buf (i.e. 4k) bytes before writing, but it will never split a log entry across a buffer boundary.  [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) changes to mod_log_*config* to allow naming of format strings. format nicknames are defined with "*logformat* fmt nickname", and can be used with "*logformat* nickname" and "*customlog* logtarget nickname". [ken coar] 1.3b2 (there is no 1.3b1) 

*) *really* disable all mod_rewrite operations if the engine is off. some things (like *rewritemap*s) were checked/performed even if they weren't supposed to be.  [ken coar] pr #991 1.3b2 (there is no 1.3b1) 

*) implement a new timer scheme which eliminates the need to call alarm() all the time.  instead a counter in the scoreboard for each child is used to show when the child has made forward progress.  the parent samples this counter every scoreboard maintenance cycle, and issues sigalrm if no progress has been made in the *timeout* period.  this reduces the static request best-case syscall count to 22 from 29.  this scheme is only used by systems with memory-based scoreboards.  [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) the proxy now properly handles connect requests which are sent to proxy servers when using *proxyremote*.  [marc slemko] pr#1024 1.3b2 (there is no 1.3b1) 

*) a *script* called apachectl has been added to the support directory.  this *script* allows you to do things such as "apachectl start" and "apachectl restart" from the command line.  [marc slemko] 1.3b2 (there is no 1.3b1) 

*) removal of mod_auth_msql.c from the distribution. there are many other *options* for databases today. rather than offer one option, offer none at this time. mod_auth_msql and other sql database authentication modules can be found at the apache module registry. http://modules.apache.org/ it would be nice to offer a generic mod_auth_sql option in the near future. 1.3b2 (there is no 1.3b1) 

*) *config*ure no longer accepts the -make option, since it creates makefile on the fly based on makefile.tmpl and *config*uration. 1.3b2 (there is no 1.3b1) 

*) add aplog_error() providing a mechanism to define levels of verbosity to the server error logging. this addition also provides the ability to log errors using syslogd. error logging is *config*urable on a per-server basis using the *loglevel* directive. conversion of log_*() in progress. [randy terbush] 1.3b2 (there is no 1.3b1) 

*) add the server version (server_version macro) to the "server *config*ured and running" entry in the error_log.  also build an object file at link-time that contains the current time (server_built global const char[]), and include that in the message.  [ken coar] 1.3b2 (there is no 1.3b1) 

*) if no *transferlog* is given explicitly, decline to log.  this supports coexistence with other logging modules, such as the custom one that uunet uses. [david j. mackenzie] 1.3b2 (there is no 1.3b1) 

*) change mod_cern_meta to be *config*urable on a per-directory basis. [david j. mackenzie] 1.3b2 (there is no 1.3b1) 

*) add 'include' directive to allow inclusion of *config*uration files within *config*uration files. [randy terbush] 1.3b2 (there is no 1.3b1) 

*) api: added post_read_request api phase which is run right after reading the request from a client, or right after an internal *redirect*.  it is useful for modules setting environment variables that depend only on the headers/contents of the request.  it does not run during subrequests because subrequests inherit pretty much everything from the main request. [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) port: apache has need for *mutex*es to serialize its children around accept.  in prior versions either fcntl file locking or flock file locking were used.  the method is chosen by the definition of use_xxx_serialized_accept in conf.h.  xxx is fcntl for fcntl(), and flock for flock().  new *options* have been added: - sysvsem to use system v style semaphores - pthread to use posix threads (appears to work on solaris only) - uslock to use irix uslock based on timing various techniques, the following changes were made to the defaults: - linux 2.x uses flock instead of fcntl - solaris 2.x uses pthreads - irix uses sysv semaphores -- however multiprocessor irix boxes work far faster if you -duse_uslock_serialized_accept [dean gaudet, pierre-yves kerembellec <pierre-yves.kerembellec vtcom.fr>, martijn koster <m.koster pobox.com>] 1.3b2 (there is no 1.3b1) 

*) port: the semantics of accept/select make it very desirable to use *mutex*es to serialize accept when multiple *listen*s are in use.  but in the case where only a single socket is open it is sometimes redundant to serialize accept().  not all unixes do a good job with potentially dozens of children blocked on accept() on the same socket.  it's now possible to define single_*listen*_unserialized_accept and the server will avoid serialization when *listen*ing on only one socket, and use serialization when *listen*ing on multiple sockets. [dean gaudet] pr#467 1.3b2 (there is no 1.3b1) 

*) *config*ure changes: testlib replaced by testcompile, which has some additional capability (such as doing a sanity check of the compiler and flags selected); the version of solaris is now available via the #define value of solaris2; irix n32bit libs now supported and selectable by new *config*uration rule: irixn32; we no longer default to -o2 optimization.  [jim jagielski] 1.3b2 (there is no 1.3b1) 

*) updated *config*ure: *config*uration now uses addmodule to specify module source or binary file location, relative to src directory. modules can be dropped into modules/extra, or in their own directory, and modules can come with a makefile or *config*ure can create one.  modules can add compiler or library information to generated makefiles. [paul sutton] 1.3b2 (there is no 1.3b1) 

*) mod_browser has been removed, since it's replaced by mod_*setenv*if. [ken coar] 1.3b2 (there is no 1.3b1) 

*) directory_walk optimization to reduce an o(n*m) loop to o(n+m) where n is the number of *<directory*> sections, and m is the number of components in the filename of an object. to achieve this optimization the following *config* changes were made: - wildcards (* and ?, not the regex forms) in *<directory*>s, *<files*>s, and *<location*>s now treat a slash as a special character.  for *example* "/home/*/public_html" previously would match "/home/a/andrew/public_html", now it only matches things like "/home/bob/public_html".  this mimics /bin/sh behaviour. - it's possible now to use [] wildcarding in *<directory*>, *<files*> or *<location*>. - regex *<directory*>s are applied after all non-regex *<directory*>s. [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) enhanced and cleaned up the url rewriting engine of mod_rewrite: first the *group*ed parts of *rewriterule* pattern matches (parenthesis!) can be accessed now via backreferences $1..$9 in *rewritecond*s test-against strings in addition to *rewriterule*s subst string. second the *group*ed parts of *rewritecond* pattern matches (parenthesis!) can be accessed now via backreferences %1..%9 both in following *rewritecond* test-against strings and *rewriterule*s subst string. this provides maximum flexibility through the use of backreferences. additionally the rewriting engine was cleaned up by putting common code to the new expand_backrefs_inbuffer() function. [ralf s. engelschall] 1.3b2 (there is no 1.3b1) 

*) when merging the main server's *<directory*> and *<location*> sections into a vhost, put the main server's first and the vhost's second.  otherwise the vhost can't override the main server.  [dean gaudet] pr#717 1.3b2 (there is no 1.3b1) 

*) the *<directory*> code would merge and re-merge the same section after a match was found, possibly causing problems with some modules. [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) ip-based vhosts are stored and queried using a hashing function, which has been shown to improve performance on servers with many ip-vhosts. some other changes had to be made to accommodate this: - the * address for vhosts now behaves like _default_ - the matching process now is: - match an ip-vhost directly via hash (possibly matches main server) - if that fails, just pretend it matched the main server - if so far only the main server has been matched, perform name-based lookups (*servername*, *server*alias**, *serverpath*) *only on name-based vhosts* - if they fail, look for _default_ vhosts [dean gaudet, dave hankins <dhankins sugarat.net>] 1.3b2 (there is no 1.3b1) 

*) dbmmanage overhaul: - merge dbmmanage and dbmmanage.new functionality, remove dbmmanage.new - tie() to anydbm_file which will use one of db_file, ndbm_file or gdbm_file (-ldb, -lndbm, -lgdbm) (trying each in that order) - provide better seed for rand - prompt for password as per getpass(3) (turn off echo, read from /dev/tty, etc.) - use "newstyle" crypt based on $*config*{osname} ($^o) - will not add a user if already in database, use new `update' command instead - added `check' command to check a users' password - added `import' command to convert existing password text-files or dbm files exported with `view' - more de*script*ive usage, general cleanup, 'use strict' clean, etc. [doug maceachern] 1.3b2 (there is no 1.3b1) 

*) enable ``=""'' for *rewritecond* directives to match against the empty string. this is the preferred way instead of ``^$''. [ralf s. engelschall] 1.3b2 (there is no 1.3b1) 

*) mod_proxy now has a *receive*buffersize** directive, similar to *send*buffersize**, so that the tcp window can be set appropriately for lfns. [phillip a. prindeville] 1.3b2 (there is no 1.3b1) 

*) mod_browser has been replaced by the more general mod_*setenv*if (courtesy of paul sutton).  *browsermatch** directives are still available, but are now joined by *setenv*if*, un*setenv*if*, and un*setenv*ifzero directives.  [ken coar] 1.3b2 (there is no 1.3b1) 

*) "*hostnamelookups* double" forces double-reverse dns to succeed in order for remote_host to be set (for logging, or for the env var remote_host).  the old define maximum_dns has been deprecated. [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) mod_access overhaul: - now understands network/netmask syntax (i.e.  10.1.0.0/255.255.0.0) and cidr syntax (i.e. 10.1.0.0/16).  pr#762 - critical path was sped up by pre-computing a few things at *config* time. - the undocumented syntax "allow user-agents" was removed, the replacement is "allow from env=foobar" combined with mod_browser. - when used with hostnames it now forces a double-reverse lookup no matter what the directory settings are.  this double-reverse doesn't affect any of the other routines that use the remote hostname.  in particular it's still passed to cgis and the log without the double-reverse check.  related pr#860. [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) port: some variants of dgux require -lsocket -lnsl [alexander l jones <alex systems-*options*.co.uk>] pr#732 1.3b2 (there is no 1.3b1) 

*) child_main avoids an unneeded call to select() when there is only one *listen*ing socket.  [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) in the event that the server is starved for idle servers it will spawn 1, then 2, then 4, ..., then 32 servers each second, doubling each second.  it'll also give a warning in the *errorlog* since the most common reason for this is a poor *startservers* setting.  the define max_spawn_rate can be used to raise/lower the maximum.  [dean gaudet] 1.3b2 (there is no 1.3b1) 

*) apache now provides an effectively unbuffered connection for cgi *script*s.  this means that data will be sent to the client as soon as the cgi pauses or stops output; previously, apache would buffer the output up to a fixed buffer size before sending, which could result in the user viewing an empty page until the cgi finished or output a complete buffer.  it is no longer necessary to use an "nph-" cgi to get unbuffered output.  given that most cgis are written in a language that by default does buffering (e.g. perl) this shouldn't have a detrimental effect on performance. "nph-" cgis, which formerly provided a direct socket to the client without any server post-processing, were not fully compatible with http/1.1 or ssl support.  as such they would have had to implement the transport details, such as encryption or chunking, in order to work properly in certain situations.  now, the only difference between nph and non-nph *script*s is "non-parsed headers". [dean gaudet, sameer parekh, roy fielding] 1.3b2 (there is no 1.3b1) 

*) added another *config*ure helper *script*: testlib. it determines if a specified library exists.  [jim jagielski] 1.3a1 

*) port: qnx doesn't have init*group*s() which support/*suexec*.c uses. [igor n kovalenko <infoh mail.wplus.net>] 1.3a1 

*) "force-response-1.0" now only applies to requests which are http/1.0 to begin with.  "no*keepalive*" now works for http/1.1 clients.  added "downgrade-1.0" which causes apache to pretend it received a 1.0. [dean gaudet] related pr#875 1.3a1 

*) api: correct child_init() slot declaration from int to void, to match the init() declaration.  update mod_*example* to use the new hook.  [ken coar] 1.3a1 

*) support the image map format of frontpage.  for *example*: rect /url.hrm 10 20 30 40 ["chris o'byrne" <obyrne iol.ie>] pr#807 1.3a1 

*) *addmoduleinfo* directive for mod_info which allows you to annotate the output of mod_info.  ["lou d. langholtz" <ldl usi.utah.edu>] 1.3a1 

*) added *noproxy* directive to avoid using *proxyremote* for selected addresses.  added *proxydomain* directive to cause unqualified names to be qualified by *redirect*ion. [martin kraemer <martin.kraemer mch.sni.de>] 1.3a1 

*) upgraded mod_rewrite from 3.0.6+ to latest officially available version 3.0.9. this upgrade includes: fixed deadlooping on rewriting to same urls, fixed rewritelog(), fixed forced response code handling on *redirect*s from within .htaccess files, disabled pipe locking under braindead sunos 4.1.x, allow env variables to be set even on rules with no substitution, bugfixed situations where *hostnamelookups* is off, made mod_rewrite more thread-safe for nt port and fixed problem when creating an empty query string via "xxx?". this update also removes the copyright of ralf s. engelschall, i.e. now mod_rewrite no longer has a shared copyright. instead is is exclusively copyrighted by the apache *group* now. this happened because the author now has gifted mod_rewrite exclusively to the apache *group* and no longer maintains an external version. [ralf s. engelschall] 1.3a1 

*) api: added child_init function to module structure.  this is called once per "heavy-weight process" before any requests are handled. see http_*config*.h for more details.  [dean gaudet] 1.3a1 

*) *anonymous*_logemail was logging on each subrequest. [dean gaudet] pr#421, 868 1.3a1 

*) *config*ure fixed to correctly propagate user-selected *options* and settings (such as cc and optim) to makefiles other than src/makefile (notably support/makefile).  [ken coar] pr#666, #834 1.3a1 

*) index*options* suppresshtmlpreamble now causes the actual html of directory indices to start with the contents of the *headername* file if there is one.  if there isn't one, the behaviour is unchanged. [ken coar, roy fielding, andrey a. chernov] 1.3a1 

*) win32: modules can now be dynamically loaded dlls using the *loadmodule*/*loadfile* directives. note that module dlls must be compiled with the multithreaded dll version of the runtime library. [alexei kosut and ben laurie] 1.3a1 

*) automatic indexing removed from mod_dir and placed into mod_autoindex. this allows the admin to completely remove automatic indexing from the server, while still supporting the basic functions of trailing-slash *redirect*s and *directoryindex* files.  note that if you're carrying over an old *config*uration file and you use directory indexing then you'll want to add: module autoindex_module    mod_autoindex.o before mod_dir in your *config*uration.  [dean gaudet] 1.3a1 

*) *alias*match, *script**alias*match and *redirect*match directives added, giving regex support to mod_*alias*. *<directory*match>, *<location*match> and *<files*match> sections added to succeed *<directory*match ~>, etc... [alexei kosut] 1.3a1 

*) the *accessfilename* directive can now take more than one filename. ["lou d. langholtz" <ldl usi.utah.edu>] 1.3a1 

*) *config*: "*hostnamelookups*" now defaults to off because it is far better for the net if we require people that actually need this data to enable it.  [linus torvalds] 1.3a1 

*) in *config*urations using multiple *listen* statements it was possible for busy sockets to starve other sockets of service.  [dean gaudet] 1.3a1 

*) enhance *userdir* directive (mod_*userdir*) to accept a list of usernames for the 'disable' keyword, and add 'enable user...' to selectively *en*able *userdir*s if they're globally disabled. [ken coar] 1.3a1 

*) add a *listen*backlog directive to control the backlog parameter passed to *listen*().  also change the default to 511 from 512. [marc slemko] 1.3a1 

*) added iconheight and iconwidth to mod_dir's index*options* directive. when used together, these cause mod_dir to emit height and width attributes in the fancyindexing img tags.  [ken coar] 1.3a1 

*) mod_include when using *xbithack* full would send etags in addition to sending last-modifieds.  this is incorrect http/1.1 behaviour. [dean gaudet] pr#1133 1.2.6 

*) when an error occurs during a post, or other operation with a request body, the body has to be read from the net before allowing a *keepalive* *session* to continue.  [roy fielding] pr#1399 1.2.6 

*) *suexec*.c wouldn't build without -dlog_exec. [jason a. dour] 1.2.5 

*) mod_*userdir* was modifying r->finfo in cases where it wasn't setting r->filename.  since those two are meant to be in sync with each other this is a bug.  ["paul b. henson" <henson intranet.csupomona.edu>] 1.2.5 

*) mod_include did not properly handle all possible *redirect*s from sub- requests.  [ken coar] 1.2.5 

*) inetd mode (which is buggy) uses *timeout*s without having setup the jmpbuffer. [dean gaudet] pr#1064 1.2.5 

*) the *proxyremote* change in 1.2.3 introduced a bug resulting in the proxy always making requests with the full-uri instead of just the uri path. [marc slemko, roy fielding] 1.2.4 

*) the request to a remote proxy was mangled if it was generated as the result of a *proxypass* directive. url schemes other than http:// were not supported when *proxyremote* was used. pr#260, pr#656, pr#699, pr#713, pr#812 [lars eilebrecht] 1.2.3 

*) when merging the main server's *<directory*> and *<location*> sections into a vhost, put the main server's first and the vhost's second.  otherwise the vhost can't override the main server.  [dean gaudet] pr#717 1.2.2 [not released] 

*) the *<directory*> code would merge and re-merge the same section after a match was found, possibly causing problems with some modules. [dean gaudet] 1.2.2 [not released] 

*) last official synchronization of mod_rewrite with author version (because mod_rewrite is now directly developed by the author at the apache *group*): o added diff between mod_rewrite 3.0.6+ and 3.0.9 minus win32/nt stuff, but plus copyright removement. in detail: - workaround for detecting infinite rewriting loops - fixed setting of env vars when "-" is used as subst string - fixed forced response code on *redirect*s (pr#777) - fixed cases where r->args is "" - kludge to disable locking on pipes under braindead sunos - fix for rewritelog in cases where remote hostname is unknown - fixed totally damaged request_rec walk-back loop o remove static from local data and add static to global ones. o replaced ugly proxy finding stuff by simple find_linked_module("mod_proxy") call. o added missing negation char on rewritelog() o fixed a few comment typos [ralf s. engelschall] 1.2.2 [not released] 

*) *anonymous*_logemail was logging on each subrequest. [dean gaudet] pr#421, pr#868 1.2.2 [not released] 

*) "force-response-1.0" now only applies to requests which are http/1.0 to begin with.  "no*keepalive*" now works for http/1.1 clients.  added "downgrade-1.0" which causes apache to pretend it received a 1.0. additionally mod_browser now triggers during translate_name to workaround a deficiency in the header_parse phase. [dean gaudet] pr#875 1.2.2 [not released] 

*) properly treat *<files*> container like other containers in mod_info. [marc slemko] pr#848 1.2.2 [not released] 

*) security: *headername* and *readmename* were settable in .htaccess and could contain "../" allowing a local user to "publish" any file on the system.  no slashes are allowed now.  [dean gaudet] 1.2.1 

*) security: it was possible to violate the symlink *options* using mod_dir (headers, readmes, titles), mod_negotiation (type maps), or mod_cern_meta (meta files).  [dean gaudet] 1.2.1 

*) *config*: if a symlink pointed to a directory then it would be disallowed if it contained a .htaccess disallowing symlinks.  this is contrary to the rule that symlink permissions are tested with the symlink *options* of the parent directory.  [dean gaudet] pr#353 1.2.1 

*) *config*: the lockfile directive can be used to place the serializing lockfile in any location.  it previously defaulted to /usr/tmp/htlock. [somehow it took four of us: randy terbush, jim jagielski, dean gaudet, marc slemko] 1.2.1 

*) request processing now retains state of whether or not the request body has been read, so that internal *redirect*s and subrequests will not try to read it twice (and block). [roy fielding] 1.2.1 

*) attempt to work around problems with third party libraries that do not handle high numbered de*script*ors (*example*s include bind, and solaris libc).  on all systems apache attempts to keep all permanent de*script*ors above 15 (called the low slack line).  solaris users can also benefit from adding -dhigh_slack_line=256 to extra_cflags which keeps all non-file * de*script*ors above 255.  on all systems this should make supporting large numbers of vhosts with many open log files more feasible.  if this causes trouble please report it, you can disable this workaround by adding -dno_slack to extra_cflags. [dean gaudet] various prs 1.2.1 

*) related to the last entry, network sockets are now opened before log files are opened.  the only known case where this can cause problems is under solaris with many virtualhosts and many *listen* directives.  but using -dhigh_slack_line=256 described above will work around this problem.  [dean gaudet] 1.2.1 

*) update mod_rewrite from 3.0.5 to 3.0.6.  new ruleflag qsa=query_string_append.  also fixed a nasty bug in per-dir context: when a url http://... was used in conjunction with a special *redirect* flag, e.g. r=permanent, the permanent status was lost. [ronald tschalaer <ronald.tschalaer psi.ch>, ralf s. engelschall] 1.2.1 

*) proxy needs to use hard_*timeout* instead of soft_*timeout* when it is reading from one buffer and writing to another, at least until it has a custom *timeout* handler.  [roy fielding and petr lampa] 1.2b11 

*) fixed problem on irix with servers hanging in *identitycheck*, apparently due to a mismatch between sig*action* and setjmp. [roy fielding] pr#502 1.2b11 

*) log correct status code if we *timeout* before receiving a request (408) or if we received a request-line that was too long to process (414). [ed korthof and roy fielding] pr#601 1.2b11 

*) virtual hosts with the same *servername*, but on different ports, were not being selected properly.  [ed korthof] 1.2b11 

*) the os/2 handling of process *group* was broken by a porting patch for mpe, so restored prior code for os/2.  [roy fielding and garey smiley] 1.2b11 

*) if the lookup for a *directoryindex* name with content negotiation has found matching variants, but none are acceptable, return the negotiation result if there are no more *directoryindex* names to lookup. [petr lampa and roy fielding] 1.2b11 

*) if a soft_*timeout* occurs after *keepalive* is set, then the main child loop would try to read another request even though the connection has been aborted.  [roy fielding] 1.2b11 

*) *config*ure changes: allow for whitespace at the start of a module declaration. also, be more understanding about the cc=/optim= format in *config*uration. finally, fix compiler flags if using hp-ux's cc compiler. [jim jagielski] 1.2b11 

*) subrequests and internal *redirect*s now inherit the_request from the original request-line. [roy fielding] 1.2b11 

*) test for error conditions before creating output header fields, since we don't want the error message to include those fields.  likewise, reset the content_language(s) and content_encoding of the response before generating or *redirect*ing to an error message, since the new message will have its own content-* definitions. [dean gaudet] 1.2b11 

*) fixed a couple places where a check for the default content-type was not properly checking both the value *config*ured by the *defaulttype* directive and the default_type symbol in httpd.h.  changed the value of default_type to match the documented default (text/plain). [dean gaudet] pr#506 1.2b11 

*) properly initialize the flock structures used by the *mutex* locking around accept() when use_fcntl_serialized_accept is defined. [marc slemko] 1.2b11 

*) the method for determining path_info has been restored to the pre-1.2b (and ncsa httpd) definition wherein it was the extra path info beyond the cgi *script* filename.  the environment variable filepath_info has been removed, and instead we supply the original request_uri to any *script* that wants to be apache-specific and needs the real uri path. this solves a problem with existing *script*s that use extra path info in the *script**alias* directive to pass *options* to the cgi *script*. [roy fielding] 1.2b11 

*) the _default_ change in 1.2b10 will change the behaviour on *config*s that use multiple *listen* statements for *listen*ing on multiple ports. but that change is necessary to make _default_ consistent with other forms of *<virtualhost*>.  it requires such *config*s to be modified to use *<virtualhost* _default_:*>.  the documentation has been updated.  [dean gaudet] pr#530 1.2b11 

*) if an *errordocument* cgi *script* is used to respond to an error generated by another cgi *script* which has already read the message body of the request, the server would block trying to read the message body again.  [rob hartill] 1.2b11 

*) allow httpd_root, server_*config*_file, default_path, and shell_path to be *config*ured via -d in *config*uration.  [dean gaudet] pr#449 1.2b10 

*) *<virtualhost* _default_:portnum> didn't work properly.  [dean gaudet] 1.2b10 

*) in mod_proxy.c, check return values for proxy_host2addr() when reading *config*, in case the hostent struct returned is trash. [chuck murcko] pr #491 1.2b10 

*) fixed the fix in 1.2b9 for parsing url query info into args for cgi *script*s.  [dean gaudet, roy fielding, marc slemko] 1.2b9  [never announced] 

*) fix problem with *script*s not receiving a sigpipe when client drops the connection (e.g., when user presses stop).  apache will now stop trying to send a message body immediately after an error from write. [roy fielding and nathan kurz] pr#335 1.2b9  [never announced] 

*) rearrange *config*uration.tmpl so that mod_rewrite has higher priority than mod_*alias*, and mod_*alias* has higher priority than mod_proxy; rearranged other modules to enhance understanding of their purpose and relative order (and maybe even reduce some overhead). [roy fielding and sameer parekh] 1.2b9  [never announced] 

*) allow *suexec* to access files relative to current directory but not above.  (excluding leading / or any .. directory.)  [ken coar] pr#269, 319, 395 1.2b9  [never announced] 

*) fix *suexec* segfault when *group* doesn't exist. [gregory neil shapiro] pr#367, 368, 354, 453 1.2b9  [never announced] 

*) fix the above fix: if *suexec* is enabled, avoid destroying r->url while obtaining the /~user and save the username in a separate data area so that it won't be overwritten by the call to getgrgid(), and fix some misuse of the pool string allocation functions.  also fixes a general problem with parsing url query info into args for cgi *script*s. [roy fielding] pr#339, 367, 354, 453 1.2b9  [never announced] 

*) fix irix warning about bzero *undefine*d. [marc slemko] 1.2b9  [never announced] 

*) fix problem with *<directory* proxy:...>. [martin kraemer] pr#271 1.2b9  [never announced] 

*) if a soft *timeout* (or lingerout) occurs while trying to flush a buffer or write inside buff.c or fread'ing from a cgi's output, then the *timeout* would be ignored. [roy fielding] pr#373 1.2b9  [never announced] 

*) fixed sigsegv problem when a *directoryindex* file is also the source of an external *redirect*ion.  [roy fielding and paul sutton] 1.2b9  [never announced] 

*) *config*ure would create a broken makefile if the *config*uration file contained a commented-out rule.  [roy fielding] 1.2b9  [never announced] 

*) promote per_dir_*config* and subprocess_env from the subrequest to the main request in mod_negotiation.  in particular this fixes a bug where *<files*> sections wouldn't properly apply to negotiated content. [dean gaudet] 1.2b9  [never announced] 

*) fix a potential deadlock in mod_cgi *script*_err handling. [ralf s. engelschall] 1.2b9  [never announced] 

*) updated mod_rewrite to 3.0.4: fixes http *redirect*s from within .htaccess files because the *rewritebase* was not replaced correctly. updated mod_rewrite to 3.0.5: fixes problem with rewriting inside *<directory*> sections missing a trailing /.  [ralf s. engelschall] 1.2b9  [never announced] 

*) *redirect* did not preserve ?query_strings when present in the client's request.  [dean gaudet] 1.2b9  [never announced] 

*) *config*ure was finding non-modules on extra_libs. [frank cringle] pr#380 1.2b9  [never announced] 

*) add mod_*example* (illustration of api techniques).  [ken coar] 1.2b9  [never announced] 

*) hard_server_limit can be defined in the *config*uration file now. [dean gaudet] 1.2b8 

*) *suexec*.c doesn't close the log file, allowing cgis to continue writing to it.  [marc slemko] 1.2b8 

*) the addition of *<location*> and <file> directives made the sub_req_lookup_simple() function bogus, so we now handle the special cases directly.  [dean gaudet] 1.2b8 

*) improved lingering_close by adding a special *timeout*, removing the spurious log messages, removing the nonblocking settings (they are not needed with the better *timeout*), and adding commentary about the no_lingclose and use_so_linger issues.  no_lingclose is now the default for sunos4, unixware, next, and irix.  [roy fielding] 1.2b8 

*) fixed the handling of module and *script*-added header fields. improved the interface for sending header fields and reduced the duplication of code between sending okay responses and errors. we now always send both headers_out and err_headers_out, and ensure that the server-reserved fields are not being overridden, while not overriding those that are not reserved.  [roy fielding] 1.2b8 

*) fixed the determination of whether or not we should make the connection persistent for all of the cases where some other part of the server has already indicated that we should not.  also improved the ordering of the test so that chunked encoding will be set whenever it is desired instead of only when *keepalive* is enabled. added persistent connection capability for most error responses (those that do not indicate a bad input stream) when accessed by an http/1.1 client. [roy fielding] 1.2b8 

*) added missing *timeout*s for sending header fields, error responses, and the last chunk of chunked encoding, each of which could have resulted in a process being stuck in write forever.  using soft_*timeout* requires that the sender check for an aborted connection rather than continuing after an eintr.  *timeout*s that used to be initiated before send_http_header (and never killed) are now initiated only within or around the routines that actually do the sending, and not allowed to propagate above the caller.  [roy fielding] 1.2b8 

*) per_dir_defaults weren't set correctly until directory_walk for name-based vhosts.  this fixes an obscure bug with the wrong *config* info being used for vhosts that share the same ip as the server. [dean gaudet] 1.2b8 

*) generate makefile dependency for *config*uration based on the actual name given when running the *config*ure process.  [dean gaudet] 1.2b8 

*) try to continue gracefully by disabling the vhost if a dns lookup fails while parsing the *config*uration file.  [dean gaudet] 1.2b8 

*) reduced *identitycheck* *timeout* to 30 seconds, as per rfc 1413 minimum. [ken coar] 1.2b8 

*) fixed problem with *errordocument* not working for virtual hosts due to one of the performance changes in 1.2b7. [dean gaudet] 1.2b8 

*) updated mod_rewrite to version 3.0.2, which: fixes compile error on aix; improves the *redirect*ion stuff to enable the users to generally *redirect* to http, https, gopher and ftp; added time variable for *rewritecond* which expands to yyyymmddhhmmss strings and added the special patterns >string, <string and =string to *rewritecond*, which can be used in conjunction with %{time} or other variables to create time-dependent rewriting rules. [ralf s. engelschall] 1.2b8 

*) bpushfd() no longer notes cleanups for the file de*script*ors it is handed. module authors may need to adjust their code for proper cleanup to take place (that is, call note_cleanups_for_fd()). this change fixes problems with file de*script*ors being erroneously closed when the proxy module was in use. [ben laurie] 1.2b8 

*) fix bug in *suexec* reintroduced by changes in 1.2b7 which allows init*group*s() to hose the *group* information needed for later comparisons. [randy terbush] 1.2b8 

*) clear memory allocated for *listen*ers. [randy terbush] 1.2b8 

*) improved handling of ip address as a virtualhost address and introduced "_default_" as a synonym for the default vhost *config*. [dean gaudet] pr #212 1.2b7 

*) mod_negotiation fixes [petr lampa] pr#157, pr#158, pr#159 - replace *protocol* response numbers with symbols - save variant-list into main request notes - free allocated memory from subrequests - merge notes, headers_out and err_headers_out 1.2b7 

*) more proxy ftp bug fixes: - changed send_dir() to remove user/passwd from displayed url. - changed login error messages to be more de*script*ive. - remove setting of so_debug socket option - make ftp_getrc() more lenient about multiline responses, specifically, 230 responses which don't have continuation 230- on each line). these seem to be all nt ftp servers, and while perhaps questionable, they appear to be legal by rfc 959. - add missing kill_*timeout*() after transfer to user completes. [chuck murcko] 1.2b7 

*) reduced the default *timeout* from 1200 seconds to 300, and the one in the sample *config*file from 400 to 300.  [marc slemko] 1.2b7 

*) fixed problem with mod_cgi-generated internal *redirect*s trying to read the request message-body twice. [archie cobbs and roy fielding] 1.2b7 

*) reduced *timeout* on lingering close, removed possibility of a blocked read causing the child to hang, and stopped logging of errors if the socket is not connected (reset by client).  [roy fielding] 1.2b7 

*) rearranged main child loop to remove duplication of code in select/accept and keep-alive requests, fixed several bugs regarding checking scoreboard_image for exit indication and failure to account for all success conditions and trap all error conditions, prevented multiple flushes before closing the socket; close the entire socket buffer instead of just one de*script*or, prevent logging of eproto and econnaborted on platforms where supported, and generally improved readability.  [roy fielding] 1.2b7 

*) several fixes for *suexec* wrapper. [randy terbush] - make wrapper work for files on nfs filesystem. - fix portability problem of maxpathlen. - fix array overrun problem in clean_env(). - fix allocation of path environment variable 1.2b7 

*) removed extraneous blank line is de*script*ion of mod_status chars. [kurt kohler] 1.2b7 

*) fixed core dump when *documentroot* is a cgi. [ben laurie, reported by <geddis tesserae.com>] 1.2b7 

*) fixed potential file de*script*or leak in mod_asis; updated it and http_core to use pfopen/pfclose instead of fopen/fclose. [randy terbush and roy fielding] 1.2b7 

*) return a 302 response code to the client when sending a *redirect* due to a missing trailing '/' on a directory instead of a 301; now it is cacheable. [markus gyger] 1.2b7 

*) fix condition where, if a bad directive occurs in .htaccess, and sub_request() goes first to this directory, then log_reason() will sigsegv because it doesn't have initialized r->per_dir_*config*. [pr#162 from petr lampa, fix by marc slemko and dean gaudet] 1.2b7 

*) remove free() from clean_env() in *suexec* wrapper. this was nuking the clean environment on some systems. 1.2b7 

*) improved buffered output to the client by delaying the flush decision until the buff code is actually about to read the next request. this fixes a problem introduced in 1.2b5 with clients that send an extra crlf after a post request. also improved chunked output performance by combining writes using writev() and removing as many bflush() calls as possible.  note: platforms without writev() must add -dno_writev to the compiler cflags, either in *config*uration or *config*ure, unless we have already done so.  [dean gaudet] 1.2b7 

*) fixed http_*protocol* to correctly output all http/1.1 headers, including for the special case of a 304 response.  [paul sutton] 1.2b7 

*) change *keepalive* semantics (on|off instead of a number), add max*keepalive*requests directive. [alexei kosut] 1.2b5 

*) don't call can_exec() if *suexec*_enabled. calling this requires *script*s executed by the *suexec* wrapper to be world executable, which defeats one of the advantages of running the wrapper. [randy terbush] 1.2b5 

*) mod_info assumed that the *config* files were relative to *serverroot*. [ken the rodent] 1.2b5 

*) cgi *script*s called as an error document resulting from failed cgi execution would hang waiting for post'ed data. [rob hartill] 1.2b5 

*) several security enhancements to *suexec* wrapper. it is _highly_ recommended that previously installed versions of the wrapper be replaced with this version.  [randy terbush, jason dour] - ~user execution now properly restricted to ~user's home directory and below. - execution restricted to uid/gid > 100 - restrict passed environment to known variables - call setgid() before init*group*s() (portability fix) - remove use of *setenv*() (portability fix) 1.2b5 

*) fix incorrect comparison which could allow number of children = maxclients + 1 if less than hard_server_limit. also fix potential problem if *startservers* > hard_server_limit. [ed korthof] 1.2b5 

*) replace instances of inet_ntoa() with inet_addr() for *proxyblock*. it's more portable. [martin kraemer] 1.2b5 

*) add *proxyblock* directive w/ip address caching. add ip address caching to nocache directive as well. *proxyblock* works with all handlers; nocache now also works with ftp for *anonymous* logins. still more code cleanup. [chuck murcko] 1.2b5 

*) *suexec* wrapper was freeing memory that had not been malloc'ed. 1.2b5 

*) correctly allow access and auth directives in *<files*> sections in server *config* files. [alexei kosut] 1.2b5 

*) fix bug with *serverpath* that could cause certain files to be not found by the server. [alexei kosut] 1.2b5 

*) fix handling of *errordocument* so that it doesn't remove a trailing double-quote from text and so that it properly checks for unsupported status codes using the new index_of_response interface. [roy fielding] 1.2b5 

*) multiple fixes to the lingering_close code in order to avoid being interrupted by a stray *timeout*, to avoid lingering on a connection that has already been aborted or never really existed, to ensure that we stop lingering as soon as any error condition is received, and to prevent being stuck indefinitely if the read blocks.  also improves reporting of error conditions.  [marc slemko and roy fielding] 1.2b5 

*) fixed initialization of parameter structure for sig*action*. [<mgyger itr.ch>, adrian filipi-martin] 1.2b5 

*) fixed bug in bcwrite regarding failure to account for partial writes. avoided calling bflush() when the client is pipelining requests. removed unnecessary flushes from http_*protocol*. [dean gaudet] 1.2b5 

*) added de*script*ion of "." mode in server-status [jim jagielski] 1.2b4 

*) fix possible race condition in accept_*mutex*_init() that could leave a small security hole open allowing files to be overwritten in cases where the server uid has write permissions. [marc slemko] 1.2b4 

*) fix awk compatibilty problem in *config*ure. [jim jagielski] 1.2b4 

*) fix portablity problem in util_*script* where arg_max may not be defined for some systems. 1.2b4 

*) os/2 changes to support an mmap style scoreboard file and unix style magic #! token for better *script* portability. [garey smiley] 1.2b4 

*) fix bug in *suexec* wrapper introduced in b3 that would cause failed execution for ~*userdir* cgi. [jason dour] 1.2b4 

*) fix init*group*s() business in *suexec* wrapper. [jason dour] 1.2b4 

*) fix month off by one in *suexec* wrapper logging. 1.2b3: 

*) add changes to improve the error message given for invalid *servername* parameters. [dirk vangulik] 1.2b3: 

*) remove requirement for resource*config*/access*config* if not using the three *config* file layout. [randy terbush] 1.2b3: 

*) changes to *suexec* wrapper to fix the following problems: 1.  symlinked homedirs will kill ~*userdir*s. 2.  init*group*s() on linux 2.0.x clobbers gr->grid. 3.  cgi command lines paramters problems 4.  pw-pwdir for "docroot check" still the httpd user's pw record. [randy terbush, jason dour] 1.2b3: 

*) change create_argv() to accept variable arguments. this fixes a problem where arguments were not getting passed to the cgi via argv[] when the *suexec* wrapper was active. [randy terbush, jake buchholz] 1.2b3: 

*) collapse multiple slashes in path urls to properly apply handlers defined by *<location*>. [alexei kosut] 1.2b3: 

*) define a sane set of default_user and default_*group* values for aix. 1.2b3: 

*) reset *timeout* while reading via get_client_block() in mod_cgi.c fixes problem with timed out transfers of large files. [rasmus lerdorf] 1.2b3: 

*) add the ability to pass different makefile.tmpl files to *config*ure using the -make flag. [rob hartill] 1.2b3: 

*) fix coredump triggered when sending a sighup to the server caused by an assertion failure, in turn caused by an uninitialised field in a *listen*_rec. [ben laurie] 1.2b3: 

*) defined rlim_t and wanthsregex=yes and fixed waitpid() *substitute* for next. [jim jagielski] 1.2b3: 

*) removed recent modification to promote the status code on internal *redirect*s, since the correct fix was to change the default log format in mod_log_*config* so that it outputs the original status. [rob hartill] 1.2b2: 

*) update set_signals() to use sig*action*() for setting handlers. this appears to fix a re-entrant problem in the seg_fault() bus_error() handlers. [randy terbush] 1.2b2: 

*) proxy_http.c bugfixes:  [chuck murcko] 1) fixes possible null pointer reference w/nocache 2) fixes nocache behavior when using *proxyremote* (*proxyremote* host would cache nothing if it was in the local domain, and the local domain was in the nocache list) 3) adds host: header when not available 4) some code cleanup and clarification 1.2b2: 

*) mod_include.c bugfixes: 1) fixed an ommission that caused include variables to not be parsed in *config* errmsg directives [howard fear] 2) remove have_posix_regex cruft [alexei kosut] 3) patch to fix compiler warnings [<perrot lal.in2p3.fr>] 4) allow backslash-escaping to all quoted text [ben yoshino <ben wiliki.eng.hawaii.edu>] 5) pass variable to command line if not set in xssi's env [howard fear] 1.2b2: 

*) closed file-globbing hole in test-cgi *script*. [brian behlendorf] 1.2b2: 

*) fixed problem in set_[user|*group*] that prevented cgi execution for non-virtualhosts when *suexec* was enabled. [randy terbush] 1.2b2: 

*) changed default *group* to "no*group*" instead of "nobody" [randy terbush] 1.2b2: 

*) added comment to explain (r->chunked = 1) side-effect in http_*protocol*.c [roy fielding] 1.2b2: 

*) updated *config*ure for ... os/2          (def_wanthsregex=yes, other code changes) *-dg-dgux*    (bad pattern match) qnx           (def_wanthsregex=yes) *-sunos4*     (def_wanthsregex=yes, -dusebcopy) *-ultrix      (new) *-unixware211 (new) and added some user diagnostic info.  [ben laurie] 1.2b2: 

*) fixed bug where *redirect* in .htaccess files would cause memory leak. [nathan neulinger] 1.1.1 

*) multiviews now works correctly with *addhandler* [alexei kosut] 1.1.1 

*) fix misspelling of "*anonymous*_authorative" directive in mod_auth_anon. 1.1.0 

*) make virtual hosts default to main server *keepalive* parameters. [alexei kosut, ben laurie] 1.1.0 

*) mod_env now turned on by default in *config*uration.tmpl. 1.1.0 

*) previously broken multi-method *<limit*> parsing fixed. [robert thau] 1.1b4 

*) virtualhosts based on host: headers no longer conflict with the *listen* directive. 1.1b4 

*) post now allowed to directory index cgi *script*s. 1.1b4 

*) *action*s now work with files of the default type. 1.1b4 

*) bugs which were fixed: a) more mod_proxy bugs b) early termination of inetd requests c) compile warnings on several systems d) problems when *script*s stop reading output early 1.1b3 

*) connect method for proxy module, which means tunneling ssl should work. (no crypto needed)  also a nocache *config* directive. 1.1b3 

*) "*serverpath*" directive added - allows for graceful transition for host:-header-based virtual hosts. 1.1b3 

*) *anonymous* authentication module improvements. 1.1b3 

*) bugs which were fixed: a) numerous mod_proxy bugs b) cgi early-termination bug [ben laurie] c) *keepalive*s not working with virtual hosts d) refererignore problems e) closing fd's twice in mod_include (causing core dumps on linux and elsewhere). 1.1b2 

*) internal *redirect*s which occur in mod_dir.c now preserve the query portion of a request (the bit after the question mark). [adam sussman] 1.0.3 

*) escape active characters '<', '>' and '&' in html output in directory listings, error messages and *redirect*ion links. [david robinson] 1.0.3 

*) reset *timeout* timer after each successful fwrite() to the network. this patch adds a reset_*timeout*() procedure that is called by send_fd() to reset the *timeout* ever time data is written to the net. [nathan schrenk] 1.0.3 

*) *timeout*() signal handler now checks for sigpipe and reports lost connections in a more user friendly way. [rob hartill] 1.0.3 

*) location of the "scoreboard" file which used to live in /tmp is now *config*urable (for oses that can't use mmap) via *scoreboardfile* which works similar to *pidfile* (in httpd.conf) [rob hartill] 1.0.3 

*) output warning when *minspareservers* is set to <= 0 and change it to 1 [rob hartill] 1.0.3 

*) past changes to http_*config*.c to only use the setrlimit function on systems defining rlimit_nofile broke the feature on sunos4. now defines have_resource for sunos and prototypes the needed functions. 1.0.2 

*) merge multiple headers from cgi *script*s instead of taking last one. [david robinson] 1.0.2 

*) silence mod_log_referer and mod_log_agent if not *config*ured [randy terbush] 1.0.1 

*) the replacement for init*group*s() did not call {set,end}grent(). this had two implications: if anything else used getgrent(), then init*group*s() would fail, and it was consuming a file de*script*or. [ben laurie] 1.0.1 

*) .ht*group* files can have more than one line giving members for a given *group* (each must have the *group* name in front), for ncsa back-compatibility [robert thau] 0.8.16                                       05 nov 1995 

*) *addtype*, *addencoding*, and *addlanguage* directives take multiple extensions on a single command line [david robinson] 0.8.16                                       05 nov 1995 

*) *userdir* can be disabled for a given virtual host by saying "*userdir* disabled" in the *<virtualhost*> section --- it was a bug that this didn't work.  [david robinson] 0.8.16                                       05 nov 1995 

*) httpd does a perror() before exiting if it can't log its pid to the *pidfile*, to make diagnosing the error a bit easier. [david robinson] 0.8.16                                       05 nov 1995 

*) fixed bug involving handling uris with escaped %-characters in *redirect*s [david robinson] 0.8.15                                       14 oct 1995 

*) eliminated core dumps with improperly formatted dbm *group* files [mark cox] 0.8.15                                       14 oct 1995 

*) correctly handles internal *redirect*s to files with names containing '%' [david robinson] 0.8.15                                       14 oct 1995 

*) somewhat better fix for the old "*alias* /foo/ /bar/" business [david robinson] 0.8.15                                       14 oct 1995 

*) don't repeatedly open the *errorlog* if a bunch of *<virtualhost*> entries all name the same one. [david robinson] 0.8.15                                       14 oct 1995 

*) sample *config* files have extra note for sco users [ben laurie] 0.8.15                                       14 oct 1995 

*) *config*uration has note for hp-ux users [rob hartill] 0.8.15                                       14 oct 1995 

*) addde*script*ion works (better) [ben laurie] 0.8.14                                       19 sep 1995 

*) leaves an intelligible error diagnostic when it can't set *group* privileges on standalone startup [andrew wilson] 0.8.14                                       19 sep 1995 

*) make *indexignore* *work* (ooops) [jarkko torppa] 0.8.13                                       07 sep 1995 

*) properly default *servername* for virtual servers [robert thau] 0.8.13                                       07 sep 1995 

*) on self-identified bsd systems (we don't try to guess any more), allocate a few extra file de*script*ors per virtual host with setrlimit, if we can, to avoid running out. [randy terbush] 0.8.13                                       07 sep 1995 

*) doesn't pause three seconds after including a cgi *script* which is too slow to die off (this is done by not even trying to kill off subprocesses, including the sigterm/pause/sigkill routine, until after the entire document has been processed).  [robert thau] 0.8.12                                       31 aug 1995 

*) doesn't do ssi if *options* includes is off.  (ooops).  [david robinson] 0.8.12                                       31 aug 1995 

*) *options* includesnoexec allows inclusion of at least text/* [roy fielding] 0.8.12                                       31 aug 1995 

*) allows .htaccess files to override *<directory*> sections naming the same directory [david robinson] 0.8.12                                       31 aug 1995 

*) removed an efficiency hack in sub_req_lookup_uri which was causing certain extremely marginal cases (e.g., *script**alias* of a *particular* index.html file) to fail.  [david robinson] 0.8.12                                       31 aug 1995 

*) *config*uration *script* accepts "module" lines with trailing whitespace. [robert thau] 0.8.12                                       31 aug 1995 

*) wildcard *<directory*> specifications work.  [robert thau] 0.8.11                                       24 aug 1995 

*) doesn't reset *directoryindex* to 'index.html' when other directory *options* are set in a .htaccess file.  [robert thau] 0.8.11                                       24 aug 1995 

*) corrected several directives in sample srm.conf --- includes corrections to directory indexing icon-related directives (using unknown.gif rather than unknown.xbm as the *defaulticon*, doing icons for encodings right, and turning on *addencoding* by default). [roy fielding] 0.8.11                                       24 aug 1995 

*) corrected de*script*ions of args to *addicon* and *addalt* in command table [james cloos] 0.8.11                                       24 aug 1995 

*) fixed *script**alias*/*alias* inter*action* by moving *script**alias* handling to mod_*alias*.c, merging it almost completely with handling of *alias*, and adding a 'notes' field to the request_rec which allows the cgi module to discover whether the *alias* module has put this request through *script**alias* (which it needs to know for back-compatibility, as the old ncsa code did not check *options* execcgi in *script**alias* directories). [robert thau] 0.8.10                                       18 aug 1995 

*) *allowoverride* applies to the named directory, and not just subdirectories.  [david robinson] 0.8.10                                       18 aug 1995 

*) <!--exec cgi="/some/uri/here"--> always treats the item named by the uri as a cgi *script*, even if it would have been treated as something else if requested directly, for ncsa back-compatibility.  (note that this means that people who know the name of the *script* can see the code just by asking for it).  [robert thau] 0.8.9                                        12 aug 1995 

*) new version of dbmmanage *script* included in support directory as dbmmanage.new. 0.8.9                                        12 aug 1995 

*) *addicon* and *addalt* commands work properly [rob hartill] 0.8.9                                        12 aug 1995 

*) really honor *cachenegotiateddocs* [florent guillaume] 0.8.9                                        12 aug 1995 

*) give *redirect* priority over *alias*, for ncsa bug compatibility [david robinson] 0.8.9                                        12 aug 1995 

*) if dbm auth is improperly *config*ured, report a server error and don't dump core. 0.8.9                                        12 aug 1995 

*) more improvements to default *config*uration for a/ux [jim jagielski] 0.8.9                                        12 aug 1995 

*) sunos library prototypes now never included unless explicitly requested in the *config*uration (via -dsunos_lib_prototypes); people using gnu libc on sunos are screwed by prototypes for the standard library. (those who wish to compile clean with gcc -wall on a standard sunos setup need the prototypes, and may obtain them using -dsunos_lib_prototypes.  those wishing to use -wall on a system with nonstandard libraries are presumably competent to make their own arrangements). 0.8.8                                        08 aug 1995 

*) strips trailing '/' characters off both args to the *alias* command, to make '*alias* /foo/ /bar/' work. 0.8.7                                        03 aug 1995 

*) don't hang when restarting with a child from '*transferlog* "|..."' running [reported by david robinson] 0.8.7                                        03 aug 1995 

*) added some of the more recent significant changes (*addlanguage* stuff, experimental *logformat* support) to changes file in distribution root directory 0.8.6                                        02 aug 1995 

*) added last-minute *config*urable log experiment, as optional module 0.8.5                                        01 aug 1995 

*) correctly set r->bytes_sent for http/0.9 requests, so they get logged properly.  (one-line fix to http_*protocol*.c). 0.8.5                                        01 aug 1995 

*) *identitycheck* bugfix [chuck murcko]. 0.8.5                                        01 aug 1995 

*) corrected cgi-src/makefile entry for new imagemap *script*.  [alexei kosut] 0.8.5                                        01 aug 1995 

*) more sample *config* file corrections; add extension to *addtype* for *.asis, move *addtype* generic de*script*ion to its proper place, and fix miscellaneous typos. [ alexei kosut ] 0.8.5                                        01 aug 1995 

*) changes to server-pool management parms --- renamed current *startservers* to *minspareservers*, created separate *startservers* parameter which means what it says, and renamed maxservers to *maxspareservers* (though the old name still works, for ncsa 1.4 back-compatibility).  the old names were generally regarded as too confusing.  also altered "docs" in sample *config* files. 0.8.4 

*) more improvements to default *config* files --- sample directives (commented out) for *xbithack*, bindaddress, *cachenegotiateddocs*, virtualhost; decent set of *addlanguage* defaults, *addtype*s for send-as-is and imagemap magic types, and improvements to samples for *directoryindex* [alexei kosut] 0.8.4 

*) yet more improvements to default *config* files --- changes to alexei's sample *addlanguage* directives, and sample *languagepriority* [ florent guillaume ] 0.8.4 

*) set *config* file locations properly if not set in httpd.conf [ david robinson ] 0.8.4 

*) don't escape uris in internal *redirect*s multiple times; don't do that when translating path_info to path_translated either. [ david robinson ] 0.8.4 

*) upgraded imagemap *script* in cgi-bin to 1.8 version from more recent ncsa distributions. 0.8.3 

*) bug fix to previous bug fix --- if .htaccess file and *<directory*> exist for the same directory, use both and don't segfault.  [reported by david robinson] 0.8.3 

*) lightly edited sample *config* files to refer people to our documentation instead of ncsa's, and to list rob mccool as *original* author (also deleted his old, and no doubt non-functional email address).  would be nice to have *example*s of new features... 0.8.2                                        19 jul 1995 

*) don't say "access forbidden" when a cgi *script* is not found.  [mark cox] 0.8.2                                        19 jul 1995 

*) imagemap module is enabled in default *config*uration 0.8.2                                        19 jul 1995 

*) mark cox's mod_cookies added to the distribution as an optional module (commented out in the default *config*uration, and noted as an experiment, along with mod_dld). [mark cox] 0.8.2                                        19 jul 1995 

*) new *config* *script*.  see install for info.  [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) scoreboard mechanism for regulating the number of extant server processes.  maxservers and *startservers* defaults are the same as for ncsa, but the meanings are slightly different.  (actually, i should probably lower the maxservers default to 10). before asking for a new connection, each server process checks the number of other servers which are also waiting for a connection.  if there are more than maxservers, it quietly dies off.  conversely, every second, the root, or caretaker, process looks to see how many servers are waiting for a new connection; if there are fewer than *startservers*, it starts a new one.  this does not depend on the number of server processes already extant. the accounting is arranged through a "scoreboard" file, named /tmp/htstatus.*, on which each process has an independent file de*script*or (they need to seek without interference). the end effect is that maxservers is the maximum number of servers on an *inactive* server machine, but more will be forked off to handle unusually heavy loads (or unusually slow clients); these will die off when they are no longer needed --- without reverting to the overhead of full forking operation.  there is a hard maximum of 150 server processes compiled in, largely to avoid forking out of control and dragging the machine down. (this is arguably too high). in my server endurance tests, this mechanism did not appear to impose any significant overhead, even after i forced it to put the scoreboard file on a normal filesystem (which might have more overhead than tmpfs).  [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) set http_foo variables for ssi <!--#exec cmd-->s, not just cgi *script*s. [cliff skolnick] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) read .htaccess files even in directory with *<directory*> section. (former incompatibility noted on mailing list, now fixed). [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) don't produce double error reports for some very obscure cases mainly involving auth *config*uration (the "all modules decline to handle" case which is a sure sign of a server bug in most cases, but also happens when authentication is badly mis*config*ured). [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) fixed auth_name-related typos in http_core.c [brian behlendorf] also, fixed auth typo in http_*protocol*.c unmasked by this fix. 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) reordered modules in modules.c so that *redirect* takes priority over *script**alias*, for ncsa bug-compatibility [rob hartill] --- believe it or not, he has an actual site with a *script**alias* and a *redirect* declared for the *exact same directory*.  even *my* compatibility fetish wouldn't motivate me to fix this if the fix required any effort, but it doesn't, so what the hey. 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) two styles of *timeout* --- hard and soft.  soft_*timeout*()s just put the connection to the client in an "aborted" state, but otherwise allow whatever handlers are running to clean up.  hard_*timeout*()s abort the request in progress completely; anything not tied to some resource pool cleanup will leak.  they're still around because i haven't yet come up with a more elegant way of handling *timeout*s when talking to something that isn't the client.  the default_handler and the dir_handler now use soft *timeout*s, largely so i can test the feature.  [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) *transferlog* "| my_postprocessor ..." seems to be there.  note that the case of log handlers dying prematurely is probably handled very gracelessly at this point, and if the logger stops reading input, the server will hang.  (it is known to correctly restart the logging process on server restart; this is (should be!) going through the same sigterm/pause/sigkill routine used to ding an errant cgi *script*).  [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) *identitycheck* code is compiled in, but has not been tested.  (i don't know anyone who runs identd). [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) deleted the block_alarms() stuff from dbm_auth; no longer necessary, as *timeout*s are not in scope. [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) quoted-string args in *config* files now handled correctly (doesn't drop the last character). [robert thau; reported by randy terbush] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) another cliff bug --- "get /~user" now properly *redirect*s (the *userdir* code no longer sets up bogus path_info which fakes out the directory handler). [cliff skolnick] changes with shambhala 0.5.2                                     06 jul 1995 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) changes to http_main.c --- root server no longer plays silly games with sigchld, and so now detects and replaces dying children.  child processes just die on sigterm, without taking the whole process *group* with them.  potential problem --- if any child process refuses to die, we hang in restart. maxrequestsperchild may still not work, but it certainly works better than it did before this!  [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) mod_dir.c bug fixes: *readmename* and *headername* work (or work better, at least); over-long de*script*ion lines properly terminated. [mark cox] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) generalized cleanup interface in alloc.c --- any function can be registered with alloc.c as a cleanup for a resource pool; tracking of files and file de*script*ors has been reimplemented in terms of this interface, so i can give it some sort of a test. [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) more changes in alloc.c --- new cleanup_for_exec() function, which tracks down and closes all file de*script*ors which have been registered with the alloc.c machinery before the server exec()s a child process for cgi or <!--#exec-->.  cgi children now get started with exactly three file de*script*ors open.  hopefully, this cures the problem rob h. was having with overly persistent cgi connections. [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) mutual exclusion around the accept() in child_main() --- this is required on at least sgi, solaris and linux, and is #ifdef'ed in by default on those systems only (-dfcntl_serialized_accept). this uses fcntl(f_setlk,...) on the error log de*script*or because flock() on that de*script*or won't work on systems which have bsd flock() semantics, including (i think) linux 1.3 and solaris. this does work on sunos (when the server is idle, only one process in the pool is waiting on accept()); it *ought* to work on the other systems. [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) block_alarms() to avoid leaking the dbm* in dbm auth (this should be unnecessary if i go to the revised *timeout*-handling scheme). [robert thau] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) add wildcard content handlers for *xbithack*; default_hander now invoked with that mechanism (as a handler hanging off mod_core) [rst] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) *xbithack* supported as a wildcard content-handler, and *config*urable at run-time (not just at compile time, as in the "patchy server" releases) [rst] changes with shambhala 0.4.4                                     30 jun 1995 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) handle *addtype* x/y .z [rst, reported by cox] changes with shambhala 0.4.3 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) fixed very dumb bug in mod_*alias*; "*alias*" and "*redirect*" are not synonymous [rst, terbush] changes with shambhala 0.4.1                                     28 jun 1995 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) first-cut virtual host implementation; some refit in the *config* reading code, and log management, was necessary to support this [rst] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) significant code reorg within the server core to *group* related functions together [rst] 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) replace dying child processes. [rst] changes with shambhala 0.1                                       12 jun 1995 major rewrite of the pre-existing "patchy server" codebase, by robert thau (rst).  significant portions of the server code, such as *config*uration-file handling and http authentication support, were ripped out and rewritten from scratch.  code that was not completely rewritten was significantly altered. major changes with this release include: 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) introduction of the module api; in request handling, the central machinery just dispatches to various modules, which actually do most of the work.  *config*uration handling is similar --- modules declare their own commands, and the central machinery just dispatches to them. api features from shambhala/0.1 were substantially unchanged in apache 1.0 and 1.1.  (1.0 api features not yet present in this release, such as wildcard handlers and subpools, were added in subsequent shambhala releases, and were also generally rst's work). 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

*) this release included the following modules: mod_access      (access control --- allow and deny directives), mod_*alias*       (*alias* and *redirect* commands), mod_auth        (straight http authentication, based on flat-files) mod_auth_dbm    (same, with dbm files) mod_cgi         (cgi *script*s and, in this release, *script**alias*) mod_common_log  (clf access logs; later renamed mod_log_common) mod_dir         (directory indexing) mod_include     (server-side includes) mod_mime        (*addtype* directives) mod_negotiation (content negotiation) mod_*userdir*     (support for users' public_html directories) it also included a mod_ai_backcompat, which was a private hack for back-compatibility with rst's own ai-lab servers. all of these modules were substantially complete, and functional or nearly so (a few, which implemented features not in use at thau's site, required patches of a few lines). 0.8.0 (nee shambhala 0.6.2)                  16 jul 1995 

2078
redirect 110
options 102
script 256
config 644

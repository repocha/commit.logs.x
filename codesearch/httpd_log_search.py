import codesearch

REPO = '/home/tianyin/httpd-trunk/httpd'
CLOG = 'aaa.commit.log'
OUTDIR = 'httpd_commits'

LOG_STMT = ['ap_log_perror',
            'ap_log_error',
            'ap_log_rerror',
            'ap_log_cerror',
            'ap_log_cserror'
           ]

codesearch.select_commits('httpd', CLOG, REPO, LOGSTMT, OUTDIR)

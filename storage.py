from util import *

'''
# host list
    host['192.168.5.1'] = {
        'ip'        : '192.168.5.1',
        'ttl'       : [ 127, 63, 62 ],
        'subip'     : [ '10.32.0.1', '10.32.0.3' ],
        'ipid'      : [ 10, 12, 341, 2322],
        'target'    : [
            'c.csdnimg.cn' : [
                'ua'     : [ '', '', '' ],
                'cookie' : [ '', '', '' ],
            ],
        ],
}
'''

host_list = {}

def __host_get( ip ):
    if ip not in host_list:
        host_list[ip]={}
        host_list[ip]['ip']     = ip
        host_list[ip]['ttl']    = []
        host_list[ip]['subip']  = []
        host_list[ip]['ipid']   = []
        host_list[ip]['target'] = {}
    return host_list[ip]

def __entry_set( entry, key, value ):
    if value not in entry[key]:
        entry[key].append( value )
    return entry

def __host_set( ip, key, value ):
    entry = __host_get( ip )
    return __entry_set( entry, key, value )

def host_set_ttl( ip, ttl ):
    __host_set( ip, 'ttl', ttl )

def host_set_subip( ip, subip ):
    __host_set( ip, 'subip', subip )
    pass

def host_set_ipid( ip, ipid ):
    __host_set( ip, 'ipid', ipid )
    pass

def host_set_ua( ip, ua ):
    print ip,ua
    if len(ua.strip())> 1:
        __host_set( ip, 'ua', ua )
    pass

def host_set_cookie( ip, cookie ):
    uid_key = [ 'id=', 'ID=', 'uid=', 'UID=' ]
    for co in cookie.split( ';' ):
        if len(co.strip())> 1:
            if any( v in co for v in uid_key ):
                __host_set( ip, 'cookie', co )

COOKIE_KEY = [ 'id=', 'ver=' ]

def __host_get_target( ip, target ):
    entry = __host_get( ip )
    if target not in entry['target']:
        entry['target'][target]             = {}
        entry['target'][target]['ua']       = []
        entry['target'][target]['cookie']   = []
    return entry['target'][target]

def __form_cookie_list( cookie ):
    cookie_list = []
    for co in cookie.split( ';' ):
        if len(co.lstrip())> 1:
            if any( v in co.lower() for v in COOKIE_KEY ):
                cookie_list.append( co )
    return cookie_list

def host_set_http_request( ip, target, ua, cookie ):
    entry = __host_get_target( ip, target )

    # store user-agent
    __entry_set( entry, 'ua', ua )

    # store cookie list entry
    co = __form_cookie_list( cookie )
    for v in co:
        __entry_set( entry, 'cookie', v )
    return

def show_all_result():
    for key, host in host_list.iteritems():
        print "---------------------------------------------------------------"\
              "----------------------------------------------------------------"

        print host['ip'],
        if len(host['ttl']) > 1:
            print "(*)",

        # show  TTL
        print '\n\tTTL List:',
        for ttl in host['ttl']:
            print ttl,

        # show target host ua info
        print '\n\tTarget Host list'
        for target in host['target']:
            print '\t\t- host:', target
            print '\t\t\tUA:'
            for ua in host['target'][target]['ua']:
                print '\t\t\t  ', ua
            print '\t\t\tCookie:'
            for co in host['target'][target]['cookie']:
                print '\t\t\t  ', co

        # show IPID
        print '\n\tIPID List\t',
        cnt = 0
        for ipid in host['ipid']:
            print '{0:6d}'.format(ipid),
            cnt +=1
            if cnt%16 == 0:
                print '\n\t\t\t',

        # Show end
        print ''

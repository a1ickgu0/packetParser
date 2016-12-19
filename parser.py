import dpkt
import storage
from util import *

# util functions
import util

class Parser( object ):
    def __init__( self ):
        # List of all hosts.
        self.hosts = []
        # List containing all ICMP requests.
        self.icmp_requests = []
        # List containing all HTTP requests.
        self.http_requests = []
        # current ip address
        self.cur_ip_string = ""

    def __str__( self ):
        return ""

    def _http_rsp_process( self, response ):
        return

    def _http_req_process( self, request ):
        if request.method in ('GET', 'POST'):
            ua = request.headers['user-agent']
            ho = request.headers['host']
            co = request.headers['cookie']
            storage.host_set_http_request( self.cur_ip_string, ho , ua, co )
        return

    def _tcp_process( self, tcp ):
        if len(tcp.data) <= 0:
            return

        try:
            if tcp.dport is 80:
                request = dpkt.http.Request(tcp.data)
                self._http_req_process( request )
            elif tcp.sport is 80:
                response = dpkt.http.Response(tcp.data)
                self._http_rsp_process( response )
        except:
            pass

        return

    def _icmp_process( self, icmp ):
        return

    def _dhcp_process( self, dhcp ):
        return

    def _packet_process( self, buf ):
        eth = dpkt.ethernet.Ethernet(buf)
        if not isinstance(eth.data, dpkt.ip.IP):
            return

        # Get IP
        ip = eth.ip
        self.cur_ip_string = inet2str(ip.src)

        if not is_private_ip( self.cur_ip_string ):
            return

        storage.host_set_ttl( self.cur_ip_string, ip.ttl )

        storage.host_set_ipid( self.cur_ip_string, ip.id )

        # Get TCP
        if isinstance ( ip.data, dpkt.tcp.TCP ):
            tcp = ip.data
            return self._tcp_process( tcp )

        # Get ICMP
        if isinstance( ip.data, dpkt.icmp.ICMP ):
            return

        # Get DHCP
        if isinstance( ip.data, dpkt.dhcp.DHCP ):
            return

    def packet_process( self, buf ):
        self._packet_process( buf )

    def openfile( self, file ):
        pkt_num    = 0
        pkt_size   = 0

        f = open( file )
        pcap = dpkt.pcap.Reader(f)
        for ts, buf in pcap:
            self._packet_process( buf )
            pkt_num  += 1
        f.close()

        # show result
        print 'Total Packet Number:' + str( pkt_num )
        storage.show_all_result()

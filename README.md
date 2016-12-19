# packetParser
parse pcap file to get useful info as follow:


```
192.168.217.22 
	TTL List: 63 
	Target Host list
		- host: config.pinyin.sogou.com
			UA:
			   SogouIme
			Cookie:
			   YYID=5BE9C5BEE1DYTRFDE8D32CDE79B61BBF
			    IMEVER=8.1.0.8588
			    SUID=8C0B23783108990A000000005684J6HI4
			    IMESKINID=2:
			    CXID=2D9617SDFS
		- host: elephant.browser.360.cn
			UA:
			   Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36 QIHU 360SE
			Cookie:
			   __huid=10pb86Zha4ViYF2P%2FnWOFGXFh2DWK2ioRiDuASHGH677SS
			    __guid=13234303.2957272904621498000.1432325
		- host: ping.pinyin.sogou.com
			UA:
			   SogouIMEMiniSetup_imepopup
			   SOGOU_POPUP
			Cookie:
			   YYID=5BE9C5BEE1DB450938UY76TTXDB61BBF
			    IMEVER=8.1.0.8588
			    SUID=8C0B23783108990A000000005684J6HI4
			    IMESKINID=2:
			    CXID=2D9617SDFS

	IPID List	  7126   7127   7129   7130   7131   7133   7134   7135   7136   7137   7138   7149   7150   7151   7152   7153 
			  7171   7174   7175   7176   7177   7178   7179   7181   7182   7185   7186   7187   7188   7189   7191   7192 
			  7193   7194   7195   7211   7213   7214   7215   7216   7226   7227   7238   7239   7240   7241   7242   7268 
			  7273   7274   7275   7276   7277   7278   7279   7280   7282   7283   7284   7285   7286   7289   7290   7291 
			  7292   7293   7294   7295   7296   7297   7298   7299   7300   7301   7303   7304   7305   7306   7307   7308 

```

Depend on follow package:

* [dpkt](https://dpkt.readthedocs.io)
* [IPy](https://github.com/autocracy/python-ipy) 

```
sudo pip install dpkt
sudo pip install ipy
```





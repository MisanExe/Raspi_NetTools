import os
import sys
import utilities as ut
import network as nt


   
def main():

    #read and store ssid 
    SSID_buffer_str = sys.stdin.read()
    SSID_filtred = ut.filter_SSID(SSID_buffer_str)
    ut.print_ssid(SSID_filtred)

    #prompt to enter id of ssid 
    net = nt.network("KATIE", "3231KATIE")
    net.store_network(SSID_filtred)
    net.reload_network_file()

    #prompt to enter password
    #prompt to success

   


if __name__ == "__main__":
    main()
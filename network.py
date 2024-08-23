import subprocess as sb

class network:

    #network file
    
    def __init__(self, ssid, password):
        self.__ssid = ssid
        self.__pwd = password
        self.__nt_file_path = "/etc/wpa_supplicant/wpa_supplicant.conf"
        self.__nt_test_file_path = "test_file.txt"

    def store_network(self, network_ls):

        is_ssid_in_network = False
        #check if empty
        for str in network_ls:
            if self.__ssid in str:
                print("ssid found")
                is_ssid_in_network = True
                break  
        

        #open file
        if is_ssid_in_network:
            with open(self.__nt_file_path, "a") as file:
                
                scl_open = "{" #semi colon open
                scl_close = "{" #semi colon close
                net_string = f"network={scl_open}\n\tssid={self.__ssid}\n\tpsk={self.__pwd}\n{scl_close}"
                
                file.write(net_string)

    def reload_network_file(self):
        res = sb.run(['wpa_cli', 'reconfigure'], capture_output=True, text=True)
       # res2 = sb.run(['iwconfig'], capture_output=True, text=True)
        res3 = sb.run(['systemctl','restart','wpa_supplicant'], )
       # sudo systemctl restart wpa_supplicant

    #def __is_reload_successful(self, str):

    
   # def __is_connected():


        #print(type(res.stdout)) 
        #print(type(res2.stdout))
        #wpa_cli reconfigure


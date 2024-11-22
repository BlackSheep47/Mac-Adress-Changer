# Mac Address Changer 

import subprocess  # for more info https://docs.python.org/3/library/subprocess.html
import optparse



def mac_change(interface, Macaddress):
    #subprocess.call(f"ifconfig {networkcard} down", shell=True) # system command using subprocess (change ip for if for linux)
    subprocess.call(["ifconfig", interface,"down"]) #(User will not hijack the program by the list method)  


    #subprocess.call(f"ifconfig {networkcard} hw ether {Macaddress}", shell=True)
    subprocess.call(["ifconfig", interface, "hw", "ether", Macaddress]) #(User will not hijack the program by the list method)

    #subprocess.call(f"ifconfig {networkcard} up", shell=True)
    subprocess.call(["ifconfig", interface, "up"]) #(User will not hijack the program by the list method) limit user input 

    print(f"Mac address successfully changed!! {Macaddress}")


parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change it's mac address")
parser.add_option("-m", "--macaddress", dest="Macaddress", help="New Mac Address")

(options, arguments) = parser.parse_args()

#subprocess.call("ifconfig", shell=True)# show present network card present 
##subprocess.call(["ifconfig"]) #This new list method for limit the user input command (User will not hijack the program by the list method)
##print("Choose your network card !!")

#interface = options.interface # select you network card for example wlan0 eth0 etc
#Macaddress = options.Macaddress

#mac_change(interface, Macaddress)
mac_change(options.interface, options.Macaddress)







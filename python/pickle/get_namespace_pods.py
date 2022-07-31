import subprocess as sp
import os

projects = ['AMC', 'GTM', 'DEH', 'MDD', 'MCE', 'LCI', 'OAE', 'RID', 'CLO', 'EFR', 'BSL', 'EZR', 'BSL', 'ADL', 'RMI', 'OTC', 'AEI']

for proj in projects:
    print(proj)
    cmd1="kubectl get ns | grep -i " + proj + " | awk '{print $1}'"
    cmd2="kubectl get ns | grep -i " + proj + " | awk '{print $1}' | wc -l"
    # x=os.popen(cmd, 'r', 1)
    # print(x.read())
    str_ns=sp.check_output(cmd1,shell=True)
    # print(type(str_ns))
    no_ns=sp.check_output(cmd2,shell=True)
    list_ns = str_ns.split('\n')[:-1]
    # print(type(list_ns))
    # print(list_ns)
    total_pods = 0
    for i in list_ns:
        cmd3="kubectl get pods -n " + i + " | grep -iv name | wc -l"
        no_pods = int(sp.check_output(cmd3,shell=True))
        total_pods = total_pods + no_pods
    
    print("ns: "+ proj + str(no_ns))
    print("pods: " + proj + str(total_pods))
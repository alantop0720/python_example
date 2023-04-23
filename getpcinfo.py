import os, sys
import wmi
import hashlib
import base64
c = wmi.WMI()
#处理器
def printCPU():
    tmpdict = {}
    tmpdict["CpuCores"] = 0
    for cpu in c.Win32_Processor():     
        tmpdict["cpuid"] = cpu.ProcessorId.strip()
        tmpdict["CpuType"] = cpu.Name
        tmpdict['systemName'] = cpu.SystemName
        try:
            tmpdict["CpuCores"] = cpu.NumberOfCores
        except:
            tmpdict["CpuCores"] += 1
        tmpdict["CpuClock"] = cpu.MaxClockSpeed 
        tmpdict['DataWidth'] = cpu.DataWidth
    print (tmpdict)
    return  tmpdict

#主板
def printMain_board():
    boards = []
    # print len(c.Win32_BaseBoard()):
    for board_id in c.Win32_BaseBoard():
        tmpmsg = {}
        tmpmsg['UUID'] = board_id.qualifiers['UUID'][1:-1]   #主板UUID,有的主板这部分信息取到为空值，ffffff-ffffff这样的
        tmpmsg['SerialNumber'] = board_id.SerialNumber                #主板序列号
        tmpmsg['Manufacturer'] = board_id.Manufacturer       #主板生产品牌厂家
        tmpmsg['Product'] = board_id.Product                 #主板型号
        boards.append(tmpmsg)
    print (boards)
    return boards

#BIOS
def printBIOS():
    bioss = []
    for bios_id in c.Win32_BIOS():
        tmpmsg = {}
        tmpmsg['BiosCharacteristics'] = bios_id.BiosCharacteristics   #BIOS特征码
        tmpmsg['version'] = bios_id.Version                           #BIOS版本
        tmpmsg['Manufacturer'] = bios_id.Manufacturer.strip()                 #BIOS固件生产厂家
        tmpmsg['ReleaseDate'] = bios_id.ReleaseDate                   #BIOS释放日期
        tmpmsg['SMBIOSBIOSVersion'] = bios_id.SMBIOSBIOSVersion       #系统管理规范版本
        bioss.append(tmpmsg)
    print (bioss)
    return bioss

#硬盘
def printDisk():
    disks = []
    for disk in c.Win32_DiskDrive():
        # print disk.__dict__
        tmpmsg = {}
        tmpmsg['SerialNumber'] = disk.SerialNumber.strip()
        tmpmsg['DeviceID'] = disk.DeviceID
        tmpmsg['Caption'] = disk.Caption
        tmpmsg['Size'] = disk.Size
        tmpmsg['UUID'] = disk.qualifiers['UUID'][1:-1]
        disks.append(tmpmsg)
    for d in disks:
        print (d)
    return disks

#电池信息，只有笔记本才会有电池选项
def printBattery():
    isBatterys = False
    for b in c.Win32_Battery():
        isBatterys = True
    return isBatterys

#网卡mac地址：
def printMacAddress():
    macs = []
    for n in  c.Win32_NetworkAdapter():
        mactmp = n.MACAddress
        if mactmp and len(mactmp.strip()) > 5:
            tmpmsg = {}
            tmpmsg['MACAddress'] = n.MACAddress
            tmpmsg['Name'] = n.Name
            tmpmsg['DeviceID'] = n.DeviceID
            tmpmsg['AdapterType'] = n.AdapterType
            tmpmsg['Speed'] = n.Speed
            macs.append(tmpmsg)
    print (macs)
    return macs



if __name__ == '__main__':
   
    hd1=printCPU()
    
    hd3=printMain_board()
    #printBIOS()
    #printDisk()
    hd2=printMacAddress()
    print(type(hd1))
    print(type(hd2))
    print(type(hd3))
    print(hd1['cpuid'],hd1['systemName'],hd2[0]['MACAddress'],hd3[0]['UUID'],hd3[0]['SerialNumber'])
    sum = hd1['cpuid'] + hd1['systemName'] + hd2[0]['MACAddress'] + hd3[0]['UUID']+ hd3[0]['SerialNumber']
    shastr = sum.encode('gbk')
    sha = hashlib.sha1(shastr).hexdigest()
    if (sha == 'b696fcbb46e27a09458019942dd10856b0023fea'):
        print('reg user')
    else:
        print('no reg user')
        
    print(sha)
    #print(sum)
    #print(type(sum))
    s1 = base64.encodestring(shastr)
    print(s1)
    #s2 = base64.decodestring(s1)
    #print(s1,s2)
    #print (printBattery())
    
    xmlfilename = 'result.xml'
    f = open(xmlfilename, 'w') # 若是'wb'就表示写二进制文件
    f.write(sha)
    f.close()

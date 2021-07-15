urls = {
    'ookla': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT time as DateTime,AppName,Region,SiteName,MobileTechnology,MobileNumber,MobileModel,DeviceID,MobileOSVersion,Jitter,Latency,PacketLoss,DownloadThroughput,UploadThroughput FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='Ookla' AND MobileTechnology='5G'",

    'cell info': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT time as DateTime,AppName,Region,SiteName,MobileTechnology,MobileNumber,MobileModel,DeviceID,MobileOSVersion,OperatorID,RSRP,RSRQ,RSSNR,RSSI,eNB,PCI,NID,VoiceNW,DataNW,TAC,ECI,LCID,Power,GPSCoordinate FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='Cell Info' AND MobileTechnology='LTE'",

    'mobilehealth': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT time as DateTime, AppName, Region, SiteName, MobileTechnology, BatteryTemperature, BatteryCapacity, CpuUtilization, MemUtilization, CU_CpuUtilization, CU_MemUtilization, CurrentBattery FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='MobileHealth' AND MobileTechnology='LTE'",

    'dialerpad': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, RBT_Time, MOS FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='DialerPad' AND MobileTechnology='5G'",

    'sms': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, SendSMS_Time, SendMMS_Time, USSD_Time FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='SMS' AND MobileTechnology='5G'",

    'dnsandrtt (url resolution time)': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, URL, Resolution_Time FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='DNSandRTT' AND MobileTechnology='5G'",

    'dnsandrtt (url latency)': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, URL, RTT FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='DNSandRTT' AND MobileTechnology='5G'",

    'dropbox': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT Region, SiteName, MobileTechnology, MobileNumber, MobileModel, DeviceID, MobileOSVersion,OperatorID,DownloadThroughput,UploadThroughput,SuccessRate FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='DropBox' AND MobileTechnology='5G'",

    'youtube': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, VideoThroughput, VideoMOS FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='YouTube' AND MobileTechnology='5G'",

    'whatsapp': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, VideoThroughput, VideoMOS, PhotoThroughput, MessageSent_Time, FindContact_Time, MessageDelivered_Time FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='WhatsApp' AND MobileTechnology='5G'",

    'snapchat': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, PhotoThroughput, SuccessRate FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='SnapChat' AND MobileTechnology='5G'",

    'twitter': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, VideoThroughput, VideoMOS, PhotoThroughput, SendTweet_Time FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='Twitter' AND MobileTechnology='5G'",

    'facebook': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, Region, SiteName, MobileTechnology, MobileNumber, MobileModel, DeviceID, MobileOSVersion, OperatorID, SuccessRate, VideoThroughput,VideoMOS, PhotoThroughput, SendStory_Time FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='Facebook' AND MobileTechnology='5G'",

    'instagram': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, VideoThroughput, VideoMOS, PhotoThroughput FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='Instagram' AND Region = 'AAN' AND MobileTechnology='5G'",

    'skype': "http://2.51.14.64:8086/query?db=eProbeDB&q=SELECT AppName, MessageSent_Time, SuccessRate FROM MobileAppsPerformance WHERE time > now() - 24h AND AppName='Skype' AND MobileTechnology='5G'",
}

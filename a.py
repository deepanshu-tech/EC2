r=[
    {
        "Groups": [],
        "Instances": [
            {
                "AmiLaunchIndex": 0,
                "ImageId": "ami-013f17f36f8b1fefb",
                "InstanceId": "i-048b8cf7815d335ce",
                "InstanceType": "t2.micro",
               
                "Monitoring": {"State": "disabled"},
                "Placement": {
                    "AvailabilityZone": "us-east-1a",
                    "GroupName": "",
                    "Tenancy": "default",
                },
                "PrivateDnsName": "",
                "ProductCodes": [],
                "PublicDnsName": "",
                "State": {"Code": 48, "Name": "terminated"},
                "StateTransitionReason": "User initiated (2022-04-23 11:25:40 GMT)",
                "Architecture": "x86_64",
                "BlockDeviceMappings": [],
                "ClientToken": "e9b9f92d-50e1-454b-a2b8-afd43c877808",
                "EbsOptimized": False,
                "EnaSupport": True,
                "Hypervisor": "xen",
                "NetworkInterfaces": [],
                "RootDeviceName": "/dev/sda1",
                "RootDeviceType": "ebs",
                "SecurityGroups": [],
                "StateReason": {
                    "Code": "Client.UserInitiatedShutdown",
                    "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
                },
                "VirtualizationType": "hvm",
                "CpuOptions": {"CoreCount": 1, "ThreadsPerCore": 1},
                "CapacityReservationSpecification": {
                    "CapacityReservationPreference": "open"
                },
                "HibernationOptions": {"Configured": False},
                "MetadataOptions": {
                    "State": "pending",
                    "HttpTokens": "optional",
                    "HttpPutResponseHopLimit": 1,
                    "HttpEndpoint": "enabled",
                    "HttpProtocolIpv6": "disabled",
                    "InstanceMetadataTags": "disabled",
                },
                "EnclaveOptions": {"Enabled": False},
                "PlatformDetails": "Linux/UNIX",
                "UsageOperation": "RunInstances",
          
                "MaintenanceOptions": {"AutoRecovery": "default"},
            }
        ],
        "OwnerId": "368837817128",
        "ReservationId": "r-01a747ddcbb80566e",
    },
    {
        "Groups": [],
        "Instances": [
            {
                "AmiLaunchIndex": 0,
                "ImageId": "ami-013f17f36f8b1fefb",
                "InstanceId": "i-047b3cfbcabbeeed4",
                "InstanceType": "t2.micro",
        
                "Monitoring": {"State": "disabled"},
                "Placement": {
                    "AvailabilityZone": "us-east-1a",
                    "GroupName": "",
                    "Tenancy": "default",
                },
                "PrivateDnsName": "ip-172-31-21-232.ec2.internal",
                "PrivateIpAddress": "172.31.21.232",
                "ProductCodes": [],
                "PublicDnsName": "ec2-54-209-163-85.compute-1.amazonaws.com",
                "PublicIpAddress": "54.209.163.85",
                "State": {"Code": 16, "Name": "running"},
                "StateTransitionReason": "",
                "SubnetId": "subnet-0048a9ab45e4e0c42",
                "VpcId": "vpc-0308b63982999329f",
                "Architecture": "x86_64",
                "BlockDeviceMappings": [
                    {
                        
                            "DeleteOnTermination": True,
                            "Status": "attached",
                            "VolumeId": "vol-09496f348e5771988",
                        },
                    
                ],
                "ClientToken": "70c91ba6-b436-4eb7-a4f1-32ec00b728da",
                "EbsOptimized": False,
                "EnaSupport": True,
                "Hypervisor": "xen",
                "NetworkInterfaces": [
                    {
                        "Association": {
                            "IpOwnerId": "amazon",
                            "PublicDnsName": "ec2-54-209-163-85.compute-1.amazonaws.com",
                            "PublicIp": "54.209.163.85",
                        },
                        {
                            "AttachmentId": "eni-attach-0fd86e495740612e4",
                            "DeleteOnTermination": True,
                            "DeviceIndex": 0,
                            "Status": "attached",
                            "NetworkCardIndex": 0,
                        },
                        "Description": "",
                        "Groups": [
                            {"GroupName": "default", "GroupId": "sg-024a16cfffbc661c5"}
                        ],
                        "Ipv6Addresses": [],
                        "MacAddress": "0a:44:b1:d6:dc:37",
                        "NetworkInterfaceId": "eni-03f49f6b198b2e17f",
                        "OwnerId": "368837817128",
                        "PrivateDnsName": "ip-172-31-21-232.ec2.internal",
                        "PrivateIpAddress": "172.31.21.232",
                        "PrivateIpAddresses": [
                            {
                                "Association": {
                                    "IpOwnerId": "amazon",
                                    "PublicDnsName": "ec2-54-209-163-85.compute-1.amazonaws.com",
                                    "PublicIp": "54.209.163.85",
                                },
                                "Primary": True,
                                "PrivateDnsName": "ip-172-31-21-232.ec2.internal",
                                "PrivateIpAddress": "172.31.21.232",
                            }
                        ],
                        "SourceDestCheck": True,
                        "Status": "in-use",
                        "SubnetId": "subnet-0048a9ab45e4e0c42",
                        "VpcId": "vpc-0308b63982999329f",
                        "InterfaceType": "interface",
                    }
                ],
                "RootDeviceName": "/dev/sda1",
                "RootDeviceType": "ebs",
                "SecurityGroups": [
                    {"GroupName": "default", "GroupId": "sg-024a16cfffbc661c5"}
                ],
                "SourceDestCheck": True,
                "VirtualizationType": "hvm",
                "CpuOptions": {"CoreCount": 1, "ThreadsPerCore": 1},
                "CapacityReservationSpecification": {
                    "CapacityReservationPreference": "open"
                },
                "HibernationOptions": {"Configured": False},
                "MetadataOptions": {
                    "State": "applied",
                    "HttpTokens": "optional",
                    "HttpPutResponseHopLimit": 1,
                    "HttpEndpoint": "enabled",
                    "HttpProtocolIpv6": "disabled",
                    "InstanceMetadataTags": "disabled",
                },
                "EnclaveOptions": {"Enabled": False},
                "PlatformDetails": "Linux/UNIX",
                "UsageOperation": "RunInstances",
                "UsageOperationUpdateTime": datetime.datetime(
                    2022, 4, 23, 11, 18, 12, tzinfo=tzutc()
                ),
                "PrivateDnsNameOptions": {
                    "HostnameType": "ip-name",
                    "EnableResourceNameDnsARecord": False,
                    "EnableResourceNameDnsAAAARecord": False,
                },
                "MaintenanceOptions": {"AutoRecovery": "default"},
            }
        ],
        "OwnerId": "368837817128",
        "ReservationId": "r-0caab4eff60e1191d",
    },
]


for i in r:
    print(i)
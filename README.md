# NetPhoenix
## Report 1: Project Progress Report

**Project Title:** NetPhoenix: An Automated Self-Healing Network for Fault Detection and Recovery

**Project Domain:** Computer Networks and Network Automation

**Project Status:** Initial network implementation completed; Python automation pending.

## 1. Introduction

Computer networks are an important part of today's IT infrastructure. When a network link fails, communication can be interrupted until the problem is identified and resolved. This project focuses on building a network that can maintain connectivity through an alternate path when a link fails.

NetPhoenix is being developed using virtual routers in EVE-NG. The aim is to understand how dynamic routing and network automation can help improve network availability.

## 2. Objectives

- Create a virtual network using VyOS routers.
- Configure IP addressing and OSPF routing.
- Provide an alternate path between routers.
- Simulate a network link failure and check connectivity.
- Develop a Python script to monitor network health and detect failures.
- Study network behavior during failures using packet analysis.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| EVE-NG Community Edition | Creating the virtual network |
| VMware Workstation Pro | Running the EVE-NG virtual machine |
| VyOS | Virtual router configuration |
| OSPF | Dynamic routing |
| Python | Planned monitoring and automation |
| Netmiko | Planned remote router management |
| Wireshark | Planned packet capture and analysis |
| GitHub | Project files and documentation |

## 4. Work Completed

### 4.1 Virtual Lab Setup

EVE-NG Community Edition was installed in VMware Workstation Pro. A new lab named NetPhoenix was created, and two VyOS routers, R1 and R2, were added and installed.

### Network Topology

The topology contains two VyOS routers connected through two separate Ethernet links.

![NetPhoenix topology](../screenshots/topology.png)

*Figure 1: Virtual network topology created in EVE-NG.*

### 4.2 IP Addressing

IP addresses were assigned to both routers using two separate subnets.

| Router | Interface | IP Address |
|---|---|---|
| R1 | eth0 | 10.0.12.1/30 |
| R2 | eth0 | 10.0.12.2/30 |
| R1 | eth1 | 10.0.13.1/30 |
| R2 | eth1 | 10.0.13.2/30 |

### 4.3 OSPF Configuration

OSPF was configured on both routers in Area 0. The neighbor status was checked using the `run show ip ospf neighbor` command.

![OSPF before failover](../screenshots/ospf-before-failover.png)

*Figure 2: OSPF neighbor status before the failure test.*

### 4.4 Connectivity Testing

Ping tests were performed between R1 and R2 to verify that the configured links were working.

![Ping before failover](../screenshots/ping-before-failover.png)

*Figure 3: Connectivity test before simulating a link failure.*

### 4.5 Manual Failover Test

The first interface on R1 was disabled to simulate a link failure. Connectivity was then tested through the alternate link. Ping replies were received while the alternate path was available. The original interface was restored after the test.

![Ping during failover](../screenshots/ping-during-failover.png)

*Figure 4: Ping test during the manual failover experiment.*

![OSPF after restoration](../screenshots/ospf-after-restoration.png)

*Figure 5: OSPF neighbor status after the original interface was restored.*

## 5. Results

The initial networking stage has been completed.

- Both VyOS routers are running in EVE-NG.
- IP addressing has been configured on both links.
- OSPF neighbor relationships have been observed.
- Ping tests between the routers were successful.
- A manual link failure was simulated.
- Connectivity through the alternate path was verified.

The results demonstrate basic network redundancy and manual failover. Python-based automated detection and recovery have not yet been implemented.

## 6. Work Remaining

The next stage will focus on Python-based automation using Netmiko. The planned tasks include connecting to the routers through SSH, monitoring connectivity, detecting a predefined failure, verifying recovery, and recording test results.

Wireshark will also be used to capture traffic and study OSPF behavior during failures. Further testing will be carried out before the final project report is prepared.

## 7. Conclusion

In this stage, the virtual network was created and basic routing was configured. Testing showed that connectivity could continue when one interface was disabled, provided the alternate path remained available.

The next stage will focus on developing and testing Python-based automation to detect failures and verify recovery.

# infinq

## INQ Utility for Solaris

### Background
InfiniBox volumes can be inquired using the HPT 'infinihost volume list' command. due to architecture limitation, it works very slow on Sun Solaris Sparc hosts.
The Following utility can be used to query all SCSI devices, and uses SCSI queries to get the required data.
infinq supports multipathed devices and both iSCSI and FC connectivity.

### Prerequisites
* Python 2.7.x. need to be installed
* sg3_utils has to be installed - can be downloaded from [here](https://github.com/hreinecke/sg3_utils)


### Sample Output 
#timex python infinq.py
Device                                     Size         Volume          Array      Pool
---------------------------------------------------------------------------------------
c0t6742B0F0000005DB000000000001A6D0d0       1.00 GB     test_sol69      ibox1499   APJ-Pool
c0t6742B0F0000005DB000000000001A6CEd0       1.00 GB     test_sol68      ibox1499   APJ-Pool
c0t6742B0F0000005DB000000000001A6BCd0       1.00 GB     test_sol59      ibox1499   APJ-Pool
c0t6742B0F0000005DB000000000001A6BEd0       1.00 GB     test_sol60      ibox1499   APJ-Pool


### Limitations
tested with 1,000 InfiniBox devices
 


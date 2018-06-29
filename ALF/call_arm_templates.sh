#!/bin/bash

cd /root/ALF/VNET_SUBNET/ && ./deploy.sh

cd ../LINUX_ARM_VM/ && ./deploy-vm.sh

cd ../WIN_ARM_VM/ && ./deploy-vm.sh

cd ../WIN_ARM_SQL/ && ./deploy-sql-vm.sh

#!/bin/bash

# Setup directories.
project_dir=$HOME/deadstream
test_dir=$HOME/deadstream_tmp
backup_dir=$HOME/deadstream_previous.`cat /dev/random | tr -cd 'a-f0-9' | head -c 12`
log_file=$HOME/update.log

echo "Updating "
date

# Stop the running services
echo "sudo service timemachine stop"
sudo service timemachine stop
echo "sudo service serve_options stop"
sudo service serve_options stop

# check if archive needs refreshing
update_archive=`find $project_dir/timemachine/metadata/ids.json -mtime +40 | wc -l`

# clone the repo into the test_dir
cd $HOME
rm -rf $test_dir
mkdir -p $test_dir
cd $HOME
git clone https://github.com/eichblatt/deadstream.git deadstream_tmp
mkdir -p $test_dir
cd $test_dir
echo "git checkout dev"
git checkout dev
pip3 install .

# If the archive has been refreshed in the last 40 days, copy it to the test dir
if [ $update_archive == 0 ]; then
   echo "cp -R $project_dir/timemachine/metadata $test_dir/timemachine/."
   cp -R $project_dir/timemachine/metadata $test_dir/timemachine/.
fi

# Set up the services. NOTE: This actually points to the old ones... Should fix this
cd $test_dir/bin
echo "pwd is $PWD"
./services.sh
stat=$?
if [ $stat != 0 ]; then
   echo "status of services command: $stat"
   echo "rm -rf $test_dir"
   rm -rf $test_dir
   exit $stat
fi

# Run the main program, make sure a button press and knob turn work.
python3 $test_dir/main.py --test_update
stat=$?
echo "status of test command: $stat"

# If this succeeds, put the new folder in place.
if [ $stat == 0 ]; then
   echo "mv $project_dir $backup_dir"
   mv $project_dir $backup_dir
   echo "mv $test_dir $project_dir"
   mv $test_dir $project_dir
fi

# Restart the services (Can i get the timemachine service to launch the serve_options?)
echo "sudo service timemachine restart"
sudo service timemachine restart
echo "sudo service serve_options restart"
sudo service serve_options restart

exit $stat

echo "Publishing $1"
rosrun image_pub image_pub_node _img_path:=/home/nvidianav/test-data/"$1" _pub_rate:=30 _repeat:=true

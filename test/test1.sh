a=`python3 give_chart.py`
echo $a
python3 python3_picture_load1.py $a  &
python3 python3_picture_load.py $a &

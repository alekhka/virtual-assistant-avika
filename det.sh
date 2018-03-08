export AUDIODEV=plughw:1,0
while true; do
rec /tmp/recording.flac rate 32k silence 1 0.1 5% 1 3.0 5% &
p=$!
sleep 1
until [ "$var1" != "$var2" ]; do
    var1=`du "/tmp/recording.flac"`
    sleep 1
    var2=`du "/tmp/recording.flac"`
done
echo "Sound Detected"
until [ "$var1" == "$var2" ]; do
    var1=`du "/tmp/recording.flac"`
    sleep 0.5
    var2=`du "/tmp/recording.flac"`
done
echo "Silence Detected"
sleep 2
kill $p

mv /tmp/recording.flac /home/pi/reco.flac
python srec.py
done
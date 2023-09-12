# raspberrypi

<h3>라즈베리파이 초기 설정</h3>
<br>
  sudo apt update<br>
  sudo apt upgrade
<li>
  한글설정
</li>
sudo apt-get install fonts-unfonts-core -y (은폰트) <br>
sudo apt-get install ibus ibus-hangul -y (한글 입력기)
<br>
<br>

<li>
  아두이노 설치
</li>
sudo apt-get install arduino -y
<br>
<br>

## <h3>InfluxDB2 설치 방법</h3>
<hr>
<li>
  InfluxDB download key using wget
</li>
```
wget -q https://repos.influxdata.com/influxdata-archive_compat.key
echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
```
<br>
<br>

<li>Packages are up to date && install Influxdb2</li>
sudo apt-get update && sudo apt-get install influxdb2 -y
<br>
<br>

<li>에러)influxdb2의 패키지를 찾을 수 없을경우 influxdb1으로 설치</li>
sudo apt-get install influxdb -y
<br>
<br>

<li>InfluxDB as a background service on startup</li>
sudo service influxdb start(influxdb 시작 명령어)
<br>
<br>

<li>InfluxDB is status(service)</li>
sudo service influxdb status(infulxdb localhost로 접속 가능?명렁어)

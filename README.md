# raspberrypi
<h3>라즈베리파이 초기 설정</h3>
    
    sudo apt update
  
    sudo apt upgrade
    
<br>
<br>
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

    wget -q https://repos.influxdata.com/influxdata-archive_compat.key
  
    echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee 
    /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
  
    echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list

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
    ->InfluxDB2로 설치했을 시

<br>
<br>

<li>influxdb import with python</li>

    sudo pip install influxdb

<br>
<br>
<li>InfluxDB 데이터베이스 만들기</li>

    $ influx
    >create database <데이터베이스명>
    확인 : show databases


<h3>Grafana Installation</h3>

<li>Repository의 GPG key를 더하기</li>

    wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

<li>Repository를 더하기</li>

    echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a                 /etc/apt/sources.list.d/grafana.list

<li>프로그램 설치</li>

    sudo apt update
    sudo apt install grafana

<li>프로그램 실행</li>

    sudo service grafana-server start
    서버를 구동하고 default 호스트 주소 & 자기 자신의 아이피 주소로 접속 가능
    아이피로 들어갈 시 전체적으로 데이터를 처리하는? 부분이 좀 더 빠른 거 같음



# macOS or Linux의 cron을 nano 에디터로 설정
> macOS에는 nano가 기본적으로 설치되어 있다. 아래의 설치 방법은 Linux Ubuntu 기준.

```
$ sudo apt-get install nano
```

나노 에디터를 활용해서 ".bash_profile"이라는 설정파일을 편집 하기 위한 명령어 입력.

```
$ nano ~/.bash_profile
```
cron을 수정할 때 nano 사용하게 하기 위해 추가.
```
export EDITOR=nano
```
수정을 완료하면, Ctrl + X를 눌러 에디터를 닫는다. (에디터를 닫기 전에 파일을 저장할지 묻는 대화상자가 나오면, y를 눌러 저장을 선택하고 [Enter]를 누른다.)

"~/.bash_profile"을 수정했으면 다시 로그인하거나, "source ~/.bash_profile" 명령어를 실행해 설정을 반영한다.

# crontab으로 cron 설정
위 단계가 정상적으로 끝나면, "crontab" 명령어로 cron을 설정. crontab을 실행할 때 "-e" 옵션을 추가해서 실행한다. 이렇게 하면 cron 설정 화면이 열리는데, 처음 "crontab"을 실행했다면 아무것도 작성되지 않은 설정 파일이 열리게 된다.

```
$ crontab -e
```
텍스트 에디터가 열리면 "everyday-dollar.py"라는 프로그램을 매일 아침 7시에 실행하기 위한 테스트 코드를 아래와 같이 작성한다. (파이썬 파일이 존재하는 경로에 맞게 /path/to 부분의 경로를 변경한다.)
```
0 7 * * * /path/to/python3 /path/to/everyday-dollar.py
```
nano 에디터를 이용해 위와 같이 작성하고 Ctrl + X를 눌러 에디터를 닫는다. 위와 마찬가지로 파일을 저장할지 묻는 대화상자가 나오면 y를 눌러 저장을 선택한 뒤 파일 이름을 확인하고 [Enter]를 누른다. 이렇게 하면 매일 아침 7시에 설정한 스크립트를 실행한다.

# cron 실행시 환경변수 설정
cron을 실행할 때 주의 할점은 cron 실행시 환경변수가 최소한으로만 설정된다는 것이다. 따라서 경로가 맞지 않아 명령이 실행되지 않는 경우가 발생할 수 있다. 이럴 땐 crontab으로 설정하는 설정 파일 앞부분에서 환경변수를 따로 설정해야 한다.
```
PATH=/usr/local/bin:/usr/bin:/bin
PYTHONIOENCODING='utf-8'

0 7 * * * /path/to/python3 /path/to/everyday-dollar.py
```
crontab에 지정하는 환경변수는 우변을 따로 전개하지 않으므로 이에도 주의해야 한다.
```
PATH=/usr/local/bin:$PATH # 잘못된 지정 방식
```
또한 현재 폴더가 사용자 홈 폴더로 지정된다는 것도 주의해야 한다. 따라서 로그 등을 저장할 때는 전체 경로를 지정하거나 현재 폴더를 변경하는 등의 대책이 필요하다.

>한마디로 프로그램을 cron에 등록해서 실행하면 사용자 홈 폴더에 everyday-dollar.py(네이버 환율 데이터 크롤링) 정보가 저장된다.

# crontab 설정 방법
crontab을 사용해 설정 파일을 작성하는 방법은 기본적으로 아래와 같다.
```
[서식] crontab
(분) (시) (일) (월) (요일) <실행할 명령어의 경로>
```
각 필드에는 다음과 같은 숫자를 입력한다.

항목|설명
:-:|:-:
분|0-59
시|0-23
일|1-31
월|1-12
요일|0-7(0과 7은 일요일)

또한 숫자 외에도 다음과 같은 것을 지정할 수 있다.

이름|사용 예|설명
:-:|:-:|:-:
리스트|0,10,30|0, 10, 30을 각각 지정한다.
범위|1-5|1, 2, 3, 4, 5를 범위로 지정한다.
간격|*/10|10, 20, 30처럼 10 간격으로 지정한다.
와일드카드|*|모두 지정한다.

## EX.)
다음은 macOS에서 매 분마다 "Hi"라고 출력하는 프로그램의 예.
```
* * * * * /usr/bin/say "Hi"
```
다음은 매일 아침 8시 30분에 "Good morning"이라고 인사하는 프로그램의 예.
```
30 8 * * * /usr/bin/say "Good morning"
```
다음은 매월 20일 18시 32분에 /home/moon/something.sh라는 프로그램을 실행하는 예.
```
32 18 20 * * /home/moon/something.sh
```
다음은 매년 5월 6일 7시 8분에 "Have a nice day"라고 인사하는 프로그램의 예.
```
08 07 06 05 * /usr/bin/say "Have a nice day"
```
다음은 매주 월요일 아침 7시 50분에 "쓰레기 버리는 날입니다!"라고 알려주는 설정의 예.
```
50 07 * * 1 /usr/bin/say "쓰레기 버리는 날입니다!"
```

cron으로 요일을 지정할 때는 다음과 같은 숫자를 지정한다.

요일|숫자
:-:|:-:
월요일|1
화요일|2
수요일|3
목요일|4
금요일|5
토요일|6
일요일|7 또는 0

매월의 마지막 날에 뭔가를 하고 싶은 경우엔 기본적인 crontab으로는 지정할 수 없다. 따라서 아래와 같이 test 명령어와 조합해서 사용하면 매월 마지막 날을 검출할 수 있다.
```
50 23 28-31 * * /usr/bin/test/ $(date -d '+1 day' +%d) -eq 1 && <실행할 명령어>
```
 또한 cron은 표준 출력 또는 오류 출력이 있으면 메일을 준다. 이러한 기능을 비활성화하고 싶을 때는 crontab의 앞에 MAILTO를 비워둔다.
 ```
 MAILTO=""
 ```
# Windows 작업 스케줄러 설정
윈도우에선 schtasks를 이용해서 예약 작업을 설정한다. 아래와 같이 명령어를 작성하면 schtasks를 이용해서 예약 작업을 설정할 때 필요한 인자들에 대한 정보가 출력된다.
```
C:\>schtasks /create /?

# 출력 예:
SCHTASKS /Create [/S system [/U username [/P [password]]]]
    [/RU username [/RP password]] /SC schedule [/MO modifier] [/D day]
    [/M months] [/I idletime] /TN taskname /TR taskrun [/ST starttime]
    [/RI interval] [ {/ET endtime | /DU duration} [/K] [/XML xmlfile] [/V1]]
    [/SD startdate] [/ED enddate] [/IT | /NP] [/Z] [/F] [/HRESULT] [/?]

    ...중략
```
윈도우 10 사용자라면 파워쉘을 이용해서 스케줄러를 작성하면 된다. 아래는 파워쉘에서 "schtasks /create /?" 명령어를 실행했을 때 나타나는 설명 부분이다.

```
/S system|연결할 원격 시스템을 지정합니다. 생략되면
                       기본값으로 로컬 시스템이 시스템 매개 변수로 지정됩니다.

    /U   username      SchTasks.exe을(를) 실행해야 하는 사용자 컨텍스트를
                       지정합니다.

    /P   [password]    제공된 사용자 컨텍스트에 대한 암호를 지정합니다.
                       생략된 경우 입력하도록 묻습니다.

    /RU  username      작업을 실행할 "다음 계정으로 실행"의 사용자 계정(사용자 컨텍스트)을
                       지정합니다. 시스템 계정에
                       유효한 값은"", "NT AUTHORITY\SYSTEM"
                       또는 "SYSTEM"입니다.
                       v2 작업의 경우, 3가지 유형에 모두 대해 잘 알려진 SID뿐만 아니라 "NT AUTHORITY\LOCALSERVICE" 및
                       "NT AUTHORITY\NETWORKSERVICE"도
                       사용할 수 있습니다.

    /RP  [password]    "다음 계정으로 실행"의 사용자 암호를 지정합니다.
                       암호를 묻도록 하려면 값이  "*"이거나
                       비어 있어야 합니다. 시스템 계정에는 이 암호가 해당되지
                       않습니다. /RU 또는 /XML 스위치와 함께 사용해야
                       합니다.

    /SC   schedule     일정 빈도를 지정합니다.
                       유효한 일정 유형: MINUTE, HOURLY,DAILY, WEEKLY,
                       MONTHLY, ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT.

    /MO   modifier     일정 반복을 미세하게 제어할 수 있도록 일정 유형을
                       구체화합니다. 유효한 값은 아래
                       "한정자" 구역에 나열되어 있습니다.

    /D    days         작업을 실행할 요일을 지정합니다. 유효한
                       값: MON, TUE, WED, THU, FRI, SAT, SUN 및
                       MONTHLY 일정에는 1 - 31(달의 날짜)
                       와일드카드 "*"는 모든 날을 지정합니다.

    /M    months       달을 지정합니다. 달의 첫 번째 날이
                       기본값입니다. 유효한 값: JAN, FEB, MAR, APR,
                       MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC. 와일드카드 "*"는
                       모든 날을 지정합니다.

    /I    idletime     예약된 ONIDLE 작업을 실행하기 전에
                       기다리는 유휴 상태 시간을 지정합니다.
                       유효한 범위: 1 - 999분

    /TN   taskname     이 예약된 작업을 고유하게 식별하는 경로\이름 형식의
                       문자열을 지정합니다.

    /TR   taskrun      예약된 시간에 실행할 프로그램의 경로 및 파일 이름을
                       지정합니다.
                       예: C:\windows\system32\calc.exe

    /ST   starttime    작업을 실행할 시작 시간을 지정합니다. 시간
                       형식은 HH:mm입니다(24시간 형식). 예를 들어, 14:30은
                       오후 2:30입니다. /ST를 지정하지 않은 경우 기본값은 현재
                       시간입니다. 이 옵션은 /SC ONCE와 함께 요구됩니다.

    /RI   interval     반복 간격(분)을 지정합니다. 다음
                       일정 유형에는 해당되지 않습니다: MINUTE, HOURLY,
                       ONSTART, ONLOGON, ONIDLE, ONEVENT.
                       유효한 범위는 1-599940분입니다.
                       /ET 또는 /DU를 지정하면 기본값으로 10분이
                       설정됩니다.

    /ET   endtime      작업 실행 종료 시간을 지정합니다. 시간 형식은
                       HH:mm입니다(24시간 형식). 예를 들어, 14:50은 오후 2:50입니다.
                       다음 일정 유형에는 해당되지 않습니다: ONSTART,
                       ONLOGON, ONIDLE, ONEVENT.

    /DU   duration     작업을 실행할 기간을 지정합니다. 시간
                       형식은 HH:mm입니다. /ET 및 다음 일정 유형에는
                       해당되지 않습니다: ONSTART, ONLOGON, ONIDLE, ONEVENT.
                       /V1 작업의 경우 /RI를 지정하면 기본값으로 1시간이
                       설정됩니다.

    /K                 endtime 또는 duration 시간에 작업을 끝냅니다.
                       다음 일정 유형에는 해당되지 않습니다: ONSTART,
                       ONLOGON, ONIDLE, ONEVENT. /ET 또는 /DU가 지정되어야
                       합니다.

    /SD   startdate    작업을 실행할 첫 번째 날짜를 지정합니다. 형식은
                       yyyy/mm/dd입니다. 기본값은 현재
                       날짜입니다. 다음 일정 유형에는 해당되지 않습니다: ONCE,
                       ONSTART, ONLOGON, ONIDLE, ONEVENT.

    /ED   enddate      작업을 실행할 마지막 날짜를 지정합니다. 형식은
                       yyyy/mm/dd입니다. 다음 일정 유형에는 해당되지
                       않습니다: ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT.

    /EC   ChannelName  OnEvent 트리거에 대한 이벤트 채널을 지정합니다.

    /IT                            작업 실행 시 /RU 사용자가 로그온되어 있는 경우에만
                       작업을 대화형으로 실행할 수 있도록 합니다.
                       사용자가 로그인해야 이 작업이 실행됩니다.

    /NP                암호를 저장하지 않습니다. 이 작업은 주어진 사용자로서
                       상호 작용 없이 실행됩니다. 로컬 리소스만 사용할 수 있습니다.

    /Z                 마지막 실행 후 삭제할 작업을 표시합니다.

    /XML  xmlfile      파일에 지정된 작업 XML에서 작업을 만듭니다.
                       작업 XML에 이미 사용자가 있는 경우
                       /RU 및 /RP 스위치를 함께 사용하거나 /RP만 함께 사용할 수 있습니다.

    /V1                Vista 이전 플랫폼에 표시되는 작업을 만듭니다.
                       /XML과 호환되지 않습니다.

    /F                 지정한 작업이 이미 있는 경우 작업을 강제로 만들고
                       경고를 표시하지 않습니다.

    /RL   level        작업을 위해 실행 수준을 설정합니다.  유효한 값은
                       LIMITED 및 HIGHEST입니다. 기본값은 LIMITED입니다.

    /DELAY delaytime   트리거가 발생한 후 작업 실행을 지연할
                       대기 시간을 지정합니다. 시간 형식은
                       mmmm:ss입니다. 이 옵션은 ONSTART, ONLOGON, ONEVENT
                       일정 유형에만 유효합니다.

    /HRESULT           진단성 향상을 위해 프로세스 종료 코드는
                       HRESULT 형식이 됩니다.

    /?                 이 도움말 메시지를 표시합니다.  
```
다음은 한정자라 불리는 /MO 스위치에 대한 범위에 해당하는 값이다.

항목|설명
:-:|:-:
MINUTE| 1 - 1439 minutes.
HOURLY| 1 - 23 hours.
DAILY| 1 - 365 days.
WEEKLY| weeks 1 - 52.
ONCE| No modifiers.
ONSTART| No modifiers.
ONLOGON| No modifiers.
ONIDLE| No modifiers.
MONTHLY| 1 - 12, or FIRST, SECOND, THIRD, FOURTH, LAST, and LASTDAY.
ONEVENT| XPath event query string.

실행 예제는 파워셀을 아래와 같이 통해 확인 가능하다. ~~MS 만세!~~
```
ONEVENT:  XPath 이벤트 쿼리 스트링.
예:
   ==> "ABC" 원격 컴퓨터에 "doc" 예약된 작업을 만듭니다.
       한 시간마다 notepad.exe를 "runasuser" 사용자로 실행합니다.

       SCHTASKS /Create /S ABC /U user /P password /RU runasuser
                /RP runaspassword /SC HOURLY /TN doc /TR notepad

   ==> "ABC" 원격 컴퓨터에 "accountant" 예약된 작업을 만듭니다.
       시작 날짜와 끝 날짜 사이에 지정한 시작 시간부터 종료 시간까지
       5분마다 calc.exe를 실행합니다.

       SCHTASKS /Create /S ABC /U domain\user /P password /SC MINUTE
                /MO 5 /TN accountant /TR calc.exe /ST 12:00 /ET 14:00
                /SD 06/06/2006 /ED 06/06/2006 /RU runasuser /RP userpassword

   ==> "gametime" 예약된 작업을 만듭니다. 매월 첫 번째 일요일에
       프리셀을 실행합니다.

       SCHTASKS /Create /SC MONTHLY /MO first /D SUN /TN gametime
                /TR c:\windows\system32\freecell

   ==> "ABC" 원격 컴퓨터에 "report" 예약된 작업을 만듭니다.
       매주마다 notepad.exe를 실행합니다.

       SCHTASKS /Create /S ABC /U user /P password /RU runasuser
                /RP runaspassword /SC WEEKLY /TN report /TR notepad.exe

   ==> "ABC" 원격 컴퓨터에 "logtracker" 예약된 작업을 만듭니다.
       지정된 시작 시간부터 종료 시간 없이 5분마다
       notepad.exe.를 실행합니다. /RP 암호를
       묻습니다.

       SCHTASKS /Create /S ABC /U domain\user /P password /SC MINUTE
                /MO 5 /TN logtracker
                /TR c:\windows\system32\notepad.exe /ST 18:30
                /RU runasuser /RP

   ==> "gaming" 예약된 작업을 만듭니다. 매일 12:00부터 14:00까지
       freecell.exe를 실행하고 종료합니다.

       SCHTASKS /Create /SC DAILY /TN gaming /TR c:\freecell /ST 12:00
                /ET 14:00 /K
   ==> 이벤트 101이 시스템 채널에 게시될 때마다
       wevtvwr.msc를 실행하는 "EventLog" 예약된 작업을 만듭니다.

       SCHTASKS /Create /TN EventLog /TR wevtvwr.msc /SC ONEVENT
                /EC System /MO *[System/EventID=101]
   ==> 따옴표 두 세트를 사용하여 파일 경로에 공백을 사용할 수 있습니다.
       CMD.EXE와 SchTasks.exe에 각각 하나씩 따옴표 세트를 사용합니다.
       CMD에 대한 외부 따옴표로는 큰따옴표를 사용하고, 내부 따옴표로는
       작은 따옴표 또는 이스케이프된 큰따옴표를 사용해야 합니다.
       SCHTASKS /Create
          /tr "'c:\program files\internet explorer\iexplorer.exe'
          \"c:\log data\today.xml\"" ...
```

- 참고문헌 : 파이썬을 이용한 머신러닝, 딥러닝 실전 개발 입문
- Schtasks.exe 참고사이트 : https://msdn.microsoft.com/en-us/library/windows/desktop/bb736357(v=vs.85)

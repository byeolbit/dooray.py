# Dooray.py (WIP)

Dooray! 메신저의 슬래시 커맨드를 좀 더 편하게 쓰기 위한 래퍼 라이브러리입니다.

슬래시 커맨드의 자세한 설명은 두레이의 [슬래시 커맨드 가이드](https://helpdesk.dooray.com/share/pages/9wWo-xwiR66BO5LGshgVTg/2900083523359058679)를 참고하세요.

## 사용 예시

```py
from dooray import slash_command

client = slash_command.Client()

@client.command()
def hello():
  return 'hello world!'


client.run('token')

```

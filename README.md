# 장고 마이그레이션 팁: 불필요한 리소스 줄이기

이 프로젝트는 **파이 웹 심포지움 2024**의 **"장고 마이그레이션 팁: 불필요한 리소스 줄이기"** 발표를 위한 예시 코드입니다.

프로젝트는 LocaleMiddleware를 사용하고 있어 문자열 번역이 가능합니다.
세 언어(한국어, 영어, 독일어)의 번역을 시험해볼 수 있으며, `LANGUAGE_CODE` 변경에 따른 영향을 확인하려면 반드시 다음 명령어를 실행해주세요:
```
python manage.py compilemessages
```

`django.mo` 파일이 생성되지 않으면 locale 변경에 따른 마이그레이션 파일 변화를 확인하기 어렵습니다.
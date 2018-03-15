# Nichibu bot - slack bot

## Getting Started

### Prerequisites

Cài python3 và pip3. Nếu máy bạn đã có thì bỏ qua bước này.

Cài [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
```
$ [sudo] pip3 install virtualenv
$ sudo apt install python3-venv
```

### Installing

Clone project từ git

Tạo môi trường ảo bằng virtualenv
```
$ cd nichibu-bot
$ python3 -m venv .env
```

Chạy môi trường ảo và cài các package cần thiết
```
$ source .env/bin/activate
$ pip3 install -r requirement.txt
```

Tạo biến môi trường của Bot User OAuth Access Token:
```
$ export SLACK_BOT_TOKEN='Mã của bạn'
```

Thoát môi trường ảo
```
$ deactivate
```

### Run project

```
$ source env/bin/activate
$ python3 main.py
```

## Deployment

Không có gì đặc biệt

## Built With

* [python3](https://www.python.org/)
* [slack-client](https://slack.com/)

## Versioning

0.1

## Authors

**Nichibu chatbot team**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

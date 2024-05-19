<!-- markdownlint-disable MD030 -->

# [![Langflow](https://github.com/langflow-ai/langflow/blob/dev/docs/static/img/hero.png)](https://www.langflow.org)

English | [中文](./README-ZH.md) | [日本語](./README-JA.md) | [한국어](./README-KR.md) | Русский

### [Langflow](https://www.langflow.org) - это новый визуальный способ создания, итерации и развертывания приложений искусственного интеллекта.

# ⚡️ Документация и сообщество

- [Документация](https://docs.langflow.org)
- [Discord](https://discord.com/invite/EqksyE2EX9)

# 📦 Установка

Вы можете установить Langflow с помощью pip:

```shell
# Убедитесь, что у вас установлена Python версии 3.10 на вашей системе.
# Установите предварительную версию.
python -m pip install langflow --pre --force-reinstall

# или стабильную версию.
python -m pip install langflow -U
```

Затем запустите Langflow с помощью:

```shell
python -m langflow run
```

Вы также можете предварительно просмотреть Langflow в [HuggingFace Spaces](https://huggingface.co/spaces/Langflow/Langflow-Preview). [Клонируйте пространство, используя эту ссылку](https://huggingface.co/spaces/Langflow/Langflow-Preview?duplicate=true), чтобы создать собственное рабочее пространство Langflow всего за несколько минут.

# 🎨 Создание потоков

Создание потоков с Langflow легко. Просто перетащите компоненты со боковой панели на холст и соедините их, чтобы начать создавать ваше приложение.

Исследуйте, редактируя параметры подсказок, группируя компоненты в один высокоуровневый компонент и создавая собственные Пользовательские компоненты.

Когда закончите, вы можете экспортировать ваш поток в виде JSON-файла.

Загрузите поток с помощью:

```python
from langflow.load import run_flow_from_json

results = run_flow_from_json("path/to/flow.json", input_value="Hello, World!")
```

# 🖥️ Интерфейс командной строки (CLI)

Langflow предоставляет интерфейс командной строки (CLI) для удобного управления и конфигурации.

## Использование

Вы можете запустить Langflow, используя следующую команду:

```shell
langflow run [OPTIONS]
```

Каждая опция подробно описана ниже:

- `--help`: Отображает все доступные опции.
- `--host`: Задает хост, к которому привязывается сервер. Можно установить с помощью переменной окружения `LANGFLOW_HOST`. По умолчанию `127.0.0.1`.
- `--workers`: Устанавливает количество рабочих процессов. Можно установить с помощью переменной окружения `LANGFLOW_WORKERS`. По умолчанию `1`.
- `--timeout`: Задает время ожидания рабочего процесса в секундах. По умолчанию `60`.
- `--port`: Устанавливает порт для прослушивания. Можно установить с помощью переменной окружения `LANGFLOW_PORT`. По умолчанию `7860`.
- `--config`: Задает путь к файлу конфигурации. По умолчанию `config.yaml`.
- `--env-file`: Указывает путь к файлу `.env`, содержащему переменные окружения. По умолчанию `.env`.
- `--log-level`: Задает уровень логирования. Можно установить с помощью переменной окружения `LANGFLOW_LOG_LEVEL`. По умолчанию `critical`.
- `--components-path`: Указывает путь к каталогу с пользовательскими компонентами. Можно установить с помощью переменной окружения `LANGFLOW_COMPONENTS_PATH`. По умолчанию `langflow/components`.
- `--log-file`: Указывает путь к файлу журнала. Можно установить с помощью переменной окружения `LANGFLOW_LOG_FILE`. По умолчанию `logs/langflow.log`.
- `--cache`: Выбирает тип кэша для использования. Варианты: `InMemoryCache` и `SQLiteCache`. Можно установить с помощью переменной окружения `LANGFLOW_LANGCHAIN_CACHE`. По умолчанию `SQLiteCache`.
- `--dev/--no-dev`: Переключает режим разработки. По умолчанию `no-dev`.
- `--path`: Указывает путь к каталогу фронтенда с файлами сборки. Эта опция предназначена только для разработки. Можно установить с помощью переменной окружения `LANGFLOW_FRONTEND_PATH`.
- `--open-browser/--no-open-browser`: Переключает опцию открытия браузера после запуска сервера. Можно установить с помощью переменной окружения `LANGFLOW_OPEN_BROWSER`. По умолчанию `open-browser`.
- `--remove-api-keys/--no-remove-api-keys`: Переключает опцию удаления ключей API из проектов, сохраненных в базе данных. Можно установить с помощью переменной окружения `LANGFLOW_REMOVE_API_KEYS`. По умолчанию `no-remove-api-keys`.
- `--install-completion [bash|zsh|fish|powershell|pwsh]`: Устанавливает завершение для указанной оболочки.
- `--show-completion [bash|zsh|fish|powershell|pwsh]`: Отображает завершение для указанной оболочки, позволяя скопировать его или настроить установку.
- `--backend-only`: Этот параметр, по умолчанию `False`, позволяет запускать только сервер backend без frontend. Можно также установить с помощью переменной окружения `LANGFLOW_BACKEND_ONLY`.
- `--store`: Этот параметр, по умолчанию `True`, включает функции хранилища, используйте `--no-store` для деактивации. Можно настроить с помощью переменной окружения `LANGFLOW_STORE`.

Эти параметры важны для пользователей, которым необходимо настраивать поведение Langflow, особенно в разработке или специализированных сценариях развертывания.

### Переменные окружения

Вы можете настроить многие из параметров CLI, используя переменные окружения. Их можно экспортировать в вашей операционной системе или добавить в файл `.env`, который будет загружен с помощью опции `--env-file`.

Пример файла `.env`, названного `.env.example`, включен в проекте. Скопируйте этот файл в новый файл с именем `.env` и замените примерные значения на ваши реальные настройки. Если вы устанавливаете значения как в вашей ОС, так и в файле `.env`, настройки из `.env` будут иметь приоритет.

# Деплоймент

## Разверните Langflow на платформе Google Cloud Platform.

Следуйте нашему пошаговому руководству для развертывания Langflow на платформе Google Cloud Platform (GCP) с использованием Google Cloud Shell. Руководство доступно в документе [**Langflow в Google Cloud Platform**](GCP_DEPLOYMENT.md).

В качестве альтернативы, нажмите кнопку **"Открыть в Cloud Shell"** ниже, чтобы запустить Google Cloud Shell, клонировать репозиторий Langflow и начать **интерактивное руководство**, которое проведет вас через процесс настройки необходимых ресурсов и развертывания Langflow в вашем проекте GCP.

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/langflow-ai/langflow&working_dir=scripts/gcp&shellonly=true&tutorial=walkthroughtutorial_spot.md)

## Разверните на Railway.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/JMXEWp?referralCode=MnPSdg)

## Разверните на Render.

<a href="https://render.com/deploy?repo=https://github.com/langflow-ai/langflow/tree/main">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render" />
</a>

# 👋 Внести вклад

Мы приветствуем вклад от разработчиков всех уровней в наш проект с открытым исходным кодом на GitHub. Если вы хотите внести свой вклад, пожалуйста, ознакомьтесь с нашими [руководствами по внесению вклада](./CONTRIBUTING.md) и помогите сделать Langflow более доступным.

---

[![Star History Chart](https://api.star-history.com/svg?repos=langflow-ai/langflow&type=Timeline)](https://star-history.com/#langflow-ai/langflow&Date)

# 🌟 Участники

[![langflow contributors](https://contrib.rocks/image?repo=langflow-ai/langflow)](https://github.com/langflow-ai/langflow/graphs/contributors)

# 📄 Лицензия

Langflow выпущен под лицензией MIT. Подробности можно найти в файле [LICENSE](LICENSE).

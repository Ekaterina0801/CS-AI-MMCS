# Шпаргалка · Git для второй лабораторной

<sub>[← Условие](README.md) · [Теория](THEORY.md)</sub>

## Путь изменения

```
сохранить в редакторе → git add → git commit → git push
     рабочая папка        индекс     история      GitHub
```

## Работа с веткой

```
git switch -c ветка → правка → add → commit → git switch main → git merge --no-ff ветка → git push
```

## Команды

| Задача | Команда |
|---|---|
| скачать свой пустой репозиторий | `git clone YOUR_REPO_URL cs-practice` |
| задать автора коммитов | `git config user.name "Имя"` · `git config user.email "почта"` |
| что изменилось | `git status` · короче: `git status --short` |
| что изменено, но не подготовлено | `git diff` |
| что уйдёт в коммит | `git diff --staged` |
| подготовить файл | `git add lab02/NOTES.md` |
| зафиксировать | `git commit -m "Что изменилось"` |
| история | `git log --oneline` · последние три: `git log --oneline -3` |
| назвать основную ветку `main` | `git branch -M main` (после первого коммита) |
| текущая ветка | `git branch --show-current` |
| создать ветку и перейти в неё | `git switch -c explain-branches` |
| список веток | `git branch` |
| вернуться в `main` | `git switch main` |
| слить ветку с коммитом слияния | `git merge --no-ff explain-branches` |
| история всех веток графом | `git log --oneline --graph --all` |
| удалить слитую ветку | `git branch -d explain-branches` |
| адреса удалённых репозиториев | `git remote -v` |
| первая отправка | `git push -u origin main` |
| следующие отправки | `git push` |
| полный SHA сдаваемой версии | `git rev-parse HEAD` |

## `git status --short`

| Вывод | Значит |
|---|---|
| `?? файл` | новый, не отслеживается — нужен `add` |
| `A  файл` | новый файл подготовлен |
| ` M файл` | изменён, не подготовлен — нужен `add` |
| `M  файл` | изменение подготовлено — можно коммитить |
| `MM файл` | после `add` изменили ещё раз — повторите `add` |
| пусто | всё зафиксировано |

## Хорошее сообщение коммита

| ✅ Так | ❌ Не так |
|---|---|
| `Describe local Git states` | `update` |
| `Explain Git and GitHub` | `фикс` |
| `List Git commands used` | `1`, `asdf`, `готово` |
| `Explain branches` | `ветка` |

Одно сообщение — одно законченное изменение. Сервис считает «update», «фикс» и подобное
неинформативными.

## Частые ошибки

| Симптом | Причина | Что сделать |
|---|---|---|
| `nothing added to commit` | забыли `git add` | подготовьте файл и повторите `commit` |
| в коммит не попала последняя правка | правили после `add` (`MM`) | снова `git add`, потом `commit` |
| `Please tell me who you are` | не задан автор | `git config user.name` и `user.email` |
| `fatal: not a git repository` | терминал открыт не в папке репозитория | `cd cs-practice` |
| `push` просит пароль и не принимает его | пароль аккаунта не подходит для Git | вход через браузер или токен |
| `rejected … fetch first` | на GitHub есть коммиты, которых нет у вас | обратитесь к преподавателю, **не** делайте `--force` |
| коммиты не видны на GitHub | не выполнили `push` | `git push origin main` |
| сервис не видит ваших коммитов | сделан `git init` внутри клона | работайте в клоне без `init` |
| `src refspec main does not match any` | ветка называется `master` | `git branch -M main`, затем `push` |
| «Репозиторий недоступен» в сервисе | репозиторий создан как Private | Settings → Change visibility → Public |
| в `main` нет правки из ветки | ветка ещё не слита | `git switch main`, затем `git merge --no-ff ветка` |
| после `merge` нет коммита слияния | Git сделал fast-forward | в следующий раз `--no-ff`; сейчас — ещё одна ветка с правкой и слияние с `--no-ff` |
| `switch` отказывается переключаться | есть незакоммиченные правки | закоммитьте их, затем переключайтесь |
| открылся экран с `:` и не выходит | просмотрщик `log` | нажмите `q` |

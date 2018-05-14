# Created by dmitry at 14.05.18
Feature: Страница поиска в youtube
  # Enter feature description here
  Поиск видео в youtube по слову Jenkins
  С сохранением описания видео в файл

  Scenario: Поиск видео
    Given Заходим на сайт "youtube.com"
    Then Находим поле для ввода информации
    And Вводим в поле для ввода информации "Jenkins"
    And Нажимаем кнопку поиска
    Then Переходим по ссылке на первое видео
    Then Извлекаем описание видео
    And Сохраняем описание видео в файл
    Then Делаем скриншот старницы видео
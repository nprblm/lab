# Lab_2
- Створив папку Lab2, додав туди README.md файл
- Інсталював pipenv  
- Встановив бібліотеку requests
- Створив файл app.py
- Перевірив чи програма працює(Так, працює)
- Встановив бібліотеку pytest
- Запустив тести та перевірив чи вони виконались успішно(Так, виконались)
- У програмі дописав функцію home_work яка перевіряє час доби AM/PM та відповідно друкує: Доброго дня/ночі
- Написав тест, який перевіряє правильність виконання функції home_work
- Перенаправив результат виконання тестів у файл results.txt а також додав результат виконання програми у кінець цього ж файлу. Зробив це за допомогою команд :   
     $ pipenv run pytest tests/tests.py > results.txt  
     $ pipenv run python app.py >> results.txt  
- Зробив коміт
- Заповнив Make файл та запустив його на лінуксі
# Lab_1
- клонував репозиторій: $ git clone https://github.com/nprblm/rep.git
- хеш:  
        $ git log  
        commit 4bfbf0f3d5df0cee05004a4996551a2b7eb9603f (HEAD -> main, origin/main)  
        Author: Vitalik Bella <vitalii.bella.itis.2018@lpnu.ua>  
        Date:   Tue Nov 3 18:37:10 2020 +0300  
    
    Add comments for lab_1  

- команди для комміту:  
        $ git status  
        $ git commit -a -m "Add comments for lab_1"  
        $ git push  
- Перейшов в гілку main:  
     $ git checkout main    
     В цій гілці не відображаються зміни інших гілок, бо це головна гілка репозиторію, а інша гілка є "копією"  
                  
- Переключився на нову гілку:  
    $ git checkout new-branch
    Switched to a new branch 'new-branch'
    $ git checkout new-branch  
    Switched to a new branch 'new-branch'    
- Чому виник конфлікт:  
    конфлікт виник через те що були 2 одинакові файли з різним текстом і щоб правильно їх об'єднати потрібно щоб весь текст в одному з файлів був наявний в іншому файлі(який з'єднуємо)  
    

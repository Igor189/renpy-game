# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nar = Character('Рассказчик', color="#008B8B", image='narrator')
define l = Character('Лиза', color="#ec88df", image='lisa')
define v = Character('Вася', color="#416c40", image='vasya')
define m = Character('Маша', color="#e1f540", image='masha')
define s= Character('Продавщица', color="#7a4a1e", image='seller')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
init:
    $ left2=Position(xalign=0.2, yalign=0.0)
    $ right2=Position(xalign=0.8, yalign=0.0)

label start:

    scene bg books

    show narrator normal

    nar '''Приветсвую дорогой игрок!

    Раз уж ты зашел в эту игру, то, наверное тебе интересно узнать, какую же историю я тебе расскажу.
    '''
    nar @ inquiringly "Тебе ведь правда интересно?"


    menu:
        "Да.":
            jump choise_1_yes
        "Нет.":
            jump choise_1_no

    label choise_1_yes:
        nar @ happy "Конечно да! А ради чего еще проходить подобные игры?"
        jump choise_1_done

    label choise_1_no:
        nar @ inquiringly "Нет?"
        nar @ angry "Я все равно позволю себе рассказать эту историю."
        jump choise_1_done
    label choise_1_done:
        nar "Чтож, история начинается 15 годами ранее..."
        hide narrator

        show bg room
        with fade

        "3 часа до прихода гостей"

        show masha happy at left2

        m "Наконец то приедет тетя из Хабаровска! {w}А с ней вся ее семья!"
        m "Вася! Лиза! {w}Мне нужна помощь, нельзя пускать гостей в такую квартиру."

        show lisa happy at right2 with moveinright

        l "Я тут!"
        l blush"Что нужно делать?"
        show lisa normal

        m surprised "Твоя задача... "
        m normal "Убраться в квартире."

        l happy "Поняла! {w}Ну я пошла."
        hide lisa with moveoutright

        show vasya angry at right2 with moveinright

        v "Слушаю."
        m worried "Опять ты не в настроении..."
        m "Тебе нужно сходить за хлебом."
        menu:
            "Хорошо.":
                jump choise_2_yes
            "Нет, у меня своих дел по горло.":
                jump choise_2_no

        label choise_2_yes:
            m @ happy "Наконец то ты хоть как то помогаешь семье!"
            jump choise_2_done

        label choise_2_no:
            scene bg books
            with fade

            show narrator normal

            nar "Вася остался дома, чтож, Ваш выбор."
            nar @ surprised "Как ни странно, в таком случае история заканчивается."
            nar "Чтож, Вы прошли игру."
            nar @ happy "Поздравляю!"
            nar "Возможно, чтобы найти другие концовки, Вам нужно попробовать пойти другим путем."
            nar @ happy "Удачи!"
            return
        label choise_2_done:
            scene bg store
            with dissolve

            show seller normal at left2
            show vasya normal at right2 with moveinright

            s "Добрый день! {w}Вам подсказать что нибудь?"
            v "Добрый! Буханку бородинского."

            scene bg books
            with fade

            show narrator normal

            nar "Вроде бы обыкновенная ситуация. Ничего не предвещало беды."
            nar @ happy "Но дальше начинается самое интересное."

            scene bg room
            with fade

            show vasya happy at right2

            v "Я вернулся!"

            show lisa2 at left2 with moveinleft

            l "П... {w}Папа?"

            m "Дочь! Кто там приешел?"

            hide lisa2 with moveoutleft
            show masha normal at left2 with moveinleft

            m angry "Это ты? {w}Где ты пропадал на протяжении 15 лет?"
            v surprised "15 лет???"
            m curious"Не прикидывайся дураком! {w}Мы кое как концы с концами сводили пока ты где то шлялся!"
            v angry "Хватит нести чушь! {w}Я по твоему велению в магазин пошел, прошло минут 20 от силы."
            v normal "Мы вообще готовы к приезду твоей тети?"
            m angry "Тетя умерла лет 10 назад! {w}Не смей ее упоминать, она тебя ждала в тот вечер!"
            m worried "Как и все мы."

            v angry "Я устал от этого бреда! Смотри."
            v normal "Вот смотри, в сегодяшней газете написано что сегодня..."
            v surprised "2037 год."
            v sad "Но... {w}Как такое вообще возможно?"

            scene bg books
            with fade

            show narrator normal
            nar "Действительно странное дело."
            nar inquiringly "Но как же наш герой воспримет эту информацию?"

            scene bg room
            with fade

            show vasya normal at right2
            show masha normal at left2

            m "Совсем из ума выжил!"
            m surprised "И как ты теперь представляешь нашу жизнь?"

            menu:
                "Это невыносимо! Подделывать даты, а ради чего? Я ухожу из этого дурдома, вернусь как осознаете свою ошибку.":
                    jump choise_3_yes
                "Я незнаю как это произошло, но нужно как то восстанавливать семью.":
                    jump choise_3_no

            label choise_3_yes:
                scene bg street
                with dissolve
                nar "Вася вышел из квартиры"
                nar "Рассерженный на всех, он стал переходить дорогу, по которой ездили машины..."
                show car with moveinleft
                hide car with moveoutright

                scene bg books
                with fade

                show narrator normal
                nar "Вот и еще один печальный конец истории."
                nar @ sad "К сожалению дочь будет расти без отца."
                nar "Как бы то ни было, Васи больше нет. {w}А значит вы нашли еще одну концовку!"
                nar @ happy "Поздравляю!"
                return

            label choise_3_no:
                m angry "Ты думаешь все так просто?"
                m worried "Лиза 15 лет жила без отца. {w}Ей было очень тяжело."
                v sad "Мне очень жаль."
                extend happy "Но я думаю, все еще можно исправить!"

                scene bg books
                with fade

                show narrator happy
                nar "Этот конец не такой уж и печальный."
                nar @ inquiringly "Не правда ли?."
                nar normal "В любом случае, не смотря на прошедшие годы, семья восстановилась."
                nar sad "Хотя это был отнюдь не самый простой путь."
                nar @ happy "Вот Вы дошли еще до одной концовки! {w}Поздравляю!"
                return


    return

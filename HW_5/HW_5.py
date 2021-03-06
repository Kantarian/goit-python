# Задача#
# Разбор строк -- это очень частая задача, которая возникает перед разработчиком в любой сфере и области разработки, Web DataScience, DataMining.
#
# В этом уроки вы научились работать со строками более глубоко, ознакомились с "малыми" методами и регулярными
# выражениями. Теперь у вас есть полный набор инструментов для обработки строк с помощью Python.
#
# Напишите функцию normalize, которая:
#
# Проводит транслитерацию кириллического алфавита на латинский.
# Заменяет все символы кроме латинских букв, цифр на '_'.
# Критерии приёма задания#
# Функция normalize:
#
# принимает на вход строку и возвращает строку;
# проводит транслитерацию кириллических символов на латиницу;
# заменяет все символы кроме букв латинского алфавита и цифр на символ '_';
# транслитерация может не соответствовать стандарту, но быть читабельной;
# большие буквы остаются большими, а меленькие -- маленькими после транслитерации.



def normalize(string):
    string = str(string)
    dictionary = {
        ord('а'): 'a',
        ord('б'): 'b',
        ord('в'): 'v',
        ord('г'): 'g',
        ord('д'): 'd',
        ord('е'): 'e',
        ord('ё'): 'yo',
        ord('ж'): 'zh',
        ord('з'): 'z',
        ord('и'): 'i',
        ord('й'): 'y',
        ord('к'): 'k',
        ord('л'): 'l',
        ord('м'): 'm',
        ord('н'): 'n',
        ord('о'): 'o',
        ord('п'): 'p',
        ord('р'): 'r',
        ord('с'): 's',
        ord('т'): 't',
        ord('у'): 'u',
        ord('ф'): 'f',
        ord('х'): 'h',
        ord('ц'): 'ts',
        ord('ч'): 'ch',
        ord('ш'): 'sh',
        ord('щ'): 'shch',
        ord('ъ'): 'y',
        ord('ы'): 'y',
        ord('ь'): "'",
        ord('э'): 'e',
        ord('ю'): 'yu',
        ord('я'): 'ya',

        ord('А'): 'A',
        ord('Б'): 'B',
        ord('В'): 'V',
        ord('Г'): 'G',
        ord('Д'): 'D',
        ord('Е'): 'E',
        ord('Ё'): 'Yo',
        ord('Ж'): 'Zh',
        ord('З'): 'Z',
        ord('И'): 'I',
        ord('Й'): 'Y',
        ord('К'): 'K',
        ord('Л'): 'L',
        ord('М'): 'M',
        ord('Н'): 'N',
        ord('О'): 'O',
        ord('П'): 'P',
        ord('Р'): 'R',
        ord('С'): 'S',
        ord('Т'): 'T',
        ord('У'): 'U',
        ord('Ф'): 'F',
        ord('Х'): 'H',
        ord('Ц'): 'Ts',
        ord('Ч'): 'Ch',
        ord('Ш'): 'Sh',
        ord('Щ'): 'Shch',
        ord('Ъ'): 'Y',
        ord('Ы'): 'Y',
        ord('Ь'): "'",
        ord('Э'): 'E',
        ord('Ю'): 'Yu',
        ord('Я'): 'Ya',
    }
    t_string = string.translate(dictionary)
    f_string = ''
    for st in t_string:

        if st.isalpha() or st.isnumeric() or st == "'":
            f_string = f_string + st
        else:
            st = '_'
            f_string = f_string + st
    print(f_string)
    return t_string


normalize('Привет как дела в 5 вечера? Что делаешь? asdf')


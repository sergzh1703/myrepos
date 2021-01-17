import os
from pathlib import Path
from shutil import copy
# my = os.getcwdb() #проверить текущий каталог ответ в байтах
# my_P = Path.cwd()  #проверить текущий каталог ответ строка
# print(my, type(my), my_P,type(my_P), sep = '\n')

#os.makedirs(r'/home/sergey/Test/test_os') #создать каталог и путь к нему если не существует
#print(os.path.exists(r'/home/sergey/Test/test_os'))
#Path(r'/home/sergey/Test_p/test_p').mkdir(parents=True, exist_ok=True) #создать каталог и путь к нему если не существует
#os.rmdir(r'/home/sergey/Test_p/test_p') #удалить каталог
#os.rmdir(r'/home/sergey/Test', )
#os.remove('tmp.txt') #удалить файл
#txt_files = list(Path('.').glob("*.py")) #список файлов в текущем каталоге
# txt_files = list(Path('/home/sergey').glob('t*')) #список файлов в директории
# print("Txt files:", txt_files)
# for file in txt_files:
#     if os.path.isfile(file):#проверка что это файл
#       os.remove(file)
#     if os.path.isdir(file):#проверка что это директория
#        os.rmdir(file)
#print(file.name) # Возвращает только имя файла без пути
#print("Txt files:", txt_files)
source_faile = list(Path('.').glob('Test_pathlib*'))
taget_file = r'/home/sergey/Git/myrepos/job_with_file.py'
taget_file_path = Path(taget_file)
print(taget_file_path.exists())
print(source_faile[0])
source = f'{Path.cwd()}/{source_faile[0].name}'
print(f'source:{source}',f'dest:{taget_file}',sep = '\n')
print(os.path.exists(source),os.path.exists(taget_file))
copy(source, taget_file)
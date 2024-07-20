class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname and password in self.users:
            self.current_user = (nickname, password)

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users.append(nickname)
            self.users.append(password)
            self.users.append(age)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        if args not in self.videos:
            self.videos.append(args)

    def get_videos(self, search):
        for i in self.videos:
            i.upper()
            if i.upper() in search.upper() or search.upper() in i.upper():
                return self.videos





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
a = ur.add(v1, v2)


# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
#ur.watch_video('Для чего девушкам парень программист?')
#ur.register('vasya_pupkin', 'lolkekcheburek', 13)
#ur.watch_video('Для чего девушкам парень программист?')
#ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
#ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
#ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
#print(ur.current_user)

# Попытка воспроизведения несуществующего видео
#ur.watch_video('Лучший язык программирования 2024 года!')









В workspace Personal Account есть 2 таргета - Supervisor (Стройнадзор) и Personal Account (Руководитель)

Для каждого таргета существует файл ServerType, в котором есть поля host и scheme. Файлы лежат в модулях PersonalAccountPersistent и SupervisorPersistent соответственно.

Чтобы сменить сервер, необходимо вписать в эти файлы релевантные host и scheme соответственно. Например, "https" - scheme, "google.ru" - host. 

В данный момент существует 2 типа конфигурации - Release и Debug, для каждого из них в вышеуказанных файлах существуют свои host и scheme. На данный момент лучше указывать один и тот же host и scheme для каждого типа конфигурации во избежание проблем с некорректными параметрами для текущей версии приложения. Например, 

private var host: String {
        switch self {
        case .debug:
            return "for-example.ru"
        case .release:
            return "for-example.ru"
        }
}

private var scheme: String {
        switch self {
        case .debug:
            return "https"
        case .release:
            return "https"
        }
    }

Чтобы собрать приложение, необходимо установить на макбук/мак приложение xCode. Также необходимо на уровне системы установить Cocoapods (https://guides.cocoapods.org/using/getting-started.html). После установки, в консоли необходимо перейти в папку проекта и ввести  команду "pod install", нажать enter. После завершения процесса установки, нужно открыть файл с расширением .xcworkspace в папке проекта. Затем кликнуть на какое-либо приложение (слева модули Supervisor и PersonalAccount) и в настройках general и signing & capabilities выставить соответствующие параметры (display name, app version, bundle identifier). Также нужно выбрать команду для подписи. После этого можно запустить приложение на подключенном устройстве, или через вкладку Product -> Archive начать подготовку архива для дальнейшей дистрибьюции. 
#send notification for testing

from plyer import notification

title = 'Hello Amazing people!'
message= 'Somshit virusreading! Take care!'


notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10000,
                    toast=False)

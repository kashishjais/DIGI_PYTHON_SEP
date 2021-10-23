
def setting_fun(filename='settings',**details):
    if details:
        with open('settings.abcd','w') as file:
            for k,v in details.items():
                file.write(f'{k} ->{v}\n')

setting_fun(color='blue',alpha=1,gamma=3,filename='color_setting.txt')




def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print('\nI have a ' + animal_type.title() + '.')
    print('It\'s name is '+pet_name.title()+'.')


describe_pet(pet_name='Tom', animal_type='cat')

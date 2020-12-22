def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print('\nI have a ' + animal_type.title() + '.')
    print('\nIt\'s name is '+pet_name.title()+'.')


describe_pet(animal_type='dog', pet_name='Tom')

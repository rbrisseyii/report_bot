from zipfile import ZipFile

color = './color.png'
outline = './outline.png'
manifest = './manifest.json'

if __name__ == '__main__':
    with ZipFile('Blackbaud CRM.zip', mode='w') as zip_obj:
        zip_obj.write(color)
        zip_obj.write(outline)
        zip_obj.write(manifest)

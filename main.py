from helpers import GiveMeImageFromUrl
from helpers import ClientPhotolab

# URL на jpeg файл
url_img = 'https://i1.7fon.org/1000/m586751.jpg'
api = ClientPhotolab()

foo = GiveMeImageFromUrl(url=url_img)
content_filename = foo.get_img_from_url()

content_url = api.image_upload(content_filename)
print(f'content_url: {content_url}')

for combo_id in [5635874]:
    original_content_url = content_url
    print('===')
    print('start process combo_id: {}'.format(combo_id))
    i = 0
    for step in api.photolab_steps_advanced(combo_id)['steps']:
        template_name = str(step['id'])
        contents = []
        for i in range(0, len(step['image_urls'])):
            image_url = step['image_urls'][i]
            if len(step['image_urls'][i]) == 0:
                image_url = original_content_url
            contents.append({
                'url': image_url,
                'rotate': 0,
                'flip': 0,
                'crop': '0,0,1,1'
            })
        if len(contents) == 0:
            contents.append({
                'url': original_content_url,
                'rotate': 0,
                'flip': 0,
                'crop': '0,0,1,1'
            })
        result_url = api.photolab_process(template_name, contents)
        i = i + 1
        if i != 0:
            original_content_url = result_url
        print('---for template_name: {}, result_url: {}'.format(template_name, result_url))

    print(f'result_url: {result_url}')
    bar = GiveMeImageFromUrl(result_url)
    bar.get_img_from_url_processed()

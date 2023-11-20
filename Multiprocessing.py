import concurrent.futures
import time

'''start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

    for result in results:
        print(result)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')'''

#Without Process
start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


secs = [5, 4, 3, 2, 1]
results = []
for sec in secs:
    results.append(do_something(sec))

for result in results:
    print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

#Run Image Parallel
'''import time,os
import concurrent.futures
from PIL import Image, ImageFilter
import logging

img_names = [
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1549692520-acc6669e2f0c.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1493976040374-85c8e12f0c0e.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1504198453319-5ce911bafcde.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1507143550189-fed454f93097.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1513938709626-033611b8cc03.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1516117172878-fd2c41f4a759.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1516972810927-80185027ca84.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1522364723953-452d3431c267.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1524429656589-6633a470097c.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1530224264768-7ff8c1789d79.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1532009324734-20a7a5813719.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1541698444083-023c97d3f4b6.jpg',
    r'C:\Users\balkrishna\Desktop\INTERNSHIP\Original\photo-1564135624576-c5c88640f235.jpg',

]

t1 = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    output_path = os.path.join('processed', os.path.basename(img_name))
    img.save(output_path)
    return f'{img_name} was processed...'
    #img.save(f'processed/{img_name}')
    #print(f'{img_name} was processed...')

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_image, img_names)
    for result in results:
        print(result)
    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds')'''

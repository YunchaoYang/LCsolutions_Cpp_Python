DICOM dataset,是DICOM文件的主要组成部分，其由DICOM数据元素按照指定的顺序排列。 
DataElement 数据元素最基本的数据单元是数据元，按照TAG从小到大顺序排列，即一个数据元表示一个TAG。TAG从小到大顺序排列
DataElement 主要由4个部分组成：
 - TAG号：由4个字节组成，包括2字节的组号和2字节的元素号（例如：0010 0040 表示患者性别，其中的组号：0002描述设备通讯信息、0008描述特征参数、0010描述患者信息、0028描述图像信息参数）。我们后期所需要的DICOM文件相关数据时，就是根据TAG来获取。
 - 值表示（VR，value representation）：由两个字节的字符组成，存储描述该项数据元信息的数据类型，包含例如：LO（Long String，长字符串）、IS（Interger String，整型字符串），DA（data，日期）等等共27种数据类型。
 - 值长度（value length）：存储描述该项信息的数据长度
 - 值域（value)：存储描述该项信息的数据值

 其中数据元信息可以根据信息的不同，分为4类：
 - Patient
    - Study
      - Series
        - Image

! [Patient tag](https://img-blog.csdnimg.cn/20200702220449443.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4MzMwMTQ4,size_16,color_FFFFFF,t_70)

! [Study tag](https://img-blog.csdnimg.cn/20200702220506227.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4MzMwMTQ4,size_16,color_FFFFFF,t_70)


```python
增删查改

ds = pydicom.dcmread("rtplan.dcm")
print(ds.patientName)
ds.PatientName = "ABC"
ds[0x0010,0x0010].value = "abc"
ds.saveas("newrtplan.dcm")
if("PatientName" in ds):
  print(ds.PatientName)

del ds.PatientName

ds.add_new(0x00100010, 'PN', 'a000')


ds.dir()  # 查看病人所有信息字典keys
############ 查看dicom对应图片值 #####################
print(ds.pixel_array.shape)  
print(ds.pixel_array)
##读取显示图片  
pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)  
pylab.show()  

##修改图片中的元素，不能直接使用data_array,需要转换成PixelData  
for n,val in enumerate(ds.pixel_array.flat): # example: zero anything < 300  
    if val < 300:  
        ds.pixel_array.flat[n]=0  
ds.PixelData = ds.pixel_array.tostring()  
ds.save_as('newfilename.dcm')  
```

### dicom文件预处理
首先需要导入我们需要的处理的dicom文件，dicom文件是一组连续的图片，我们根据图片中的位置信息对每张图片进行间隔计算，然后把结果存到一个列表中，然后将图片中的像素信息进行提取，缩放到1mm1mm1mm的尺度，get_cube_from_img这个函数是从图像中根据坐标找到目标的中心，并且切一个包含目标的矩阵，然后把这个三维的矩阵平铺开成一个64个2维的矩阵并保存。归一化的目的是为了加快模型收敛的速度，如果要保存成灰度图，需要像素值乘以255.

```python
def is_dicom_file(filename):
    '''
       判断某文件是否是dicom格式的文件
    :param filename: dicom文件的路径
    :return:
    '''
    file_stream = open(filename, 'rb')
    file_stream.seek(128)
    data = file_stream.read(4)
    file_stream.close()
    if data == b'DICM':
        return True
    return False


def load_patient(src_dir):
    '''
        读取某文件夹内的所有dicom文件
    :param src_dir: dicom文件夹路径
    :return: dicom list
    '''
    files = os.listdir(src_dir)
    slices = []
    for s in files:
        if is_dicom_file(src_dir + '/' + s):
            instance = dicom.read_file(src_dir + '/' + s)
            slices.append(instance)
    slices.sort(key=lambda x: int(x.InstanceNumber))
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness
    return slices


def get_pixels_hu_by_simpleitk(dicom_dir):
    '''
        读取某文件夹内的所有dicom文件,并提取像素值(-4000 ~ 4000)
    :param src_dir: dicom文件夹路径
    :return: image array
    '''
    reader = SimpleITK.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dicom_dir)
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    img_array = SimpleITK.GetArrayFromImage(image)
    img_array[img_array == -2000] = 0
    return img_array


def rescale_patient_images(images_zyx, org_spacing_xyz, target_voxel_mm, is_mask_image=False):
    '''
        将dicom图像缩放到1mm:1mm:1mm的尺度
        :param images_zyx: 缩放前的图像(3维)
        :return: 缩放后的图像(3维)
    '''

    print("Spacing: ", org_spacing_xyz)
    print("Shape: ", images_zyx.shape)

    # print "Resizing dim z"
    resize_x = 1.0
    resize_y = float(org_spacing_xyz[2]) / float(target_voxel_mm)
    interpolation = cv2.INTER_NEAREST if is_mask_image else cv2.INTER_LINEAR
    res = cv2.resize(images_zyx, dsize=None, fx=resize_x, fy=resize_y, interpolation=interpolation)
    # print "Shape is now : ", res.shape

    res = res.swapaxes(0, 2)
    res = res.swapaxes(0, 1)
    # print "Shape: ", res.shape
    resize_x = float(org_spacing_xyz[0]) / float(target_voxel_mm)
    resize_y = float(org_spacing_xyz[1]) / float(target_voxel_mm)

    # cv2 can handle max 512 channels..
    if res.shape[2] > 512:
        res = res.swapaxes(0, 2)
        res1 = res[:256]
        res2 = res[256:]
        res1 = res1.swapaxes(0, 2)
        res2 = res2.swapaxes(0, 2)
        res1 = cv2.resize(res1, dsize=None, fx=resize_x, fy=resize_y, interpolation=interpolation)
        res2 = cv2.resize(res2, dsize=None, fx=resize_x, fy=resize_y, interpolation=interpolation)
        res1 = res1.swapaxes(0, 2)
        res2 = res2.swapaxes(0, 2)
        res = np.vstack([res1, res2])
        res = res.swapaxes(0, 2)
    else:
        res = cv2.resize(res, dsize=None, fx=resize_x, fy=resize_y, interpolation=interpolation)

    res = res.swapaxes(0, 2)
    res = res.swapaxes(2, 1)

    print("Shape after: ", res.shape)
    return res


def get_cube_from_img(img3d, center_x, center_y, center_z, block_size):
    start_x = max(center_x - block_size / 2, 0)
    if start_x + block_size > img3d.shape[2]:
        start_x = img3d.shape[2] - block_size

    start_y = max(center_y - block_size / 2, 0)
    start_z = max(center_z - block_size / 2, 0)
    if start_z + block_size > img3d.shape[0]:
        start_z = img3d.shape[0] - block_size
    start_z = int(start_z)
    start_y = int(start_y)
    start_x = int(start_x)
    res = img3d[start_z:start_z + block_size, start_y:start_y + block_size, start_x:start_x + block_size]
    return res


def normalize_hu(image):
    '''
    将输入图像的像素值(-4000 ~ 4000)归一化到0~1之间
    :param image 输入的图像数组
    :return: 归一化处理后的图像数组
    '''
    MIN_BOUND = -1000.0
    MAX_BOUND = 400.0
    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image > 1] = 1.
    image[image < 0] = 0.
    return image


def load_patient_images(src_dir, wildcard="*.*", exclude_wildcards=[]):
    '''
    读取一个病例的所有png图像，返回值为一个三维图像数组
    :param image 输入的一系列png图像
    :return: 三维图像数组
    '''
    src_img_paths = glob.glob(src_dir + wildcard)
    for exclude_wildcard in exclude_wildcards:
        exclude_img_paths = glob.glob(src_dir + exclude_wildcard)
        src_img_paths = [im for im in src_img_paths if im not in exclude_img_paths]
    src_img_paths.sort()
    images = [cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) for img_path in src_img_paths]
    images = [im.reshape((1,) + im.shape) for im in images]
    res = np.vstack(images)
    return res


def save_cube_img(target_path, cube_img, rows, cols):
    '''
        将3维cube图像保存为2维图像,方便勘误检查
        :param 二维图像保存路径, 三维输入图像
        :return: 二维图像
    '''
    assert rows * cols == cube_img.shape[0]
    img_height = cube_img.shape[1]
    img_width = cube_img.shape[1]
    res_img = np.zeros((rows * img_height, cols * img_width), dtype=np.uint8)

    for row in range(rows):
        for col in range(cols):
            target_y = row * img_height
            target_x = col * img_width
            res_img[target_y:target_y + img_height, target_x:target_x + img_width] = cube_img[row * cols + col]

    cv2.imwrite(target_path, res_img)
if __name__ == '__main__':
    dicom_dir = './data/dicom_demo/'
    # 读取dicom文件的元数据(dicom tags)
    slices = load_patient(dicom_dir)
    # 获取dicom的spacing值
    pixel_spacing = slices[0].PixelSpacing
    pixel_spacing.append(slices[0].SliceThickness)
    print('The dicom spacing : ', pixel_spacing)
    # 提取dicom文件中的像素值
    image = get_pixels_hu_by_simpleitk(dicom_dir)
    # 标准化不同规格的图像尺寸, 统一将dicom图像缩放到1mm:1mm:1mm的尺度
    image = rescale_patient_images(image, pixel_spacing, 1.00)
    for i in tqdm(range(image.shape[0])):
        img_path = "./temp_dir/dcm_2_png/img_" + str(i).rjust(4, '0') + "_i.png"
        # 将像素值归一化到[0,1]区间
        org_img = normalize_hu(image[i])
        # 保存图像数组为灰度图(.png)
        cv2.imwrite(img_path, org_img * 255)

    # 加载上一步生成的png图像
    pngs = load_patient_images("./temp_dir/dcm_2_png/", "*_i.png")
    # 输入人工标记的结节位置: coord_x, coord_y, coord_z
    cube_img = get_cube_from_img(pngs, 272, 200, 134, 64)
    print(cube_img)
    save_cube_img('./temp_dir/chapter3_3dcnn_img_X.png', cube_img, 8, 8)
```


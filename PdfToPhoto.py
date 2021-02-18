import datetime
import os
import fitz  # fitz就是pip install PyMuPDF

def pdf_to_photo(pdfPath, imagePath):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.writePNG(imagePath + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


if __name__ == "__main__":
    # 1、PDF地址
    while True:
        pdfPath = input('请输入要转换的PDF地址：')#'E:\我的资源\手机文件\题库（营养学）.pdf'
        if not pdfPath:
            print('你还没输入PDF地址呢！')
        else:
            break
    # 2、需要储存图片的目录
    while True:
        imagePath =input('请输入要输出图片到那个地方')# 'E:\我的资源\Python\PythonFiles\项目\文字提取\图片'
        if not pdfPath:
            print('你还没填输出图片的地址呢！')
        else:
            break
    pdf_to_photo(pdfPath, imagePath)
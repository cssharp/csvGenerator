#coding:utf-8
import paramsDict
import json
import csv
import io
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class GenHelper:
    baseColumn = ['title','cid','seller_cids','stuff_status','location_state','location_city','item_type','price','auction_increment','num','valid_thru','freight_payer','post_fee','ems_fee','express_fee','has_invoice','has_warranty','approve_status','has_showcase','list_time','description','cateProps','postage_id','has_discount','modified','upload_fail_msg','picture_status','auction_point','picture','video','skuProps','inputPids','inputValues','outer_id','propAlias','auto_fill','num_id','local_cid','navigation_type','user_name','syncStatus','is_lighting_consigment','is_xinpin','foodparame','features','buyareatype','global_stock_type','global_stock_country','sub_stock_type','item_size','item_weight','sell_promise','custom_design_flag','wireless_desc','barcode','sku_barcode','newprepay','subtitle','cpv_memo','input_custom_cpv','qualification','add_qualification','o2o_bind_service','tmall_extend','product_combine','tmall_item_prop_combine','taoschema_extend']
    baseColumnZh = [u'宝贝名称',u'宝贝类目',u'店铺类目',u'新旧程度',u'省',u'城市',u'出售方式',u'宝贝价格',u'加价幅度',u'宝贝数量',u'有效期',u'运费承担',u'平邮',u'EMS',u'快递',u'发票',u'保修',u'放入仓库',u'橱窗推荐',u'开始时间',u'宝贝描述',u'宝贝属性',u'邮费模版ID',u'会员打折',u'修改时间',u'上传状态',u'图片状态',u'返点比例',u'新图片',u'视频',u'销售属性组合',u'用户输入ID串',u'用户输入名-值对',u'商家编码',u'销售属性别名',u'代充类型',u'数字ID',u'本地ID',u'宝贝分类',u'用户名称',u'宝贝状态',u'闪电发货',u'新品',u'食品专项',u'尺码库',u'采购地',u'库存类型',u'国家地区',u'库存计数',u'物流体积',u'物流重量',u'退换货承诺',u'定制工具',u'无线详情',u'商品条形码',u'sku',u'条形码',u'7天退货',u'宝贝卖点',u'属性值备注',u'自定义属性值',u'商品资质',u'增加商品资质',u'关联线下服务',u'tmall扩展字段',u'产品组合',u'tmall属性组合',u'taoschema扩展字段']
    def __init__(self, sourcePath, directPath):
        self.path = sourcePath
        self.directPath = directPath

    def genCsv(self):
        with open(self.path, 'r') as f:
            strx = f.read()
        j = json.loads(strx)
        self.csvValue = paramsDict.newbalance

        self.csvValue['title'] = j['name']
        self.csvValue['price'] = float( j['price'])*7+120
        self.csvValue['num'] = 10
        self.csvValue['list_time'] = '2017-8-15 10:00:01'
        self.csvValue['picture'] = j['itemUrl']
        self.csvValue['picture_status'] = ''
        self.csvValue['description'] = ''
        self.csvValue['cateProps'] = ''
        self.csvValue['skuProps'] = '' 
        self.csvValue['inputPids'] = ''
        self.csvValue['inputValues'] = ''
        self.csvValue['propAlias'] = ''
        self.csvValue['num_id'] = ''
        self.csvValue['features'] = ''
        self.csvValue['input_custom_cpv'] = ''
        value = [unicode(self.csvValue[t]) for t in self.baseColumn]

        with io.open(self.directPath, 'wb') as csvfile:
            spamwriter=csv.writer(csvfile,
 dialect='excel')
            spamwriter.writerow(['version 1.00'])
            spamwriter.writerow(self.baseColumn)
            spamwriter.writerow(self.baseColumnZh)
            spamwriter.writerow(value)


if __name__ == '__main__':
    g = GenHelper('./tmp/new-balance_460BK3.txt', 'cc.csv')
    g.genCsv()

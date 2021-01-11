from django.db import models


# Create your models here.

class RootModel(models.Model):

    class Meta:
        abstract = True

    def to_serialize(self):
        obj_dict = {}
        for key in self.__dict__:
            val = self.__dict__[key]
            if type(val) == int or type(val) == str:
                obj_dict[key] = val
        return obj_dict


class ServeModel(RootModel):
    # 服务网络地址
    serve_address = models.CharField(max_length=200)
    # 域名
    serve_domain = models.CharField(max_length=200)
    # 端口
    serve_port = models.IntegerField()
    # 服务的磁盘地址
    serve_path = models.CharField(max_length=1000)
    # 上次启动时间
    last_start_time = models.DateTimeField(blank=True, null=True)
    # 上次停止时间
    last_stop_time = models.DateTimeField(blank=True, null=True)
    # 上次操作人员
    last_opera_user = models.CharField(max_length=20, default='root')
    # 服务描述
    description = models.CharField(max_length=200)

    def __str__(self):
        return 'address:' + self.serve_address


class ServeLogModel(RootModel):
    serve = models.ForeignKey(ServeModel, on_delete=models.CASCADE)
    log_content = models.TextField()
    create_time = models.DateTimeField()


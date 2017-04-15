# -*- coding: utf-8 -*-
from collections import OrderedDict
from .common import KhipuService


class KhipuServicePaymentStatus(KhipuService):

    def __init__(self, receiver_id, secret, service_name, **kwargs):
        super(
            KhipuServicePaymentStatus, self).__init__(
                receiver_id, secret, service_name, **kwargs)
        self.data = {'receiver_id': receiver_id}
        self.data = OrderedDict([
            ('receiver_id', receiver_id),
            ('payment_id', kwargs.pop('payment_id')),       
        ])

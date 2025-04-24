import json
import requests

class Curie:
    def __init__(self, host):
        self._host = host
        self._s = requests.Session()

    @property
    def url_base(self):
        return f"http://{self._host}:5111/"
        
    @property
    def low_lo(self):
        r = self._s.get(self.url_base + "low_lo")

        return json.loads(r.text)['frequency']

    @low_lo.setter
    def low_lo(self, v):               
        r = self._s.get(self.url_base + "low_lo", params={'freq': v})

    @property
    def high_lo(self):
        r = self._s.get(self.url_base + "high_lo")

        return json.loads(r.text)['frequency']

    @high_lo.setter
    def high_lo(self, v):               
        r = self._s.get(self.url_base + "high_lo", params={'freq': v})

    @property
    def gains(self):
        r = self._s.get(self.url_base + "gain")

        return json.loads(r.text)
        
    def set_gain(self, trx, chan, g):
        r = self._s.get(self.url_base + "gain",
                        params={'trx': trx, 'chan': chan, 'v': g })

    @property
    def biases(self):
        r = self._s.get(self.url_base + "bias")
        
        return json.loads(r.text)

    def set_bias(self, chan, iq, bias):
        r = self._s.get(self.url_base + "bias",
                        params={'iq': iq, 'chan': chan, 'v': bias })
    
    @property
    def rx0_gain(self):
        return self.gains['rx']['0']

    @rx0_gain.setter
    def rx0_gain(self, v):
        self.set_gain('rx', '0', v)

    @property
    def rx1_gain(self):
        return self.gains['rx']['1']

    @rx1_gain.setter
    def rx1_gain(self, v):
        self.set_gain('rx', '1', v)
        
    @property
    def tx0_gain(self):
        return self.gains['tx']['0']

    @tx0_gain.setter
    def tx0_gain(self, v):
        self.set_gain('tx', '0', v)

    @property
    def tx1_gain(self):
        return self.gains['tx']['1']

    @tx1_gain.setter
    def tx1_gain(self, v):
        self.set_gain('tx', '1', v)


    @property
    def I0_bias(self):
        return self.biases['0']['I']

    @I0_bias.setter
    def I0_bias(self, v):
        self.set_bias('0', 'I', v)

    @property
    def I1_bias(self):
        return self.biases['1']['I']

    @I1_bias.setter
    def I1_bias(self, v):
        self.set_bias('1', 'I', v)
        
    @property
    def Q0_bias(self):
        return self.biases['0']['Q']
    
    @Q0_bias.setter
    def Q0_bias(self, v):
        self.set_bias('0', 'Q', v)

    @property
    def Q1_bias(self):
        return self.biases['1']['Q']

    @Q1_bias.setter
    def Q1_bias(self, v):
        self.set_bias('1', 'Q', v)

        

#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class Login(object):
    
    g_onKickedFromServer = EventHook()
    
    g_receiveLoginQueueNumber = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._accountDBID_s = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (10000000000, 'accountDBID_s'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (32, 'onKickedFromServer'),
            (64, 'receiveLoginQueueNumber'),
            
        ])
        # sort methods by size
        self._methods.sort(key=itemgetter(0))
        return

    @property
    def attributesMap(self):
        d = {}
        for i, (_, name) in enumerate(self._properties):
            d[i] = name
        return d

    @property
    def methodsMap(self):
        d = {}
        for i, (_, name) in enumerate(self._methods):
            d[i] = name
        return d

    ####################################
    #      METHODS
    ####################################


    # method size: 32
    @unpack_func_args(['INT32'])
    def onKickedFromServer(self, arg1):
        self.g_onKickedFromServer.fire(self, arg1)

    # method size: 64
    @unpack_func_args(['UINT64'])
    def receiveLoginQueueNumber(self, arg1):
        self.g_receiveLoginQueueNumber.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    # property size: 10000000000
    @property
    def accountDBID_s(self):
        return self._accountDBID_s

    @accountDBID_s.setter
    def accountDBID_s(self, value):
        self._accountDBID_s, = unpack_variables(value, ['STRING'])


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)
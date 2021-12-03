# coding:utf-8
from LxBasic import bscObjItf, bscMethods

from . import grhObjItf


class AbsGrhObjStack(bscObjItf.ItfBscObjStack):
    def _initAbsGrhObjStack(self, *args):
        self._initItfBscObjStack(*args)


class AbsGrhObjStackSite(grhObjItf.ItfGrhObjStackSite):
    def _initAbsGrhObjStackSite(self, *args):
        self._initItfGrhVariantObjStack(*args)


# object scene ******************************************************************************************************* #
class AbsGrhObjSceneLoader(grhObjItf.ItfGrhObjSceneLoader):
    def _initAbsGrhObjScene(self, *args, **kwargs):
        self._initItfGrhObjScene(*args, **kwargs)


# object loader ****************************************************************************************************** #
class AbsGrhObjLoader(grhObjItf.ItfGrhObjLoader):
    def _initAbsGrhObjLoader(self, *args):
        self._initItfGrhObjLoader(*args)


# object queryraw **************************************************************************************************** #
class AbsGrhPortQueryraw(grhObjItf.ItfGrhPortQueryraw):
    def _initAbsGrhPortQueryraw(self, *args):
        self._initItfGrhPortQueryraw(*args)


class AbsGrhNodeQueryraw(grhObjItf.ItfGrhNodeQueryraw):
    def _initAbsGrhNodeQueryraw(self, *args):
        self._initItfGrhNodeQueryraw(*args)


class AbsGrhObjQueryrawCreator(grhObjItf.ItfGrhObjQueryrawCreator):
    def _initAbsGrhObjQueryBuilder(self, *args):
        self._initItfGrhObjQueryrawCreator(*args)


# object query ******************************************************************************************************* #
class AbsGrhPortQuery(grhObjItf.ItfGrhPortQuery):
    def _initAbsGrhPortQuery(self, *args):
        self._initItfGrhPortQuery(*args)


class AbsGrhNodeQuery(grhObjItf.ItfGrhNodeQuery):
    def _initAbsGrhNodeQuery(self, *args):
        self._initItfGrhNodeQuery(*args)


class AbsGrhObjQueryBuilder(grhObjItf.ItfGrhObjQueryBuilder):
    def _initAbsGrhObjQueryBuilder(self, *args):
        self._initItfGrhObjQueryBuilder(*args)


# translator object query cache ************************************************************************************** #
class AbsGrhTrsObjLoader(grhObjItf.ItfGrhTrsObjLoader):
    def _initAbsGrhTrsObjLoader(self, *args):
        self._initItfGrhTrsObjLoader(*args)


# translator object query cache ************************************************************************************** #
class AbsGrhTrsPortQueryraw(grhObjItf.ItfGrhTrsPortQueryraw):
    def _initAbsGrhTrsPortQueryraw(self, *args):
        self._initItfGrhPortQueryraw(*args)


class AbsGrhTrsNodeQueryraw(grhObjItf.ItfGrhTrsNodeQueryraw):
    def _initAbsGrhTrsNodeQueryraw(self, *args):
        self._initItfGrhTrsNodeQueryraw(*args)


class AbsGrhTrsObjQueryrawCreator(grhObjItf.ItfGrhTrsObjQueryrawCreator):
    def _initAbsGrhTrsObjQueryrawCreator(self, *args):
        self._initItfGrhTrsObjQueryBuilder(*args)


# translator object query ******************************************************************************************** #
class AbsGrhTrsPortQuery(grhObjItf.ItfGrhTrsPortQuery):
    def _initAbsGrhTrsPortQuery(self, *args):
        self._initItfGrhTrsPortQuery(*args)


class AbsGrhTrsNodeQuery(grhObjItf.ItfGrhTrsNodeQuery):
    def _initAbsGrhTrsNodeQuery(self, *args):
        self._initItfGrhTrsNodeQuery(*args)


class AbsGrhTrsObjQueryBuilder(grhObjItf.ItfGrhTrsObjQueryBuilder):
    def _initAbsGrhTrsObjQueryBuilder(self, *args):
        self._initItfGrhTrsObjQueryBuilder(*args)


# cache ************************************************************************************************************** #
class AbsGrhObjQueue(grhObjItf.ItfGrhObjQueue):
    def _initAbsGrhObjQueue(self, *args):
        self._initItfGrhObjQueue(*args)


# object ************************************************************************************************************* #
class AbsGrhPort(grhObjItf.ItfGrhPort):
    def _initAbsGrhPort(self, *args, **kwargs):
        self._initItfGrhPort(*args, **kwargs)

    # **************************************************************************************************************** #
    def _obj__set_parent_build_(self, *args):
        objpathStr = args[0]
        self._parentPathStr = objpathStr

    def _obj__set_children_build_(self, *args):
        portpathStrList = args[0]
        self._childPathStrList = portpathStrList

    # **************************************************************************************************************** #
    def _obj__get_parent_exist_(self, *args):
        if args:
            if isinstance(args[0], self.__class__):
                portObject = args[0]
                return portObject.portpathString() == self._parentPathStr
            elif isinstance(args[0], (str, unicode)):
                portpathString = args[0]
                return portpathString == self._parentPathStr
        return self._parentPathStr is not None

    def _obj__get_parent_obj_(self):
        if self._obj__get_parent_exist_() is True:
            return self.node().port(
                self._parentPathStr,
                self.assignString()
            )

    def _obj__get_child_obj_list_(self, *args, **kwargs):
        return [
            self._obj__get_child_obj_(i)
            for i in self._childPathStrList
        ]

    def _obj__get_child_exist_(self, *args):
        if args:
            portpathString = args[0]
            return portpathString in self._childPathStrList
        return self._obj__get_parent_exist_()

    def _obj__get_child_obj_(self, *args):
        if self.hasChildren():
            if isinstance(args[0], (str, unicode)):
                portpathString = args[0]
                return self.node().port(portpathString, self.assignString())
            elif isinstance(args[0], (int, float)):
                return self.node().port(self._childPathStrList[int(args[0])], self.assignString())

    def _obj__get_children_exist_(self):
        return self._childPathStrList != []

    # **************************************************************************************************************** #
    @classmethod
    def _get_attrpath_str_(cls, *args):
        return cls.CLS_grh__obj__path(*args).toString()


class AbsGrhNode(grhObjItf.ItfGrhNode):
    def _initAbsGrhNode(self, *args, **kwargs):
        self._initItfGrhNode(*args, **kwargs)


# connector ********************************************************************************************************** #
class AbsGrhConnector(grhObjItf.ItfGrhConnector):
    def _initAbsGrhConnector(self, *args):
        self._initItfGrhConnector(*args)


# geometry assign **************************************************************************************************** #
class AbsGrhGeometryAssign(grhObjItf.ItfGrhGeometryAssign):
    def _initAbsGrhGeometryAssign(self, *args, **kwargs):
        self._initItfGrhGeometryAssign(*args, **kwargs)


# object proxy ******************************************************************************************************* #
class AbsGrhPortProxy(grhObjItf.ItfGrhPortProxy):
    def _initAbsGrhPortProxy(self, *args, **kwargs):
        self._initItfGrhPortProxy(*args, **kwargs)


class AbsGrhNodeProxy(grhObjItf.ItfGrhNodeProxy):
    def _initAbsGrhNodeProxy(self, *args, **kwargs):
        self._initItfGrhNodeProxy(*args, **kwargs)


class AbsGrhShaderProxy(grhObjItf.ItfGrhNodeProxy):
    def _initAbsGrhShaderProxy(self, *args, **kwargs):
        self._initItfGrhNodeProxy(*args, **kwargs)

    # **************************************************************************************************************** #
    def inputMaterialNamespaceString(self):
        return self._obj_proxy_cls__get_connect_obj_proxy_namespace_str_(self)

    # **************************************************************************************************************** #
    def _shader_proxy__get_material_context_(self):
        for portObj in self._bindObj.otports():
            if portObj.hasTargets():
                targetPortObjs = portObj.targets()
                for targetPortObj in targetPortObjs:
                    targetNodeObj = targetPortObj.node()
                    materialNamespaceStr = self.inputMaterialNamespaceString()
                    if targetNodeObj.hasProxy(materialNamespaceStr) is True:
                        return targetPortObj.portnameString()

    def _shader_proxy__get_material_node_proxy_(self):
        for portObj in self._bindObj.otports():
            if portObj.hasTargets():
                targetPortObjs = portObj.targets()
                for targetPortObj in targetPortObjs:
                    targetNodeObj = targetPortObj.node()
                    materialNamespaceStr = self.inputMaterialNamespaceString()
                    if targetNodeObj.hasProxy(materialNamespaceStr) is True:
                        return targetNodeObj.proxy(materialNamespaceStr)


class AbsGrhMaterialProxy(grhObjItf.ItfGrhNodeProxy):
    VAR_grh_material_proxy__surface_shader_port_str = None
    VAR_grh_material_proxy__displacement_shader_port_str = None
    VAR_grh_material_proxy__volume_port_str = None

    def _initAbsGrhMaterialProxy(self, *args, **kwargs):
        self._initItfGrhNodeProxy(*args, **kwargs)

    # **************************************************************************************************************** #
    def _material_proxy_cls__set_shader_connect(self, *args):
        materialShaderInportObj, _ = args
        connectNamespaceStr = self.connectNamespaceString()
        if isinstance(_, AbsGrhPort):
            shaderNodeObj = _.node()
            shaderOtportObj = _
            shaderNodeProxyObj = shaderNodeObj.proxy(connectNamespaceStr)
        elif isinstance(_, AbsGrhNode):
            shaderNodeObj = _
            shaderOtportObj = shaderNodeObj.otport()
            shaderNodeProxyObj = shaderNodeObj.proxy(connectNamespaceStr)
        elif isinstance(_, AbsGrhShaderProxy):
            shaderNodeProxyObj = _
            shaderOtportObj = shaderNodeProxyObj.bindObject().otport()
        else:
            raise TypeError()
        # set namespace
        if shaderNodeProxyObj.namespace().isRoot() is True:
            shaderNodeProxyObj.setNamespaceString(connectNamespaceStr)
        # connect
        shaderOtportObj.connectTo(materialShaderInportObj)

    def _material_proxy_cls__set_shader_proxy_connect(self, *args):
        materialShaderInportObj, shaderNodeProxyObj = args
        connectNamespaceStr = self.connectNamespaceString()
        shaderOtportObj = shaderNodeProxyObj.bindObject().otport()
        # set namespace
        # 1.check has namespace
        if shaderNodeProxyObj.namespace().isRoot() is True:
            shaderNodeProxyObj.setNamespaceString(connectNamespaceStr)
        # connect
        shaderOtportObj.connectTo(materialShaderInportObj)

    # **************************************************************************************************************** #
    def bindSurfaceInport(self):
        return self._bindObj.inport(
            self.VAR_grh_material_proxy__surface_shader_port_str
        )

    def connectSurfaceShaderFrom(self, *args):
        self._material_proxy_cls__set_shader_connect(
            self.bindSurfaceInport(),
            *args
        )

    def connectSurfaceShaderProxyFrom(self, *args):
        self._material_proxy_cls__set_shader_proxy_connect(
            self.bindSurfaceInport(),
            *args
        )

    def surfaceShader(self):
        if self.bindSurfaceInport().hasSource():
            connectNamespaceStr = self.connectNamespaceString()
            shaderProxyObj = self.bindSurfaceInport().source().node().proxy(connectNamespaceStr)
            if shaderProxyObj:
                return shaderProxyObj
            else:
                bscMethods.PyMessage.traceWarning(
                    'Not available Material Surface Shader: nodepath="{}"'.format(
                        self.pathString()
                    )
                )

    # **************************************************************************************************************** #
    def bindDisplacementInport(self):
        return self._bindObj.inport(
            self.VAR_grh_material_proxy__displacement_shader_port_str
        )

    def connectDisplacementShaderFrom(self, *args):
        self._material_proxy_cls__set_shader_connect(
            self.bindDisplacementInport(),
            *args
        )

    def connectDisplacementShaderProxyFrom(self, *args):
        self._material_proxy_cls__set_shader_proxy_connect(
            self.bindDisplacementInport(),
            *args
        )

    def displacementShader(self):
        if self.bindDisplacementInport().hasSource():
            connectNamespaceStr = self.connectNamespaceString()
            return self.bindDisplacementInport().source().node().proxy(connectNamespaceStr)

    # **************************************************************************************************************** #
    def bindVolumeInport(self):
        return self._bindObj.inport(
            self.VAR_grh_material_proxy__volume_port_str
        )

    def connectVolumeShaderFrom(self, *args):
        self._material_proxy_cls__set_shader_connect(
            self.bindDisplacementInport(),
            *args
        )

    def connectVolumeShaderProxyFrom(self, *args):
        self._material_proxy_cls__set_shader_proxy_connect(
            self.bindDisplacementInport(),
            *args
        )

    def volumeShader(self):
        if self.bindVolumeInport().hasSource():
            connectNamespaceStr = self.connectNamespaceString()
            return self.bindVolumeInport().source().node().proxy(connectNamespaceStr)

    # **************************************************************************************************************** #
    def shaders(self):
        return bscMethods.List.cleanupTo(
            [self.surfaceShader(), self.displacementShader(), self.volumeShader()]
        )

    # **************************************************************************************************************** #
    def materialOtport(self):
        return self.bindOtport(u'material')


class AbsGrhGeometryProxy(grhObjItf.ItfGrhNodeProxy):
    def _initAbsGrhGeometryProxy(self, *args, **kwargs):
        self._initItfGrhNodeProxy(*args, **kwargs)

        self._portsetStackObj = self.CLS_grh__node_proxy__portset_stack(self)

    # **************************************************************************************************************** #
    def inputMaterialNamespaceString(self):
        return self._obj_proxy_cls__get_connect_obj_proxy_namespace_str_(self)

    # **************************************************************************************************************** #
    def property(self, *args):
        return self.bindPortProxy(*args)

    def hasProperty(self, *args):
        return self.hasBindPortProxy(*args)

    def properties(self):
        return [
            i
            for i in self.bindPortProxies()
            if i.bindObject().assignString() == self.DEF_grh__keyword__property
        ]

    def changedProperties(self):
        lis = []
        for portProxyObj in self.properties():
            portObj = portProxyObj.bindObject()
            if portObj.isChanged():
                lis.append(portProxyObj)
        return lis

    # **************************************************************************************************************** #
    def visibility(self, *args):
        return self.bindPortProxy(*args)

    def hasVisibility(self, *args):
        return self.hasBindPortProxy(*args)

    def visibilities(self):
        return [
            i
            for i in self.bindPortProxies()
            if i.bindObject().assignString() == self.DEF_grh__keyword__visibility
        ]

    def changedVisibilities(self):
        lis = []
        for i in self.visibilities():
            portObj = i.bindObject()
            if portObj.isChanged():
                lis.append(i)
        return lis

    # **************************************************************************************************************** #
    def materialInport(self):
        return self.bindInport(u'material')

    # **************************************************************************************************************** #
    def materialAsport(self):
        return self.bindAsport(u'materialassign')

    def hasAssignmentMaterials(self):
        return self.materialAsport().hasAssignmentNodes()

    def assignmentMaterials(self):
        return self.materialAsport().assignmentNodes()

    def assignmentMaterialProxies(self):
        namespaceStr = self.connectNamespaceString()
        return [i.proxy(namespaceStr) for i in self.assignmentMaterials() if i.hasProxy(namespaceStr)]

    # **************************************************************************************************************** #
    def _node_proxy__set_input_node_connect_(self, *args):
        geometryProxyObj, materialProxyObj = self, args[0]
        sourceObj, targetObj = materialProxyObj.materialOtport(), geometryProxyObj.materialInport()
        sourceObj.connectTo(targetObj)

    def _node_proxy__set_assignment_node_add_(self, *args):
        geometryProxyObj, materialProxyObj = self, args[0]
        # geometryProxyObj.materialAsport().restoreAssignment()
        geometryProxyObj.materialAsport().addAssignmentNode(materialProxyObj.bindObject())

    # **************************************************************************************************************** #
    def _geometry_proxy__set_propertyset_update_(self, *args):
        if self._portsetStackObj._obj_stack__get_obj_exist_(*args) is True:
            portsetObj = self._portsetStackObj._obj_stack__get_obj_(*args)
            portsetObj.restore()
        else:
            portsetObj = self.CLS_grh__node_proxy__portset(*args)
            self._portsetStackObj._obj_stack__set_obj_add_(portsetObj)

        portProxyObjList = self.changedProperties()
        if portProxyObjList:
            for portProxyObj in portProxyObjList:
                portsetObj.addPort(portProxyObj)

        return portsetObj

    def setPropertyset(self, portsetObj):
        if self._portsetStackObj._obj_stack__get_obj_exist_(portsetObj) is False:
            self._portsetStackObj._obj_stack__set_obj_add_(portsetObj)

    def propertyset(self, *args):
        return self._portsetStackObj._obj_stack__get_obj_(*args)


# node graph ********************************************************************************************************* #
class AbsGrhNodeGraph(grhObjItf.ItfGrhNodeGraph):
    def _initAbsGrhNodeGraph(self, *args, **kwargs):
        self._initItfGrhNodeGraph(*args, **kwargs)


class AbsGrhNodeGraphPortProxy(grhObjItf.ItfGrhNodeGraphPortProxy):
    def _initAbsGrhNodeGraphPortProxy(self, *args, **kwargs):
        self._initAbsItfNodeGraphOtportProxy(*args, **kwargs)


# node translate ***************************************************************************************************** #
class AbsGrhObjTranslator(grhObjItf.ItfGrhObjTranslator):
    def _initAbsGrhObjTranslator(self, *args):
        self._initItfGrhObjTranslator(*args)


class AbsGrhTrsNode(grhObjItf.ItfGrhTrsNode):
    def _initAbsGrhTrsNode(self, *args):
        self._initItfGrhTrsNode(*args)


# node proxy translate *********************************************************************************************** #
class AbsGrhTrsNodeProxy(grhObjItf.ItfGrhTrsNodeProxy):
    def _initAbsGrhTrsNodeProxy(self, *args, **kwargs):
        self._initItfGrhTrsNodeProxy(*args, **kwargs)


class AbsGrhTrsShaderProxy(grhObjItf.ItfGrhTrsNodeProxy):
    def _initAbsGrhTrsShaderProxy(self, *args, **kwargs):
        self._initItfGrhTrsNodeProxy(*args, **kwargs)

        self._trs_shader_proxy__set_nodes_()

    # **************************************************************************************************************** #
    def _trs_shader_proxy__set_nodes_(self):
        srcNodeObjs = self._srcNodeObj.allInputNodes()
        for srcNodeObj in srcNodeObjs:
            cvtNodeTypepathStr = self.CLS_grh__trs_node_proxy__trs_node.getCvtNodeTypepathString(srcNodeObj)
            if self.CLS_grh__trs_node_proxy__trs_node.IST_grh__trs_node__obj_query_builder.hasCvtNodeTypepath(cvtNodeTypepathStr):
                srcNodePathStr = srcNodeObj.pathString()
                _trsNodeObject = self._grh__trs_node_proxy__get_trs_node_cache_obj_(srcNodePathStr)
            else:
                if cvtNodeTypepathStr not in self.VAR_grh__trs_node_proxy__except_src_node_typepath_list:
                    bscMethods.PyMessage.traceError(
                        u'''Unregistered Source Node Type: typepath="{}".'''.format(
                            cvtNodeTypepathStr
                        )
                    )


class AbsGrhTrsMaterialProxy(grhObjItf.ItfGrhTrsNodeProxy):
    CLS_grh__trs_input_node_proxy = None

    VAR_grh__trs_material_proxy_surface_shader_portpath = None
    VAR_grh__trs_material_proxy_displacement_shader_portpath = None
    VAR_grh__trs_material_proxy_volume_shader_portpath = None

    def _initAbsGrhTrsMaterialProxy(self, *args, **kwargs):
        self._initItfGrhTrsNodeProxy(*args, **kwargs)

        self._grh__trs_material_proxy__set_shaders_()

    # **************************************************************************************************************** #
    def _grh__trs_material_proxy__get_shader_(self, *args):
        srcPortObj = args[0]
        if srcPortObj.hasSource():
            _srcMaterialPortpathStr = srcPortObj.portpathString()
            _srcShaderObj = srcPortObj.source().node()
            #
            _srcShaderTypepathStr = _srcShaderObj.typepathString()
            _srcShaderNodepathStr = _srcShaderObj.pathString()
            if self.getSrcNodeTypeExists(_srcShaderTypepathStr):
                return _srcMaterialPortpathStr, _srcShaderNodepathStr
            else:
                if _srcShaderTypepathStr not in self.VAR_grh__trs_node_proxy__except_src_node_typepath_list:
                    bscMethods.PyMessage.traceError(
                        u'''Unregistered Source Shader Type: typepath="{}"; nodepath="{}".'''.format(
                            _srcShaderTypepathStr,
                            _srcShaderNodepathStr,
                        )
                    )

    def _grh__trs_material_proxy__set_shaders_(self):
        def get_shader_fnc(portpathRaw_):
            if isinstance(portpathRaw_, (str, unicode)):
                _srcMaterialPortpathStr = portpathRaw_
                _srcMaterialPortObj = self._srcNodeObj.inport(_srcMaterialPortpathStr)
                return self._grh__trs_material_proxy__get_shader_(_srcMaterialPortObj)
            elif isinstance(portpathRaw_, (tuple, list)):
                _srcMaterialPortObjs = [self._srcNodeObj.inport(_i) for _i in portpathRaw_ if self._srcNodeObj.hasInport(_i)]
                _srcMainMaterialPortpathStr, _srcSubMaterialPortpathStr = portpathRaw_
                _srcMainMaterialPortObj, _srcSubMaterialPortObj = (
                    self._srcNodeObj.inport(_srcMainMaterialPortpathStr),
                    self._srcNodeObj.inport(_srcSubMaterialPortpathStr)
                )
                if _srcMainMaterialPortObj.hasSource():
                    return self._grh__trs_material_proxy__get_shader_(_srcMainMaterialPortObj)
                elif _srcSubMaterialPortObj.hasSource():
                    return self._grh__trs_material_proxy__get_shader_(_srcSubMaterialPortObj)

        tgtMaterialProxyObj = self.tgtNodeProxy()

        surfaceShaderPortpath = self.VAR_grh__trs_material_proxy_surface_shader_portpath
        _ = get_shader_fnc(surfaceShaderPortpath)
        if _ is not None:
            srcMaterialPortpathStr, srcShaderNodepathStr = _
            connectNamespaceStr = tgtMaterialProxyObj.connectNamespaceString()
            # proxy object
            trsShaderProxyObj = self.CLS_grh__trs_input_node_proxy(
                srcShaderNodepathStr,
                namespace=connectNamespaceStr
            )
            tgtShaderProxyObj = trsShaderProxyObj.tgtNodeProxy()
            self.tgtNodeProxy().connectSurfaceShaderProxyFrom(tgtShaderProxyObj)

        displacementShaderPortpath = self.VAR_grh__trs_material_proxy_displacement_shader_portpath
        _ = get_shader_fnc(displacementShaderPortpath)
        if _ is not None:
            srcMaterialPortpathStr, srcShaderNodepathStr = _
            connectNamespaceStr = tgtMaterialProxyObj.connectNamespaceString()
            # proxy object
            trsShaderProxyObj = self.CLS_grh__trs_input_node_proxy(
                srcShaderNodepathStr,
                namespace=connectNamespaceStr
            )
            tgtShaderProxyObj = trsShaderProxyObj.tgtNodeProxy()
            self.tgtNodeProxy().connectDisplacementShaderProxyFrom(tgtShaderProxyObj)

        volumeShaderPortpath = self.VAR_grh__trs_material_proxy_volume_shader_portpath
        _ = get_shader_fnc(volumeShaderPortpath)
        if _ is not None:
            srcMaterialPortpathStr, srcShaderNodepathStr = _
            connectNamespaceStr = tgtMaterialProxyObj.connectNamespaceString()
            # proxy object
            trsShaderProxyObj = self.CLS_grh__trs_input_node_proxy(
                srcShaderNodepathStr,
                namespace=connectNamespaceStr
            )
            tgtShaderProxyObj = trsShaderProxyObj.tgtNodeProxy()
            self.tgtNodeProxy().connectVolumeShaderProxyFrom(tgtShaderProxyObj)


class AbsGrhTrsGeometryProxy(grhObjItf.ItfGrhTrsNodeProxy):
    CLS_grh__trs_input_node_proxy = None

    VAR_grh__trs_src_material_portpath = None

    def _initAbsGrhTrsGeometryProxy(self, *args, **kwargs):
        self._initItfGrhTrsNodeProxy(*args, **kwargs)

        self._trs_geometry_proxy__set_materials_()
        self._trs_geometry_proxy__set_ports_()

    # **************************************************************************************************************** #
    def _trs_geometry_proxy__get_src_material_obj_list_(self):
        pass

    def _trs_geometry_proxy__get_src_port_obj_list_(self):
        pass

    # **************************************************************************************************************** #
    def _trs_geometry_proxy__set_materials_(self):
        tgtGeometryProxyObj = self.tgtNodeProxy()
        srcMaterialObjs = self._trs_geometry_proxy__get_src_material_obj_list_()
        for srcMaterialObj in srcMaterialObjs:
            srcMaterialNodepathStr = srcMaterialObj.pathString()
            # material proxy namespace = geometry proxy namespace = look name
            materialNamespaceStr = tgtGeometryProxyObj.inputMaterialNamespaceString()
            trsMaterialProxyObj = self.CLS_grh__trs_input_node_proxy(
                srcMaterialNodepathStr,
                namespace=materialNamespaceStr
            )
            tgtMaterialProxyObj = trsMaterialProxyObj.tgtNodeProxy()
            tgtGeometryProxyObj.connectNodeProxyFrom(tgtMaterialProxyObj)

    def _trs_geometry_proxy__set_ports_(self):
        srcPortObjList = self._trs_geometry_proxy__get_src_port_obj_list_()
        if srcPortObjList:
            trsNodeQueryObj = self.trsNodeQuery()
            tgtNodeObj = self.tgtNode()
            for srcPortObj in srcPortObjList:
                srcPortpathStr = srcPortObj.portpathString()
                trsPortQueryObj = trsNodeQueryObj.trsPortQuery(srcPortpathStr)
                tgtPortpathStr = trsPortQueryObj.target_portpath
                if tgtNodeObj.hasInport(tgtPortpathStr):
                    tgtPortObj = tgtNodeObj.inport(tgtPortpathStr)
                    translatorCls = self.trsNode().CLS_grh__trs_node__obj_translator
                    srcPortraw = translatorCls._obj_translator__set_portraw_convert_(trsPortQueryObj, srcPortObj)
                    tgtPortObj.setPortraw(srcPortraw)

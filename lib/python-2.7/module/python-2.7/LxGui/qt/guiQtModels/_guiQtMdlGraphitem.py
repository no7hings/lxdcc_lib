# coding:utf-8
from LxGui.qt import guiQtObjItf, qtCore, guiQtWgtAbs, guiQtMdlAbs

#

#

#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
CLS_point = QtCore.QPoint
CLS_pointF = QtCore.QPointF
CLS_line = QtCore.QLine
CLS_rect = QtCore.QRect
CLS_rectF = QtCore.QRectF
CLS_polygon = QtGui.QPolygon
CLS_polygonF = QtGui.QPolygonF
CLS_painterPath = QtGui.QPainterPath


#
class xGraphNodeItemModel(guiQtMdlAbs.AbsGuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideItemAttr()
        self.__connectUi(widget)
    #
    def __overrideItemAttr(self):
        self._isSelectEnable = True
        self._isSelectable = True
        self._isSelected = False
        self._isPressHovered = False
        #
        self._isExpandEnable = True
        self._isExpandable = True
        self._isExpanded = False
    #
    def __initUi(self):
        self._explainLabel = self._explainClass()
        self._attributePort = self._attributeClass()
        #
        self._uiBasicRect, self._shadowRect = CLS_rect(), CLS_rect()
        self._uiIconRect, self._gui_qt__mdl__type_str_Rect = CLS_rect(), CLS_rect()
        self._inputConnectionRect, self._outputConnectionRect = CLS_rect(), CLS_rect()
        self._inputConnectionShadowRect, self._outputConnectionShadowRect = CLS_rect(), CLS_rect()
        #
        self._outputPoint, self._inputPoint = CLS_point(), CLS_point()
        #
        self._uiOffset, self._uiSide, self._uiSpacing, self._uiShadowRadius = 0.0, 2.0, 2.0, 4.0
        #
        self._uiBasicWidth, self._uiBasicHeight = 240.0, 40.0
        #
        self._uiBasicIconWidth, self._uiBasicIconHeight = 16.0, 16.0
        #
        self._uiBasisFontSize = 16.0
        #
        self._uiBasicWidthRound, self._uiBasicHeightRound = 10.0, 10.0
        #
        self._uiFrameWidth, self._uiFrameHeight = 40.0, 40.0
        self._uiBasicConnectionWidth, self._uiBasicConnectionHeight = 20.0, 20.0
    #
    def __initVar(self):
        self._uiFontSize = 16.0
        #
        self._uiWidthRound, self._uiHeightRound = 4.0, 4.0
        #
        self._mTranslate = 0.0, 0.0
        #
        self._isMoveable = True
        #
        self._inputConnectionDropFlag, self._outputConnectionDropFlag = False, False
        #
        self._moveStartCursorPos = CLS_point()
        #
        self._globalPoint = CLS_point()
        #
        self._uiIconKeyword = None
        self._uiIcon = None
        #
        self._gui_qt__mdl__index_str_ = None
        self._gui_qt__mdl__name_str_ = None
        #
        self._inputConnectionLis, self._outputConnectionLis = [], []
        self._isInputConnectionEnable, self._isOutputConnectionEnable = False, False
        #
        self._inputAttributeLis, self._outputAttributeLis = [], []
        self._isInputEnable, self._isOutputEnable = False, False
        #
        self._selectRect = CLS_rectF()
    #
    def __connectUi(self, widget):
        self.setWidget(widget)
    #
    def __setClass(self):
        (
            self._explainClass, self._attributeClass,
            self._actionClass,
            self.cls_pointClass, self.cls_pointFClass,
            self.cls_rectClass, self.cls_rectFClass,
            self._pathClass
        ) = (
            self._viewModel._explainClass, self._viewModel._attributeClass,
            self._viewModel._actionClass,
            self._viewModel.cls_pointClass, self._viewModel.cls_pointFClass,
            self._viewModel.cls_rectClass, self._viewModel.cls_rectFClass,
            self._viewModel._pathClass
        )
    #
    def _updateGlobalPos(self, x, y):
        xScale, yScale = self._viewModel._mScale
        self._globalPoint.setX((x - self._mTranslate[0])/xScale), self._globalPoint.setY((y - self._mTranslate[1])/yScale)
    #
    def _getLocalPos(self):
        xScale, yScale = self._viewModel._mScale
        return self._globalPoint.x()*xScale + self._mTranslate[0], self._globalPoint.y()*yScale + self._mTranslate[1]
    #
    def _getLocalSize(self):
        xScale, yScale = self._viewModel._mScale
        return self._uiBasicWidth*xScale, self._uiBasicHeight*yScale
    #
    def _updateWidgetGeometry(self):
        (x, y), (w, h) = self._getLocalPos(), self._getLocalSize()
        #
        self._widget.setGeometry(
            x, y,
            w, h
        )
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        xScale, yScale = self._viewModel._mScale
        #
        shadowRadius = self._uiShadowRadius
        spacing = self._uiSpacing
        basicWidth, basicHeight = self._uiBasicWidth, self._uiBasicHeight
        basicIconWidth, basicIconHeight = self._uiBasicIconWidth, self._uiBasicIconHeight
        #
        self._uiWidthRound, self._uiHeightRound = self._uiBasicWidthRound*xScale, self._uiBasicHeightRound*yScale
        #
        self._uiBasicRect.setRect(
            xPos + 1, yPos + 1,
            width - shadowRadius, height - shadowRadius
        )
        self._shadowRect.setRect(
            xPos + shadowRadius, yPos + shadowRadius,
            width - shadowRadius - 1, height - shadowRadius - 1
        )
        # Connection
        side = 0
        fw, fh = self._uiFrameWidth, self._uiFrameHeight
        cw, ch = self._uiBasicConnectionWidth, self._uiBasicConnectionHeight
        #
        x1, y1, w1, h1 = (
            xPos + (fw - cw)/2 * xScale + side, yPos + (fh - ch)/2 * yScale + side,
            cw * xScale - 1, ch * yScale - 1
        )
        x2, y2, w2, h2 = (
            xPos + width - (fw - cw)/2 * xScale - cw * xScale - side, yPos + (fh - ch)/2 * yScale + side,
            cw * xScale - 1, ch * yScale - 1
        )
        self._inputConnectionRect.setRect(
            x1, y1,
            w1, h1
        )
        self._outputConnectionRect.setRect(
            x2, y2,
            w2, h2
        )
        self._inputConnectionShadowRect.setRect(
            x1 + shadowRadius/2, y1 + shadowRadius/2,
            w1, h1
        )
        self._outputConnectionShadowRect.setRect(
            x2 + shadowRadius/2, y2 + shadowRadius/2,
            w2, h2
        )
        #
        if self._uiIcon is not None:
            self._uiIconRect.setRect(
                xPos + (basicHeight - basicIconWidth)/2*xScale, yPos + (basicHeight - basicIconHeight)/2*xScale,
                basicIconWidth*xScale, basicIconHeight*xScale
            )
        if self._type is not None:
            self._gui_qt__mdl__type_str_Rect.setRect(
                xPos, yPos,
                width - shadowRadius, height - shadowRadius
            )
        #
        self._uiFontSize = max(self._uiBasisFontSize*yScale, 1)
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._updateWidgetGeometry()
        self._gui_qt__mdl__set_rect_geometry_update_()
        self._updateConnection()
    #
    def _addInputConnection(self,  connection):
        self._inputConnectionLis.append(connection)
        #
        self._isInputConnectionEnable = self._inputConnectionLis != []
        #
        self._widget._uiInputConnectionBackgroundRgba = 63, 255, 127, 255
    #
    def _addOutputConnection(self, connection):
        self._outputConnectionLis.append(connection)
        #
        self._isOutputConnectionEnable = self._outputConnectionLis != []
        #
        self._widget._uiOutputConnectionBackgroundRgba = 255, 0, 63, 255
    #
    def _dragMoveBy(self, point, offsetPoint=None):
        if not offsetPoint:
            offsetPoint = CLS_point()
        #
        point = point - offsetPoint
        x, y = point.x(), point.y()
        #
        self._widget.move(x, y)
        self._updateConnection()
        #
        self._updateGlobalPos(x, y)
    #
    def _updateInputConnectionBy(self, point):
        if self._inputConnectionLis:
            for connection in self._inputConnectionLis:
                connection._itemModel.setOutputPoint(point)
    #
    def _updateOutputConnectionBy(self, point):
        if self._outputConnectionLis:
            for connection in self._outputConnectionLis:
                connection._itemModel.setInputPoint(point)
    #
    def _updateConnectionPosBy(self, inputPoint, outputPoint):
        self._updateInputConnectionBy(inputPoint), self._updateOutputConnectionBy(outputPoint)
    #
    def _updateConnectionPoint(self):
        xPos, yPos = self.x(), self.y()
        width, height = self.width() - self._uiShadowRadius, self.height() - self._uiShadowRadius
        xScale, yScale = self._viewModel._mScale
        #
        offset = self._uiBasicHeight*xScale/2
        #
        self._inputPoint.setX(xPos + offset), self._outputPoint.setY(yPos + offset)
        self._outputPoint.setX(xPos + width - offset), self._inputPoint.setY(yPos + offset)
    #
    def _updateConnection(self):
        if self._widget.isVisible():
            self._updateConnectionPoint()
            #
            self._updateConnectionPosBy(self._inputPoint, self._outputPoint)
        #
        self._explainLabel._itemModel.update()
        self._attributePort._itemModel.update()
    #
    def _gui_qt__set_enter_event_update_(self, event):
        self.setPressHovered(True)
    #
    def _gui_qt__set_leave_event_update_(self, event):
        self.setPressHovered(False)
    #
    def _pressSelectAction(self, event):
        point = event.pos()
        if self._isSelectable is True:
            if self._inputConnectionRect.contains(point):
                self._inputConnectionDropFlag, self._outputConnectionDropFlag = True, False
                self._separateSelectFlag, self._extraSelectFlag = False, False
            elif self._outputConnectionRect.contains(point):
                self._inputConnectionDropFlag, self._outputConnectionDropFlag = False, True
                self._separateSelectFlag, self._extraSelectFlag = False, False
            else:
                self._inputConnectionDropFlag, self._outputConnectionDropFlag = False, False
                #
                isExtendSelect, selectedCount = self._viewModel.isExtendSelect(), self._viewModel.selectedCount()
                #
                if isExtendSelect is True:
                    if selectedCount == 0:
                        self._viewModel.separateSelectAt(self._index)
                    else:
                        self._extraSelectFlag = True
                else:
                    if selectedCount == 0:
                        self._viewModel.separateSelectAt(self._index)
                    else:
                        self._separateSelectFlag = True
    #
    def _dragSelectAction(self):
        if self._isSelectable:
            isExtendSelect, selectedCount = self._viewModel.isExtendSelect(), self._viewModel.selectedCount()
            if isExtendSelect is True:
                if selectedCount <= 1:
                    self._viewModel.separateSelectAt(self._index)
                else:
                    self._separateSelectFlag, self._extraSelectFlag = False, False
            else:
                if self._isSelected:
                    if selectedCount <= 1:
                        self._viewModel.separateSelectAt(self._index)
                    else:
                        self._separateSelectFlag, self._extraSelectFlag = False, False
                else:
                    self._viewModel.separateSelectAt(self._index)
    #
    def _releaseSelectAction(self):
        if self._dragFlag is False:
            if self._inputConnectionDropFlag is True:
                self._inputConnectionDropAction()
            elif self._outputConnectionDropFlag is True:
                self._outputConnectionDropAction()
            elif self._separateSelectFlag is True:
                self._viewModel.separateSelectAt(self._index)
            elif self._extraSelectFlag is True:
                self._viewModel.extendSelectAt(self._index)
        #
        self._separateSelectFlag, self._extraSelectFlag = False, False
    #
    def _dragMoveStartAction(self, event):
        point = event.globalPos()
        if self._isMoveable is True:
            self._moveStartCursorPos = point
            self._moveStartCursorPos -= self.pos()
    #
    def _dragMoveExecuteAction(self, event):
        # Flag
        self._dragFlag = True
        # Action
        if self._isMoveable is True:
            point = event.globalPos() - self._moveStartCursorPos
            #
            selectedCount = self._viewModel.selectedCount()
            isMultiMove = selectedCount > 1
            if isMultiMove:
                self._viewModel._updateNodesExtendMoveBy(self, point)
            else:
                self._viewModel._updateNodeSeparateMoveBy(self, point)
    #
    def _dragMoveStopAction(self):
        self._dragFlag = False
    #
    def _inputConnectionDropAction(self):
        if self._inputAttributeLis:
            def getEnabled():
                return True
            def enabledSwitch():
                pass
            actions = [(i, 'checkBox', getEnabled, enabledSwitch) for i in self._inputAttributeLis]
            if actions:
                menu = self._actionClass(self._widget)
                menu.setFocusProxy(self._widget)
                menu.installEventFilter(self._widget)
                menu.setActionData(actions)
                menu.setDrop()
    #
    def _outputConnectionDropAction(self):
        if self._outputAttributeLis:
            def getEnabled():
                return True
            def enabledSwitch():
                pass
            actions = [(i, 'checkBox', getEnabled, enabledSwitch) for i in self._outputAttributeLis]
            if actions:
                menu = self._actionClass(self._widget)
                menu.setFocusProxy(self._widget)
                menu.installEventFilter(self._widget)
                menu.setActionData(actions)
                menu.setDrop()
    #
    def _attributeDropAction(self, event):
        if self._dragFlag is False:
            pass
    #
    def _expandClickAction(self):
        self._explainLabel._itemModel.setExpanded(self._isExpanded)
        self._attributePort.setVisible(self._isExpanded)
        #
        self._viewModel._updateNodeRect(self)
        self._viewModel._updateGroupGeometryBy([self])
    #
    def _updateTranslate(self, args):
        self._mTranslate = args
    #
    def _updateAttribute(self):
        pass
    #
    def update(self):
        self._gui_qt__mdl__set_geometry_update_()
        #
        self._widget.update()
    #
    def setViewModel(self, model):
        self._viewModel = model
        self._graphModelWidget = self._viewModel._widget
        #
        self.__setClass()
        #
        self.__initUi()
        self.__initVar()
    #
    def setNameString(self, string):
        self._explainLabel.setParent(self._graphModelWidget)
        #
        self._explainLabel._itemModel.update()
        #
        self._explainLabel._itemModel.setNameString(string)
        # self._explainLabel._itemModel.setIndex(self._index)
        self._explainLabel._itemModel.setProxyItem(self._widget)
    #
    def setAttributes(self, inputAttributes, outputAttributes):
        self._attributePort.itemModel().setViewModel(self._viewModel)
        self._attributePort.itemModel().setProxyItem(self._widget)
        #
        self._attributePort.itemModel().update()
        #
        self._attributePort.itemModel().setVisible(self._isExpanded)
        self._attributePort.itemModel().setInputAttributes(inputAttributes)
        #
        self.setInputAttributes(inputAttributes), self.setOutputAttributes(outputAttributes)
    #
    def setInputAttributes(self, lis):
        self._inputAttributeLis = lis
        self._isInputEnable = self._inputAttributeLis != []
    #
    def setOutputAttributes(self, lis):
        self._outputAttributeLis = lis
        self._isOutputEnable = self._outputAttributeLis != []
    #
    def setSelected(self, boolean):
        self._isSelected = boolean
        #
        if boolean is True:
            self._widget.raise_()
            #
            self._explainLabel.raise_()
        #
        self._gui_qt__set_press_style_update_()
        #
        self._attributePort._itemModel.setSelected(boolean)
    #
    def setPressHovered(self, boolean, ignoreAction=False):
        self._isPressHovered = boolean
        #
        self._gui_qt__set_press_style_update_()
        #
        self._attributePort._itemModel.setPressHovered(boolean)
    #
    def selectRect(self):
        x, y = self._widget.x(), self._widget.y()
        w, h = self.width(), self.height()
        #
        self._selectRect.setRect(
            x, y,
            w, h
        )
        return self._selectRect
    #
    def setVisible(self, boolean):
        self._widget.setVisible(boolean)
        self._explainLabel.setVisible(boolean)
        #
        self._attributePort.setVisible(self._isExpanded and boolean is True)
    #
    def width_(self):
        return self._widget.width()
    #
    def height_(self):
        return self._widget.height() + [0, self._attributePort.height()][self._isExpanded]
    #
    def _gui_qt__set_press_style_(self, state):
        if state is qtCore.UnpressableState:
            self._widget._wgt__border_rgba = 95, 95, 95, 255
            self._widget._wgt__background_rgba = 0, 0, 0, 0
            #
            self._widget._wgt__name_rgba = 95, 95, 95, 255
            #
            self._widget._uiFontItalic = True
        else:
            if state is qtCore.SelectedState:
                self._widget._wgt__background_rgba = 95, 95, 95, 255
                self._widget._wgt__border_rgba = [(255, 127, 0, 255), (255, 127, 64, 255)][self.isPressHovered()]
            elif state is qtCore.UnselectedState:
                self._widget._wgt__background_rgba = [(127, 127, 127, 127), (95, 95, 95, 255)][self.isPressHovered()]
                self._widget._wgt__border_rgba = [(127, 127, 127, 255), (64, 255, 255, 255)][self.isPressHovered()]
            elif state is qtCore.CurrentState:
                self._widget._wgt__background_rgba = 95, 95, 95, 255
                self._widget._wgt__border_rgba = [(255, 127, 0, 255), (255, 127, 64, 255)][self.isPressHovered()]
            elif state is qtCore.SubSelectedState:
                self._widget._wgt__background_rgba = 95, 95, 95, 255
                self._widget._wgt__border_rgba = [(255, 127, 0, 255), (255, 127, 64, 255)][self.isPressHovered()]
            #
            self._widget._uiFontItalic = False


#
class xGraphGroupItemModel(guiQtMdlAbs.AbsGuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideItemAttr()
        self.__connectUi(widget)
    #
    def __overrideItemAttr(self):
        pass
    #
    def __initUi(self):
        self._explainLabel = self._explainClass()
        #
        self._uiBasicRect, self._rimRect = CLS_rect(), CLS_rect()
        self._uiIconRect, self._gui_qt__mdl__type_str_Rect = CLS_rect(), CLS_rect()
        #
        self._inputConnectionRect, self._outputConnectionRect = CLS_rect(), CLS_rect()
        #
        self._inputPoint, self._outputPoint = CLS_point(), CLS_point()
        #
        self._uiOffset, self._uiSide, self._uiSpacing, self._uiShadowRadius = 0.0, 8.0, 2.0, 4.0
        #
        self._uiBasisFontSize = 20.0
        #
        self._uiBasicWidth, self._uiBasicHeight = 240.0, 40.0
        #
        self._uiBasicWidthRound, self._uiBasicHeightRound = 10.0, 10.0
        #
        self._uiFrameWidth, self._uiFrameHeight = 40.0, 40.0
        self._uiBasicConnectionWidth, self._uiBasicConnectionHeight = 20.0, 20.0
        #
        self._uiIconKeyword = None
        self._uiIcon = None
        #
        self._gui_qt__mdl__index_str_ = None
        self._gui_qt__mdl__name_str_ = None
    #
    def __initVar(self):
        self._isMoveable = True
        self._isPressable = True
        self._isSelectable = True
        #
        self._isPressHovered = False
        self._isSelected = False
        self._isPressCurrent = False
        #
        self._isExpandEnable = True
        self._isExpandable = True
        self._isExpanded = True
        #
        self._nodeIndexLis = []
        self._nodeModelItemLis = []
        #
        self._moveStartCursorPos = CLS_point()
        #
        self._pos = 0, 0
        self._size = 0, 0
        #
        self._uiFontSize = 20.0
        #
        self._uiWidthRound, self._uiHeightRound = 10.0, 10.0
        #
        self._inputConnectionLis, self._outputConnectionLis = [], []
        self._isInputConnectionEnable, self._isOutputConnectionEnable = False, False
        self._inputConnectionPosDic, self._outputConnectionPosDic = {}, {}
    #
    def __connectUi(self, widget):
        self._widget = widget
    #
    def __setClass(self):
        (
            self._explainClass,
            self._actionClass,
            self.cls_pointClass, self.cls_pointFClass,
            self.cls_rectClass, self.cls_rectFClass,
            self._pathClass
        ) = (
            self._viewModel._explainClass,
            self._viewModel._actionClass,
            self._viewModel.cls_pointClass, self._viewModel.cls_pointFClass,
            self._viewModel.cls_rectClass, self._viewModel.cls_rectFClass,
            self._viewModel._pathClass
        )
    #
    def _updateNodeLis(self):
        self._nodeModelItemLis = [self._viewModel._nodeModelItemLis[i] for i in self._nodeIndexLis]
    #
    def _updateInputConnectionLis(self):
        lis = []
        dic = {}
        nodes = self._nodeModelItemLis
        if nodes:
            for node in nodes:
                connections = node._itemModel._inputConnectionLis
                if connections:
                    for connection in connections:
                        connection.lower()
                        lis.append(connection)
                        #
                        inputPoint, outputPoint = connection._itemModel.points()
                        x1, y1, x2, y2 = inputPoint.x(), inputPoint.y(), outputPoint.x(), outputPoint.y()
                        dic.setdefault((x1, y1, x2, y2), []).append(connection)
        #
        self._inputConnectionLis = lis
        self._isInputConnectionEnable = self._inputConnectionLis != []
        self._inputConnectionPosDic = dic
    #
    def _updateOutputConnectionLis(self):
        lis = []
        dic = {}
        nodes = self._nodeModelItemLis
        if nodes:
            for node in nodes:
                connections = node._itemModel._outputConnectionLis
                if connections:
                    for connection in connections:
                        connection.lower()
                        lis.append(connection)
                        #
                        inputPoint, outputPoint = connection._itemModel.points()
                        x1, y1, x2, y2 = inputPoint.x(), inputPoint.y(), outputPoint.x(), outputPoint.y()
                        dic.setdefault((x1, y1, x2, y2), []).append(connection)
        #
        self._outputConnectionLis = lis
        self._isOutputConnectionEnable = self._outputConnectionLis != []
        self._outputConnectionPosDic = dic
    #
    def _updateWidgetGeometry(self):
        xScale, yScale = self._viewModel._mScale
        side = self._uiSide
        #
        xPos, yPos = self._pos
        if self._isExpanded is True:
            width, height = self._size
        else:
            width, height = self._uiBasicWidth*xScale, self._uiBasicHeight*yScale
        #
        self._widget.setGeometry(
            xPos - side, yPos - side,
            width + side*2, height + side*2
        )
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        xScale, yScale = self._viewModel._mScale
        #
        side = self._uiSide
        #
        self._uiWidthRound, self._uiHeightRound = self._uiBasicWidthRound*xScale, self._uiBasicHeightRound*yScale
        #
        self._uiBasicRect.setRect(
            xPos + 2, yPos + 2,
            width - 4, height - 4
        )
        self._rimRect.setRect(
            xPos + 1, yPos + 1,
            width - 2, height - 2
        )
        #
        if self._isExpanded is False:
            fw, fh = self._uiFrameWidth, self._uiFrameHeight
            cw, ch = self._uiBasicConnectionWidth, self._uiBasicConnectionHeight
            #
            self._inputConnectionRect.setRect(
                (fw - cw)/2*xScale + side, (fh - ch)/2*yScale + side,
                cw*xScale, ch*yScale
            )
            self._outputConnectionRect.setRect(
                width - (fw - cw)/2*xScale - cw*xScale - side, (fh - ch)/2*yScale + side,
                cw*xScale, ch*yScale
            )
            #
            self._gui_qt__mdl__type_str_Rect.setRect(
                xPos, yPos,
                width, height
            )
            #
            self._uiFontSize = max(self._uiBasisFontSize*yScale, 1)
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._updateWidgetGeometry()
        self._gui_qt__mdl__set_rect_geometry_update_()
        #
        self._updateConnection()
    #
    def _dragMoveBy(self, point):
        if self._nodeIndexLis:
            self._viewModel._updateNodesGroupMoveBy(self, point)
            #
            self._widget.move(point)
            #
            self._updateConnection()
    #
    def _updateConnectionPoint(self):
        xPos, yPos = self.x(), self.y()
        width, height = self.width(), self.height()
        xScale, yScale = self._viewModel._mScale
        #
        side = self._uiSide
        #
        offset = self._uiBasicHeight*yScale/2 + side
        #
        self._inputPoint.setX(xPos + offset), self._inputPoint.setY(yPos + offset)
        self._outputPoint.setX(xPos + width - offset), self._outputPoint.setY(yPos + offset)
    #
    def _updateConnection(self):
        if self._isExpanded is False:
            self._updateConnectionPoint()
            #
            nodes = self._nodeModelItemLis
            if nodes:
                for node in nodes:
                    node._itemModel._updateConnectionPosBy(self._inputPoint, self._outputPoint)
        #
        self._explainLabel._itemModel.update()
    #
    def _gui_qt__set_enter_event_update_(self, event):
        self.setPressHovered(True)
    #
    def _gui_qt__set_leave_event_update_(self, event):
        self.setPressHovered(False)
    #
    def _pressSelectAction(self, event):
        self._viewModel._updateCurGroup(self._index)
    #
    def _dragMoveStartAction(self, event):
        point = event.globalPos()
        if self._isMoveable is True:
            self._moveStartCursorPos = point
            self._moveStartCursorPos -= self._widget.pos()
    #
    def _dragMoveExecuteAction(self, event):
        # Flag
        self._dragFlag = True
        # Action
        if self._isMoveable is True:
            point = event.globalPos() - self._moveStartCursorPos
            #
            self._dragMoveBy(point)
    #
    def _dragMoveStopAction(self):
        self._dragFlag = False
    #
    def _expandClickAction(self):
        def setNodeVisible():
            nodes = self._nodeModelItemLis
            if nodes:
                for node in nodes:
                    # Clear Select
                    itemModel = node._itemModel
                    #
                    self._viewModel.subSelectedIndex(itemModel._index)
                    #
                    itemModel.setVisible(self._isExpanded)
                    if self._isExpanded is False:
                        itemModel._updateConnectionPosBy(self._inputPoint, self._outputPoint)
                    else:
                        itemModel._updateConnection()
        #
        def setConnectionVisible():
            def setBranch(dic):
                if dic:
                    for k, v in dic.items():
                        for seq, i in enumerate(v):
                            if seq == 0:
                                i.show()
                            else:
                                i.hide()
            #
            setBranch(self._inputConnectionPosDic), setBranch(self._outputConnectionPosDic)
        #
        self._explainLabel._itemModel.setExpanded(self._isExpanded)
        setNodeVisible()
        #
        self._updateInputConnectionLis(), self._updateOutputConnectionLis()
        setConnectionVisible()
        #
        self.update()
    #
    def update(self):
        x, y, w, h = self._viewModel._getRectByIndexLis(self._nodeIndexLis)
        self._pos = x, y
        self._size = w, h
        #
        self._gui_qt__mdl__set_geometry_update_()
        #
        self._updateWidgetState()
    #
    def setViewModel(self, model):
        self._viewModel = model
        self._graphModelWidget = self._viewModel._widget
        #
        self.__setClass()
        #
        self.__initUi()
        self.__initVar()
    #
    def setPressCurrent(self, boolean, ignoreAction=True):
        self._isPressCurrent = boolean
        #
        if boolean is True:
            self._explainLabel.raise_()
        #
        self._updateWidgetState()
    #
    def setIndexes(self, lis):
        self._nodeIndexLis = lis
        #
        self._updateNodeLis()
        self._updateInputConnectionLis(), self._updateOutputConnectionLis()
    #
    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self._uiIconKeyword = iconKeywordStr
        #
        self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword)
    #
    def setNameString(self, string):
        self._explainLabel.setParent(self._graphModelWidget)
        #
        self._explainLabel._itemModel.setProxyItem(self._widget)
        self._explainLabel._itemModel.setNameString(string)
        # self._explainLabel._itemModel.setIndex(self._index)
        #
        self._explainLabel._itemModel.setExpanded(self._isExpanded)
        self._explainLabel._itemModel.update()
    #
    def nodes(self):
        return [self._viewModel._nodeModelItemLis[i] for i in self._nodeIndexLis]
    #
    def _gui_qt__set_press_style_(self, state):
        pass


#
class xGraphConnectionItemModel(guiQtMdlAbs.AbsGuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideItemAttr()
        self.__connectUi(widget)
    #
    def __overrideItemAttr(self):
        self._inputAttribute, self._outputAttribute = None, None
        #
        self._index = -1
        #
        self._isPressable = True
        #
        self._isSelectable = True
        self._isSelected = False
        self._isPressHovered = False
    #
    def __initUi(self):
        self._inputPoint, self._outputPoint = CLS_pointF(), CLS_pointF()
        #
        self._startPoint, self._endPoint = CLS_pointF(), CLS_pointF()
        #
        self._curvePath = CLS_painterPath()
        #
        self._pressFlag = False
        self._dragFlag = False
    #
    def __initVar(self):
        self._dir = 0
        self._drawDir = 0
        #
        self._inputNode = None
        self._outputNode = None
    #
    def __connectUi(self, widget):
        self._widget = widget
    #
    def __setClass(self):
        (
            self._explainClass,
            self._actionClass,
            self.cls_pointClass, self.cls_pointFClass,
            self.cls_rectClass, self.cls_rectFClass,
            self._pathClass
        ) = (
            self._viewModel._explainClass,
            self._viewModel._actionClass,
            self._viewModel.cls_pointClass, self._viewModel.cls_pointFClass,
            self._viewModel.cls_rectClass, self._viewModel.cls_rectFClass,
            self._viewModel._pathClass
        )
    #
    def _updateWidgetGeometry(self):
        xIp, yIp = self._inputPoint.x(), self._inputPoint.y()
        xOp, yOp = self._outputPoint.x(), self._outputPoint.y()
        #
        xPos, yPos = min(xOp, xIp), min(yOp, yIp)
        #
        width, height = abs(xIp - xOp), abs(yIp - yOp)
        #
        self._widget.setGeometry(
            xPos - 1, yPos - 1,
            width + 2, height + 2
        )
        #
        if xOp < xIp and yOp > yIp:
            self._dir = 1
        elif xOp > xIp and yOp < yIp:
            self._dir = 1
        else:
            self._dir = 0
        #
        if xOp < xIp:
            self._drawDir = 1
        else:
            self._drawDir = 0
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        def addCubic(p1, p2, index):
            c1, c2 = self.cls_pointFClass((p1.x() + p2.x())/index, p1.y()), self.cls_pointFClass((p1.x() + p2.x())/index, p2.y())
            path.cubicTo(c1, c2, p2)
            path.lineTo(p2)
            path.cubicTo(c2, c1, p1)
        #
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        if self._dir == 0:
            self._startPoint.setX(xPos + 1), self._startPoint.setY(yPos + 1)
            self._endPoint.setX(xPos + width - 2), self._endPoint.setY(yPos + height - 2)
        else:
            self._startPoint.setX(xPos + 1), self._startPoint.setY(yPos + height - 2)
            self._endPoint.setX(xPos + width - 2), self._endPoint.setY(yPos + 1)
        #
        path = CLS_painterPath(self._startPoint)
        #
        self._curvePath = path
        #
        addCubic(self._startPoint, self._endPoint, [2, 1][self._drawDir])
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._updateWidgetGeometry()
        self._gui_qt__mdl__set_rect_geometry_update_()
    #
    def _gui_qt__mdl__set_mouse_move_event_update_(self, event):
        if self._curvePath.contains(event.pos()):
            self._isPressHovered = True
        else:
            self._isPressHovered = False
            event.ignore()
        #
        self._gui_qt__set_press_style_update_()
    #
    def _pressSelectAction(self, event):
        if self._isSelectable is True:
            if self._isPressHovered:
                isExtendSelect = self._viewModel.isExtendSelect()
                #
                if isExtendSelect is True:
                    self._viewModel.extendSelectAt(self._index)
                else:
                    self._viewModel.separateSelectAt(self._index)
                #
                event.accept()
            else:
                event.ignore()
    #
    def update(self):
        self._gui_qt__mdl__set_geometry_update_()
        #
        self._widget.update()
    #
    def setViewModel(self, model):
        self._viewModel = model
        self._graphModelWidget = self._viewModel._widget
        #
        self.__setClass()
        #
        self.__initUi()
        self.__initVar()
    #
    def setInputPoint(self, point):
        self._inputPoint.setX(point.x()), self._inputPoint.setY(point.y())
        #
        self.update()
    #
    def setOutputPoint(self, point):
        self._outputPoint.setX(point.x()), self._outputPoint.setY(point.y())
        #
        self.update()
    #
    def inputPoint(self):
        return self._inputPoint
    #
    def outputPoint(self):
        return self._outputPoint
    #
    def points(self):
        return self._outputPoint, self._inputPoint
    #
    def setInputNode(self, node):
        self._outputPoint = node._itemModel._outputPoint
        self._inputNode = node
    #
    def setOutputNode(self, node):
        self._inputPoint = node._itemModel._inputPoint
        self._outputNode = node
    #
    def setInputAttribute(self, attribute):
        self._inputAttribute = attribute
    #
    def setOutputAttribute(self, attribute):
        self._outputAttribute = attribute
    #
    def setSelected(self, boolean):
        self._isSelected = boolean
        #
        self._gui_qt__set_press_style_update_()
    #
    def selectRect(self):
        x, y = self.x(), self.y()
        w, h = self.width(), self.height()
        #
        rectF = CLS_rectF()
        rectF.setRect(
            x, y,
            w, h
        )
        return rectF
    #
    def _gui_qt__set_press_style_(self, state):
        if state is qtCore.UnpressableState:
            self._widget._wgt__border_rgba = 95, 95, 95, 255
            self._widget._wgt__background_rgba = 0, 0, 0, 0
            #
            self._widget._wgt__name_rgba = 95, 95, 95, 255
            #
            self._widget._uiFontItalic = True
        else:
            if state is qtCore.SelectedState:
                self._widget._wgt__background_rgba = 95, 95, 95, 255
                self._widget._wgt__border_rgba = [(255, 127, 0, 255), (255, 127, 64, 255)][self.isPressHovered()]
            elif state is qtCore.UnselectedState:
                self._widget._wgt__background_rgba = [(127, 127, 127, 127), (95, 95, 95, 255)][self.isPressHovered()]
                self._widget._wgt__border_rgba = [(127, 127, 127, 255), (64, 255, 255, 255)][self.isPressHovered()]
            elif state is qtCore.CurrentState:
                self._widget._wgt__background_rgba = 95, 95, 95, 255
                self._widget._wgt__border_rgba = [(255, 127, 0, 255), (255, 127, 64, 255)][self.isPressHovered()]
            elif state is qtCore.SubSelectedState:
                self._widget._wgt__background_rgba = 95, 95, 95, 255
                self._widget._wgt__border_rgba = [(255, 127, 0, 255), (255, 127, 64, 255)][self.isPressHovered()]
            #
            self._widget._uiFontItalic = False


#
class xGraphExplainItemModel(guiQtMdlAbs.AbsGuiQtItemMdl):
    def __init__(self, widget, (pointClass, rectClass)):
        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideItemAttr()
        self.__connectUi(widget)
        self.__setClass(pointClass, rectClass)
        #
        self.__initUi()
        self.__initVar()
    #
    def __overrideItemAttr(self):
        self._isExpandEnable = True
        self._isExpandable = True
        self._isExpanded = False
    #
    def __initUi(self):
        self._uiExpandRect = CLS_rect()
        self._gui_qt__mdl__index_str_Rect = CLS_rect()
        self._gui_qt__mdl__name_str_Rect = CLS_rect()
        #
        self._uiSpacing = 4
        #
        self._gui_qt__mdl__index_str_Width, self._gui_qt__mdl__name_str_Width = 32, 32
        #
        self._uiFrameWidth, self._uiFrameHeight = 20, 20
        self._uiIconWidth, self._uiIconHeight = 16, 16
    #
    def __initVar(self):
        pass
    #
    def __connectUi(self, widget):
        self._widget = widget
    #
    def __setClass(self, *args):
        self.cls_pointClass, self.cls_rectClass = args
    #
    def _updateWidgetGeometry(self):
        if self._proxyItem is not None:
            width = 0
            xPos, yPos = self._proxyItem.x(), self._proxyItem.y()
            width += self._uiFrameWidth
            if self._gui_qt__mdl__index_str_ is not None:
                width += self._gui_qt__mdl__index_str_Width + self._uiSpacing
            if self._gui_qt__mdl__name_str_ is not None:
                self._gui_qt__mdl__name_str_Width = self._widget.fontMetrics().width(self._gui_qt__mdl__name_str_)
                width += self._gui_qt__mdl__name_str_Width
            #
            height = self._uiFrameHeight
            #
            self._widget.setGeometry(
                xPos, yPos - height,
                width, height
            )
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        #
        width, height = self.width(), self.height()
        #
        if self._isExpandEnable is True:
            self._uiExpandRect.setRect(
                (self._uiFrameWidth - self._uiIconWidth)/2, (self._uiFrameHeight - self._uiIconHeight)/2,
                self._uiIconWidth, self._uiIconHeight
            )
            xPos += self._uiFrameWidth
        if self._gui_qt__mdl__name_str_ is not None:
            self._gui_qt__mdl__name_str_Rect.setRect(
                xPos, yPos,
                self._gui_qt__mdl__name_str_Width, self._uiFrameHeight
            )
            xPos += self._gui_qt__mdl__name_str_Width
        if self._gui_qt__mdl__index_str_ is not None:
            self._gui_qt__mdl__index_str_Rect.setRect(
                xPos, yPos,
                self._gui_qt__mdl__index_str_Width, height
            )
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._updateWidgetGeometry()
        self._gui_qt__mdl__set_rect_geometry_update_()
    #
    def _gui_qt__set_enter_event_update_(self, event):
        if self._proxyItem is not None:
            self._proxyItem._itemModel._gui_qt__set_enter_event_update_(event)
        #
        self.setPressHovered(True)
    #
    def _gui_qt__set_leave_event_update_(self, event):
        if self._proxyItem is not None:
            self._proxyItem._itemModel._gui_qt__set_leave_event_update_(event)
        #
        self.setPressHovered(False)
    #
    def _gui_qt__mdl__set_mouse_press_event_update_(self, event):
        self._pressFlag, self._dragFlag = True, False
        #
        if self._proxyItem is not None:
            self._proxyItem._itemModel._dragMoveStartAction(event)
    #
    def _gui_qt__mdl__set_mouse_press_move_event_update_(self, event):
        self._pressFlag, self._dragFlag = False, True
        #
        if self._proxyItem is not None:
            self._proxyItem._itemModel._dragMoveExecuteAction(event)
    #
    def _gui_qt__mdl__set_mouse_release_event_update_(self, event):
        if self._proxyItem is not None:
            self._proxyItem._itemModel._dragMoveStopAction()
            #
            if self._pressFlag is True:
                self._proxyItem._itemModel._dragMoveStopAction()
                #
                self._proxyItem._itemModel._expandClickSwitchAction()
        #
        self._pressFlag, self._dragFlag = False, False
    #
    def update(self):
        self._updateWidgetGeometry()
        self._gui_qt__mdl__set_rect_geometry_update_()
        #
        self._updateWidgetState()
    #
    def _setQtExpandStyle(self, state):
        pass


#
class xGraphAttributePortItemModel(
    guiQtObjItf.ItfGuiQtItemDef,
    guiQtObjItf.ItfQtViewModel
):
    def __init__(self, widget):
        super(xGraphAttributePortItemModel, self).__init__(widget)
        self._initGuiQtItemDef()
        #
        self.__overrideItemAttr()
        self.__connectUi(widget)
    #
    def __overrideItemAttr(self):
        self._inputAttributeLis, self._outputAttributeLis = None, None
        #
        self._itemMode = qtCore.ListMode
        #
        self._isExpandEnable = True
        #
        self._isSelectEnable = True
        self._isSelectable = True
        #
        self._isColorEnable = True
    #
    def __initUi(self):
        self._uiBasicRect, self._shadowRect = CLS_rect(), CLS_rect()
        #
        self._uiBasicWidthRound, self._uiBasicHeightRound = 10.0, 10.0
        #
        self._uiOffset, self._uiSide, self._uiSpacing, self._uiShadowRadius = 0.0, 2.0, 2.0, 4.0
    #
    def __initVar(self):
        self._uiWidthRound, self._uiHeightRound = 4.0, 4.0
    #
    def __connectUi(self, widget):
        self._widget = widget
    #
    def __setClass(self):
        (
            self._explainClass,
            self._actionClass,
            self.cls_pointClass, self.cls_pointFClass,
            self.cls_rectClass, self.cls_rectFClass,
            self._pathClass
        ) = (
            self._viewModel._explainClass,
            self._viewModel._actionClass,
            self._viewModel.cls_pointClass, self._viewModel.cls_pointFClass,
            self._viewModel.cls_rectClass, self._viewModel.cls_rectFClass,
            self._viewModel._pathClass
        )
    #
    def _updateWidgetGeometry(self):
        if self._proxyItem is not None:
            xPos, yPos = self._proxyItem.x(), self._proxyItem.y()
            width, height = self.absSize()
            width_, height_ = self._proxyItem.width(), self._proxyItem.height()
            #
            x, y = xPos, yPos + height_
            w, h = width_, height
            #
            self._widget.setGeometry(
                x, y,
                w, h
            )
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        xScale, yScale = self._viewModel._mScale
        #
        shadowRadius = self._uiShadowRadius
        #
        self._uiWidthRound, self._uiHeightRound = self._uiBasicWidthRound*xScale, self._uiBasicHeightRound*yScale
        #
        self._uiBasicRect.setRect(
            xPos + 1, yPos + 1,
            width - shadowRadius, height - shadowRadius
        )
        self._shadowRect.setRect(
            xPos + shadowRadius, yPos + shadowRadius,
            width - shadowRadius - 2, height - shadowRadius - 2
        )
    #
    # def _gui_qt__set_enter_event_update_(self, event):
    #     if self._proxyItem is not None:
    #         self._proxyItem._itemModel._gui_qt__set_enter_event_update_(event)
    #     #
    #     self.setPressHovered(True)
    # #
    # def _gui_qt__set_leave_event_update_(self, event):
    #     if self._proxyItem is not None:
    #         self._proxyItem._itemModel._gui_qt__set_leave_event_update_(event)
    #     #
    #     self.setPressHovered(False)
    # #
    # def _gui_qt__mdl__set_mouse_press_event_update_(self, event):
    #     self._pressFlag, self._dragFlag = True, False
    #     #
    #     if self._proxyItem is not None:
    #         self._proxyItem._itemModel._pressSelectAction(event)
    #         self._proxyItem._itemModel._dragMoveStartAction(event)
    # #
    # def _gui_qt__mdl__set_mouse_press_move_event_update_(self, event):
    #     self._pressFlag, self._dragFlag = False, True
    #     #
    #     if self._proxyItem is not None:
    #         self._proxyItem._itemModel._dragSelectAction()
    #         self._proxyItem._itemModel._dragMoveExecuteAction(event)
    # #
    # def _gui_qt__mdl__set_mouse_release_event_update_(self, event):
    #     if self._proxyItem is not None:
    #         self._proxyItem._itemModel._releaseSelectAction()
    #         self._proxyItem._itemModel._dragMoveStopAction()
    #     #
    #     self._pressFlag, self._dragFlag = False, False
    #
    def setViewModel(self, model):
        self._viewModel = model
        self._widget.setParent(model._widget)
        #
        self.__setClass()
        #
        self.__initUi()
        self.__initVar()
    #
    def setProxyItem(self, item):
        self._proxyItem = item
    #
    def setSelected(self, boolean):
        self._isSelected = boolean
        if boolean is True:
            self._widget.raise_()
        #
        self._gui_qt__set_press_style_update_()
    #
    def setInputAttributes(self, attributes):
        inputItem = guiQtWgtAbs._QtAttributeitem()
        inputItemModel = inputItem.itemModel()
        inputItemModel.setName('input')
        self.addItem(inputItem)
        if attributes:
            for i in attributes:
                attributeItem = guiQtWgtAbs._QtAttributeitem()
                attributeItem.setName(i)
                inputItem.addChild(attributeItem)
        #
        self.update()

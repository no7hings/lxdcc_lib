# coding=utf-8
from LxBasic import bscMethods

from LxPreset import prsMethods
#
from LxCore.preset.prod import assetPr, sceneryPr, scenePr
#
from LxCore.operation import mailOp, dingTalkOp
#
none = ''


#
def getShowInfo(dbUnitId, typepathString, variantString, stageString):
    viewModule = none
    viewLink = none
    viewUnit = none
    viewClass = none
    viewName = none
    if prsMethods.Asset.isValidCategory(typepathString):
        viewModule = prsMethods.Asset.moduleShowname()
        viewLink = prsMethods.Asset.linkShowname_(stageString)
        viewUnit = assetPr.getAssetViewInfo(dbUnitId, typepathString, variantString)
        viewClass = prsMethods.Asset.categoryShowname(typepathString)
        viewName = assetPr.getAssetViewName(dbUnitId)
    elif prsMethods.Scenery.isValidCategory(typepathString):
        viewModule = prsMethods.Scenery.moduleShowname()
        viewLink = prsMethods.Scenery.linkShowname_(stageString)
        viewUnit = sceneryPr.getSceneryViewInfo(dbUnitId, typepathString, variantString)
        viewClass = prsMethods.Scenery.categoryShowname(typepathString)
        viewName = sceneryPr.getSceneryViewName(dbUnitId)
    elif prsMethods.Scene.isValidCategory(typepathString):
        viewModule = prsMethods.Scene.moduleShowname()
        viewLink = prsMethods.Scene.linkShowname_(stageString)
        viewUnit = scenePr.getSceneViewInfo(dbUnitId, typepathString, variantString)
        viewClass = prsMethods.Scene.categoryShowname(typepathString)
        viewName = scenePr.getSceneViewName(dbUnitId)
    return viewModule, viewLink, viewUnit, viewClass, viewName


#
def sendProductMessageByDingTalk(
        dbUnitId,
        projectName,
        typepathString, moduleName, variantString, stageString,
        timeTag,
        description, note
):
    projectNameData = prsMethods.Project.mayaDatumDict()
    viewProject = projectName
    if projectName in projectNameData:
        viewProject = projectNameData[projectName][1]
    #
    timeString = bscMethods.OsTimetag.toChnPrettify(timeTag, useMode=1)
    #
    viewModule, viewLink, viewUnit, viewClass, viewName = getShowInfo(dbUnitId, typepathString, variantString, stageString)
    #
    userName = bscMethods.OsPlatform.username()
    userCnName = prsMethods.Personnel.userChnname()
    #
    if not note:
        note = u'N/a'
    #
    mainBody = u'''????????????\n\n  ?????????{}\n  ?????????{}\n  ?????????{} # {}\n\n  ?????????{} # {}\n  ?????????{}\n\n  ?????????{}\n  ?????????{}'''.format(
        viewProject,
        viewLink,
        viewUnit, moduleName,
        userCnName, userName,
        timeString,
        description,
        note
    )
    dingTalkRobot = dingTalkOp.DingTalkRobotMethod(mainBody)
    dingTalkRobot.send()


#
def sendProductMessageByMail(
        htmlLog,
        dbUnitId,
        projectName,
        typepathString, moduleName, variantString, stageString,
        description, note
):
    toMails = prsMethods.Personnel.userMailsFilterByUsernames(
        prsMethods.Personnel.usernamesFilterByMailSendEnable()
    )
    #
    projectNameData = prsMethods.Project.mayaDatumDict()
    viewProject = projectName
    if projectName in projectNameData:
        viewProject = projectNameData[projectName][1]
    #
    viewModule, viewLink, viewUnit, viewClass, viewName = getShowInfo(dbUnitId, typepathString, variantString, stageString)
    #
    summary = u'''???????????????{0} - {1} - {2}???'''.format(viewProject, viewModule, viewUnit)
    subject = u'''{0} - {1} - {2}'''.format(viewProject, viewModule, viewUnit)
    #
    userCnName = prsMethods.Personnel.userChnname()
    #
    if not description:
        description = u'N/a'
    #
    if not note:
        note = u'N/a'
    #
    if htmlLog is None:
        u'N/a'u'???????????????'
    #
    mainBody = u'''
        <html>
        <body style=";background:#ffffff;">
        <h1><span style="font-family:'Arial';font-size:12pt;font-weight:600;color:#000000;">????????????</span></h1>
        <p>?????????{}</p>
        <p>?????????{}</p>
        <p>?????????{}</p>
        <p>?????????{}</p>
        <p>?????????{}</p>
        <p>?????????{}</p>
        <p>?????????</p>
        <p>{}</p>
        </body>
        </html>'''.format(
        userCnName,
        viewProject,
        viewLink,
        viewName,
        description,
        note,
        htmlLog
    )
    mailOp.sendMail(
        toMails, summary, subject, mainBody
    )

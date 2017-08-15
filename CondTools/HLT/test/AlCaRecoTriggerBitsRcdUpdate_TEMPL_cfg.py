# Config file template to write new/update AlCaRecoTriggerBits stored
# in AlCaRecoTriggerBitsRcd that is used to get selected HLT paths for
# the HLTHighLevel filter for AlCaReco production.
#
# Please understand that there are two IOVs involved:
# 1) One for the output tag. Here the usually used default is 1->inf,
#    changed by process.AlCaRecoTriggerBitsRcdUpdate.firstRunIOV
#    and process.AlCaRecoTriggerBitsRcdUpdate.lastRunIOV.
# 2) The IOV of the tag of the input AlCaRecoTriggerBitsRcd.
#    That is chosen by process.source.firstRun (but irrelevant if 
#    process.AlCaRecoTriggerBitsRcdUpdate.startEmpty = True)
#
# See also further comments below, especially the WARNING.
#
#  Author    : Marco Musich
#  Date      : Feb 2016

import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing 

process = cms.Process("UPDATEDB")

options = VarParsing.VarParsing()
options.register( "inputDB", 
                  "frontier://FrontierProd/CMS_CONDITIONS",  #default value
                  VarParsing.VarParsing.multiplicity.singleton, 
                  VarParsing.VarParsing.varType.string,
                  "the input DB"
                  )

options.register( "inputTag", 
                  "AlCaRecoHLTpaths8e29_1e31_v24_offline",  #default value
                  VarParsing.VarParsing.multiplicity.singleton, 
                  VarParsing.VarParsing.varType.string,
                  "the input tag"
                  )

options.register( "outputDB", 
                  "sqlite_file:AlCaRecoTriggerBits.db",  #default value
                  VarParsing.VarParsing.multiplicity.singleton, 
                  VarParsing.VarParsing.varType.string,
                  "the output DB"
                  )

options.register( "outputTag", 
                  "testTag",  #default value
                  VarParsing.VarParsing.multiplicity.singleton, 
                  VarParsing.VarParsing.varType.string,
                  "the input DB"
                  )

options.register( "firstRun", 
                  1,  #default value
                  VarParsing.VarParsing.multiplicity.singleton, 
                  VarParsing.VarParsing.varType.int,
                  "the first run"
                  )

options.parseArguments()

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr = cms.untracked.PSet(placeholder = cms.untracked.bool(True))
process.MessageLogger.cout = cms.untracked.PSet(INFO = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(1)
    ))

# the module writing to DB
process.load("CondTools.HLT.AlCaRecoTriggerBitsRcdUpdate_cfi")
# The IOV that you want to write out, defaut is 1 to -1/inf. 
process.AlCaRecoTriggerBitsRcdUpdate.firstRunIOV = options.firstRun # docu see...
#process.AlCaRecoTriggerBitsRcdUpdate.lastRunIOV = -1 # ...cfi
# If you want to start from scratch, comment the next line:
process.AlCaRecoTriggerBitsRcdUpdate.startEmpty = False


# remove and update value (HLT paths)
# In case you want to remove 'keys', use this possibly comma separated list.
# Also if you want to replace settings for one 'key', you have to remove it first.
process.AlCaRecoTriggerBitsRcdUpdate.listNamesRemove = ["HcalCalGammaJet"]
# Here specifiy 'key' and corresponding paths for new entries or updated ones:
# process.AlCaRecoTriggerBitsRcdUpdate.triggerListsAdd = [
#     cms.PSet(listName = cms.string('AlCaEcalTrg'), # to be updated
#              hltPaths = cms.vstring('AlCa_EcalPhiSym*')
#              )
#     ]

#add
process.AlCaRecoTriggerBitsRcdUpdate.triggerListsAdd = [
    ## add Gamma+jet to each IOV
    cms.PSet(listName = cms.string('HcalCalGammaJet'),
             hltPaths = cms.vstring('HLT_L1SingleEG*', 'HLT_Photon*')),

    cms.PSet(listName = cms.string('HcalCalPedestal'), 
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('HcalCalHBHEMuonFilter'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('HcalCalIsolatedBunchSelector'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('HcalCalIsolatedBunchFilter'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('HcalCalIsoTrkFilter'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('EcalESAlign'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('EcalRecalElectron'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('EcalUncalWElectron'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('EcalUncalZElectron'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('EcalUncalZSCElectron'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('EcalCalWElectron'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('EcalCalZElectron'),
             hltPaths = cms.vstring('*')),

    # Cosmic during Collisions
    cms.PSet(listName = cms.string('MuAlGlobalCosmicsInCollisions'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('TkAlCosmicsInCollisions'),
             hltPaths = cms.vstring('*')),

    # Pixle has their own workflow. They don't need this one. Just for completenes for now
    cms.PSet(listName = cms.string('SiPixelLorentzAngle'),
             hltPaths = cms.vstring('HLT1MuonIso','HLT2MuonNonIso','HLT2MuonJPsi','HLT2MuonUpsilon','HLT2MuonZ','HLT2MuonSameSign')),

    ### PCL is added as "*" pass through
    cms.PSet(listName = cms.string('PromptCalibProdSiStripGainsAAG'),
             hltPaths = cms.vstring('*')),
    cms.PSet(listName = cms.string('PromptCalibProdSiStrip'),
             hltPaths = cms.vstring('*')),

    ## PA stuff
    cms.PSet(listName = cms.string('TkAlUpsilonMuMuPA'),
             hltPaths = cms.vstring('HLT_*')),
    cms.PSet(listName = cms.string('TkAlZMuMuPA'),
             hltPaths = cms.vstring('HLT_*')),
    cms.PSet(listName = cms.string('TkAlMuonIsolatedPA'),
             hltPaths = cms.vstring('HLT_*'))
    ]

#update key
process.AlCaRecoTriggerBitsRcdUpdate.alcarecoToClone = []

#update key
process.AlCaRecoTriggerBitsRcdUpdate.alcarecoToReplace = [
    cms.PSet(oldKey = cms.string('SiStripCalMinBiasAfterAbortGap'),
             newKey = cms.string('SiStripCalMinBiasAAG')
             ),
    cms.PSet(oldKey = cms.string('SiStripCalMinBiasAfterAbortGapHI'),
             newKey = cms.string('SiStripCalMinBiasAAGHI')
             ),
    cms.PSet(oldKey = cms.string('MuAlcaDtCalibHI'),
             newKey = cms.string('DtCalibHI')
             ),
    cms.PSet(oldKey = cms.string('ALCARECOLumiPixels'),
             newKey = cms.string('LumiPixels')
             ),
    cms.PSet(oldKey = cms.string('ALCARECOHcalCalMinBias'),
             newKey = cms.string('HcalCalMinBias')
             ),
    cms.PSet(oldKey = cms.string('ALCARECOEcalCalPi0Calib'),
             newKey = cms.string('EcalCalPi0Calib')
             ),
    cms.PSet(oldKey = cms.string('ALCARECOEcalCalEtaCalib'),
             newKey = cms.string('EcalCalEtaCalib')
             ),
    cms.PSet(oldKey = cms.string('MuAlcaDtCalibCosmics'),
             newKey = cms.string('DtCalibCosmics')
             ),
    cms.PSet(oldKey = cms.string('MuAlcaDtCalibMu'),
             newKey = cms.string('DtCalib')
             ),
    cms.PSet(oldKey = cms.string('AlCaEcalTrg'),
             newKey = cms.string('EcalTrg')
             ),
    cms.PSet(oldKey = cms.string('VertexPixelZeroBias'),
             newKey = cms.string('LumiPixelsMinBias')
             ),
    cms.PSet(oldKey = cms.string('PromptCalibProdForBS'),
             newKey = cms.string('PromptCalibProd')
             )

    ]




# No data, but have to specify run number if you do not want 1, see below:
process.source = cms.Source("EmptySource",
                            #numberEventsInRun = cms.untracked.uint32(1),
                            firstRun = cms.untracked.uint32(options.firstRun) # 1 is default
                            )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

# DB input - needed only for AlCaRecoTriggerBitsRcdUpdate.startEmpty = False
# WARNING:
# Take care in case the input tag has several IOVs: The run number that will be 
# used to define which payload you get is defined by the run number in the
# EmptySource above!
# Either a global tag...
# from Configuration.AlCa.autoCond import autoCond
# process.load("Configuration.StandardSequences.CondDBESSource_cff")
# process.GlobalTag.globaltag = autoCond['run2_data'] #choose your tag

# ...or (recommended since simpler) directly from DB/sqlite

process.load("CondCore.CondDB.CondDB_cfi")

# DB input service: 
process.CondDB.connect = options.inputDB
process.dbInput = cms.ESSource("PoolDBESSource",
                               process.CondDB,
                               toGet = cms.VPSet(cms.PSet(record = cms.string('AlCaRecoTriggerBitsRcd'),
                                                          tag = cms.string(options.inputTag)
                                                          )
                                                 )
                               )

# DB output service:
process.CondDB.connect = options.outputDB
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDB,
                                          timetype = cms.untracked.string('runnumber'),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('AlCaRecoTriggerBitsRcd'),
                                                                     tag = cms.string(options.outputTag) # choose output tag you want
                                                                     )
                                                            )
                                          )

# Put module in path:
process.p = cms.Path(process.AlCaRecoTriggerBitsRcdUpdate)



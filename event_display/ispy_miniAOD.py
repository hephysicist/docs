import FWCore.ParameterSet.Config as cms

process = cms.Process('ISPY')

process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

process.source = cms.Source('PoolSource',
                            fileNames = cms.untracked.vstring(
    #'/store/data/Run2018D/MuonEG/MINIAOD/UL2018_MiniAODv2_GT36-v1/60000/6546A3C1-9150-0B49-900A-A22645E81002.root'
    '/store/mc/RunIISummer20UL18MiniAODv2/bbHToTauTau_M-125_4FS_TuneCP5_yb2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/44940BE9-880E-3044-BEB7-1402BE90B200.root'
    #'root://cmsxrootd.fnal.gov///store/data/Run2018D/MuonEG/MINIAOD/UL2018_MiniAODv2_GT36-v1/60000/8934A7DA-B306-6D41-8D29-706641AED88B.root'
    ),
# eventsToProcess = cms.untracked.VEventRange(
     
#     '324022:181382595',
#     '324022:181453151',
#     '324022:181666505',
#     '324022:181316760',
#     '324022:181219702',
#     '324022:181345380',
#     '324022:180713478',
#     '324022:181381957',
#     '324022:182838735',
#     '324022:182671022',
#     '324022:182947972',
#     '324022:181963473',
#     '324022:183246234',
#     '324022:182153807',
#     '324022:182607624',
#     '324022:183276465',
#     '324022:183576609',
#     '324022:182332555',
#     '324022:183062666',
#     '324022:184877794',
#     '324022:183742314',
#     '324022:184990961',
#     '324022:184608880',
#     '324022:183641722',
#     '324022:185227403',
#     '324022:184703905',
#     '324022:184482600',
#     '324022:184054334',
#     '324022:186902927',
#     '324022:186444351',
#     '324022:186003062',
#     '324022:185371725',
#     '324022:187078918',
#     '324022:185371215',
#     '324022:187054050',
#     '324022:186260884',
#     '324022:186143411',
#     '324022:186641352',
#     '324022:186611659',
#     '324022:186864979',
#     '324022:187399731',
#     '324022:188556961',
#     '324022:188430893',
#     '324022:188402668',
#     '324022:187291154',
#     '324022:187476054',
#     '324022:187607009',
#     '324022:189718997',
#     '324022:189739755',
#     '324022:190457085',
#     '324022:190330569',
#     '324022:191447093',
#     '324022:192005251',
#     '324022:191864131',
#     #'324022:190600684',
#     '324022:191303860',
#     '324022:192311802',
#     '324022:190794108',
#     '324022:191059674',
#     '324022:192275064',
#     '324022:191345231',
#     '324022:191635311',
#     '324022:190638421',
#     '324022:191410778',
#     '324022:192439125',
#     '324022:193884862',
#     '324022:192517436',
#     '324022:192371006',
#     '324022:193487723',
#     '324022:193466069',
#     '324022:193989751',
#     '324022:193931136',
#     '324022:192763133',
#     '324022:192730168',
#     '324022:193853274',
#     '324022:192977799',
#     '324022:195198654',
#     '324022:195033247',
#     '324022:195688200',
#     '324022:194678597',
#     '324022:194588490',
#     '324022:194829849',
#     '324022:194747531',
#     '324022:194820780',
#     '324022:196583442',
#     '324022:195999410',
#     '324022:197072429',
#     '324022:197015245',
#     '324022:196051626',
#     '324022:197225177',
#     '324022:196486052',
#     '324022:196198869',
#     '324022:195843998',
#     '324022:196833167',
#     '324022:195930597',
#     '324022:198066751',
#     '324022:198196399',
#     '324022:198408303',
#     '324022:198652491',
#     '324022:197978958',
#                             )
)

  
from FWCore.MessageLogger.MessageLogger_cfi import *

process.add_(
    cms.Service('ISpyService',
    outputFileName = cms.untracked.string('miniAOD.ig'),
    outputIg = cms.untracked.bool(True),
    outputMaxEvents = cms.untracked.int32(30), # These are the number of events per ig file 
    debug = cms.untracked.bool(False)
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(30) # These are the number of events to cycle through in the input root file
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
    )

# process.load('ISpy.Analyzers.ISpyEvent_cfi')
# process.load('ISpy.Analyzers.ISpyEBRecHit_cfi')
# process.load('ISpy.Analyzers.ISpyEERecHit_cfi')
# process.load('ISpy.Analyzers.ISpyESRecHit_cfi')

# process.load('ISpy.Analyzers.ISpyHBRecHit_cfi')
# process.load('ISpy.Analyzers.ISpyHERecHit_cfi')

# process.load('ISpy.Analyzers.ISpyGenJet_cfi')

# process.load('ISpy.Analyzers.ISpyPATMuon_cfi')
# process.load('ISpy.Analyzers.ISpyPATElectron_cfi')
# process.load('ISpy.Analyzers.ISpyPATJet_cfi')
# process.load('ISpy.Analyzers.ISpyPATMET_cfi')
# process.load('ISpy.Analyzers.ISpyPATPhoton_cfi')

# process.load('ISpy.Analyzers.ISpyPackedCandidate_cfi')
# process.load('ISpy.Analyzers.ISpyVertex_cfi')

# process.ISpyEBRecHit.iSpyEBRecHitTag = cms.InputTag('reducedEgamma:reducedEBRecHits')
# process.ISpyEERecHit.iSpyEERecHitTag = cms.InputTag('reducedEgamma:reducedEERecHits')
# process.ISpyESRecHit.iSpyESRecHitTag = cms.InputTag('reducedEgamma:reducedESRecHits')

# process.ISpyHBRecHit.iSpyHBRecHitTag = cms.InputTag('reducedEgamma:reducedHBHEHits')
# process.ISpyHERecHit.iSpyHERecHitTag = cms.InputTag('reducedEgamma:reducedHBHEHits')

# process.ISpyPATElectron.iSpyPATElectronTag = cms.InputTag('slimmedElectrons')
# process.ISpyPATElectron.isAOD = cms.untracked.bool(True)

#process.ISpyPackedCandidate.iSpyPackedCandidateTag = cms.InputTag('packedPFCandidates')

# process.ISpyGenJet.iSpyGenJetTag = cms.InputTag('slimmedGenJetsAK8SoftDropSubJets')   
# process.ISpyPATJet.iSpyPATJetTag = cms.InputTag('slimmedJets')
# process.ISpyPATMET.iSpyPATMETTag = cms.InputTag('slimmedMETs')

# process.ISpyPATMuon.iSpyPATMuonTag = cms.InputTag("slimmedMuons")

# process.ISpyPATPhoton.iSpyPATPhotonTag = cms.InputTag('slimmedPhotons')

# process.ISpyVertex.iSpyPriVertexTag = cms.InputTag('offlineSlimmedPrimaryVertices')

# process.iSpy = cms.Path(process.ISpyEvent*
#                         process.ISpyEBRecHit*
#                         process.ISpyEERecHit*
#                         process.ISpyESRecHit*
#                         process.ISpyHBRecHit*
#                         process.ISpyHERecHit*
#                         process.ISpyPATElectron*
#                         process.ISpyPATJet*
#                         process.ISpyPATMET*
#                         process.ISpyPATMuon*
#                         process.ISpyPATPhoton*
#                         process.ISpyPackedCandidate*
#                         process.ISpyVertex)

process.load("ISpy.Analyzers.ISpyEvent_cfi")

process.load('ISpy.Analyzers.ISpyEBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyEERecHit_cfi')
process.load('ISpy.Analyzers.ISpyESRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHERecHit_cfi')
process.load('ISpy.Analyzers.ISpyHFRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHORecHit_cfi')
process.load('ISpy.Analyzers.ISpyPFEcalRecHit_cfi')
process.load('ISpy.Analyzers.ISpyPFHcalRecHit_cfi')

process.load('ISpy.Analyzers.ISpyPATMuon_cfi')
#process.load('ISpy.Analyzers.ISpyPATElectron_cfi')
process.load('ISpy.Analyzers.ISpyPATPhoton_cfi')
process.load('ISpy.Analyzers.ISpyPackedCandidate_cfi')
process.load('ISpy.Analyzers.ISpyVertex_cfi')
process.load('ISpy.Analyzers.ISpyPATJet_cfi')
process.load('ISpy.Analyzers.ISpyPATMET_cfi')


process.ISpyEBRecHit.iSpyEBRecHitTag = cms.InputTag('reducedEgamma:reducedEBRecHits')
process.ISpyEERecHit.iSpyEERecHitTag = cms.InputTag('reducedEgamma:reducedEERecHits')
process.ISpyESRecHit.iSpyESRecHitTag = cms.InputTag('reducedEgamma:reducedESRecHits')

process.ISpyHBRecHit.iSpyHBRecHitTag = cms.InputTag('reducedEgamma:reducedHBHEHits')
process.ISpyHERecHit.iSpyHERecHitTag = cms.InputTag('reducedEgamma:reducedHBHEHits')

#process.ISpyPATElectron.iSpyPATElectronTag          = cms.InputTag('slimmedElectrons')
process.ISpyPATMuon.iSpyPATMuonTag                  = cms.InputTag("slimmedMuons")
process.ISpyPackedCandidate.iSpyPackedCandidateTag  = cms.InputTag('packedPFCandidates')
process.ISpyPATJet.iSpyPATJetTag                    = cms.InputTag('slimmedJets')
process.ISpyPATMET.iSpyPATMETTag                    = cms.InputTag('slimmedMETsPuppi')
process.ISpyVertex.iSpyPriVertexTag                 = cms.InputTag('offlineSlimmedPrimaryVertices')

process.ISpyPATJet.etMin = cms.double(15.0)
process.ISpyPATJet.etaMax = cms.double(2.5)
process.ISpyPATMuon.ptMin = cms.double(15.0)


process.iSpy = cms.Path(process.ISpyEvent*
                        process.ISpyPFEcalRecHit*
                        process.ISpyPFHcalRecHit*
                        process.ISpyPackedCandidate*
                        process.ISpyPATMuon*
                        process.ISpyPATJet*
                        process.ISpyPATMET*
                        process.ISpyVertex*
                        process.ISpyEvent*
                        process.ISpyEBRecHit*
                        process.ISpyEERecHit*
                        process.ISpyESRecHit*
                        process.ISpyHBRecHit*
                        process.ISpyHERecHit*
                        #process.ISpyPATElectron*
                        process.ISpyPATPhoton*
                        process.ISpyVertex)

process.schedule = cms.Schedule(process.iSpy)



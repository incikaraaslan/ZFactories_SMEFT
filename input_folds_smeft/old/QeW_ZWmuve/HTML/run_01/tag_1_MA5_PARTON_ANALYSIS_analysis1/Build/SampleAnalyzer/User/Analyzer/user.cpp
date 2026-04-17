#include "SampleAnalyzer/User/Analyzer/user.h"
using namespace MA5;

MAbool user::Initialize(const MA5::Configuration& cfg,
                      const std::map<std::string,std::string>& parameters)
{
  // Initializing PhysicsService for MC
  PHYSICS->mcConfig().Reset();

  // definition of the multiparticle "hadronic"
  PHYSICS->mcConfig().AddHadronicId(-5);
  PHYSICS->mcConfig().AddHadronicId(-4);
  PHYSICS->mcConfig().AddHadronicId(-3);
  PHYSICS->mcConfig().AddHadronicId(-2);
  PHYSICS->mcConfig().AddHadronicId(-1);
  PHYSICS->mcConfig().AddHadronicId(1);
  PHYSICS->mcConfig().AddHadronicId(2);
  PHYSICS->mcConfig().AddHadronicId(3);
  PHYSICS->mcConfig().AddHadronicId(4);
  PHYSICS->mcConfig().AddHadronicId(5);
  PHYSICS->mcConfig().AddHadronicId(21);

  // definition of the multiparticle "invisible"
  PHYSICS->mcConfig().AddInvisibleId(-16);
  PHYSICS->mcConfig().AddInvisibleId(-14);
  PHYSICS->mcConfig().AddInvisibleId(-12);
  PHYSICS->mcConfig().AddInvisibleId(12);
  PHYSICS->mcConfig().AddInvisibleId(14);
  PHYSICS->mcConfig().AddInvisibleId(16);

  // ===== Signal region ===== //
  Manager()->AddRegionSelection("myregion");

  // ===== Selections ===== //

  // ===== Histograms ===== //
  Manager()->AddHisto("1_THT", 40,0.0,500.0);
  Manager()->AddHisto("2_MET", 40,0.0,500.0);
  Manager()->AddHisto("3_SQRTS", 40,0.0,500.0);
  Manager()->AddHisto("4_PT", 40,0.0,500.0);
  Manager()->AddHisto("5_ETA", 40,-10.0,10.0);
  Manager()->AddHisto("6_MT_MET", 40,0.0,500.0);

  // No problem during initialization
  return true;
}

MAbool user::Execute(SampleFormat& sample, const EventFormat& event)
{
  MAfloat32 __event_weight__ = 1.0;
  if (weighted_events_ && event.mc()!=0) __event_weight__ = event.mc()->weight();

  if (sample.mc()!=0) sample.mc()->addWeightedEvents(__event_weight__);
  Manager()->InitializeForNewEvent(__event_weight__);

  // Clearing particle containers
  {
      _P_mu_m_I1I_PTorderingfinalstate_REG_.clear();
      _P_mu_mPTorderingfinalstate_REG_.clear();
  }

  // Filling particle containers
  {
    for (MAuint32 i=0;i<event.mc()->particles().size();i++)
    {
      if (isP__mu_mPTorderingfinalstate((&(event.mc()->particles()[i])))) _P_mu_mPTorderingfinalstate_REG_.push_back(&(event.mc()->particles()[i]));
    }
  }

  // Sorting particles
  // Sorting particle collection according to PTordering
  // for getting 1th particle
  _P_mu_m_I1I_PTorderingfinalstate_REG_=SORTER->rankFilter(_P_mu_mPTorderingfinalstate_REG_,1,PTordering);

  // Histogram number 1
  //   * Plot: THT
  {
    Manager()->FillHisto("1_THT", PHYSICS->Transverse->EventTHT(event.mc()));
  }

  // Histogram number 2
  //   * Plot: MET
  {
    Manager()->FillHisto("2_MET", PHYSICS->Transverse->EventMET(event.mc()));
  }

  // Histogram number 3
  //   * Plot: SQRTS
  {
    Manager()->FillHisto("3_SQRTS", PHYSICS->SqrtS(event.mc()));
  }

  // Histogram number 4
  //   * Plot: PT ( mu-[1] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_mu_m_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("4_PT", _P_mu_m_I1I_PTorderingfinalstate_REG_[ind[0]]->pt());
    }
  }
  }

  // Histogram number 5
  //   * Plot: ETA ( mu-[1] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_mu_m_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("5_ETA", _P_mu_m_I1I_PTorderingfinalstate_REG_[ind[0]]->eta());
    }
  }
  }

  // Histogram number 6
  //   * Plot: MT_MET ( mu-[1] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_mu_m_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("6_MT_MET", _P_mu_m_I1I_PTorderingfinalstate_REG_[ind[0]]->mt_met(event.mc()->MET().momentum()));
    }
  }
  }

  return true;
}

void user::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

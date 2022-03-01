# Instructions
In order to run this validation a few quick changes are needed to a few files 

## src/SteppingAction.cc

void SteppingAction::txtPrint(const G4Step *aStep) {
  G4Track *Track = aStep->GetTrack();
  G4StepPoint *PointPre = aStep->GetPreStepPoint();
  G4StepPoint *PointPost = aStep->GetPostStepPoint();
  if(true) {
    if(PointPre->GetPhysicalVolume() && PointPost->GetPhysicalVolume()) {
                std::ofstream outfile;
                outfile.open("data.txt", std::ios_base::app);
                outfile << std::setprecision(9);
                outfile << PointPre->GetPosition().x() << ',' << PointPre->GetPosition().y() << ',' << PointPre->GetPosition().z() << ',' <<  PointPost->GetPosition().x()<< ','
         << PointPost->GetPosition().y()<< ',' << PointPost->GetPosition().z()<< ',' <<  PointPost->GetGlobalTime() << ','
        <<  PointPre->GetPhysicalVolume()->GetName().data() << ',' <<  PointPost->GetPhysicalVolume()->GetName().data() << ',' <<  Track->GetParticleDefinition()->GetParticleName().data() << std::endl;
                outfile.close();
}
}
}

## include/SteppingAction.hh
void txtPrint(const G4Step *aStep);

## src/EventAction.cc
if(true) {
    std::ofstream outfile;
    outfile.open("data.txt", std::ios_base::app);
    outfile << "================= EVENT " << evt->GetEventID() << "=================" << std::endl;
    outfile.close();
    };

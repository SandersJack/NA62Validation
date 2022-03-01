# Instructions
In order to run this validation a few quick changes are needed to a few files 

## src/SteppingAction.cc

void SteppingAction::txtPrint(const G4Step *aStep) { <br />
  G4Track *Track = aStep->GetTrack();<br />
  G4StepPoint *PointPre = aStep->GetPreStepPoint();<br />
  G4StepPoint *PointPost = aStep->GetPostStepPoint();<br />
  if(true) {<br />
    if(PointPre->GetPhysicalVolume() && PointPost->GetPhysicalVolume()) { <br />
                std::ofstream outfile;<br />
                outfile.open("data.txt", std::ios_base::app);<br />
                outfile << std::setprecision(9);<br />
                outfile << PointPre->GetPosition().x() << ',' << PointPre->GetPosition().y() << ',' << PointPre->GetPosition().z() << ',' <<  PointPost->GetPosition().x()<< ',' <br />
         << PointPost->GetPosition().y()<< ',' << PointPost->GetPosition().z()<< ',' <<  PointPost->GetGlobalTime() << ',' <br />
        <<  PointPre->GetPhysicalVolume()->GetName().data() << ',' <<  PointPost->GetPhysicalVolume()->GetName().data() << ',' <<  Track->GetParticleDefinition()->GetParticleName().data() << std::endl; <br />
                outfile.close();<br />
}<br />
}<br />
}<br />

## include/SteppingAction.hh
void txtPrint(const G4Step *aStep);

## src/EventAction.cc
if(true) { <br />
    std::ofstream outfile; <br />
    outfile.open("data.txt", std::ios_base::app); <br />
    outfile << "================= EVENT " << evt->GetEventID() << "=================" << std::endl;<br />
    outfile.close();<br />
    };

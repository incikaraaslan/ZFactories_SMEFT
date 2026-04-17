void selection_10()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo21","canvas_plotflow_tempo21",0,0,700,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S11_DELTAR_0 = new TH1F("S11_DELTAR_0","S11_DELTAR_0",40,0.0,10.0);
  // Content
  S11_DELTAR_0->SetBinContent(0,0.0); // underflow
  S11_DELTAR_0->SetBinContent(1,0.018390123327925355);
  S11_DELTAR_0->SetBinContent(2,0.03972267018687976);
  S11_DELTAR_0->SetBinContent(3,0.0709858786448073);
  S11_DELTAR_0->SetBinContent(4,0.09636424463893474);
  S11_DELTAR_0->SetBinContent(5,0.1393970926416546);
  S11_DELTAR_0->SetBinContent(6,0.18610809725997335);
  S11_DELTAR_0->SetBinContent(7,0.24569208344752588);
  S11_DELTAR_0->SetBinContent(8,0.30380481058747555);
  S11_DELTAR_0->SetBinContent(9,0.35897516877572005);
  S11_DELTAR_0->SetBinContent(10,0.4001690634233051);
  S11_DELTAR_0->SetBinContent(11,0.4354780874177689);
  S11_DELTAR_0->SetBinContent(12,0.4649022825432826);
  S11_DELTAR_0->SetBinContent(13,0.407892979196798);
  S11_DELTAR_0->SetBinContent(14,0.20302698793029866);
  S11_DELTAR_0->SetBinContent(15,0.12284602083167741);
  S11_DELTAR_0->SetBinContent(16,0.0709858786448073);
  S11_DELTAR_0->SetBinContent(17,0.04523970198722652);
  S11_DELTAR_0->SetBinContent(18,0.026481777992061035);
  S11_DELTAR_0->SetBinContent(19,0.013976495328617375);
  S11_DELTAR_0->SetBinContent(20,0.006988246664687371);
  S11_DELTAR_0->SetBinContent(21,0.0062526423313431475);
  S11_DELTAR_0->SetBinContent(22,0.0029424193326195295);
  S11_DELTAR_0->SetBinContent(23,0.0025746176657580762);
  S11_DELTAR_0->SetBinContent(24,0.0007356049331170142);
  S11_DELTAR_0->SetBinContent(25,0.0018390123327925352);
  S11_DELTAR_0->SetBinContent(26,0.0011034069998269943);
  S11_DELTAR_0->SetBinContent(27,0.0);
  S11_DELTAR_0->SetBinContent(28,0.0003678024665585071);
  S11_DELTAR_0->SetBinContent(29,0.0003678024665585071);
  S11_DELTAR_0->SetBinContent(30,0.0);
  S11_DELTAR_0->SetBinContent(31,0.0);
  S11_DELTAR_0->SetBinContent(32,0.0);
  S11_DELTAR_0->SetBinContent(33,0.0);
  S11_DELTAR_0->SetBinContent(34,0.0);
  S11_DELTAR_0->SetBinContent(35,0.0);
  S11_DELTAR_0->SetBinContent(36,0.0);
  S11_DELTAR_0->SetBinContent(37,0.0);
  S11_DELTAR_0->SetBinContent(38,0.0);
  S11_DELTAR_0->SetBinContent(39,0.0);
  S11_DELTAR_0->SetBinContent(40,0.0);
  S11_DELTAR_0->SetBinContent(41,0.0); // overflow
  S11_DELTAR_0->SetEntries(10000);
  // Style
  S11_DELTAR_0->SetLineColor(9);
  S11_DELTAR_0->SetLineStyle(1);
  S11_DELTAR_0->SetLineWidth(1);
  S11_DELTAR_0->SetFillColor(9);
  S11_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_22","mystack");
  stack->Add(S11_DELTAR_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 10 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("#DeltaR [ e-_{1}, mu+_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_10.png");

}

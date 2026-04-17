void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo17","canvas_plotflow_tempo17",0,0,700,500);
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
  TH1F* S9_DELTAR_0 = new TH1F("S9_DELTAR_0","S9_DELTAR_0",40,0.0,10.0);
  // Content
  S9_DELTAR_0->SetBinContent(0,0.0); // underflow
  S9_DELTAR_0->SetBinContent(1,0.0);
  S9_DELTAR_0->SetBinContent(2,0.0);
  S9_DELTAR_0->SetBinContent(3,0.0);
  S9_DELTAR_0->SetBinContent(4,0.0);
  S9_DELTAR_0->SetBinContent(5,0.0);
  S9_DELTAR_0->SetBinContent(6,0.0);
  S9_DELTAR_0->SetBinContent(7,0.0);
  S9_DELTAR_0->SetBinContent(8,0.0);
  S9_DELTAR_0->SetBinContent(9,0.0);
  S9_DELTAR_0->SetBinContent(10,0.0);
  S9_DELTAR_0->SetBinContent(11,0.0);
  S9_DELTAR_0->SetBinContent(12,0.0);
  S9_DELTAR_0->SetBinContent(13,328.51438691210893);
  S9_DELTAR_0->SetBinContent(14,217.04819135288074);
  S9_DELTAR_0->SetBinContent(15,99.02506605487818);
  S9_DELTAR_0->SetBinContent(16,64.81182741792088);
  S9_DELTAR_0->SetBinContent(17,40.09758840252698);
  S9_DELTAR_0->SetBinContent(18,27.992658884782877);
  S9_DELTAR_0->SetBinContent(19,17.48489930340811);
  S9_DELTAR_0->SetBinContent(20,12.86148948760304);
  S9_DELTAR_0->SetBinContent(21,9.330885628260985);
  S9_DELTAR_0->SetBinContent(22,6.304651748825018);
  S9_DELTAR_0->SetBinContent(23,4.6234118158049915);
  S9_DELTAR_0->SetBinContent(24,2.858108886134004);
  S9_DELTAR_0->SetBinContent(25,2.0174889196239914);
  S9_DELTAR_0->SetBinContent(26,1.6812409330199862);
  S9_DELTAR_0->SetBinContent(27,1.1768679531140183);
  S9_DELTAR_0->SetBinContent(28,1.344992946415981);
  S9_DELTAR_0->SetBinContent(29,0.7565582698589998);
  S9_DELTAR_0->SetBinContent(30,0.6724962732079985);
  S9_DELTAR_0->SetBinContent(31,0.6724962732079985);
  S9_DELTAR_0->SetBinContent(32,0.16812409330199862);
  S9_DELTAR_0->SetBinContent(33,0.3362480866040012);
  S9_DELTAR_0->SetBinContent(34,0.25218608995299996);
  S9_DELTAR_0->SetBinContent(35,0.0);
  S9_DELTAR_0->SetBinContent(36,0.0840620266510001);
  S9_DELTAR_0->SetBinContent(37,0.16812409330199862);
  S9_DELTAR_0->SetBinContent(38,0.0);
  S9_DELTAR_0->SetBinContent(39,0.0840620266510001);
  S9_DELTAR_0->SetBinContent(40,0.0840620266510001);
  S9_DELTAR_0->SetBinContent(41,0.16812409330199862); // overflow
  S9_DELTAR_0->SetEntries(10000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ mu-_{1}, mu+_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");

}

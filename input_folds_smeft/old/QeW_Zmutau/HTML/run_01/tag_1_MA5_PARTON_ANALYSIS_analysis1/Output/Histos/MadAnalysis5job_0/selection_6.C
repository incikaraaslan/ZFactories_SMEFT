void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo13","canvas_plotflow_tempo13",0,0,700,500);
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
  TH1F* S7_ETA_0 = new TH1F("S7_ETA_0","S7_ETA_0",40,-10.0,10.0);
  // Content
  S7_ETA_0->SetBinContent(0,0.0); // underflow
  S7_ETA_0->SetBinContent(1,0.0);
  S7_ETA_0->SetBinContent(2,0.0);
  S7_ETA_0->SetBinContent(3,0.0);
  S7_ETA_0->SetBinContent(4,0.0);
  S7_ETA_0->SetBinContent(5,0.0);
  S7_ETA_0->SetBinContent(6,0.0);
  S7_ETA_0->SetBinContent(7,0.0);
  S7_ETA_0->SetBinContent(8,0.0);
  S7_ETA_0->SetBinContent(9,0.0);
  S7_ETA_0->SetBinContent(10,0.0);
  S7_ETA_0->SetBinContent(11,9.47e-08);
  S7_ETA_0->SetBinContent(12,1.894e-07);
  S7_ETA_0->SetBinContent(13,6.629e-07);
  S7_ETA_0->SetBinContent(14,1.3258e-06);
  S7_ETA_0->SetBinContent(15,4.4509e-06);
  S7_ETA_0->SetBinContent(16,8.7124e-06);
  S7_ETA_0->SetBinContent(17,2.97358e-05);
  S7_ETA_0->SetBinContent(18,6.70476e-05);
  S7_ETA_0->SetBinContent(19,0.0001446069);
  S7_ETA_0->SetBinContent(20,0.000214022);
  S7_ETA_0->SetBinContent(21,0.0002200828);
  S7_ETA_0->SetBinContent(22,0.0001414818);
  S7_ETA_0->SetBinContent(23,7.11197e-05);
  S7_ETA_0->SetBinContent(24,2.68001e-05);
  S7_ETA_0->SetBinContent(25,1.02276e-05);
  S7_ETA_0->SetBinContent(26,4.6403e-06);
  S7_ETA_0->SetBinContent(27,1.1364e-06);
  S7_ETA_0->SetBinContent(28,5.682e-07);
  S7_ETA_0->SetBinContent(29,9.47e-08);
  S7_ETA_0->SetBinContent(30,0.0);
  S7_ETA_0->SetBinContent(31,0.0);
  S7_ETA_0->SetBinContent(32,0.0);
  S7_ETA_0->SetBinContent(33,0.0);
  S7_ETA_0->SetBinContent(34,0.0);
  S7_ETA_0->SetBinContent(35,0.0);
  S7_ETA_0->SetBinContent(36,0.0);
  S7_ETA_0->SetBinContent(37,0.0);
  S7_ETA_0->SetBinContent(38,0.0);
  S7_ETA_0->SetBinContent(39,0.0);
  S7_ETA_0->SetBinContent(40,0.0);
  S7_ETA_0->SetBinContent(41,0.0); // overflow
  S7_ETA_0->SetEntries(10000);
  // Style
  S7_ETA_0->SetLineColor(9);
  S7_ETA_0->SetLineStyle(1);
  S7_ETA_0->SetLineWidth(1);
  S7_ETA_0->SetFillColor(9);
  S7_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_14","mystack");
  stack->Add(S7_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ ta+_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_6.png");

}

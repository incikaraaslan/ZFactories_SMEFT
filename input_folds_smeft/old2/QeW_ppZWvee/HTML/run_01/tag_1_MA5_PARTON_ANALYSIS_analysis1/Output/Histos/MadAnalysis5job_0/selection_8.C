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
  TH1F* S9_ETA_0 = new TH1F("S9_ETA_0","S9_ETA_0",40,-10.0,10.0);
  // Content
  S9_ETA_0->SetBinContent(0,0.0); // underflow
  S9_ETA_0->SetBinContent(1,0.0);
  S9_ETA_0->SetBinContent(2,0.0);
  S9_ETA_0->SetBinContent(3,0.0);
  S9_ETA_0->SetBinContent(4,0.0);
  S9_ETA_0->SetBinContent(5,0.0);
  S9_ETA_0->SetBinContent(6,0.0);
  S9_ETA_0->SetBinContent(7,0.0003678024706018292);
  S9_ETA_0->SetBinContent(8,0.0007356049412036584);
  S9_ETA_0->SetBinContent(9,0.002206815023535241);
  S9_ETA_0->SetBinContent(10,0.0062526424000796275);
  S9_ETA_0->SetBinContent(11,0.015079897496113952);
  S9_ETA_0->SetBinContent(12,0.03825145794221156);
  S9_ETA_0->SetBinContent(13,0.06804345406247442);
  S9_ETA_0->SetBinContent(14,0.13498346612624543);
  S9_ETA_0->SetBinContent(15,0.19714211944439808);
  S9_ETA_0->SetBinContent(16,0.23208338314059035);
  S9_ETA_0->SetBinContent(17,0.25893291211398767);
  S9_ETA_0->SetBinContent(18,0.28872492642735864);
  S9_ETA_0->SetBinContent(19,0.2946097971451734);
  S9_ETA_0->SetBinContent(20,0.2931385544751865);
  S9_ETA_0->SetBinContent(21,0.3122643093364847);
  S9_ETA_0->SetBinContent(22,0.2780586669752858);
  S9_ETA_0->SetBinContent(23,0.28284005570954396);
  S9_ETA_0->SetBinContent(24,0.27107041423604733);
  S9_ETA_0->SetBinContent(25,0.23833601454483538);
  S9_ETA_0->SetBinContent(26,0.18831486334874242);
  S9_ETA_0->SetBinContent(27,0.1327767020833979);
  S9_ETA_0->SetBinContent(28,0.07356049412036585);
  S9_ETA_0->SetBinContent(29,0.039354868152956766);
  S9_ETA_0->SetBinContent(30,0.015447704564973887);
  S9_ETA_0->SetBinContent(31,0.00662044427090866);
  S9_ETA_0->SetBinContent(32,0.003310222035492197);
  S9_ETA_0->SetBinContent(33,0.0007356049412036584);
  S9_ETA_0->SetBinContent(34,0.0);
  S9_ETA_0->SetBinContent(35,0.0003678024706018292);
  S9_ETA_0->SetBinContent(36,0.0);
  S9_ETA_0->SetBinContent(37,0.0);
  S9_ETA_0->SetBinContent(38,0.0);
  S9_ETA_0->SetBinContent(39,0.0);
  S9_ETA_0->SetBinContent(40,0.0);
  S9_ETA_0->SetBinContent(41,0.0); // overflow
  S9_ETA_0->SetEntries(10000);
  // Style
  S9_ETA_0->SetLineColor(9);
  S9_ETA_0->SetLineStyle(1);
  S9_ETA_0->SetLineWidth(1);
  S9_ETA_0->SetFillColor(9);
  S9_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ mu+_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");

}

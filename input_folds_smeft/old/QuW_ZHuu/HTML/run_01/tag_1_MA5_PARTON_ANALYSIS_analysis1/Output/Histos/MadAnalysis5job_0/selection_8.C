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
  S9_DELTAR_0->SetBinContent(13,3.182324803300012);
  S9_DELTAR_0->SetBinContent(14,1.5939939014749904);
  S9_DELTAR_0->SetBinContent(15,0.48470997004000177);
  S9_DELTAR_0->SetBinContent(16,0.21007878701499771);
  S9_DELTAR_0->SetBinContent(17,0.10249129366499729);
  S9_DELTAR_0->SetBinContent(18,0.04303499734000016);
  S9_DELTAR_0->SetBinContent(19,0.020384998740000077);
  S9_DELTAR_0->SetBinContent(20,0.012457499230000047);
  S9_DELTAR_0->SetBinContent(21,0.006228749615000024);
  S9_DELTAR_0->SetBinContent(22,0.0022649998600000085);
  S9_DELTAR_0->SetBinContent(23,0.0022649998600000085);
  S9_DELTAR_0->SetBinContent(24,0.0005662499650000021);
  S9_DELTAR_0->SetBinContent(25,0.0005662499650000021);
  S9_DELTAR_0->SetBinContent(26,0.0011324999300000042);
  S9_DELTAR_0->SetBinContent(27,0.0);
  S9_DELTAR_0->SetBinContent(28,0.0);
  S9_DELTAR_0->SetBinContent(29,0.0);
  S9_DELTAR_0->SetBinContent(30,0.0);
  S9_DELTAR_0->SetBinContent(31,0.0);
  S9_DELTAR_0->SetBinContent(32,0.0);
  S9_DELTAR_0->SetBinContent(33,0.0);
  S9_DELTAR_0->SetBinContent(34,0.0);
  S9_DELTAR_0->SetBinContent(35,0.0);
  S9_DELTAR_0->SetBinContent(36,0.0);
  S9_DELTAR_0->SetBinContent(37,0.0);
  S9_DELTAR_0->SetBinContent(38,0.0);
  S9_DELTAR_0->SetBinContent(39,0.0);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,0.0); // overflow
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
  stack->GetXaxis()->SetTitle("#DeltaR [ u_{1}, u~_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");

}

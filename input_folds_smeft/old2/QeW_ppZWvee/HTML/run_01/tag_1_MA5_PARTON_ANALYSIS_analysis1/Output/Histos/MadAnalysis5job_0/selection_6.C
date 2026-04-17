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
  S7_ETA_0->SetBinContent(6,0.0007356049396423756);
  S7_ETA_0->SetBinContent(7,0.0003678024698211878);
  S7_ETA_0->SetBinContent(8,0.0044136300377027845);
  S7_ETA_0->SetBinContent(9,0.005149234377572364);
  S7_ETA_0->SetBinContent(10,0.013976495452599257);
  S7_ETA_0->SetBinContent(11,0.03825145966034325);
  S7_ETA_0->SetBinContent(12,0.07429609530524317);
  S7_ETA_0->SetBinContent(13,0.10923737712038258);
  S7_ETA_0->SetBinContent(14,0.16477548008988915);
  S7_ETA_0->SetBinContent(15,0.182797852891512);
  S7_ETA_0->SetBinContent(16,0.222888265923303);
  S7_ETA_0->SetBinContent(17,0.23980725670584396);
  S7_ETA_0->SetBinContent(18,0.2361291500386834);
  S7_ETA_0->SetBinContent(19,0.27107041366071466);
  S7_ETA_0->SetBinContent(20,0.26445002158409076);
  S7_ETA_0->SetBinContent(21,0.26739240695568667);
  S7_ETA_0->SetBinContent(22,0.2677601676413364);
  S7_ETA_0->SetBinContent(23,0.24238178142965755);
  S7_ETA_0->SetBinContent(24,0.22950875796205947);
  S7_ETA_0->SetBinContent(25,0.2243594668059958);
  S7_ETA_0->SetBinContent(26,0.1949353299972774);
  S7_ETA_0->SetBinContent(27,0.1728671148333773);
  S7_ETA_0->SetBinContent(28,0.1151221478635744);
  S7_ETA_0->SetBinContent(29,0.07282489262323195);
  S7_ETA_0->SetBinContent(30,0.03494123363339152);
  S7_ETA_0->SetBinContent(31,0.015447708130823721);
  S7_ETA_0->SetBinContent(32,0.005517037047317818);
  S7_ETA_0->SetBinContent(33,0.001839012349105939);
  S7_ETA_0->SetBinContent(34,0.0003678024698211878);
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
  stack->GetXaxis()->SetTitle("#eta [ e-_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_6.png");

}

void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo9","canvas_plotflow_tempo9",0,0,700,500);
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
  TH1F* S5_ETA_0 = new TH1F("S5_ETA_0","S5_ETA_0",40,-10.0,10.0);
  // Content
  S5_ETA_0->SetBinContent(0,0.0); // underflow
  S5_ETA_0->SetBinContent(1,0.0);
  S5_ETA_0->SetBinContent(2,0.0);
  S5_ETA_0->SetBinContent(3,0.0);
  S5_ETA_0->SetBinContent(4,0.0);
  S5_ETA_0->SetBinContent(5,0.0);
  S5_ETA_0->SetBinContent(6,0.0);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,0.0);
  S5_ETA_0->SetBinContent(10,0.08406199160000082);
  S5_ETA_0->SetBinContent(11,0.08406199160000082);
  S5_ETA_0->SetBinContent(12,0.16812398320000163);
  S5_ETA_0->SetBinContent(13,0.504371949600005);
  S5_ETA_0->SetBinContent(14,1.5131158488000147);
  S5_ETA_0->SetBinContent(15,2.858107714400028);
  S5_ETA_0->SetBinContent(16,10.003379000399898);
  S5_ETA_0->SetBinContent(17,24.798287522000244);
  S5_ETA_0->SetBinContent(18,64.22336358240042);
  S5_ETA_0->SetBinContent(19,123.99148760999621);
  S5_ETA_0->SetBinContent(20,193.4266806715981);
  S5_ETA_0->SetBinContent(21,191.15698089840066);
  S5_ETA_0->SetBinContent(22,128.69888713960347);
  S5_ETA_0->SetBinContent(23,60.86088391840039);
  S5_ETA_0->SetBinContent(24,23.537357648000228);
  S5_ETA_0->SetBinContent(25,8.910571109600086);
  S5_ETA_0->SetBinContent(26,3.4465416556000337);
  S5_ETA_0->SetBinContent(27,1.6812398320000164);
  S5_ETA_0->SetBinContent(28,0.4203099580000041);
  S5_ETA_0->SetBinContent(29,0.08406199160000082);
  S5_ETA_0->SetBinContent(30,0.16812398320000163);
  S5_ETA_0->SetBinContent(31,0.0);
  S5_ETA_0->SetBinContent(32,0.0);
  S5_ETA_0->SetBinContent(33,0.0);
  S5_ETA_0->SetBinContent(34,0.0);
  S5_ETA_0->SetBinContent(35,0.0);
  S5_ETA_0->SetBinContent(36,0.0);
  S5_ETA_0->SetBinContent(37,0.0);
  S5_ETA_0->SetBinContent(38,0.0);
  S5_ETA_0->SetBinContent(39,0.0);
  S5_ETA_0->SetBinContent(40,0.0);
  S5_ETA_0->SetBinContent(41,0.0); // overflow
  S5_ETA_0->SetEntries(10000);
  // Style
  S5_ETA_0->SetLineColor(9);
  S5_ETA_0->SetLineStyle(1);
  S5_ETA_0->SetLineWidth(1);
  S5_ETA_0->SetFillColor(9);
  S5_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_10","mystack");
  stack->Add(S5_ETA_0);
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
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_4.png");

}

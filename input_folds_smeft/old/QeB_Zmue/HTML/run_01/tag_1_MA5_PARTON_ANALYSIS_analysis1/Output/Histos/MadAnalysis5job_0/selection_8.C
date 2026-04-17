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
  S9_DELTAR_0->SetBinContent(13,0.00010603639062799813);
  S9_DELTAR_0->SetBinContent(14,6.913407388960086e-05);
  S9_DELTAR_0->SetBinContent(15,3.443126695680043e-05);
  S9_DELTAR_0->SetBinContent(16,1.9197878303199964e-05);
  S9_DELTAR_0->SetBinContent(17,1.2979608852800271e-05);
  S9_DELTAR_0->SetBinContent(18,8.770741224800065e-06);
  S9_DELTAR_0->SetBinContent(19,5.865263481600044e-06);
  S9_DELTAR_0->SetBinContent(20,4.398947611200032e-06);
  S9_DELTAR_0->SetBinContent(21,2.7697077552000207e-06);
  S9_DELTAR_0->SetBinContent(22,2.1180118128000154e-06);
  S9_DELTAR_0->SetBinContent(23,1.4391618728000106e-06);
  S9_DELTAR_0->SetBinContent(24,1.0590059064000077e-06);
  S9_DELTAR_0->SetBinContent(25,8.417739256000062e-07);
  S9_DELTAR_0->SetBinContent(26,7.060039376000052e-07);
  S9_DELTAR_0->SetBinContent(27,5.973879472000044e-07);
  S9_DELTAR_0->SetBinContent(28,2.986939736000022e-07);
  S9_DELTAR_0->SetBinContent(29,2.172319808000016e-07);
  S9_DELTAR_0->SetBinContent(30,1.086159904000008e-07);
  S9_DELTAR_0->SetBinContent(31,2.172319808000016e-07);
  S9_DELTAR_0->SetBinContent(32,8.146199280000061e-08);
  S9_DELTAR_0->SetBinContent(33,0.0);
  S9_DELTAR_0->SetBinContent(34,1.3576998800000102e-07);
  S9_DELTAR_0->SetBinContent(35,2.71539976000002e-08);
  S9_DELTAR_0->SetBinContent(36,2.71539976000002e-08);
  S9_DELTAR_0->SetBinContent(37,2.71539976000002e-08);
  S9_DELTAR_0->SetBinContent(38,0.0);
  S9_DELTAR_0->SetBinContent(39,2.71539976000002e-08);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,2.71539976000002e-08); // overflow
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
  stack->GetXaxis()->SetTitle("#DeltaR [ mu-_{1}, e+_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");

}

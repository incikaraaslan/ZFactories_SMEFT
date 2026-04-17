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
  S9_DELTAR_0->SetBinContent(13,0.0001053963097024993);
  S9_DELTAR_0->SetBinContent(14,6.954908640250084e-05);
  S9_DELTAR_0->SetBinContent(15,3.4000563129999906e-05);
  S9_DELTAR_0->SetBinContent(16,2.0069021847499887e-05);
  S9_DELTAR_0->SetBinContent(17,1.308967120499974e-05);
  S9_DELTAR_0->SetBinContent(18,9.043281832500074e-06);
  S9_DELTAR_0->SetBinContent(19,5.458557502500044e-06);
  S9_DELTAR_0->SetBinContent(20,4.399434405000036e-06);
  S9_DELTAR_0->SetBinContent(21,2.8514852625000233e-06);
  S9_DELTAR_0->SetBinContent(22,1.9553041800000157e-06);
  S9_DELTAR_0->SetBinContent(23,1.439321132500012e-06);
  S9_DELTAR_0->SetBinContent(24,1.0048090925000083e-06);
  S9_DELTAR_0->SetBinContent(25,8.418670775000069e-07);
  S9_DELTAR_0->SetBinContent(26,6.789250625000056e-07);
  S9_DELTAR_0->SetBinContent(27,5.974540550000049e-07);
  S9_DELTAR_0->SetBinContent(28,2.4441302250000197e-07);
  S9_DELTAR_0->SetBinContent(29,1.9009901750000156e-07);
  S9_DELTAR_0->SetBinContent(30,1.357850125000011e-07);
  S9_DELTAR_0->SetBinContent(31,1.9009901750000156e-07);
  S9_DELTAR_0->SetBinContent(32,1.6294201500000133e-07);
  S9_DELTAR_0->SetBinContent(33,0.0);
  S9_DELTAR_0->SetBinContent(34,1.357850125000011e-07);
  S9_DELTAR_0->SetBinContent(35,2.7157002500000224e-08);
  S9_DELTAR_0->SetBinContent(36,5.431400500000045e-08);
  S9_DELTAR_0->SetBinContent(37,2.7157002500000224e-08);
  S9_DELTAR_0->SetBinContent(38,0.0);
  S9_DELTAR_0->SetBinContent(39,2.7157002500000224e-08);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ mu+_{1}, ta-_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");

}

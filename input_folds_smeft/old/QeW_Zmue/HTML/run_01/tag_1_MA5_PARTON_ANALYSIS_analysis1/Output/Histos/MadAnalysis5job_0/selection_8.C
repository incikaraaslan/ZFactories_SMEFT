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
  S9_DELTAR_0->SetBinContent(13,0.00036976049804750017);
  S9_DELTAR_0->SetBinContent(14,0.0002410781987269999);
  S9_DELTAR_0->SetBinContent(15,0.00012006569936599972);
  S9_DELTAR_0->SetBinContent(16,6.69451196465e-05);
  S9_DELTAR_0->SetBinContent(17,4.5261339761e-05);
  S9_DELTAR_0->SetBinContent(18,3.058454983849998e-05);
  S9_DELTAR_0->SetBinContent(19,2.0452819892000016e-05);
  S9_DELTAR_0->SetBinContent(20,1.5339619918999983e-05);
  S9_DELTAR_0->SetBinContent(21,9.658277948999997e-06);
  S9_DELTAR_0->SetBinContent(22,7.385741960999999e-06);
  S9_DELTAR_0->SetBinContent(23,5.018516973499999e-06);
  S9_DELTAR_0->SetBinContent(24,3.6928709804999993e-06);
  S9_DELTAR_0->SetBinContent(25,2.935358984499999e-06);
  S9_DELTAR_0->SetBinContent(26,2.4619139869999993e-06);
  S9_DELTAR_0->SetBinContent(27,2.0831579889999993e-06);
  S9_DELTAR_0->SetBinContent(28,1.0415789944999997e-06);
  S9_DELTAR_0->SetBinContent(29,7.575119959999997e-07);
  S9_DELTAR_0->SetBinContent(30,3.7875599799999987e-07);
  S9_DELTAR_0->SetBinContent(31,7.575119959999997e-07);
  S9_DELTAR_0->SetBinContent(32,2.8406699849999994e-07);
  S9_DELTAR_0->SetBinContent(33,0.0);
  S9_DELTAR_0->SetBinContent(34,4.734449974999999e-07);
  S9_DELTAR_0->SetBinContent(35,9.468899949999997e-08);
  S9_DELTAR_0->SetBinContent(36,9.468899949999997e-08);
  S9_DELTAR_0->SetBinContent(37,9.468899949999997e-08);
  S9_DELTAR_0->SetBinContent(38,0.0);
  S9_DELTAR_0->SetBinContent(39,9.468899949999997e-08);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,9.468899949999997e-08); // overflow
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
  stack->GetXaxis()->SetTitle("#DeltaR [ e+_{1}, mu-_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");

}

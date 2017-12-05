{
    TStyle* style = new TStyle("graphStyle","graphStyle");
    style->SetMarkerSize(3);
    style->SetMarkerColor(kRed);
    style->SetMarkerStyle(8);

    gROOT->SetStyle("graphStyle");
    gROOT->ForceStyle();

    TFile* outputFile = new TFile("eigenvalues.root","RECREATE");
    TMultiGraph* mg = new TMultiGraph("eigenvalues","eigenvalues");

    vector<TGraph*> graphs;

    for(double L=-0.3; L<=0.3; L += 0.01)
    {
        if(L==0)
        {
            continue;
        }

        string fileName;
        stringstream numberFormatter;

        if(L<0)
        {
            numberFormatter << fixed << setprecision(2) << 0-L;
            fileName = "_" + numberFormatter.str() + ".txt";
        }

        else
        {
            numberFormatter << fixed << setprecision(2) << L;
            fileName = numberFormatter.str() + ".txt";
        }

        cout << fileName << endl;

        ifstream file(fileName);

        vector<double> couplingConst;
        vector<double> eigenvalues;

        string line;
        while(file >> line)
        {
            couplingConst.push_back((double)L);
            eigenvalues.push_back(stod(line));
        }

        graphs.push_back(new TGraph(eigenvalues.size(), &eigenvalues[0], &couplingConst[0]));
        mg->Add(graphs.back(), "AP");

        graphs.back()->SetMarkerColor(kRed);
        graphs.back()->SetMarkerSize(1);
    }

    mg->Draw("AP");
    mg->GetYaxis()->SetRangeUser(-10,10);
}

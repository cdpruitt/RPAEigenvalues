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

    for(int L=0; L<=10; L++)
    {
        if(L==0)
        {
            continue;
        }

        string fileName = to_string(L) + ".txt";
        ifstream file(fileName);

        vector<double> couplingConst;
        vector<double> eigenvalues;

        string line;
        while(file >> line)
        {
            couplingConst.push_back((double)L);
            eigenvalues.push_back(stod(line));

            cout << line << endl;
        }

        graphs.push_back(new TGraph(eigenvalues.size(), &eigenvalues[0], &couplingConst[0]));
        mg->Add(graphs.back(), "AP");

        graphs.back()->SetMarkerColor(kRed);
        graphs.back()->SetMarkerSize(3);
    }

    mg->Draw("AP");
}

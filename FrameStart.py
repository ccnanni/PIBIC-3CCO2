import wx

class MainWindow(wx.Frame):

    #Definindo o __init__ (inicialização do objeto)
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,300))

        #Criando uma barra de status no fim da pagina
        self.CreateStatusBar()

        #Criando as abas do menu
        MenuAplicacao = wx.Menu()
        MenuVeiculos = wx.Menu()
        MenuArea = wx.Menu()
        MenuCompensacao= wx.Menu()
        MenuCadastros = wx.Menu()

        #Colocando coisas nessas abas
        menuSobre = MenuAplicacao.Append(wx.ID_ABOUT, "&Sobre", " Sobre o programa")
        MenuAplicacao.AppendSeparator()
        menuSair = MenuAplicacao.Append(wx.ID_EXIT,"&Sair"," Termina o programa")

        menuVeiculoDB = MenuVeiculos.Append(wx.ID_ANY, "&Veiculos", " Abre o banco de dados de veiculos")
        menuVeiculosCalc = MenuVeiculos.Append(wx.ID_ANY, "&Calculo p/ rota", " Abre o calculo por rota")

        menuAreaDB = MenuArea.Append(wx.ID_ANY, "&Area", " Abre o banco de dados de Area")
        menuAreaCalc = MenuArea.Append(wx.ID_ANY, "&Calculo p/ area", " Abre o calculo por area")

        menuCompensarDB = MenuCompensacao.Append(wx.ID_ANY, "&Biomas", " Abre o banco de dados de biomas")
        menuCompensarCalc = MenuCompensacao.Append(wx.ID_ANY, "&Compensação", " Abre o calculo de compensação")

        mencadastro = MenuCadastros.Append(wx.ID_ANY, "&Cadastro", " Abre a tabela de cadastros")

        #Criando a barra de menu
        Menubar = wx.MenuBar()
        Menubar.Append(MenuAplicacao, "Applicação")
        Menubar.Append(MenuVeiculos, "Calculo por rota")
        Menubar.Append(MenuArea, "Calculo por area")
        Menubar.Append(MenuCompensacao, "Compensação")
        Menubar.Append(MenuCadastros, "Cadastros")
        self.SetMenuBar(Menubar)

        #Setando eventos
        self.Bind(wx.EVT_MENU, self.onSobre, menuSobre)
        self.Bind(wx.EVT_MENU, self.onSair, menuSair)
        self.Bind(wx.EVT_MENU, self.onVeiculoDB, menuVeiculoDB)
        self.Bind(wx.EVT_MENU, self.onVeiculoCalc, menuVeiculosCalc)
        self.Bind(wx.EVT_MENU, self.onAreaDB, menuAreaDB)
        self.Bind(wx.EVT_MENU, self.onAreaCalc, menuAreaCalc)
        self.Bind(wx.EVT_MENU, self.onCompDB, menuCompensarDB)
        self.Bind(wx.EVT_MENU, self.onCompCalc, menuCompensarCalc)
        self.Bind(wx.EVT_MENU, self.onCadastro, mencadastro)



        self.Show()
    
    #As funções da barra do menu
    def onSobre(self, e):
        dlg = wx.MessageDialog(self, "Um progama de teste (falta adicionar uma pagina de sobre)", "Sobre o Progama", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    def onSair(self, e):
        self.Close()

    #Por enquanto todos estão com o mesmo dialogo, só para ter um metodo pronto
    def onVeiculoDB(self, e):
        dlg = wx.MessageDialog(self, "Ainda em Desenvolvimento", " VeiculoDB", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    def onVeiculoCalc(self, e):
        dlg = wx.MessageDialog(self, "Ainda em Desenvolvimento", " VeiculoCalc", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    def onAreaDB(self, e):
        dlg = wx.MessageDialog(self, "Ainda em Desenvolvimento", " AreaDB", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    def onAreaCalc(self, e):
        dlg = wx.MessageDialog(self, "Ainda em Desenvolvimento", " AreaCalc", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    def onCompDB(self, e):
        dlg = wx.MessageDialog(self, "Ainda em Desenvolvimento", " CompDB", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    def onCompCalc(self, e):
        dlg = wx.MessageDialog(self, "Ainda em Desenvolvimento", " CompCalc", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    def onCadastro(self, e):
        dlg = wx.MessageDialog(self, "Ainda em Desenvolvimento", " Cadastro", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, "3C-CO2")
app.MainLoop()
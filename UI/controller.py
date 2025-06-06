import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceAnno=None
        self._choiceSquadra=None

    def handleCreaGrafo(self, e):
        self._model.creaGrafo()

    def handleDettagli(self, e):
        self._view._txt_result.clean()
        print(self._choiceSquadra)
        self._view._txt_result.controls.append(ft.Text(f"Stampo i vicini di {self._choiceSquadra.teamCode} con relativo peso dell'arco"))
        squadre=self._model.getVicini(self._choiceSquadra)
        for squadra in squadre:
            self._view.txt.controls.append(ft.Text(f"{squadra.ID}" - {squadra.teamCode}))
        self._view._page.update()

    def handlePercorso(self, e):
        pass

    def fillDDanni(self):
        anni=self._model.getAnniDD()
        for anno in anni:
            self._view._ddAnno.options.append(ft.DropdownOption(anno))
        self._view._page.update()


    def handleAnno(self, e):
        if e.control.value=="":
            self._view.txtOutSquadre_result.clean()
            self._view._txtOutSquadre.controls.append(ft.Text(f"Inserire un anno"),color="red")
            self._view._page.update()
            return
        self._choiceAnno = int(e.control.value)
        self.fillDDsquadre()
        self.fillTxtResult()
        self._view._btnCreaGrafo.disabled= False
        self._view._page.update()



    def fillTxtResult(self):

        squadre = self._model.getTeams(self._choiceAnno)
        self._view._txtOutSquadre.controls.append(
            ft.Text(f"Ho trovato {len(squadre)} squadre che hanno giocato nel  {self._choiceAnno}"))
        for squadra in squadre:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{squadra.teamCode}"))
        self._view._page.update()


    def fillDDsquadre(self):
        squadre=self._model.getTeams(self._choiceAnno)
        # options = [
        #     ft.DropdownOption(
        #         text=squadra.teamCode,  # ciò che l’utente vede
        #         key=str(squadra.ID),  # valore di ritorno in e.control.value
        #         data=squadra  # conterrà l’oggetto intero in e.control.data
        #     )
        #     for squadra in squadre
        # ]
        # self._view._ddSquadra.options = options
        # self._view._page.update()
        for squadra in squadre:
            self._view._ddSquadra.options.append(
                ft.DropdownOption(
                    text=squadra.teamCode,  # ciò che vede l’utente
                    key=squadra.ID,  # un identificatore univoco (opzionale)
                    data=squadra, on_click=self.read_retailer  # → qui passo l’oggetto Squadra intero
                )
            )

        self._view._page.update()

    # def handleSquadra(self,e):
    #     if e.control.value=="":
    #         self._view.txtOutSquadre_result.clean()
    #         self._view._txtOutSquadre.controls.append(ft.Text(f"Inserire una squadra"),color="red")
    #         self._view._page.update()
    #         return
    #     self._choiceSquadra = self._view._ddSquadra.data

    def read_retailer(self,e):
        self._choiceSquadra=e.control.data

    def handleDDYearSelection(self, e):
        teams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(
            ft.Text(f"Ho trovato {len(teams)} squadre che hanno gioccato nel {self._view._ddAnno.value}"))

        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{t.teamCode}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data=t, text=t.teamCode, on_click=self.readDDTeams))

        self._view.update_page()




import threading
import time

import customtkinter
from client.index_client import Client

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # data
        self.__username = ''
        self.__client = Client()
        self.__receive = ''
        self.__operator = ''

        #monitor
        self.__thread = threading.Thread(target=self.monitorReceive)

    # configure window
        self.title("PROMETHEUS")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="PROMETHEUS",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Modo da aparência:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Digite algo...")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Enviar", fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"),
                                                     command=self.sidebar_button_event)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, state='disabled', width=1000, height=1000)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250, height=1000)
        self.tabview.grid(row=0, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Status")
        self.tabview.add("Configurações")
        self.tabview.add("Rede")
        self.tabview.tab("Status").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Configurações").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Rede").grid_columnconfigure(0, weight=1)
        self.text_tab_1 = customtkinter.CTkTextbox(self.tabview.tab("Status"), state='disabled')
        self.text_tab_1.grid(row=0, column=0, padx=20, pady=20)
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Configurações"), text="Perfil",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Rede"), text="Lista de usuários online")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def open_input_dialog_event(self):
        # establishing connection
        dialog = customtkinter.CTkInputDialog(text="Defina apelido:", title="Editar perfil")
        self.__username = dialog.get_input()
        self.text_tab_1.configure(state="normal")
        self.text_tab_1.insert("0.0", f'\nConectando {self.__username} ao servidor.' + "\n")
        self.text_tab_1.configure(state="disabled")
        self.__client.setUsername(self.__username)
        self.__client.connectClient()
        self.__thread.start()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print(f'---- {self.entry.get()}\n')
        self.__client.setSendMessages(self.entry.get())


    def monitorReceive(self):
        while True:
            time.sleep(1)
            print('>> Monitoring...\n')
            self.__receive = self.__client.getReceiveMessage()

            if self.__receive.startswith("#"):
                self.__operator = 'BOT-PROMETHEUS'
            else:
                self.__operator = self.__username

            if len(self.__receive) > 0:
                self.textbox.configure(state="normal")
                self.textbox.insert("0.0", f'<{self.__operator}> {self.__receive}' + "\n")
                self.textbox.configure(state="disabled")
                self.__client.setReceiveMessage('')


if __name__ == "__main__":
    app = App()
    app.mainloop()

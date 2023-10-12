import customtkinter
import os
from PIL import Image
import core


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cross Fitness ADMIN")
        self.geometry("700x450")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.home_image = customtkinter.CTkImage(
            size=(20, 20),
            dark_image=Image.open(
                os.path.join(
                    image_path,
                      "home_light.png"
                )
            )
        )
        self.chart_image = customtkinter.CTkImage(
            size=(20, 20),
            dark_image=Image.open(
                os.path.join(
                    image_path, 
                    "chart-simple-light.png"
                )
            )
        )
        self.get_user_image = customtkinter.CTkImage(
            size=(20, 20),
            dark_image=Image.open(
                os.path.join(
                    image_path, 
                    "get_user_light.png"
                )
            )
        )

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel (
            self.navigation_frame, 
            text="Cross Fitness",
            compound="left", 
            font=customtkinter.CTkFont (
                size=15, 
                weight="bold"
            )
        )
        
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame, 
            corner_radius=0, 
            height=40, 
            border_spacing=10, 
            text="Home",
            fg_color="transparent", 
            text_color=("gray10", "gray90"), 
            hover_color=("gray70", "gray30"),
            image=self.home_image, 
            anchor="w", 
            command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.analytics_button = customtkinter.CTkButton(
            self.navigation_frame, 
            corner_radius=0, 
            height=40, 
            border_spacing=10, 
            text="Analytics",
            fg_color="transparent", 
            text_color=("gray10", "gray90"), 
            hover_color=("gray70", "gray30"),
            image=self.chart_image, anchor="w", 
            command=self.analytics_button_event)
        self.analytics_button.grid(row=2, column=0, sticky="ew")

        self.user_button = customtkinter.CTkButton(
            self.navigation_frame, 
            corner_radius=0, 
            height=40, 
            border_spacing=10, 
            text="Users",
            fg_color="transparent", 
            text_color=("gray10", "gray90"), 
            hover_color=("gray70", "gray30"),
            image=self.get_user_image, 
            anchor="w", 
            command=self.user_button_event)
        self.user_button.grid(row=3, column=0, sticky="ew")


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.home_frame_welcome_label = customtkinter.CTkLabel(
            self.home_frame, 
            justify=customtkinter.LEFT,
            fg_color="transparent",
            text="Cross Fitness\n Buon Lavoro",
            width=500,
            height=500,
            anchor='n',
            font=customtkinter.CTkFont (
                size=36, 
                weight="bold"
            )
        )

        self.home_frame_welcome_label.grid(
            row=0,
            column=0, 
            padx=(20, 0), 
            pady=(20, 0)
            )

        # create analytics frame
        self.analytics_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.analytics_frame.grid_columnconfigure(0, weight=1)

        self.analytics_frame_button_1 = customtkinter.CTkButton(
            self.analytics_frame, 
            text="Compute Analytics",
            command=self.compute_analytics)
        self.analytics_frame_button_1.grid(
            row=1, 
            column=0, 
            padx=20, 
            pady=20)

        # create user frame
        self.user_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.user_frame_button_1 = customtkinter.CTkButton(
            self.user_frame, 
            text="Get reservation",
            command=self.getReservation)
        self.user_frame_button_1.grid(
            row=0, 
            column=3, 
            padx=20, 
            pady=20)
        self.user_frame_textbox = customtkinter.CTkTextbox(
            self.user_frame, 
            width=150,
            height=20,
            activate_scrollbars=False
            )
        self.user_frame_textbox.grid(
            row=0,
            column=2, 
            padx=(0, 0), 
            pady=(0, 0))
        
        self.user_frame_tooltips_label = customtkinter.CTkLabel(
            self.user_frame, 
            justify=customtkinter.LEFT,
            fg_color="transparent",
            text="Insert Username: "
            )
        self.user_frame_tooltips_label.grid(
            row=0,
            column=1, 
            padx=(0, 0), 
            pady=(0, 0)
            )
        self.user_frame_output_label = customtkinter.CTkLabel(
            self.user_frame, 
            width=500,
            height=500,
            anchor='nw',
            justify=customtkinter.LEFT,
            fg_color="transparent",
            text=""
            )
        self.user_frame_output_label.grid(
            row=1,
            column=0, 
            columnspan=4,
            padx=(40, 0), 
            pady=(20, 0)
            )


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.analytics_button.configure(fg_color=("gray75", "gray25") if name == "analytics" else "transparent")
        self.user_button.configure(fg_color=("gray75", "gray25") if name == "user" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "analytics":
            self.analytics_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.analytics_frame.grid_forget()
        if name == "user":
            self.user_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.user_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def analytics_button_event(self):
        self.select_frame_by_name("analytics")
    
    def compute_analytics(self):
        core.computeChar()
        print("DONE")

    def user_button_event(self):
        self.select_frame_by_name("user")

    def getReservation(self):
        response = ""
        self.user_frame_output_label.configure(text="")
        user = self.user_frame_textbox.get(0.1,customtkinter.END)
        response = core.getReservation(user[:-1])
        self.user_frame_output_label.configure(text= response)

if __name__ == "__main__":
    app = App()
    app.mainloop()
import os
import subprocess

import tkinter as tk

from tkinter.filedialog import askopenfile, askdirectory

from ui.buttons import MenuButton
from ui.labels import HeaderLabel

class TrainingFrame(tk.Frame):
    def __init__(self, root, back_cmd=lambda: None):
        super().__init__(root)

        self.save_dir_var = tk.StringVar(value="data/runs/inference")
        self.result_name_var = tk.StringVar(value="experiment001")

        self.img_size_var = tk.IntVar(value=256)
        self.workers_var = tk.IntVar(value=8)
        self.batch_size_var = tk.IntVar(value=4)

        self.data_file_var = tk.StringVar(value="")
        self.model_config = tk.StringVar(value="")
        self.model_var = tk.StringVar(value="")
        self.training_config_var = tk.StringVar(value="")

        self.build(back_cmd)

    def open_save_dir(self):
        dir_path = askdirectory()
        self.save_dir_var.set(dir_path)

    def open_model_file(self):
        file = askopenfile(mode ='r', filetypes =[('Model Files', '*.pt')])
        self.model_path_var.set(file.name)
    
    def open_yaml_file(self, ent_var):
        file = askopenfile(mode ='r', filetypes =[('YAML Files', '*.yaml'), ('YAML Files', '*.yml')])
        ent_var.set(file.name)

    def run(self):
        script_path = os.path.join(self.master.project_path, "externals", "yolov7", "train.py")
        cmd_str = f"python {script_path} --workers {self.workers_var.get()} --batch-size {self.batch_size_var.get()}" 
        cmd_str += f" --img {self.img_size_var.get()}"
        cmd_str += f" --project {self.save_dir_var.get()}"
        cmd_str += f" --name {self.result_name_var.get()}"
        cmd_str += f" --data {self.data_file_var.get()}"
        cmd_str += f" --cfg {self.model_config.get()}"
        cmd_str += f" --weights {self.model_var.get()}"
        cmd_str += f" --hyp {self.training_config_var.get()}"

        print(cmd_str)

        stdout = subprocess.Popen(cmd_str, shell=True, stdout=subprocess.PIPE).stdout

        print(stdout.read())
        print("DONE")

    def build(self, back_cmd=lambda: None):
        greeting = HeaderLabel(self, text="Training Frame")
        greeting.pack()

        back_btn = MenuButton(self,
            text="Home Page",
            command=back_cmd
        )
        back_btn.pack()

        save_dir_btn = tk.Button(self,
            text="Save Directory",
            width=20,
            height=3,
            bg="lightgrey",
            fg="black",
            command=self.open_save_dir
        )
        save_dir_btn.pack()

        save_dir_entry = tk.Entry(self, textvariable=self.save_dir_var, state="disabled")
        save_dir_entry.pack()

        result_lbl = tk.Label(self, text="Result Name")
        result_lbl.pack()
        result_name_entry = tk.Entry(self, textvariable=self.result_name_var)
        result_name_entry.pack()

        worker_lbl = tk.Label(self, text="Number of workers")
        worker_lbl.pack()
        worker_entry = tk.Entry(self, textvariable=self.workers_var)
        worker_entry.pack()
        
        batch_size_lbl = tk.Label(self, text="Batch size")
        batch_size_lbl.pack()
        batch_size_entry = tk.Entry(self, textvariable=self.batch_size_var)
        batch_size_entry.pack()

        img_size_lbl = tk.Label(self, text="Image size")
        img_size_lbl.pack()
        img_size_entry = tk.Entry(self, textvariable=self.img_size_var)
        img_size_entry.pack()

        data_file_btn = tk.Button(self,
            text="Data file",
            width=20,
            height=3,
            bg="lightgrey",
            fg="black",
            command=lambda: self.open_yaml_file(self.data_file_var)
        )
        data_file_btn.pack()

        data_file_entry = tk.Entry(self, textvariable=self.data_file_var, state="disabled")
        data_file_entry.pack()
        
        model_config_file_btn = tk.Button(self,
            text="Model Configuration File",
            width=20,
            height=3,
            bg="lightgrey",
            fg="black",
            command=lambda: self.open_yaml_file(self.model_config)
        )
        model_config_file_btn.pack()

        model_config_file_entry = tk.Entry(self, textvariable=self.model_config, state="disabled")
        model_config_file_entry.pack()
        
        model_weights_file_btn = tk.Button(self,
            text="Model Weights File",
            width=20,
            height=3,
            bg="lightgrey",
            fg="black",
            command=lambda: self.open_yaml_file(self.model_var)
        )
        model_weights_file_btn.pack()

        model_weights_file_entry = tk.Entry(self, textvariable=self.model_var, state="disabled")
        model_weights_file_entry.pack()
        
        training_file_btn = tk.Button(self,
            text="Training Configuration File",
            width=20,
            height=3,
            bg="lightgrey",
            fg="black",
            command=lambda: self.open_yaml_file(self.training_config_var)
        )
        training_file_btn.pack()

        training_file_entry = tk.Entry(self, textvariable=self.training_config_var, state="disabled")
        training_file_entry.pack()
        
        run_btn = tk.Button(self,
            text="Run",
            width=50,
            height=10,
            bg="red",
            fg="white",
            command=self.run
        )
        run_btn.pack()


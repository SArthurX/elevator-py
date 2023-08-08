import tkinter as tk
from hand import hand_pos, update_hand_pos
from PIL import Image, ImageTk


class HandGestureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hand Gesture App")

        self.gesture_data = {}

        self.gesture = [0, 0, 0, 0, 0]

        image_path = "image.png"  
        image = Image.open(image_path)
        image = image.resize((640, 480), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)

        
        self.image_label = tk.Label(root, image=self.photo)
        self.image_label.grid(row=0, columnspan=5, padx=5, pady=5)


        self.finger_buttons = []
        for i in range(5):
            button = tk.Button(root, text=f"Finger {i+1}", command=lambda idx=i: self.toggle_finger(idx), bg="red")
            button.grid(row=1, column=i, padx=5, pady=5)
            self.finger_buttons.append(button)

        self.index_entry = tk.Entry(root, width=10)
        self.index_entry.grid(row=2, column=0, padx=5, pady=5)
        
        self.save_button = tk.Button(root, text="Save Gesture", command=self.save_gesture)
        self.save_button.grid(row=2, columnspan=5, padx=5, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.grid(row=2, column=3, padx=5, pady=10)

    def toggle_finger(self, finger_idx):
        self.gesture[finger_idx] = 1 - self.gesture[finger_idx]
        color = "green" if self.gesture[finger_idx] == 1 else "red"
        self.finger_buttons[finger_idx].config(bg=color)

    def save_gesture(self):
        index = self.index_entry.get()
        self.gesture_data[index] = self.gesture.copy()

        with open("hand_gesture.txt", "w") as file:
            for idx, gesture in self.gesture_data.items():
                gesture_str = f"{idx}: " + " ".join(str(finger_state) for finger_state in gesture)
                file.write(gesture_str + "\n")
        
        update_hand_pos(self.gesture_data)
        print("Gesture saved!")
        root.quit()
        

if __name__ == "__main__":
    root = tk.Tk()
    app = HandGestureApp(root)
    root.mainloop()


